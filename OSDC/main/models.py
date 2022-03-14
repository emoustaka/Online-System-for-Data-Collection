from django.db import models
from django.contrib.auth.models import User, Group
from datetime import datetime

# Create your models here.

class PersonalData(models.Model):
    OTHER = 'O'
    
    FEMALE = 'F'
    MALE = 'M'

    L_MANDARIN_CHINESE = 'C'
    L_ENGLISH = 'E'
    L_HINDUSTANI = 'H'
    L_SPANISH = 'S'
    L_ARABIC = 'A'
    L_MALAY = 'M'
    L_RUSSIAN = 'R'
    L_BENGALI ='B'
    L_PORTUGUESE = 'P'
    L_FRENCH ='F'
    L_GERMAN = 'G'
    L_JAPANESE = 'J'
    L_ITALIAN = 'I'

    CAUCASIAN = 'C'
    YELLOW = 'Y'
    LATINOAMERICAN = 'L'
    BLACK = 'B'

    PRIMARY_SCHOOL_GRADUATE = 'S'
    HIGHT_SCHOOL_GRADUATE = 'H'
    JUNIOR_HIGHT_SCHOOL_GRADUATE = 'J'
    HIGHER_TECHNOLOGICAL_EDUCATION = 'T'
    HIGHER_EDUCATION = 'E'
    MASTER = 'M'
    PHD = 'P'

    STATE_HEALTH_INSURANCE = 'S'
    PRIVATE_HEALTH_INSURANCE = 'P'
    STATE_AND_PRIVATE_HEALTH_INSURANCE = 'I'
    WELFARE = 'W'
    NONE = 'N'

    MARRIED = 'M'
    SINGLE = 'S'
    DIVORCED = 'D'
    WIDOWER = 'W'

    MANAGEMENT_BUSINESS_AND_FINANCIAL_OCUPATIONS = 'B'
    PROFESSIONAL_AND_RELATED_OCUPATIONS = 'L'
    SERVICE_OCUPATIONS = 'S'
    SALES_AND_RELATED_OCUPATIONS = 'D'
    OFFICE_AND_ADMINISTRATIVE_SUPPORT_OCUPATIONS = 'O'
    FARMING_FISHING_AND_FORESTRY_OCUPATIONS = 'F'
    CONSTRACTION_AND_EXTRACTIONS_OCUPATIONS = 'C'
    INSTALLATION_MAINTENANCE_AND_REPAIR_OCCUPATIONS = 'I'
    PRODUCTION_OCUPATIONS = 'P'
    TRANSPORTATION_AND_MATERIAL_MOVING_OCUPATIONS = 'T'
    ARMED_FORCES = 'A'
    UNOCUPIED = 'U'

    AFGHAN = 'AF'
    ALBANIAN = 'AN'
    ALGERIAN = 'AL'
    AMERICAN = 'AM'
    ANDORRAN = 'AD'
    ANGOLAN = 'AO'
    ANGUILLAN = 'AI'
    CITIZEN_OF_ANTIGUA_AND_BARBUDA = 'AB'
    ARGENTINE = 'AG'
    ARMENIAN = 'AR'
    AUSTRALIAN = 'AS'
    AUSTRIAN = 'AU'
    AZERBAIJANI = 'AZ'

    BAHAMIAN = 'BI'
    BAHRAINI = 'BA'
    BANGLADESHI = 'BC'
    BARBADIAN = 'BB'
    BELARUSIAN = 'BS'
    BELGIAN = 'BG'
    BELIZEAN = 'BI'
    BENINESE = 'BE'
    BERMUDIAN = 'BD'
    BHUTANESE = 'BT'
    BOLIVIAN = 'BO'
    CITIZEN_OF_BOSNIA_AND_HERZEGOVINA = 'BH'
    BOTSWANAN = 'BW'
    BRAZILIAN = 'BZ'
    BRITISH = 'BR'
    BRITISH_VIRGIN_ISLANDER = 'BV'
    BRUNEIAN = 'BN'
    BULGARIAN = 'BL'
    BURKINAN = 'BK'
    BURMESE = 'BM'
    BURUNDIAN = 'BU'

    CAMBODIAN = 'CI'
    CAMEROONIAN = 'CM'
    CANADIAN = 'CN'
    CAPE_VERDEAN = 'CV'
    CAYMAN_ISLANDER = 'CS'
    CENTRAL_AFRICAN = 'CF'
    CHADIAN = 'CA'
    CHILEAN = 'CE'
    CHINESE = 'CH'
    COLOMBIAN = 'CL'
    COMORAN = 'CO'
    CONGOLESE_CONGO = 'CC'
    CONGOLESE_DRC = 'CD'
    COOK_ISLANDER = 'CK'
    COSTA_RICAN = 'CR'
    CROATIAN = 'CT'
    CUBAN = 'CU'
    CYMRAES = 'CY'
    CYMRO = 'CB'
    CYPRIOT = 'CP'
    CZECH = 'CZ'

    DANISH = 'DA'
    DJIBOUTIAN = 'DJ'
    DOMINICAN = 'DO'
    CITIZEN_OF_THE_DOMINICAN_REPUBLIC = 'DR'
    DUTCH = 'DU'

    EAST_TIMORESE = 'ET'
    ECUADOREAN = 'EC'
    EGYPTIAN = 'EG'
    EMIRATI = 'EM'
    ENGLISH = 'EN'
    EQUATORIAL_GUINEAN = 'EQ'
    ERITREAN = 'ER'
    ESTONIAN = 'ES'
    ETHIOPIAN = 'EH'

    FAROESE = 'FA'
    FIJIAN = 'FJ'
    FILIPINO = 'FL'
    FINNISH = 'FN'
    FRENCH = 'FR'

    GABONESE = 'GB'
    GAMBIAN = 'GA'
    GEORGIAN = 'GO'
    GERMAN = 'GE'
    GHANAIAN = 'GH'
    GIBRALTARIAN = 'GI'
    GREENLANDIC = 'GN'
    GRENADIAN = 'GD'
    GUAMANIAN = 'GZ'
    GUATEMALAN = 'GT'
    CITIZEN_OF_GUINEA_BISSAU = 'GC'
    GUINEAN = 'GU'
    GUYANESE = 'GY'

    HAITIAN = 'HA'
    HELLENIC = 'HE'
    HONDURAN = 'HO'
    HONG_KONGER = 'HK'
    HUNGARIAN = 'HU'

    ICELANDIC = 'IC'
    INDIAN = 'IN'
    INDONESIAN = 'ID'
    IRANIAN = 'IR'
    IRAQI = 'IQ'
    IRISH = 'IH'
    ISRAELI = 'IS'
    ITALIAN = 'IT'
    IVORIAN = 'IV'

    JAMAICAN = 'JM'
    JAPANESE = 'JP'
    JORDANIAN = 'JO'

    KAZAKH = 'KA'
    KENYAN = 'KE'
    KITTITIAN = 'KT'
    CITIZEN_OF_KIRIBATI = 'KR'
    KOSOVAN = 'KO'
    KUWAITI = 'KU'
    KYRGYZ = 'KY'

    LAO = 'LO'
    LATVIAN = 'LT'
    LEBANESE = 'LA'
    LIBERIAN = 'LB'
    LIBYAN = 'LY'
    LICHTENSTEIN_CITIZEN = 'LC'
    LITHUANIAN = 'LI'
    LUXEMBOURGER = 'LU'

    MACANESE = 'MC'
    MALAGASY = 'ML'
    MALAWIAN = 'MW'
    MALAYSIAN = 'MY'
    MALDIVIAN = 'MD'
    MALIAN = 'MF'
    MALTESE = 'MJ'
    MARSHALLESE = 'MH'
    MARTINIQUAIS = 'MK'
    MAURITANIAN = 'MA'
    MAURITIAN = 'MU'
    MEXICAN = 'ME'
    MICRONESIAN = 'MI'
    MOLDOVAN = 'MO'
    MONEGASQUE = 'MQ'
    MONGOLIAN = 'MG'
    MONTENEGRIN = 'MT'
    MONTSERRATIAN = 'MN'
    MOROCCAN = 'MR'
    MOSOTHO = 'MS'
    MOZAMBICAN = 'MZ'

    NAMIBIAN = 'NM'
    NAURUAN = 'NU'
    NEPALESE = 'NP'
    NEW_ZEALANDER = 'NZ'
    NICARAGUAN = 'NC'
    NIGERIAN = 'NA'
    NIGERIEN = 'NE'
    NIUEAN = 'NN'
    NORTH_KOREAN = 'NK'
    NORTH_MACEDONIAN = 'ND'
    NORTHERN_IRISH = 'NI'
    NORWEGIAN = 'NO'

    OMANI = 'OM'

    PAKISTANI = 'PK'
    PALAUAN = 'PA'
    PALESTINIAN = 'PS'
    PANAMANIAN = 'PM'
    PAPUA_NEW_GUINEAN = 'PG'
    PARAGUAYAN = 'PY'
    PERUVIAN = 'PE'
    PITCAIRN_ISLANDER = 'PI'
    POLISH = 'PL'
    PORTUGUESE = 'PO'
    PRYDEINIG = 'PR'
    PUERTO_RICAN = 'PU'

    QATARI = 'QA'

    ROMANIAN = 'RO'
    RUSSIAN = 'RU'
    RWANDAN = 'RW'

    SALVADORIAN = 'SV'
    SAMMARINESE = 'SM'
    SAMOAN = 'SA'
    SAO_TOMEAN = 'ST'
    SAUDI_ARABIAN = 'SB'
    SCOTTISH = 'SC'
    SENEGALESE = 'SG'
    SERBIAN = 'SE'
    CITIZEN_OF_SEYCHELLES = 'SJ'
    SIERRA_LEONEAN = 'SL'
    SINGAPOREAN = 'SN'
    SLOVAK = 'SK'
    SLOVENIAN = 'SO'
    SOLOMON_ISLANDER = 'SI'
    SOMALI = 'SM'
    SOUTH_AFRICAN = 'SF'
    SOUTH_KOREAN = 'S_'
    SOUTH_SUNDANESE = 'SS'
    SPANISH = 'SP'
    SRI_LANKAN = 'S-'
    ST_HELENIAN = 'SH'
    ST_LUCIAN = 'SU'
    STATELESS = 'SQ'
    SUDANESE = 'SD'
    SURINAMESE = 'SR'
    SWAZI = 'SZ'
    SWEDISH = 'S+'
    SWISS = 'SW'
    SYRIAN = 'SY'

    TAIWANESE = 'TA'
    TAJIK = 'TJ'
    TANZANIAN = 'TN'
    THAI = 'TH'
    TOGOLESE = 'TG'
    TONGAN = 'TO'
    TRINIDADIAN = 'TR'
    TRISTANIAN = 'TS'
    TUNISIAN = 'TI'
    TURKISH = 'TK'
    TURKMEN = 'TM'
    TURKS_AND_CAICOS_ISLANDER = 'TC'
    TUVALUAN = 'TV'

    UGANDAN = 'UG'
    UKRAINIAN = 'UK'
    URUGUAYAN = 'UR'
    UZBEK = 'UZ'

    VATICAN_CITIZEN = 'VT'
    CITIZEN_OF_VANUATU = 'VN'
    VENEZUELAN = 'VE'
    VIETNAMESE = 'VS'
    VINCENTIAN = 'VI'

    WALLISIAN = 'WA'
    WELSH = 'WE'

    YEMENI = 'YE'

    ZAMBIAN = 'ZA'
    ZIMBABWEAN = 'ZI'

    GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (OTHER, 'Other')
    )
    FAMILY_CHOICES = (
        (MARRIED, 'Married'),
        (SINGLE, 'Single'),
        (DIVORCED, 'Divorced'),
        (WIDOWER, 'Widower')
    )
    NATIONALITY_CHOICES = (
        (AFGHAN, 'Afghan'),
        (ALBANIAN, 'Albanian'),
        (ALGERIAN, 'Algerian'),
        (AMERICAN, 'American'),
        (ANDORRAN, 'Andorran'),
        (ANGOLAN, 'Angolan'),
        (ANGUILLAN, 'Anguillan'),
        (CITIZEN_OF_ANTIGUA_AND_BARBUDA, 'Citizen of Antigua and Barbuda'),
        (ARGENTINE, 'Argentine'),
        (ARMENIAN, 'Armenian'),
        (AUSTRALIAN, 'Australian'),
        (AUSTRIAN, 'Austrian'),
        (AZERBAIJANI, 'Azerbaijani'),
        (BAHAMIAN, 'Bahamian'),
        (BAHRAINI, 'Bahraini'),
        (BANGLADESHI, 'Bangladeshi'),
        (BARBADIAN, 'Barbadian'),
        (BELARUSIAN, 'Belarusian'),
        (BELGIAN, 'Belgian'),
        (BELIZEAN, 'Belizean'),
        (BENINESE, 'Beninese'),
        (BERMUDIAN, 'Bermudian'),
        (BHUTANESE, 'Bhutanese'),
        (BOLIVIAN, 'Bolivian'),
        (CITIZEN_OF_BOSNIA_AND_HERZEGOVINA, 'Citizen of Bosnia and Herzegovina'),
        (BOTSWANAN, 'Botswanan'),
        (BRAZILIAN, 'Brazilian'),
        (BRITISH, 'British'),
        (BRITISH_VIRGIN_ISLANDER, 'British Virgin Islander'),
        (BRUNEIAN, 'Bruneian'),
        (BULGARIAN, 'Bulgarian'),
        (BURKINAN, 'Burkinan'),
        (BURMESE, 'Burmese'),
        (BURUNDIAN, 'Burundian'),
        (CAMBODIAN, 'Cambodian'),
        (CAMEROONIAN, 'Cameroonian'),
        (CANADIAN, 'Canadian'),
        (CAPE_VERDEAN, 'Cape Verdean'),
        (CAYMAN_ISLANDER, 'Cayman Islander'),
        (CENTRAL_AFRICAN, 'Central African'),
        (CHADIAN, 'Chadian'),
        (CHILEAN, 'Chilean'),
        (CHINESE, 'Chinese'),
        (COLOMBIAN, 'Colombian'),
        (COMORAN, 'Comoran'),
        (CONGOLESE_CONGO, 'Congolese (Congo)'),
        (CONGOLESE_DRC, 'Congolese (DRC)'),
        (COOK_ISLANDER, 'Cook Islander'),
        (COSTA_RICAN, 'Costa Rican'),
        (CROATIAN, 'Croatian'),
        (CUBAN, 'Cuban'),
        (CYMRAES, 'Cymraes'),
        (CYMRO, 'Cymro'),
        (CYPRIOT, 'Cypriot'),
        (CZECH, 'Czech'),
        (DANISH, 'Danish'),
        (DJIBOUTIAN, 'Djiboutian'),
        (DOMINICAN, 'Dominican'),
        (CITIZEN_OF_THE_DOMINICAN_REPUBLIC, 'Citizen of the Dominican Republic'),
        (DUTCH, 'Dutch'),
        (EAST_TIMORESE, 'East Timorese'),
        (ECUADOREAN, 'Ecuadorean'),
        (EGYPTIAN, 'Egyptian'),
        (EMIRATI, 'Emirati'),
        (ENGLISH, 'English'),
        (EQUATORIAL_GUINEAN, 'Equatorial Guinean'),
        (ERITREAN, 'Erithrean'),
        (ESTONIAN, 'Estonian'),
        (ETHIOPIAN, 'Ethiopian'),
        (FAROESE, 'Faroese'),
        (FIJIAN, 'Fijian'),
        (FILIPINO, 'Filipino'),
        (FINNISH, 'Finnish'),
        (FRENCH, 'French'),
        (GABONESE, 'Gabonese'),
        (GAMBIAN, 'Gambian'),
        (GEORGIAN, 'Georgian'),
        (GERMAN, 'German'),
        (GHANAIAN, 'Ghanaian'),
        (GIBRALTARIAN, 'Gibraltarian'),
        (GREENLANDIC, 'Greenlandic'),
        (GRENADIAN, 'Grenadian'),
        (GUAMANIAN, 'Guamanian'),
        (GUATEMALAN, 'Guatemalan'),
        (CITIZEN_OF_GUINEA_BISSAU, 'Citizen of Guinea Bissau'),
        (GUINEAN, 'Guinean'),
        (GUYANESE, 'Guyanese'),
        (HAITIAN, 'Haitian'),
        (HELLENIC, 'Hellenic'),
        (HONDURAN, 'Honduran'),
        (HONG_KONGER, 'Honk Konger'),
        (HUNGARIAN, 'Hungarian'),
        (ICELANDIC, 'Icelandic'),
        (INDIAN, 'Indian'),
        (INDONESIAN, 'Indonesian'),
        (IRANIAN, 'Iranian'),
        (IRAQI, 'Iraqi'),
        (IRISH, 'Irish'),
        (ISRAELI, 'Israeli'),
        (ITALIAN, 'Italian'),
        (IVORIAN, 'Ivorian'),
        (JAMAICAN, 'Jamaican'),
        (JAPANESE, 'Japanese'),
        (JORDANIAN, 'Jordanian'),
        (KAZAKH, 'Kazakh'),
        (KENYAN, 'Kenyan'),
        (KITTITIAN, 'Kittitian'),
        (CITIZEN_OF_KIRIBATI, 'Citizen of Kiribati'),
        (KOSOVAN, 'Kosovan'),
        (KUWAITI, 'Kuwaiti'),
        (KYRGYZ, 'Kyrgyz'),
        (LAO, 'Lao'),
        (LATVIAN, 'Latvian'),
        (LEBANESE, 'Lebanese'),
        (LIBERIAN, 'Liberian'),
        (LIBYAN, 'Libyan'),
        (LICHTENSTEIN_CITIZEN, 'Lichtenstein citizen'),
        (LITHUANIAN, 'Lithuanian'),
        (LUXEMBOURGER, 'Luxembourger'),
        (MACANESE, 'Macanese'),
        (MALAGASY, 'Malagasy'),
        (MALAWIAN, 'Malawian'),
        (MALAYSIAN, 'Malaysian'),
        (MALDIVIAN, 'Maldivian'),
        (MALIAN, 'Malian'),
        (MALTESE, 'Maltese'),
        (MARSHALLESE, 'Marshallese'),
        (MARTINIQUAIS, 'Martiniquais'),
        (MAURITANIAN, 'Mauritanian'),
        (MAURITIAN, 'Mauritian'),
        (MEXICAN, 'Mexican'),
        (MICRONESIAN, 'Micronesian'),
        (MOLDOVAN, 'Moldovan'),
        (MONEGASQUE, 'Monegasque'),
        (MONGOLIAN, 'Mongolian'),
        (MONTENEGRIN, 'Montenegrin'),
        (MONTSERRATIAN, 'Montserratian'),
        (MOROCCAN, 'Moroccan'),
        (MOSOTHO, 'Mosotho'),
        (MOZAMBICAN, 'Mozambican'),
        (NAMIBIAN, 'Namibian'),
        (NAURUAN, 'Nauruan'),
        (NEPALESE, 'Nepalese'),
        (NEW_ZEALANDER, 'New Zealander'),
        (NICARAGUAN, 'Nicaraguan'),
        (NIGERIAN, 'Nigerian'),
        (NIGERIEN, 'Nigerien'),
        (NIUEAN, 'Niuean'),
        (NORTH_KOREAN, 'North Korean'),
        (NORTH_MACEDONIAN, 'North Macedonian'),
        (NORTHERN_IRISH, 'Northern Irish'),
        (NORWEGIAN, 'Norwegian'),
        (OMANI, 'Omani'),
        (PAKISTANI, 'Pakistani'),
        (PALAUAN, 'Palauan'),
        (PALESTINIAN, 'Palestinian'),
        (PANAMANIAN, 'Panamanian'),
        (PAPUA_NEW_GUINEAN, 'Papua New Guinean'),
        (PARAGUAYAN, 'Paraguayan'),
        (PERUVIAN, 'Peruvian'),
        (PITCAIRN_ISLANDER, 'Pitcairn Islander'),
        (POLISH, 'Polish'),
        (PORTUGUESE, 'Portuguese'),
        (PRYDEINIG, 'Prydeinig'),
        (PUERTO_RICAN, 'Puerto Rican'),
        (QATARI, 'Qatari'),
        (ROMANIAN, 'Romanian'),
        (RUSSIAN, 'Russian'),
        (RWANDAN, 'Rwandan'),
        (SALVADORIAN, 'Salvadorian'),
        (SAMMARINESE, 'Sammarinese'),
        (SAMOAN, 'Samoan'),
        (SAO_TOMEAN, 'Sao Tomean'),
        (SAUDI_ARABIAN, 'Saudi Arabian'),
        (SCOTTISH, 'Scottish'),
        (SENEGALESE, 'Senegalese'),
        (SERBIAN, 'Serbian'),
        (CITIZEN_OF_SEYCHELLES, 'Citizen of Seychelles'),
        (SIERRA_LEONEAN, 'Sierra Leonean'),
        (SINGAPOREAN, 'Singaporean'),
        (SLOVAK, 'Slovak'),
        (SLOVENIAN, 'Slovenian'),
        (SOLOMON_ISLANDER, 'Solomon Islander'),
        (SOMALI, 'Somali'),
        (SOUTH_AFRICAN, 'South African'),
        (SOUTH_KOREAN, 'South Korean'),
        (SOUTH_SUNDANESE, 'South Sundanese'),
        (SPANISH, 'Spanish'),
        (SRI_LANKAN, 'Sri Lankan'),
        (ST_HELENIAN, 'St Helenian'),
        (ST_LUCIAN, 'St Lucian'),
        (STATELESS, 'Stateless'),
        (SUDANESE, 'Sudanese'),
        (SURINAMESE, 'Surinamese'),
        (SWAZI, 'Swazi'),
        (SWEDISH, 'Swedish'),
        (SWISS, 'Swiss'),
        (SYRIAN, 'Syrian'),
        (TAIWANESE, 'Taiwanese'),
        (TAJIK, 'Tajik'),
        (TANZANIAN, 'Tanzanian'),
        (THAI, 'Thai'),
        (TOGOLESE, 'Togolese'),
        (TONGAN, 'Tongan'),
        (TRINIDADIAN, 'Trinidadian'),
        (TRISTANIAN, 'Tristanian'),
        (TUNISIAN, 'Tunisian'),
        (TURKISH, 'Turkish'),
        (TURKMEN, 'Turkmen'),
        (TURKS_AND_CAICOS_ISLANDER, 'Turks and Caicos Islander'),
        (TUVALUAN, 'Tuvaluan'),
        (UGANDAN, 'Ugandan'),
        (UKRAINIAN, 'Ukrainian'),
        (URUGUAYAN, 'Uruguayan'),
        (UZBEK, 'Uzbek'),
        (VATICAN_CITIZEN, 'Vatican citizen'),
        (CITIZEN_OF_VANUATU, 'Citizen of Vanuatu'),
        (VENEZUELAN, 'Venezuelan'),
        (VIETNAMESE, 'Vietnamese'),
        (VINCENTIAN, 'Vincentian'),
        (WALLISIAN, 'Wallisian'),
        (WELSH, 'Welsh'),
        (YEMENI, 'Yemeni'),
        (ZAMBIAN, 'Zambian'),
        (ZIMBABWEAN, 'Zimbabwean')
    )
    RACE_CHOICES = (
        (CAUCASIAN, 'Caucasian'),
        (YELLOW, 'Yellow'),
        (LATINOAMERICAN, 'Latino-American'),
        (BLACK, 'Black')
    )
    LANGUAGE_CHOICES = (
        (L_MANDARIN_CHINESE, 'Mandarin Chinese'),
        (L_ENGLISH, 'English'),
        (L_HINDUSTANI, 'Hindustani'),
        (L_SPANISH, 'Spanish'),
        (L_ARABIC, 'Arabic'),
        (L_MALAY, 'Malay'),
        (L_RUSSIAN, 'Russian'),
        (L_BENGALI, 'Bengali'),
        (L_PORTUGUESE, 'Portuguese'),
        (L_FRENCH, 'French'),
        (L_GERMAN, 'German'),
        (L_JAPANESE, 'Japanese'),
        (L_ITALIAN, 'Italian'),
        (OTHER, 'Other')
    )
    OCCUPATION_CHOICES = (
        (MANAGEMENT_BUSINESS_AND_FINANCIAL_OCUPATIONS, 'Management, business and financial ocupations'),
        (PROFESSIONAL_AND_RELATED_OCUPATIONS, 'Professional and related ocupations'),
        (SERVICE_OCUPATIONS, 'Service ocupations'),
        (SALES_AND_RELATED_OCUPATIONS, 'Sales and related ocupations'),
        (OFFICE_AND_ADMINISTRATIVE_SUPPORT_OCUPATIONS, 'Officw and administrative support ocupation'),
        (FARMING_FISHING_AND_FORESTRY_OCUPATIONS, 'Farming, fishing and forestry ocupations'),
        (CONSTRACTION_AND_EXTRACTIONS_OCUPATIONS, 'Constraction and extractions ocupations'),
        (INSTALLATION_MAINTENANCE_AND_REPAIR_OCCUPATIONS, 'Installation, maintenance and repair ocupations'),
        (PRODUCTION_OCUPATIONS, 'Production ocupations'),
        (TRANSPORTATION_AND_MATERIAL_MOVING_OCUPATIONS, 'Transportation and material moving ocupations'),
        (ARMED_FORCES, 'Armed forces'),
        (UNOCUPIED, 'Unocupied')
    )
    EDUCATION_CHOICES = (
        (PRIMARY_SCHOOL_GRADUATE, 'Primary school graduate'),
        (HIGHT_SCHOOL_GRADUATE, 'Hight school graduate'),
        (JUNIOR_HIGHT_SCHOOL_GRADUATE, 'Junior hight school graduate'),
        (HIGHER_TECHNOLOGICAL_EDUCATION, 'Higher technological education'),
        (HIGHER_EDUCATION, 'Higher education'),
        (MASTER, 'Master'),
        (PHD, 'Phd')
    )
    INSURANCE_CHOICES = (
        (STATE_HEALTH_INSURANCE, 'State health insurance'),
        (PRIVATE_HEALTH_INSURANCE, 'Private health insurance'),
        (STATE_AND_PRIVATE_HEALTH_INSURANCE, 'State and private health insurance'),
        (WELFARE, 'Welfare'),
        (NONE, 'None')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="personaldata", null=True)
    lastName = models.CharField(max_length=200, default='NULL')
    firstName = models.CharField(max_length=200, default='NULL')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='NULL')
    dateOfBirth = models.DateField(default='NULL')
    telephone = models.CharField(max_length=20, default='NULL')
    email = models.CharField(max_length=200, default='NULL')
    familySituation = models.CharField(max_length=1, choices=FAMILY_CHOICES, default='NULL')
    nationality = models.CharField(max_length=2, choices=NATIONALITY_CHOICES, default='NULL')
    race = models.CharField(max_length=1, choices=RACE_CHOICES, default='NULL')
    language = models.CharField(max_length=1, choices=LANGUAGE_CHOICES, default='NULL')
    occupation = models.CharField(max_length=1, choices=OCCUPATION_CHOICES, default='NULL')
    education = models.CharField(max_length=1, choices=EDUCATION_CHOICES, default='NULL')
    healthInsurance = models.CharField(max_length=1, choices=INSURANCE_CHOICES, default='NULL')
    dateOfUpdate = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ['user']

    def __str__(self):
        return '%s' % (self.user)

