import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-partner-contact",
    description="Meta package for oca-partner-contact Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-base_country_state_translatable',
        'odoo14-addon-base_location',
        'odoo14-addon-base_location_geonames_import',
        'odoo14-addon-base_location_nuts',
        'odoo14-addon-base_partner_sequence',
        'odoo14-addon-partner_address_street3',
        'odoo14-addon-partner_address_version',
        'odoo14-addon-partner_affiliate',
        'odoo14-addon-partner_company_group',
        'odoo14-addon-partner_company_type',
        'odoo14-addon-partner_contact_access_link',
        'odoo14-addon-partner_contact_age_range',
        'odoo14-addon-partner_contact_birthdate',
        'odoo14-addon-partner_contact_department',
        'odoo14-addon-partner_contact_gender',
        'odoo14-addon-partner_contact_in_several_companies',
        'odoo14-addon-partner_contact_job_position',
        'odoo14-addon-partner_contact_lang',
        'odoo14-addon-partner_contact_nationality',
        'odoo14-addon-partner_contact_personal_information_page',
        'odoo14-addon-partner_employee_quantity',
        'odoo14-addon-partner_fax',
        'odoo14-addon-partner_firstname',
        'odoo14-addon-partner_helper',
        'odoo14-addon-partner_identification',
        'odoo14-addon-partner_industry_secondary',
        'odoo14-addon-partner_iterative_archive',
        'odoo14-addon-partner_multi_relation',
        'odoo14-addon-partner_phone_extension',
        'odoo14-addon-partner_phone_secondary',
        'odoo14-addon-partner_priority',
        'odoo14-addon-partner_ref_unique',
        'odoo14-addon-partner_second_lastname',
        'odoo14-addon-partner_tier_validation',
        'odoo14-addon-partner_vat_unique',
        'odoo14-addon-portal_partner_select_all',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
