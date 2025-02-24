# Generated by Django 3.2.13 on 2022-07-13 21:09

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0095_auto_20220617_1620'),
        ('search', '0007_transactionsearch_parent_uei'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwardSearch',
            fields=[
                ('treasury_account_identifiers', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, null=True, size=None)),
                ('award', models.BigIntegerField(serialize=False, db_column="award_id")),
                ('category', models.TextField(null=True)),
                ('type', models.TextField(null=True)),
                ('type_description', models.TextField(null=True)),
                ('generated_unique_award_id', models.TextField(null=True)),
                ('display_award_id', models.TextField(null=True)),
                ('update_date', models.DateTimeField(null=True)),
                ('piid', models.TextField(null=True)),
                ('fain', models.TextField(null=True)),
                ('uri', models.TextField(null=True)),
                ('award_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True)),
                ('total_obligation', models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True)),
                ('description', models.TextField(null=True)),
                ('total_subsidy_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True)),
                ('total_loan_value', models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True)),
                ('total_obl_bin', models.TextField(null=True)),
                ('recipient_hash', models.UUIDField(null=True)),
                ('recipient_levels', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, null=True, size=None)),
                ('recipient_name', models.TextField(null=True)),
                ('recipient_unique_id', models.TextField(null=True)),
                ('parent_recipient_unique_id', models.TextField(null=True)),
                ('recipient_uei', models.TextField(blank=True, null=True)),
                ('parent_uei', models.TextField(blank=True, null=True)),
                ('business_categories', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, null=True, size=None)),
                ('action_date', models.DateField(null=True)),
                ('fiscal_year', models.IntegerField(null=True)),
                ('last_modified_date', models.DateField(null=True)),
                ('period_of_performance_start_date', models.DateField(null=True)),
                ('period_of_performance_current_end_date', models.DateField(null=True)),
                ('date_signed', models.DateField(null=True)),
                ('ordering_period_end_date', models.DateField(null=True)),
                ('original_loan_subsidy_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True)),
                ('face_value_loan_guarantee', models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True)),
                ('awarding_agency_id', models.IntegerField(null=True)),
                ('funding_agency_id', models.IntegerField(null=True)),
                ('funding_toptier_agency_id', models.IntegerField(null=True)),
                ('funding_subtier_agency_id', models.IntegerField(null=True)),
                ('awarding_toptier_agency_name', models.TextField(null=True)),
                ('funding_toptier_agency_name', models.TextField(null=True)),
                ('awarding_subtier_agency_name', models.TextField(null=True)),
                ('funding_subtier_agency_name', models.TextField(null=True)),
                ('awarding_toptier_agency_code', models.TextField(null=True)),
                ('funding_toptier_agency_code', models.TextField(null=True)),
                ('awarding_subtier_agency_code', models.TextField(null=True)),
                ('funding_subtier_agency_code', models.TextField(null=True)),
                ('recipient_location_country_code', models.TextField(null=True)),
                ('recipient_location_country_name', models.TextField(null=True)),
                ('recipient_location_state_code', models.TextField(null=True)),
                ('recipient_location_county_code', models.TextField(null=True)),
                ('recipient_location_county_name', models.TextField(null=True)),
                ('recipient_location_zip5', models.TextField(null=True)),
                ('recipient_location_congressional_code', models.TextField(null=True)),
                ('recipient_location_city_name', models.TextField(null=True)),
                ('recipient_location_state_name', models.TextField(null=True)),
                ('recipient_location_state_fips', models.TextField(null=True)),
                ('recipient_location_state_population', models.IntegerField(null=True)),
                ('recipient_location_county_population', models.IntegerField(null=True)),
                ('recipient_location_congressional_population', models.IntegerField(null=True)),
                ('pop_country_code', models.TextField(null=True)),
                ('pop_country_name', models.TextField(null=True)),
                ('pop_state_code', models.TextField(null=True)),
                ('pop_county_code', models.TextField(null=True)),
                ('pop_county_name', models.TextField(null=True)),
                ('pop_city_code', models.TextField(null=True)),
                ('pop_zip5', models.TextField(null=True)),
                ('pop_congressional_code', models.TextField(null=True)),
                ('pop_city_name', models.TextField(null=True)),
                ('pop_state_name', models.TextField(null=True)),
                ('pop_state_fips', models.TextField(null=True)),
                ('pop_state_population', models.IntegerField(null=True)),
                ('pop_county_population', models.IntegerField(null=True)),
                ('pop_congressional_population', models.IntegerField(null=True)),
                ('cfda_program_title', models.TextField(null=True)),
                ('cfda_number', models.TextField(null=True)),
                ('cfdas', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, null=True, size=None)),
                ('sai_number', models.TextField(null=True)),
                ('type_of_contract_pricing', models.TextField(null=True)),
                ('extent_competed', models.TextField(null=True)),
                ('type_set_aside', models.TextField(null=True)),
                ('product_or_service_code', models.TextField(null=True)),
                ('product_or_service_description', models.TextField(null=True)),
                ('naics_code', models.TextField(null=True)),
                ('naics_description', models.TextField(null=True)),
                ('tas_paths', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, null=True, size=None)),
                ('tas_components', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, null=True, size=None)),
                ('disaster_emergency_fund_codes', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=list, null=True, size=None)),
                ('covid_spending_by_defc', models.JSONField(null=True)),
                ('total_covid_outlay', models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True)),
                ('total_covid_obligation', models.DecimalField(blank=True, decimal_places=2, max_digits=23, null=True)),
            ],
            options={
                'db_table': 'rpt"."award_search',
            },
        ),
        # Trick Django into believing this is a foreign primary key for purposes of using the ORM,
        # but avoid the headache that comes with foreign keys and the primary key constraint
        migrations.RunSQL(
            sql='ALTER TABLE rpt.award_search DROP COLUMN id; CREATE UNIQUE INDEX as_idx_award_id ON rpt.award_search(award_id);',
            reverse_sql="",
            state_operations=[
                migrations.AlterField(
                    model_name='awardsearch',
                    name='award',
                    field=models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        related_name='awardsearch',
                        serialize=False,
                        to='awards.award'
                    )
                )
            ]
        ),
        migrations.AddIndex(
            model_name='awardsearch',
            index=models.Index(condition=models.Q(('action_date__gte', '2007-10-01')), fields=['recipient_hash'], name='as_idx_recipient_hash'),
        ),
        migrations.AddIndex(
            model_name='awardsearch',
            index=models.Index(condition=models.Q(('recipient_unique_id__isnull', False), ('action_date__gte', '2007-10-01')), fields=['recipient_unique_id'], name='as_idx_recipient_unique_id'),
        ),
        migrations.AddIndex(
            model_name='awardsearch',
            index=models.Index(django.db.models.expressions.OrderBy(django.db.models.expressions.F('action_date'), descending=True, nulls_last=True), condition=models.Q(('action_date__gte', '2007-10-01')), name='as_idx_action_date'),
        ),
        migrations.AddIndex(
            model_name='awardsearch',
            index=models.Index(condition=models.Q(('action_date__gte', '2007-10-01')), fields=['funding_agency_id'], name='as_idx_funding_agency_id'),
        ),
        migrations.AddIndex(
            model_name='awardsearch',
            index=models.Index(condition=models.Q(('action_date__gte', '2007-10-01')), fields=['recipient_location_congressional_code'], name='as_idx_recipient_cong_code'),
        ),
        migrations.AddIndex(
            model_name='awardsearch',
            index=models.Index(condition=models.Q(('action_date__gte', '2007-10-01')), fields=['recipient_location_county_code'], name='as_idx_recipient_county_code'),
        ),
        migrations.AddIndex(
            model_name='awardsearch',
            index=models.Index(condition=models.Q(('action_date__gte', '2007-10-01')), fields=['recipient_location_state_code'], name='as_idx_recipient_state_code'),
        ),
        migrations.AddIndex(
            model_name='awardsearch',
            index=models.Index(django.db.models.expressions.OrderBy(django.db.models.expressions.F('action_date'), descending=True, nulls_last=True), condition=models.Q(('action_date__lt', '2007-10-01')), name='as_idx_action_date_pre2008'),
        ),
    ]
