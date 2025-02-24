from model_bakery import baker
from pathlib import Path
from pytest import mark

from django.core.management import call_command
from django.db import connection

from usaspending_api.common.helpers.sql_helpers import ordered_dictionary_fetcher


@mark.django_db()
def test_old_table_exists_validation():
    try:
        call_command("swap_in_new_table", "--table=test_table")
    except Exception as e:
        assert str(e) == "There are no tables matching: test_table"
    else:
        assert False, "No exception was raised"


@mark.django_db()
def test_new_table_exists_validation():
    with connection.cursor() as cursor:
        cursor.execute("CREATE TABLE test_table (col1 TEXT)")
    try:
        call_command("swap_in_new_table", "--table=test_table")
    except Exception as e:
        assert str(e) == "There are no tables matching: test_table_temp"
    else:
        assert False, "No exception was raised"


@mark.django_db()
def test_index_validation():
    with connection.cursor() as cursor:
        # Test that the same number of indexes exist on the old and new table
        cursor.execute(
            "CREATE TABLE test_table (col1 TEXT, col2 INT);"
            "CREATE TABLE test_table_temp (col1 TEXT, col2 INT);"
            "CREATE INDEX test_table_col1_index ON test_table(col1);"
            "CREATE INDEX test_table_col2_index ON test_table(col2);"
            "CREATE INDEX test_table_col1_index_temp ON test_table_temp(col1);"
        )
        try:
            call_command("swap_in_new_table", "--table=test_table")
        except Exception as e:
            assert str(e) == "The number of indexes are different for the tables: test_table_temp and test_table"
        else:
            assert False, "No exception was raised"

        # Test that the indexes have the same name after removing appended "_temp" from the name
        cursor.execute("CREATE INDEX test_table_wrong_col2_index_temp ON test_table_temp(col2)")
        try:
            call_command("swap_in_new_table", "--table=test_table")
        except Exception as e:
            assert str(e) == "The index definitions are different for the tables: test_table_temp and test_table"
        else:
            assert False, "No exception was raised"

        # Test that the indexes have the same definition after removing "_temp"
        cursor.execute(
            "DROP INDEX test_table_wrong_col2_index_temp;"
            "CREATE INDEX test_table_col2_index_temp ON test_table_temp(col2 NULLS FIRST);"
        )
        try:
            call_command("swap_in_new_table", "--table=test_table")
        except Exception as e:
            assert str(e) == "The index definitions are different for the tables: test_table_temp and test_table"
        else:
            assert False, "No exception was raised"


@mark.django_db()
def test_constraint_validation():
    with connection.cursor() as cursor:
        # Test that Foreign Keys are not allowed by default
        cursor.execute(
            "CREATE TABLE test_table (col1 TEXT, col2 INT);"
            "CREATE TABLE test_table_temp (col1 TEXT, col2 INT);"
            "ALTER TABLE test_table_temp ADD CONSTRAINT test_table_award_fk_temp FOREIGN KEY (col2) REFERENCES awards (id);"
        )
        try:
            call_command("swap_in_new_table", "--table=test_table")
        except Exception as e:
            assert str(e) == (
                "Foreign Key constraints are not allowed on 'test_table_temp' or 'test_table'."
                " It is advised to not allow Foreign Key constraints on swapped tables to avoid potential deadlock."
                " However, if needed they can be allowed with the `--allow-foreign-key` flag."
            )
        else:
            assert False, "No exception was raised"

        # Test that Foreign Keys are allowed with the use of '--allow-foreign-key';
        # This causes the next validation to fail expecting an even number of constraints
        try:
            call_command("swap_in_new_table", "--table=test_table", "--allow-foreign-key")
        except Exception as e:
            assert str(e) == "The number of constraints are different for the tables: test_table_temp and test_table."
        else:
            assert False, "No exception was raised"

        # Test that the same number of constraints exist on the old and new table
        cursor.execute(
            "ALTER TABLE test_table_temp DROP CONSTRAINT test_table_award_fk_temp;"
            "ALTER TABLE test_table ADD CONSTRAINT test_table_col_1_constraint CHECK (col1 != 'TEST');"
        )
        try:
            call_command("swap_in_new_table", "--table=test_table")
        except Exception as e:
            assert str(e) == "The number of constraints are different for the tables: test_table_temp and test_table."
        else:
            assert False, "No exception was raised"

        # Test that the constraints have the same name after removing appended "_temp" from the name
        cursor.execute(
            "ALTER TABLE test_table_temp ADD CONSTRAINT test_table_wrong_col_1_constraint_temp CHECK (col1 != 'TEST')"
        )
        try:
            call_command("swap_in_new_table", "--table=test_table")
        except Exception as e:
            assert str(e) == (
                "The constraint definitions are different for the tables: test_table_temp and test_table."
            )
        else:
            assert False, "No exception was raised"

        # Test that two CHECK constraints with different CHECK CLAUSE will fail
        cursor.execute(
            "ALTER TABLE test_table_temp DROP CONSTRAINT test_table_wrong_col_1_constraint_temp;"
            "ALTER TABLE test_table_temp ADD CONSTRAINT test_table_col_1_constraint_temp CHECK (col1 != 'TEST_WRONG');"
        )
        try:
            call_command("swap_in_new_table", "--table=test_table")
        except Exception as e:
            assert str(e) == (
                "The constraint definitions are different for the tables: test_table_temp and test_table."
            )
        else:
            assert False, "No exception was raised"

        # Test that the same amount of NOT NULL constraints exist
        cursor.execute(
            "CREATE TABLE test_table_not_null (col1 TEXT, col2 INT NOT NULL);"
            "CREATE TABLE test_table_not_null_temp (col1 TEXT, col2 INT);"
        )
        try:
            call_command("swap_in_new_table", "--table=test_table_not_null")
        except Exception as e:
            assert (
                str(e)
                == "The number of constraints are different for the tables: test_table_not_null_temp and test_table_not_null."
            )
        else:
            assert False, "No exception was raised"

        # Test that the same columns must share a NOT NULL constraint
        cursor.execute("ALTER TABLE test_table_not_null_temp ALTER COLUMN col1 SET NOT NULL")
        try:
            call_command("swap_in_new_table", "--table=test_table_not_null")
        except Exception as e:
            assert str(e) == (
                "The constraint definitions are different for the tables: test_table_not_null_temp and test_table_not_null."
            )
        else:
            assert False, "No exception was raised"