class CurrentTreatment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="currenttreatment", null=True)
    text = models.CharField(max_length=200)
    dateOfUpdate = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ['user']

    def __str__(self):
        return '%s' % (self.user)

class Tuberculosis(models.Model):
    ACTIVE = 'A'
    LATEND = 'L'

    SMEAR_MICROSCOPY = 'S'
    XPERT_RIF = 'X'
    LAM = 'L'
    TST = 'T'
    IGRAS = 'I'
    ODYSSEE = 'O'

    TYPE_CHOICES = (
        (ACTIVE, 'Active'),
        (LATEND, 'Latend')
    )

    METHOD_CHOICES = (
        (SMEAR_MICROSCOPY, 'Smear Microscopy'),
        (XPERT_RIF, 'XPERT/RIF'),
        (LAM, 'Lypoarabinomannan (LAM) Test'),
        (TST, 'Tuberculin Skin Test (TST)'),
        (IGRAS, 'Interferon Gamma Release Assays (IGRAs)'),
        (ODYSSEE, 'ODYSSEE')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tuberculosis", null=True)
    typeOfTB = models.CharField(max_length=1, choices=TYPE_CHOICES)
    vaccinationForTB = models.BooleanField()
    antibioticConsumption = models.BooleanField()
    numberOfPeopleWithTB = models.IntegerField()
    diagnosticMethodUndertaken = models.CharField(max_length=1, choices=METHOD_CHOICES)
    dateOfUpdate = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ['user']

    def __str__(self):
        return '%s' % (self.user)

class Vaccinations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vaccinations", null=True)
    chickenpox = models.BooleanField(default=False)
    dt = models.BooleanField(default=False)
    dtap = models.BooleanField(default=False)
    td = models.BooleanField(default=False)
    tdap = models.BooleanField(default=False)
    flu = models.BooleanField(default=False)
    hav = models.BooleanField(default=False)
    hbv = models.BooleanField(default=False)
    hib = models.BooleanField(default=False)
    hpv = models.BooleanField(default=False)
    mmr = models.BooleanField(default=False)
    meningococcal = models.BooleanField(default=False)
    pcv13 = models.BooleanField(default=False)
    ppsv23 = models.BooleanField(default=False)
    ipv = models.BooleanField(default=False)
    opv = models.BooleanField(default=False)
    rotavirus = models.BooleanField(default=False)
    rzv = models.BooleanField(default=False)
    bcg = models.BooleanField(default=False)
    tyfoidFever = models.BooleanField(default=False)
    yellowFever = models.BooleanField(default=False)
    covid19 = models.BooleanField(default=False)

    chickenpoxD = models.DateField(null=True)
    dtD = models.DateField(null=True)
    dtapD = models.DateField(null=True)
    tdD = models.DateField(null=True)
    tdapD = models.DateField(null=True)
    fluD = models.DateField(null=True)
    havD = models.DateField(null=True)
    hbvD = models.DateField(null=True)
    hibD = models.DateField(null=True)
    hpvD = models.DateField(null=True)
    mmrD = models.DateField(null=True)
    meningococcalD = models.DateField(null=True)
    pcv13D = models.DateField(null=True)
    ppsv23D = models.DateField(null=True)
    ipvD = models.DateField(null=True)
    opvD = models.DateField(null=True)
    rotavirusD = models.DateField(null=True)
    rzvD = models.DateField(null=True)
    bcgD = models.DateField(null=True)
    tyfoidFeverD = models.DateField(null=True)
    yellowFeverD = models.DateField(null=True)
    covid19D = models.DateField(null=True)

    dateOfUpdate = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ['user']

    def __str__(self):
        return '%s' % (self.user)

class MedicalHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="medicalhistory", null=True)
    diseses = models.CharField(max_length=200, default='NULL', null=True)
    dailyMedication = models.CharField(max_length=200, default='NULL')
    cancerOrTumor = models.BooleanField(default=False)
    bloodTransfusions = models.BooleanField(default=False)
    allergies = models.CharField(max_length=200, default='NULL')
    surgeries = models.CharField(max_length=200, default='NULL')
    dateOfUpdate = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ['user']

    def __str__(self):
        return '%s' % (self.user)

