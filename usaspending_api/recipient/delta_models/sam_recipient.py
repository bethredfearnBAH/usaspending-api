SAM_RECIPIENT_COLUMNS = {
    "awardee_or_recipient_uniqu": "STRING",
    "legal_business_name": "STRING",
    "ultimate_parent_unique_ide": "STRING",
    "ultimate_parent_legal_enti": "STRING",
    "broker_duns_id": "INTEGER NOT NULL",
    "update_date": "DATE NOT NULL",
    "address_line_1": "STRING",
    "address_line_2": "STRING",
    "city": "STRING",
    "congressional_district": "STRING",
    "country_code": "STRING",
    "state": "STRING",
    "zip": "STRING",
    "zip4": "STRING",
    "business_types_codes": "ARRAY<STRING>",
    "dba_name": "STRING",
    "entity_structure": "STRING",
    "uei": "STRING",
    "ultimate_parent_uei": "STRING",
}

sam_recipient_sql_string = rf"""
    CREATE OR REPLACE TABLE {{DESTINATION_TABLE}} (
        {", ".join([f'{key} {val}' for key, val in SAM_RECIPIENT_COLUMNS.items()])}
    )
    USING DELTA
    LOCATION 's3a://{{SPARK_S3_BUCKET}}/{{DELTA_LAKE_S3_PATH}}/{{DESTINATION_DATABASE}}/{{DESTINATION_TABLE}}'
    """
