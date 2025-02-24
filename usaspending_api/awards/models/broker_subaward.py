from django.db import models


class BrokerSubaward(models.Model):
    """
    This table is a direct copy of the "subaward" table in Broker with some
    minor USAspending enhancements (mostly indexes and stronger data typing).
    """

    created_at = models.DateTimeField(null=True, blank=True, db_index=True)
    updated_at = models.DateTimeField(null=True, blank=True, db_index=True)
    id = models.IntegerField(primary_key=True, db_index=True)
    unique_award_key = models.TextField(null=True, blank=True)
    award_id = models.TextField(null=True, blank=True)
    parent_award_id = models.TextField(null=True, blank=True)
    award_amount = models.DecimalField(max_digits=23, decimal_places=2, null=True, blank=True)
    action_date = models.DateField(blank=True, null=True)
    fy = models.TextField(null=True, blank=True)
    awarding_agency_code = models.TextField(null=True, blank=True)
    awarding_agency_name = models.TextField(null=True, blank=True)
    awarding_sub_tier_agency_c = models.TextField(null=True, blank=True)
    awarding_sub_tier_agency_n = models.TextField(null=True, blank=True)
    awarding_office_code = models.TextField(null=True, blank=True)
    awarding_office_name = models.TextField(null=True, blank=True)
    funding_agency_code = models.TextField(null=True, blank=True)
    funding_agency_name = models.TextField(null=True, blank=True)
    funding_sub_tier_agency_co = models.TextField(null=True, blank=True)
    funding_sub_tier_agency_na = models.TextField(null=True, blank=True)
    funding_office_code = models.TextField(null=True, blank=True)
    funding_office_name = models.TextField(null=True, blank=True)
    awardee_or_recipient_uniqu = models.TextField(null=True, blank=True)
    awardee_or_recipient_uei = models.TextField(null=True, blank=True)
    awardee_or_recipient_legal = models.TextField(null=True, blank=True)
    dba_name = models.TextField(null=True, blank=True)
    ultimate_parent_unique_ide = models.TextField(null=True, blank=True)
    ultimate_parent_uei = models.TextField(null=True, blank=True)
    ultimate_parent_legal_enti = models.TextField(null=True, blank=True)
    legal_entity_country_code = models.TextField(null=True, blank=True)
    legal_entity_country_name = models.TextField(null=True, blank=True)
    legal_entity_address_line1 = models.TextField(null=True, blank=True)
    legal_entity_city_name = models.TextField(null=True, blank=True)
    legal_entity_state_code = models.TextField(null=True, blank=True)
    legal_entity_state_name = models.TextField(null=True, blank=True)
    legal_entity_zip = models.TextField(null=True, blank=True)
    legal_entity_congressional = models.TextField(null=True, blank=True)
    legal_entity_foreign_posta = models.TextField(null=True, blank=True)
    business_types = models.TextField(null=True, blank=True)
    place_of_perform_city_name = models.TextField(null=True, blank=True)
    place_of_perform_state_code = models.TextField(null=True, blank=True)
    place_of_perform_state_name = models.TextField(null=True, blank=True)
    place_of_performance_zip = models.TextField(null=True, blank=True)
    place_of_perform_congressio = models.TextField(null=True, blank=True)
    place_of_perform_country_co = models.TextField(null=True, blank=True)
    place_of_perform_country_na = models.TextField(null=True, blank=True)
    award_description = models.TextField(null=True, blank=True)
    naics = models.TextField(null=True, blank=True)
    naics_description = models.TextField(null=True, blank=True)
    cfda_numbers = models.TextField(null=True, blank=True)
    cfda_titles = models.TextField(null=True, blank=True)
    subaward_type = models.TextField(null=True, blank=True)
    subaward_report_year = models.SmallIntegerField()
    subaward_report_month = models.SmallIntegerField()
    subaward_number = models.TextField(null=True, blank=True)
    subaward_amount = models.DecimalField(max_digits=23, decimal_places=2, null=True, blank=True)
    sub_action_date = models.DateField(blank=True, null=True)
    sub_awardee_or_recipient_uniqu = models.TextField(null=True, blank=True)
    sub_awardee_or_recipient_uei = models.TextField(null=True, blank=True)
    sub_awardee_or_recipient_legal = models.TextField(null=True, blank=True)
    sub_dba_name = models.TextField(null=True, blank=True)
    sub_ultimate_parent_unique_ide = models.TextField(null=True, blank=True)
    sub_ultimate_parent_uei = models.TextField(null=True, blank=True)
    sub_ultimate_parent_legal_enti = models.TextField(null=True, blank=True)
    sub_legal_entity_country_code = models.TextField(null=True, blank=True)
    sub_legal_entity_country_name = models.TextField(null=True, blank=True)
    sub_legal_entity_address_line1 = models.TextField(null=True, blank=True)
    sub_legal_entity_city_name = models.TextField(null=True, blank=True)
    sub_legal_entity_state_code = models.TextField(null=True, blank=True)
    sub_legal_entity_state_name = models.TextField(null=True, blank=True)
    sub_legal_entity_zip = models.TextField(null=True, blank=True)
    sub_legal_entity_congressional = models.TextField(null=True, blank=True)
    sub_legal_entity_foreign_posta = models.TextField(null=True, blank=True)
    sub_business_types = models.TextField(null=True, blank=True)
    sub_place_of_perform_city_name = models.TextField(null=True, blank=True)
    sub_place_of_perform_state_code = models.TextField(null=True, blank=True)
    sub_place_of_perform_state_name = models.TextField(null=True, blank=True)
    sub_place_of_performance_zip = models.TextField(null=True, blank=True)
    sub_place_of_perform_congressio = models.TextField(null=True, blank=True)
    sub_place_of_perform_country_co = models.TextField(null=True, blank=True)
    sub_place_of_perform_country_na = models.TextField(null=True, blank=True)
    subaward_description = models.TextField(null=True, blank=True)
    sub_high_comp_officer1_full_na = models.TextField(null=True, blank=True)
    sub_high_comp_officer1_amount = models.DecimalField(max_digits=23, decimal_places=2, null=True, blank=True)
    sub_high_comp_officer2_full_na = models.TextField(null=True, blank=True)
    sub_high_comp_officer2_amount = models.DecimalField(max_digits=23, decimal_places=2, null=True, blank=True)
    sub_high_comp_officer3_full_na = models.TextField(null=True, blank=True)
    sub_high_comp_officer3_amount = models.DecimalField(max_digits=23, decimal_places=2, null=True, blank=True)
    sub_high_comp_officer4_full_na = models.TextField(null=True, blank=True)
    sub_high_comp_officer4_amount = models.DecimalField(max_digits=23, decimal_places=2, null=True, blank=True)
    sub_high_comp_officer5_full_na = models.TextField(null=True, blank=True)
    sub_high_comp_officer5_amount = models.DecimalField(max_digits=23, decimal_places=2, null=True, blank=True)
    prime_id = models.IntegerField(null=True, blank=True)
    internal_id = models.TextField(null=True, blank=True)
    date_submitted = models.DateTimeField(null=True, blank=True)
    report_type = models.TextField(null=True, blank=True)
    transaction_type = models.TextField(null=True, blank=True)
    program_title = models.TextField(null=True, blank=True)
    contract_agency_code = models.TextField(null=True, blank=True)
    contract_idv_agency_code = models.TextField(null=True, blank=True)
    grant_funding_agency_id = models.TextField(null=True, blank=True)
    grant_funding_agency_name = models.TextField(null=True, blank=True)
    federal_agency_name = models.TextField(null=True, blank=True)
    treasury_symbol = models.TextField(null=True, blank=True)
    dunsplus4 = models.TextField(null=True, blank=True)
    recovery_model_q1 = models.BooleanField(null=True, blank=True)
    recovery_model_q2 = models.BooleanField(null=True, blank=True)
    compensation_q1 = models.BooleanField(null=True, blank=True)
    compensation_q2 = models.BooleanField(null=True, blank=True)
    high_comp_officer1_full_na = models.TextField(null=True, blank=True)
    high_comp_officer1_amount = models.DecimalField(max_digits=23, decimal_places=2, null=True, blank=True)
    high_comp_officer2_full_na = models.TextField(null=True, blank=True)
    high_comp_officer2_amount = models.DecimalField(max_digits=23, decimal_places=2, null=True, blank=True)
    high_comp_officer3_full_na = models.TextField(null=True, blank=True)
    high_comp_officer3_amount = models.DecimalField(max_digits=23, decimal_places=2, null=True, blank=True)
    high_comp_officer4_full_na = models.TextField(null=True, blank=True)
    high_comp_officer4_amount = models.DecimalField(max_digits=23, decimal_places=2, null=True, blank=True)
    high_comp_officer5_full_na = models.TextField(null=True, blank=True)
    high_comp_officer5_amount = models.DecimalField(max_digits=23, decimal_places=2, null=True, blank=True)
    sub_id = models.IntegerField(null=True, blank=True)
    sub_parent_id = models.IntegerField(null=True, blank=True)
    sub_federal_agency_id = models.TextField(null=True, blank=True)
    sub_federal_agency_name = models.TextField(null=True, blank=True)
    sub_funding_agency_id = models.TextField(null=True, blank=True)
    sub_funding_agency_name = models.TextField(null=True, blank=True)
    sub_funding_office_id = models.TextField(null=True, blank=True)
    sub_funding_office_name = models.TextField(null=True, blank=True)
    sub_naics = models.TextField(null=True, blank=True)
    sub_cfda_numbers = models.TextField(null=True, blank=True)
    sub_dunsplus4 = models.TextField(null=True, blank=True)
    sub_recovery_subcontract_amt = models.TextField(null=True, blank=True)
    sub_recovery_model_q1 = models.BooleanField(null=True, blank=True)
    sub_recovery_model_q2 = models.BooleanField(null=True, blank=True)
    sub_compensation_q1 = models.BooleanField(null=True, blank=True)
    sub_compensation_q2 = models.BooleanField(null=True, blank=True)
    place_of_perform_street = models.TextField(null=True, blank=True)
    sub_place_of_perform_street = models.TextField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = "broker_subaward"