@mark.django_db()
def test_column_validation():
    with connection.cursor() as cursor:
        # Test that two tables with different number of columns will fail
        cursor.execute(
            "CREATE TABLE test_table (col1 TEXT, col2 INT);"
            "CREATE TABLE test_table_temp (col1 TEXT, col2 INT, col3 INT);"
        )
        try:
            call_command("swap_in_new_table", "--table=test_table")
        except Exception as e:
            assert str(e) == f"The number of columns are different for the tables: test_table_temp and test_table."
        else:
            assert False, "No exception was raised"

        # Test that two tables with different column definitions will fail
        cursor.execute(
            "DROP TABLE test_table;"
            "DROP TABLE test_table_temp;"
            "CREATE TABLE test_table (col1 TEXT, col2 INT);"
            "CREATE TABLE test_table_temp (col1 TEXT, col2 TEXT);"
        )
        try:
            call_command("swap_in_new_table", "--table=test_table")
        except Exception as e:
            assert str(e) == (f"The column definitions are different for the tables: test_table_temp and test_table.")
        else:
            assert False, "No exception was raised"


@mark.django_db(transaction=True)
def test_happy_path(monkeypatch, tmp_path_factory):
    # Create the Award records for testing with Foreign Keys
    for i in range(2, 7):
        baker.make("awards.Award", id=i, _fill_optional=True)

    temp_dir = tmp_path_factory.mktemp("test_view")
    with open(f"{temp_dir}/vw_test_table.sql", "w") as f:
        f.write("CREATE OR REPLACE VIEW vw_test_table AS SELECT * FROM test_table;")

    monkeypatch.setattr(
        "usaspending_api.etl.management.commands.swap_in_new_table.VIEWS_TO_UPDATE",
        {"test_table": [Path(f"{temp_dir}/vw_test_table.sql")]},
    )

    try:
        with connection.cursor() as cursor:
            # Test without Foreign Keys
            cursor.execute(
                "CREATE TABLE rpt.test_table_old (col1 TEXT, col2 INT NOT NULL);"
                "CREATE TABLE rpt.test_table (col1 TEXT, col2 INT NOT NULL);"
                "CREATE TABLE temp.test_table_temp (col1 TEXT, col2 INT NOT NULL);"
                "INSERT INTO test_table (col1, col2) VALUES ('goodbye', 1);"
                "INSERT INTO test_table_temp (col1, col2) VALUES ('hello', 2), ('world', 3);"
                "CREATE INDEX test_table_col1_index ON test_table(col1);"
                "CREATE INDEX test_table_col1_index_temp ON test_table_temp(col1);"
                "ALTER TABLE test_table ADD CONSTRAINT test_table_col_1_unique UNIQUE(col1);"
                "ALTER TABLE test_table ADD CONSTRAINT test_table_col_1_constraint CHECK (col1 != 'TEST');"
                "ALTER TABLE test_table_temp ADD CONSTRAINT test_table_col_1_unique_temp UNIQUE (col1);"
                "ALTER TABLE test_table_temp ADD CONSTRAINT test_table_col_1_constraint_temp CHECK (col1 != 'TEST');"
            )
            call_command("swap_in_new_table", "--table=test_table")
            cursor.execute("SELECT * FROM test_table ORDER BY col2")
            result = ordered_dictionary_fetcher(cursor)
            assert result == [{"col1": "hello", "col2": 2}, {"col1": "world", "col2": 3}]

            cursor.execute("SELECT * FROM vw_test_table ORDER BY col2")
            result = ordered_dictionary_fetcher(cursor)
            assert result == [{"col1": "hello", "col2": 2}, {"col1": "world", "col2": 3}]

            cursor.execute(
                "SELECT * FROM information_schema.tables WHERE table_name IN ('test_table_temp', 'test_table_old')"
            )
            result = cursor.fetchall()
            assert len(result) == 0

            cursor.execute("SELECT table_schema FROM information_schema.tables WHERE table_name = 'test_table'")
            result = cursor.fetchone()[0]
            assert result == "rpt"

            # Test with "--allow-foreign-key" flag
            cursor.execute(
                "CREATE TABLE test_table_temp (col1 TEXT, col2 INT NOT NULL);"
                "INSERT INTO test_table_temp (col1, col2) VALUES ('foo', 4), ('bar', 5);"
                "CREATE INDEX test_table_col1_index_temp ON test_table_temp(col1);"
                "ALTER TABLE test_table_temp ADD CONSTRAINT test_table_col_1_unique_temp UNIQUE(col1);"
                "ALTER TABLE test_table_temp ADD CONSTRAINT test_table_col_1_constraint_temp CHECK (col1 != 'TEST');"
                "ALTER TABLE test_table ADD CONSTRAINT test_table_award_fk FOREIGN KEY (col2) REFERENCES awards (id);"
                "ALTER TABLE test_table_temp ADD CONSTRAINT test_table_award_fk_temp FOREIGN KEY (col2) REFERENCES awards (id);"
            )
            call_command("swap_in_new_table", "--table=test_table", "--allow-foreign-key")
            cursor.execute("SELECT * FROM test_table ORDER BY col2")
            result = ordered_dictionary_fetcher(cursor)
            assert result == [{"col1": "foo", "col2": 4}, {"col1": "bar", "col2": 5}]

            cursor.execute(
                "SELECT * FROM information_schema.tables WHERE table_name IN ('test_table_temp', 'test_table_old')"
            )
            result = cursor.fetchall()
            assert len(result) == 0

            # Test with "--keep-old-data" flag
            cursor.execute(
                "CREATE TABLE test_table_temp (col1 TEXT, col2 INT NOT NULL);"
                "INSERT INTO test_table_temp (col1, col2) VALUES ('the end', 6);"
                "CREATE INDEX test_table_col1_index_temp ON test_table_temp(col1);"
                "ALTER TABLE test_table_temp ADD CONSTRAINT test_table_col_1_unique_temp UNIQUE(col1);"
                "ALTER TABLE test_table_temp ADD CONSTRAINT test_table_col_1_constraint_temp CHECK (col1 != 'TEST');"
                "ALTER TABLE test_table_temp ADD CONSTRAINT test_table_award_fk_temp FOREIGN KEY (col2) REFERENCES awards (id);"
            )
            call_command("swap_in_new_table", "--table=test_table", "--allow-foreign-key", "--keep-old-data")
            cursor.execute("SELECT * FROM test_table ORDER BY col2")
            result = ordered_dictionary_fetcher(cursor)
            assert result == [{"col1": "the end", "col2": 6}]

            cursor.execute(
                "SELECT * FROM information_schema.tables WHERE table_name IN ('test_table_temp', 'test_table_old')"
            )
            result = cursor.fetchall()
            assert len(result) == 1

            cursor.execute("SELECT * FROM test_table_old ORDER BY col2")
            result = ordered_dictionary_fetcher(cursor)
            assert result == [{"col1": "foo", "col2": 4}, {"col1": "bar", "col2": 5}]
    finally:
        # Handle cleanup of test tables since this needs to occur outside a Transaction when dealing with FKs
        with connection.cursor() as cursor:
            cursor.execute(
                "DROP TABLE IF EXISTS test_table CASCADE;"
                "DROP TABLE IF EXISTS test_table_temp CASCADE;"
                "DROP TABLE IF EXISTS test_table_old CASCADE;"
            )
