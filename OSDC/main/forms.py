from django import forms
from .models import CurrentTreatment, Tuberculosis, Vaccinations, MedicalHistory, ClinicalExamination, DoctorsComments, PersonalData, GynecologicalHistory, SocialHabits
from bootstrap_datepicker_plus import DatePickerInput
import datetime

class Vaccines(forms.Form):
    chickenpox = forms.BooleanField(label="Chickenpox", required=False)
    dt = forms.BooleanField(label="DT", required=False)
    dtap = forms.BooleanField(label="DTaP", required=False)
    td = forms.BooleanField(label="Td", required=False)
    tdap = forms.BooleanField(label="Tdap", required=False)
    flu = forms.BooleanField(label="Flu", required=False)
    hav = forms.BooleanField(label="HAV", required=False)
    hbv = forms.BooleanField(label="HBV", required=False)
    hib = forms.BooleanField(label="Hib", required=False)
    hpv = forms.BooleanField(label="HPV", required=False)
    mmr = forms.BooleanField(label="MMR", required=False)
    meningococcal = forms.BooleanField(label="Meningococcal", required=False)
    pcv13 = forms.BooleanField(label="PCV13", required=False)
    ppsv23 = forms.BooleanField(label="PPSV23", required=False)
    ipv = forms.BooleanField(label="IPV", required=False)
    opv = forms.BooleanField(label="OPV", required=False)
    rotavirus = forms.BooleanField(label="Rotavirus", required=False)
    rzv = forms.BooleanField(label="RZV", required=False)
    bcg = forms.BooleanField(label="BCG", required=False)
    tyfoidFever = forms.BooleanField(label="Typhoid fever", required=False)
    yellowFever = forms.BooleanField(label="Yellow fever", required=False)
    covid19 = forms.BooleanField(label="Covid-19", required=False)


    chickenpoxD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    dtD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    dtapD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    tdD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    tdapD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    fluD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    havD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    hbvD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    hibD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    hpvD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    mmrD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    meningococcalD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    pcv13D = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    ppsv23D = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    ipvD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    opvD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    rotavirusD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    rzvD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    bcgD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    tyfoidFeverD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    yellowFeverD = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    covid19D = forms.DateField(label="Date", required=False, initial=None, widget=forms.widgets.DateInput(attrs={'type': 'date'}))

class ClinicEx(forms.Form):
    ACTIVE = 'A'
    LATEND = 'L'

    HOSPITAL_CHOICES = (
        (ACTIVE, 'Active'),
        (LATEND, 'Latend'),
    )

    height = forms.IntegerField(label="Height (cm)")
    weight = forms.FloatField(label="Weight (kg)")
    weistline = forms.FloatField(label="Weistline (cm)")
    bmi = forms.FloatField(label="Body Mass Index")
    systolic = forms.IntegerField(label="Blood pressure repetition: Systolic (mmHg)")
    diastolic = forms.IntegerField(label="Blood pressure repetition: Diastolyc (mmHg)")
    pulse = forms.IntegerField(label="Pulse (/min)")
    respiratoryRythm = forms.IntegerField(label="Respiratory rythm (/min)")
    temperature = forms.FloatField(label="Temperature (C)")
    hospital = forms.ChoiceField(label="Hospital", choices = HOSPITAL_CHOICES)

class CurTreatment(forms.Form):
    text = forms.CharField(max_length=200, widget=forms.Textarea)

class DocComments(forms.Form):
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
    general = forms.ChoiceField(label="General condition and diet",  choices = CONDITION_CHOICES)
    hearing = forms.ChoiceField(label="Hearing", choices = CONDITION_CHOICES)
    vision = forms.ChoiceField(label="Vision", choices = CONDITION_CHOICES)
    respiratoryTract = forms.ChoiceField(label="Respiratory tract", choices = CONDITION_CHOICES)
    heart = forms.ChoiceField(label="Heart", choices = CONDITION_CHOICES)
    chest = forms.ChoiceField(label="Chest", choices = CONDITION_CHOICES)
    lungs = forms.ChoiceField(label="Lungs", choices = CONDITION_CHOICES)
    abdomen = forms.ChoiceField(label="Abdomen", choices = CONDITION_CHOICES)
    myoskeleticalSystem = forms.ChoiceField(label="Myoskeletical system", choices = CONDITION_CHOICES)
    limbs = forms.ChoiceField(label="Limbs", choices = CONDITION_CHOICES)
    skin = forms.ChoiceField(label="Skin", choices = CONDITION_CHOICES)
    nervousSystem = forms.ChoiceField(label="Nervous system", choices = CONDITION_CHOICES)