class ClinicalExamination(models.Model):
    HOSPITAL_CHOICES = (

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clinicalexamination", null=True)
    height = models.IntegerField(default='0')
    weight = models.FloatField(default='0')
    weistline = models.FloatField(default='0')
    bmi = models.FloatField(default='0')
    systolic = models.IntegerField(default='0')
    diastolic = models.IntegerField(default='0')
    pulse = models.IntegerField(default='0')
    respiratoryRythm = models.IntegerField(default='0')
    temperature = models.FloatField(default='0')
    hospital = models.CharField(max_length=1, choices=HOSPITAL_CHOICES)
    dateOfUpdate = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ['user']

    def __str__(self):
        return '%s' % (self.user)

class DoctorsComments(models.Model):
    EXCELENT = 'E'
    MODERATE = 'M'
    CRITICAL = 'C'
    URGENT = 'U'
    CONDITION_CHOICES = (
        (EXCELENT, 'Excelent'),
        (MODERATE, 'Moderate'),
        (CRITICAL, 'Critical'),
        (URGENT, 'Urgent')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctorscomments", null=True)
    general = models.CharField(max_length=1, choices=CONDITION_CHOICES, default='NULL')
    hearing = models.CharField(max_length=1, choices=CONDITION_CHOICES, default='NULL')
    vision = models.CharField(max_length=1, choices=CONDITION_CHOICES, default='NULL')
    respiratoryTract = models.CharField(max_length=1, choices=CONDITION_CHOICES, default='NULL')
    heart = models.CharField(max_length=1, choices=CONDITION_CHOICES, default='NULL')
    chest = models.CharField(max_length=1, choices=CONDITION_CHOICES, default='NULL')
    lungs = models.CharField(max_length=1, choices=CONDITION_CHOICES, default='NULL')
    abdomen = models.CharField(max_length=1, choices=CONDITION_CHOICES, default='NULL')
    myoskeleticalSystem = models.CharField(max_length=1, choices=CONDITION_CHOICES, default='NULL')
    limbs = models.CharField(max_length=1, choices=CONDITION_CHOICES, default='NULL')
    skin = models.CharField(max_length=1, choices=CONDITION_CHOICES, default='NULL')
    nervousSystem = models.CharField(max_length=1, choices=CONDITION_CHOICES, default='NULL')
    dateOfUpdate = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ['user']

    def __str__(self):
        return '%s' % (self.user)

class GynecologicalHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gynecologicalhistory", null=True)
    startAge = models.IntegerField()
    endAge = models.IntegerField()
    numOfChildren = models.IntegerField()
    endometriosis = models.BooleanField()
    polycysticOvarySyndrome = models.BooleanField()
    hormonalContraceptiveTherapy = models.IntegerField()
    hormoneTherapyPregnancy = models.IntegerField()
    notCompletedPregnancies = models.IntegerField()
    dateOfUpdate = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ['user']

    def __str__(self):
        return '%s' % (self.user)

class SocialHabits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="socialhabits", null=True)
    startAge = models.IntegerField()
    endAge = models.IntegerField()
    smokingYears = models.IntegerField()
    numOfPacksOfCigarettes = models.IntegerField()
    numOfAlcoholGlasses = models.IntegerField()
    dateOfUpdate = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ['user']

    def __str__(self):
        return '%s' % (self.user)