class MedHist(forms.Form):
    diseses = forms.CharField(label="Diseases", max_length=200, required=False)
    dailyMedication = forms.CharField(label="Daily medication", max_length=200, required=False)
    cancerOrTumor = forms.BooleanField(label="History of cancer or tumor", required=False)
    bloodTransfusions = forms.BooleanField(label="History of blood transfusions", required=False)
    allergies = forms.CharField(label="Allergies", max_length=200, required=False)
    surgeries = forms.CharField(label="Surgeries", max_length=200, required=False)

class Tb(forms.Form):
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
        (LATEND, 'Latend'),
    )

    METHOD_CHOICES = (
        (SMEAR_MICROSCOPY, 'Smear Microscopy'),
        (XPERT_RIF, 'XPERT/RIF'),
        (LAM, 'Lypoarabinomannan (LAM) Test'),
        (TST, 'Tuberculin Skin Test (TST)'),
        (IGRAS, 'Interferon Gamma Release Assays (IGRAs)'),
        (ODYSSEE, 'ODYSSEE')
    )
    typeOfTB = forms.ChoiceField(label="Diagnosed with active or latend TB", choices = TYPE_CHOICES)
    vaccinationForTB = forms.BooleanField(label="Vaccinatede against TB (When did the vaccination happen?)", required=False)
    antibioticConsumption = forms.BooleanField(label="Antibiotic consumption (What kind? For how long?", required=False)
    numberOfPeopleWithTB = forms.IntegerField(label="Family member of close person diagnosed with TB?")
    diagnosticMethodUndertaken = forms.ChoiceField(label="Type of TB diagnostic method undertaken", choices = METHOD_CHOICES)

class PerData(forms.Form):
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
    PRIMARY_SCHOOL_GRADUATE = 'PS'
    HIGHT_SCHOOL_GRADUATE = 'HS'
    JUNIOR_HIGHT_SCHOOL_GRADUATE = 'JHS'
    HIGHER_TECHNOLOGICAL_EDUCATION = 'HTE'
    HIGHER_EDUCATION = 'HE'
    MASTER = 'M'
    PHD = 'P'
    STATE_HEALTH_INSURANCE = 'S'
    PRIVATE_HEALTH_INSURANCE = 'P'
    STATE_AND_PRIVATE_HEALTH_INSURANCE = 'SP'
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
    lastName = forms.CharField(label="Last Name", max_length=200)
    firstName = forms.CharField(label="Fiirst Name", max_length=200)
    gender = forms.ChoiceField(label="Gender", choices=GENDER_CHOICES)
    dateOfBirth = forms.DateField(label="Birth Date", initial=datetime.date.today, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    telephone = forms.CharField(label="Telephone", max_length=20)
    email = forms.EmailField(label="Email address", max_length=200)
    familySituation = forms.ChoiceField(label="Family Situation", choices=FAMILY_CHOICES)
    nationality = forms.ChoiceField(label="Nationality", choices=NATIONALITY_CHOICES)
    race = forms.ChoiceField(label="Race", choices=RACE_CHOICES)
    language = forms.ChoiceField(label="Language", choices=LANGUAGE_CHOICES)
    occupation = forms.ChoiceField(label="Occupation", choices=OCCUPATION_CHOICES)
    education = forms.ChoiceField(label="Education", choices=EDUCATION_CHOICES)
    healthInsurance = forms.ChoiceField(label="Health Insurance", choices=INSURANCE_CHOICES)


class GynHist(forms.Form):
    startAge = forms.IntegerField(label="Age of onset of menstruation")
    endAge = forms.IntegerField(label="Age of offset of menopause")
    numOfChildren = forms.IntegerField(label="Number of children")
    endometriosis = forms.BooleanField(label="Hystory of endometriosis", required=False)
    polycysticOvarySyndrome = forms.BooleanField(label="History of polycystic ovary syndrome", required=False)
    hormonalContraceptiveTherapy = forms.IntegerField(label="Duration of hormonal therapy for contraception")
    hormoneTherapyPregnancy = forms.IntegerField(label="Duration of hormonal therapy to achieve pregnancy")
    notCompletedPregnancies = forms.IntegerField(label="Number of pregnancies not completed")

class SocHab(forms.Form):
    startAge = forms.IntegerField(label="Starting age of smoking")
    endAge = forms.IntegerField(label="Ending age of smoking")
    smokingYears = forms.IntegerField(label="Smoking years")
    numOfPacksOfCigarettes = forms.IntegerField(label="Number of packs of cigarets per week")
    numOfAlcoholGlasses = forms.IntegerField(label="Number of alcohol glasses per week")