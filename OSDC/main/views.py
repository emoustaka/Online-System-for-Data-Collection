from http.cookies import SimpleCookie
from django.shortcuts import render, redirect
from .models import CurrentTreatment, Tuberculosis, Vaccinations, MedicalHistory, ClinicalExamination, DoctorsComments, PersonalData, GynecologicalHistory, SocialHabits
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Vaccines, ClinicEx, CurTreatment, DocComments, MedHist, Tb, PerData, GynHist, SocHab
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model
from datetime import datetime
from django.db.models import Avg, Max, Min, Sum


User = get_user_model()

# Create your views here.

def index(response):
    return redirect("/home")

def prg(response):
    current_user = response.user
    return render(response, "main/product_guide.html", {"current_user":current_user})
    
def base(response):
	return render(response, "main/base.html", {})

def data(response):
    active = Tuberculosis.objects.filter(typeOfTB='A').count()
    latend = Tuberculosis.objects.filter(typeOfTB='L').count()
    trueV = Tuberculosis.objects.filter(vaccinationForTB='True').count()
    falseV = Tuberculosis.objects.filter(vaccinationForTB='False').count()
    trueA = Tuberculosis.objects.filter(antibioticConsumption='True').count()
    falseA = Tuberculosis.objects.filter(antibioticConsumption='False').count()
    tdt = Vaccinations.objects.filter(dt='True').count() 
    fdt = Vaccinations.objects.filter(dt='False').count()
    tdtp = Vaccinations.objects.filter(dtp='True').count()
    fdtp = Vaccinations.objects.filter(dtp='False').count()
    tdtap = Vaccinations.objects.filter(dtap='True').count()
    fdtap = Vaccinations.objects.filter(dtap='False').count()
    ttd = Vaccinations.objects.filter(td='True').count()
    ftd = Vaccinations.objects.filter(td='False').count()
    ttdap = Vaccinations.objects.filter(tdap='True').count()
    ftdap = Vaccinations.objects.filter(tdap='False').count()
    tpolioopv = Vaccinations.objects.filter(polioOPV='True').count()
    fpolioopv = Vaccinations.objects.filter(polioOPV='False').count()
    tpolioipv = Vaccinations.objects.filter(polioIPV='True').count()
    fpolioipv = Vaccinations.objects.filter(polioIPV='False').count()
    tnmr = Vaccinations.objects.filter(nmr='True').count()
    fnmr = Vaccinations.objects.filter(nmr='False').count()
    tmeaseles = Vaccinations.objects.filter(measeles='True').count()
    fmeaseles = Vaccinations.objects.filter(measeles='False').count()
    thib = Vaccinations.objects.filter(hib='True').count()
    fhib = Vaccinations.objects.filter(hib='False').count()
    thepa = Vaccinations.objects.filter(hepA='True').count()
    fhepa = Vaccinations.objects.filter(hepA='False').count()
    thepb = Vaccinations.objects.filter(hepB='True').count()
    fhepb = Vaccinations.objects.filter(hepB='False').count()
    tchickenpox = Vaccinations.objects.filter(chickenPox='True').count()
    fchickenpox = Vaccinations.objects.filter(chickenPox='False').count()
    tflu = Vaccinations.objects.filter(flu='True').count()
    fflu = Vaccinations.objects.filter(flu='False').count()
    tpneumococcal = Vaccinations.objects.filter(pneumococcal='True').count()
    fpneumococcal = Vaccinations.objects.filter(pneumococcal='False').count()
    return render(response, "main/data1.html", {"active": active, "latend": latend, "trueV": trueV, "falseV": falseV, "trueA": trueA, "falseA": falseA,
                                                "tdt": tdt, "fdt": fdt, "tdtp": tdtp, "fdtp": fdtp, "tdtap": tdtap, "fdtap": fdtap, "ttd": ttd, "ftd": ftd,
                                                "ttdap": ttdap, "ftdap": ftdap, "tpolioopv": tpolioopv, "fpolioopv": fpolioopv, "tpolioipv": tpolioipv, "fpolioipv": fpolioipv,
                                                "tnmr": tnmr, "fnmr": fnmr, "tmeaseles": tmeaseles, "fmeaseles": fmeaseles, "thib": thib, "fhib": fhib,
                                                "thepa": thepa, "fhepa": fhepa, "thepb": thepb, "fhepb": fhepb, "tchickenpox": tchickenpox, "fchickenpox": fchickenpox,
                                                "tflu": tflu, "fflu": fflu, "tpneumococcal": tpneumococcal, "fpneumococcal": fpneumococcal})


def vdata(response):
    current_user = response.user

    tchickenpox = Vaccinations.objects.filter(chickenpox='True').count() 
    chickenpox = Vaccinations.objects.filter(chickenpox='False').count()
    fchickenpox = Vaccinations.objects.filter(chickenpoxD__isnull=True).count()
    pchickenpox = chickenpox - fchickenpox

    tdt = Vaccinations.objects.filter(dt='True').count()
    dt = Vaccinations.objects.filter(dt='False').count()
    fdt = Vaccinations.objects.filter(dtD__isnull=True).count()
    pdt = dt - fdt

    tdtap = Vaccinations.objects.filter(dtap='True').count()
    dtap = Vaccinations.objects.filter(dtap='False').count()
    fdtap = Vaccinations.objects.filter(dtapD__isnull=True).count()
    pdtap = dtap - fdtap

    ttd = Vaccinations.objects.filter(td='True').count()
    td = Vaccinations.objects.filter(td='False').count()
    ftd = Vaccinations.objects.filter(tdD__isnull=True).count()
    ptd = td - ftd

    ttdap = Vaccinations.objects.filter(tdap='True').count()
    tdap = Vaccinations.objects.filter(tdap='False').count()
    ftdap = Vaccinations.objects.filter(tdapD__isnull=True).count()
    ptdap = tdap - ftdap

    tflu = Vaccinations.objects.filter(flu='True').count()
    flu = Vaccinations.objects.filter(flu='False').count()
    fflu = Vaccinations.objects.filter(fluD__isnull=True).count()
    pflu = flu - fflu

    thav = Vaccinations.objects.filter(hav='True').count()
    hav = Vaccinations.objects.filter(hav='False').count()
    fhav = Vaccinations.objects.filter(havD__isnull=True).count()
    phav = hav - fhav

    thbv = Vaccinations.objects.filter(hbv='True').count()
    hbv = Vaccinations.objects.filter(hbv='False').count()
    fhbv = Vaccinations.objects.filter(hbvD__isnull=True).count()
    phbv = hbv - fhbv

    thib = Vaccinations.objects.filter(hib='True').count()
    hib = Vaccinations.objects.filter(hib='False').count()
    fhib = Vaccinations.objects.filter(hibD__isnull=True).count()
    phib = hib - fhib

    thpv = Vaccinations.objects.filter(hpv='True').count()
    hpv = Vaccinations.objects.filter(hpv='False').count()
    fhpv = Vaccinations.objects.filter(hpvD__isnull=True).count()
    phpv = hpv - fhpv

    tmmr = Vaccinations.objects.filter(mmr='True').count()
    mmr = Vaccinations.objects.filter(mmr='False').count()
    fmmr = Vaccinations.objects.filter(mmrD__isnull=True).count()
    pmmr = mmr -fmmr

    tmeningococcal = Vaccinations.objects.filter(meningococcal='True').count()
    meningococcal = Vaccinations.objects.filter(meningococcal='False').count()
    fmeningococcal = Vaccinations.objects.filter(meningococcalD__isnull=True).count()
    pmeningococcal = meningococcal - fmeningococcal

    tpcv13 = Vaccinations.objects.filter(pcv13='True').count()
    pcv13 = Vaccinations.objects.filter(pcv13='False').count()
    fpcv13 = Vaccinations.objects.filter(pcv13D__isnull=True).count()
    ppcv13 = pcv13 - fpcv13

    tppsv23 = Vaccinations.objects.filter(ppsv23='True').count()
    ppsv23 = Vaccinations.objects.filter(ppsv23='False').count()
    fppsv23 = Vaccinations.objects.filter(ppsv23D__isnull=True).count()
    pppsv23 = ppsv23 -fppsv23

    tipv = Vaccinations.objects.filter(ipv='True').count()
    ipv = Vaccinations.objects.filter(ipv='False').count()
    fipv = Vaccinations.objects.filter(ipvD__isnull=True).count()
    pipv = ipv - fipv

    topv = Vaccinations.objects.filter(opv='True').count()
    opv = Vaccinations.objects.filter(opv='False').count()
    fopv = Vaccinations.objects.filter(opvD__isnull=True).count()
    popv = opv - fopv

    trotavirus = Vaccinations.objects.filter(rotavirus='True').count()
    rotavirus = Vaccinations.objects.filter(rotavirus='False').count()
    frotavirus = Vaccinations.objects.filter(rotavirusD__isnull=True).count()
    protavirus = rotavirus - frotavirus

    trzv = Vaccinations.objects.filter(rzv='True').count()
    rzv = Vaccinations.objects.filter(rzv='False').count()
    frzv = Vaccinations.objects.filter(rzvD__isnull=True).count()
    przv = rzv - frzv

    tbcg = Vaccinations.objects.filter(bcg='True').count()
    bcg = Vaccinations.objects.filter(bcg='False').count()
    fbcg = Vaccinations.objects.filter(bcgD__isnull=True).count()
    pbcg = bcg - fbcg

    ttyfoidFever = Vaccinations.objects.filter(tyfoidFever='True').count()
    tyfoidFever = Vaccinations.objects.filter(tyfoidFever='False').count()
    ftyfoidFever = Vaccinations.objects.filter(tyfoidFeverD__isnull=True).count()
    ptyfoidFever = tyfoidFever - ftyfoidFever

    tyellowFever = Vaccinations.objects.filter(yellowFever='True').count()
    yellowFever = Vaccinations.objects.filter(yellowFever='False').count()
    fyellowFever = Vaccinations.objects.filter(yellowFeverD__isnull=True).count()
    pyellowFever = yellowFever - fyellowFever

    tcovid19 = Vaccinations.objects.filter(covid19='True').count()
    covid19 = Vaccinations.objects.filter(covid19='False').count()
    fcovid19 = Vaccinations.objects.filter(covid19D__isnull=True).count()
    pcovid19 = covid19 - fcovid19

    return render(response, "main/vdata.html", {"tchickenpox": tchickenpox, "fchickenpox": fchickenpox, "pchickenpox":pchickenpox, 
                                                "tdt": tdt, "fdt": fdt, "pdt":pdt, 
                                                "tdtap": tdtap, "fdtap": fdtap, "pdtap": pdtap, 
                                                "ttd": ttd, "ftd": ftd, "ptd": ptd, 
                                                "ttdap": ttdap, "ftdap": ftdap, "ptdap": ptdap, 
                                                "tflu": tflu, "fflu": fflu, "pflu": pflu, 
                                                "thav": thav, "fhav": fhav, "phav": phav, 
                                                "thbv": thbv, "fhbv": fhbv, "phbv": phbv, 
                                                "thib": thib, "fhib": fhib, "phib": phib, 
                                                "thpv": thpv, "fhpv": fhpv, "phpv": phpv, 
                                                "tmmr": tmmr, "fmmr": fmmr, "pmmr": pmmr, 
                                                "tmeningococcal": tmeningococcal, "fmeningococcal": fmeningococcal, "pmeningococcal": pmeningococcal, 
                                                "tpcv13": tpcv13, "fpcv13": fpcv13, "ppcv13": ppcv13, 
                                                "tppsv23": tppsv23, "fppsv23": fppsv23, "pppsv23": pppsv23, 
                                                "tipv": tipv, "fipv": fipv, "pipv": pipv, 
                                                "topv": topv, "fopv": fopv, "popv": popv, 
                                                "trotavirus": trotavirus, "frotavirus": frotavirus, "protavirus": protavirus, 
                                                "trzv": trzv, "frzv": frzv, "przv": przv, 
                                                "tbcg": tbcg, "fbcg": fbcg, "pbcg": pbcg, 
                                                "ttyfoidFever": ttyfoidFever, "ftyfoidFever": ftyfoidFever, "ptyfoidFever": ptyfoidFever, 
                                                "tyellowFever": tyellowFever, "fyellowFever": fyellowFever, "pyellowFever": pyellowFever, 
                                                "tcovid19": tcovid19, "fcovid19": fcovid19, "pcovid19": pcovid19, 
                                                "current_user":current_user})

def tbdata(response):
    active = Tuberculosis.objects.filter(typeOfTB='A').count()
    latend = Tuberculosis.objects.filter(typeOfTB='L').count()
    trueV = Tuberculosis.objects.filter(vaccinationForTB='True').count()
    falseV = Tuberculosis.objects.filter(vaccinationForTB='False').count()
    trueA = Tuberculosis.objects.filter(antibioticConsumption='True').count()
    falseA = Tuberculosis.objects.filter(antibioticConsumption='False').count()
    diagnostic1 = Tuberculosis.objects.filter(diagnosticMethodUndertaken='S').count()
    diagnostic2 = Tuberculosis.objects.filter(diagnosticMethodUndertaken='X').count()
    diagnostic3 = Tuberculosis.objects.filter(diagnosticMethodUndertaken='L').count()
    diagnostic4 = Tuberculosis.objects.filter(diagnosticMethodUndertaken='T').count()
    diagnostic5 = Tuberculosis.objects.filter(diagnosticMethodUndertaken='I').count()
    diagnostic6 = Tuberculosis.objects.filter(diagnosticMethodUndertaken='O').count()
    current_user = response.user
    return render(response, "main/tbdata.html", {"active": active, "latend": latend, "trueV": trueV, "falseV": falseV, "trueA": trueA, "falseA": falseA,
                                                "diagnostic1":diagnostic1, "diagnostic2":diagnostic2, "diagnostic3":diagnostic3, "diagnostic4":diagnostic4,
                                                "diagnostic5":diagnostic5, "diagnostic6":diagnostic6,
                                                 "current_user":current_user})

def cedata(response):
    bmi1 = ClinicalExamination.objects.filter(bmi__lte = 18.5).count()
    bmi2 = ClinicalExamination.objects.filter(bmi__gte= 18.5).filter(bmi__lte = 24.9).count()
    bmi3 = ClinicalExamination.objects.filter(bmi__gte= 25).filter(bmi__lte = 26.9).count()
    bmi4 = ClinicalExamination.objects.filter(bmi__gte= 27).filter(bmi__lte = 29.9).count()
    bmi5 = ClinicalExamination.objects.filter(bmi__gte= 30).filter(bmi__lte = 34.9).count()
    bmi6 = ClinicalExamination.objects.filter(bmi__gte= 35).filter(bmi__lte = 39.9).count()
    bmi7 = ClinicalExamination.objects.filter(bmi__gte= 40).count()

    systolic1 = ClinicalExamination.objects.filter(systolic__lte= 139).count()
    systolic2 = ClinicalExamination.objects.filter(systolic__gte= 140).count()

    diastolic1 = ClinicalExamination.objects.filter(diastolic__lte= 89).count()
    diastolic2 = ClinicalExamination.objects.filter(diastolic__gte= 90).count()

    rrm1 = ClinicalExamination.objects.filter(respiratoryRythm__lte= 11).count()
    rrm2 = ClinicalExamination.objects.filter(respiratoryRythm__gte= 12).filter(respiratoryRythm__lte = 20).count()
    rrm3 = ClinicalExamination.objects.filter(respiratoryRythm__gte= 21).count()

    temp1 = ClinicalExamination.objects.filter(temperature__lte = 36.4).count()
    temp2 = ClinicalExamination.objects.filter(temperature__gte= 36.5).filter(temperature__lte = 37).count()
    temp3 = ClinicalExamination.objects.filter(temperature__gte= 37.1).count()
    
    current_user = response.user
    return render(response, "main/cedata.html", {"bmi1":bmi1, "bmi2":bmi2, "bmi3":bmi3, "bmi4":bmi4, "bmi5":bmi5, "bmi6":bmi6, "bmi7":bmi7, 
                                                "systolic1":systolic1, "systolic2":systolic2, "diastolic1":diastolic1, "diastolic2":diastolic2, 
                                                "rrm1":rrm1, "rrm2":rrm2, "rrm3":rrm3, "temp1":temp1, "temp2":temp2, "temp3":temp3, 
                                                "current_user":current_user})

def mhdata(response):
    disesesT = MedicalHistory.objects.filter(diseses='').count()
    diseses = MedicalHistory.objects.exclude(diseses='').count()
    dailyMedicationT = MedicalHistory.objects.filter(dailyMedication='').count()
    dailyMedication = MedicalHistory.objects.exclude(dailyMedication='').count()
    cancerOrTumorT = MedicalHistory.objects.filter(cancerOrTumor='True').count()
    cancerOrTumorF = MedicalHistory.objects.filter(cancerOrTumor='False').count()
    bloodTransfusionsT = MedicalHistory.objects.filter(bloodTransfusions='True').count()
    bloodTransfusionsF = MedicalHistory.objects.filter(bloodTransfusions='False').count()
    allergiesT = MedicalHistory.objects.filter(allergies='').count()
    allergies = MedicalHistory.objects.exclude(allergies='').count()
    surgeriesT = MedicalHistory.objects.filter(surgeries='').count()
    surgeries = MedicalHistory.objects.exclude(surgeries='').count()
    current_user = response.user
    return render(response, "main/mhdata.html", {"disesesT":disesesT, "diseses":diseses, "dailyMedicationT":dailyMedicationT, "dailyMedication":dailyMedication, "cancerOrTumorT":cancerOrTumorT, "cancerOrTumorF":cancerOrTumorF, 
                                                "bloodTransfusionsT":bloodTransfusionsT, "bloodTransfusionsF":bloodTransfusionsF, "allergiesT":allergiesT, "allergies":allergies, "surgeriesT":surgeriesT, "surgeries":surgeries, 
                                                 "current_user":current_user})

def pddata(response):
    genderF = PersonalData.objects.filter(gender='F').count()
    genderM = PersonalData.objects.filter(gender='M').count()

    familyM = PersonalData.objects.filter(familySituation="M").count()
    familyS = PersonalData.objects.filter(familySituation="S").count()
    familyD = PersonalData.objects.filter(familySituation="D").count()
    familyW = PersonalData.objects.filter(familySituation="W").count()

    raceC = PersonalData.objects.filter(race="C").count()
    raceY = PersonalData.objects.filter(race="Y").count()
    raceL = PersonalData.objects.filter(race="L").count()
    raceB = PersonalData.objects.filter(race="B").count()

    insuranceS = PersonalData.objects.filter(healthInsurance="S").count()
    insuranceP = PersonalData.objects.filter(healthInsurance="P").count()
    insuranceSP = PersonalData.objects.filter(healthInsurance="SP").count()
    insuranceW = PersonalData.objects.filter(healthInsurance="W").count()
    insuranceN = PersonalData.objects.filter(healthInsurance="N").count()

    educationPS = PersonalData.objects.filter(education="PS").count()
    educationHS = PersonalData.objects.filter(education="HS").count()
    educationJHS = PersonalData.objects.filter(education="JHS").count()
    educationHTE = PersonalData.objects.filter(education="HTE").count()
    educationHE = PersonalData.objects.filter(education="HE").count()
    educationM = PersonalData.objects.filter(education="M").count()
    educationP = PersonalData.objects.filter(education="P").count()

    languageC = PersonalData.objects.filter(language="C").count()
    languageE = PersonalData.objects.filter(language="E").count()
    languageH = PersonalData.objects.filter(language="H").count()
    languageS = PersonalData.objects.filter(language="S").count()
    languageA = PersonalData.objects.filter(language="A").count()
    languageM = PersonalData.objects.filter(language="M").count()
    languageR = PersonalData.objects.filter(language="R").count()
    languageB = PersonalData.objects.filter(language="B").count()
    languageP = PersonalData.objects.filter(language="P").count()
    languageF = PersonalData.objects.filter(language="F").count()
    languageG = PersonalData.objects.filter(language="G").count()
    languageJ = PersonalData.objects.filter(language="J").count()
    languageI = PersonalData.objects.filter(language="I").count()
    languageO = PersonalData.objects.filter(language="O").count()
    
    occupationB = PersonalData.objects.filter(occupation="B").count()
    occupationL = PersonalData.objects.filter(occupation="L").count()
    occupationS = PersonalData.objects.filter(occupation="S").count()
    occupationD = PersonalData.objects.filter(occupation="D").count()
    occupationO = PersonalData.objects.filter(occupation="O").count()
    occupationF = PersonalData.objects.filter(occupation="F").count()
    occupationC = PersonalData.objects.filter(occupation="C").count()
    occupationI = PersonalData.objects.filter(occupation="I").count()
    occupationP = PersonalData.objects.filter(occupation="P").count()
    occupationT = PersonalData.objects.filter(occupation="T").count()
    occupationA = PersonalData.objects.filter(occupation="A").count()
    occupationU = PersonalData.objects.filter(occupation="U").count()

    num =PersonalData.objects.all().count()

    nat1 = PersonalData.objects.all().aggregate(Max('nationality'))
    nat1N =PersonalData.objects.filter(nationality=nat1['nationality__max']).count()
    nat2 = PersonalData.objects.exclude(nationality=nat1['nationality__max']).aggregate(Max('nationality'))
    nat2N =PersonalData.objects.filter(nationality=nat2['nationality__max']).count()
    nat3 = PersonalData.objects.exclude(nationality=nat1['nationality__max']).exclude(nationality=nat2['nationality__max']).aggregate(Max('nationality'))
    nat3N =PersonalData.objects.filter(nationality=nat3['nationality__max']).count()
    nat4 = PersonalData.objects.exclude(nationality=nat1['nationality__max']).exclude(nationality=nat2['nationality__max']).exclude(nationality=nat3['nationality__max']).aggregate(Max('nationality'))
    nat4N =PersonalData.objects.filter(nationality=nat4['nationality__max']).count()
    nat5 = PersonalData.objects.exclude(nationality=nat1['nationality__max']).exclude(nationality=nat2['nationality__max']).exclude(nationality=nat3['nationality__max']).exclude(nationality=nat4['nationality__max']).aggregate(Max('nationality'))
    nat5N =PersonalData.objects.filter(nationality=nat5['nationality__max']).count()
    nat6 = PersonalData.objects.exclude(nationality=nat1['nationality__max']).exclude(nationality=nat2['nationality__max']).exclude(nationality=nat3['nationality__max']).exclude(nationality=nat4['nationality__max']).exclude(nationality=nat5['nationality__max']).aggregate(Max('nationality'))
    nat6N =PersonalData.objects.filter(nationality=nat6['nationality__max']).count()
    nat7 = PersonalData.objects.exclude(nationality=nat1['nationality__max']).exclude(nationality=nat2['nationality__max']).exclude(nationality=nat3['nationality__max']).exclude(nationality=nat4['nationality__max']).exclude(nationality=nat5['nationality__max']).exclude(nationality=nat6['nationality__max']).aggregate(Max('nationality'))
    nat7N =PersonalData.objects.filter(nationality=nat7['nationality__max']).count()
    nat8 = PersonalData.objects.exclude(nationality=nat1['nationality__max']).exclude(nationality=nat2['nationality__max']).exclude(nationality=nat3['nationality__max']).exclude(nationality=nat4['nationality__max']).exclude(nationality=nat5['nationality__max']).exclude(nationality=nat6['nationality__max']).exclude(nationality=nat7['nationality__max']).aggregate(Max('nationality'))
    nat8N =PersonalData.objects.filter(nationality=nat8['nationality__max']).count()
    nat9 = PersonalData.objects.exclude(nationality=nat1['nationality__max']).exclude(nationality=nat2['nationality__max']).exclude(nationality=nat3['nationality__max']).exclude(nationality=nat4['nationality__max']).exclude(nationality=nat5['nationality__max']).exclude(nationality=nat6['nationality__max']).exclude(nationality=nat7['nationality__max']).exclude(nationality=nat8['nationality__max']).aggregate(Max('nationality'))
    nat9N =PersonalData.objects.filter(nationality=nat9['nationality__max']).count()
    nat10 = PersonalData.objects.exclude(nationality=nat1['nationality__max']).exclude(nationality=nat2['nationality__max']).exclude(nationality=nat3['nationality__max']).exclude(nationality=nat4['nationality__max']).exclude(nationality=nat5['nationality__max']).exclude(nationality=nat6['nationality__max']).exclude(nationality=nat7['nationality__max']).exclude(nationality=nat8['nationality__max']).exclude(nationality=nat9['nationality__max']).aggregate(Max('nationality'))
    nat10N =PersonalData.objects.filter(nationality=nat10['nationality__max']).count()

    print(num, nat1['nationality__max'], nat1N, occupationU)

    current_user = response.user
    return render(response, "main/pddata.html", {"genderF":genderF, "genderM":genderM, "familyM":familyM, "familyS":familyS, "familyD":familyD, "familyW":familyW, "raceC":raceC, "raceY":raceY, "raceL":raceL, "raceB":raceB, 
                                                "insuranceS":insuranceS, "insuranceP":insuranceP, "insuranceSP":insuranceSP, "insuranceW":insuranceW, "insuranceN":insuranceN, 
                                                "educationPS":educationPS, "educationHS":educationHS, "educationJHS":educationJHS, "educationHTE":educationHTE, "educationHE":educationHE, "educationM":educationM, "educationP":educationP, 
                                                "languageC":languageC, "languageE":languageE, "languageH":languageH, "languageS":languageS, "languageA":languageA, "languageM":languageM, "languageR":languageR, 
                                                "languageB":languageB, "languageP":languageP, "languageF":languageF, "languageG":languageG, "languageJ":languageJ, "languageI":languageI, "languageO":languageO, 
                                                "occupationB":occupationB, "occupationL":occupationL, "occupationS":occupationS, "occupationD":occupationD, "occupationO":occupationO, "occupationF":occupationF, 
                                                "occupationC":occupationC, "occupationI":occupationI, "occupationP":occupationP, "occupationT":occupationT, "occupationA":occupationA, "occupationU":occupationU, 
                                                "num":num, "nat1":nat1['nationality__max'], "nat1N":nat1N, "nat2":nat2['nationality__max'], "nat2N":nat2N, "nat3":nat3['nationality__max'], "nat3N":nat3N, 
                                                "nat4":nat4['nationality__max'], "nat4N":nat4N, "nat5":nat5['nationality__max'], "nat5N":nat5N, "nat6":nat6['nationality__max'], "nat6N":nat6N, "nat7":nat7['nationality__max'], "nat7N":nat7N, 
                                                "nat8":nat8['nationality__max'], "nat8N":nat8N, "nat9":nat9['nationality__max'], "nat9N":nat9N, "nat10":nat10['nationality__max'], "nat10N":nat10N,
                                                "current_user":current_user})
    
def ghdata(response):
    current_user = response.user

    children0 = GynecologicalHistory.objects.filter(numOfChildren = 0).count()
    children1 = GynecologicalHistory.objects.filter(numOfChildren__gte = 1).filter(numOfChildren__lte = 2).count()
    children2 = GynecologicalHistory.objects.filter(numOfChildren__gte = 3).filter(numOfChildren__lte = 4).count()
    children3 = GynecologicalHistory.objects.filter(numOfChildren__gte = 5).count()
    tendometriosis = GynecologicalHistory.objects.filter(endometriosis = "True").count()
    fendometriosis = GynecologicalHistory.objects.filter(endometriosis = "False").count()
    tpolycystic = GynecologicalHistory.objects.filter(polycysticOvarySyndrome = "True").count()
    fpolycystic = GynecologicalHistory.objects.filter(polycysticOvarySyndrome = "False").count()
    thcontracepton = GynecologicalHistory.objects.filter(hormonalContraceptiveTherapy__gte = 1).count()
    fhcontracepton = GynecologicalHistory.objects.filter(hormonalContraceptiveTherapy = 0).count()
    thpregnancy = GynecologicalHistory.objects.filter(hormoneTherapyPregnancy__gte = 1).count()
    fhpregnancy = GynecologicalHistory.objects.filter(hormoneTherapyPregnancy = 0).count()
    ncpregnancies0 = GynecologicalHistory.objects.filter(notCompletedPregnancies = 0).count()
    ncpregnancies1 = GynecologicalHistory.objects.filter(notCompletedPregnancies__gte = 1).filter(notCompletedPregnancies__lte = 2).count()
    ncpregnancies2 = GynecologicalHistory.objects.filter(notCompletedPregnancies__gte = 3).count()

    return render(response, "main/ghdata.html", {"children0":children0, "children1":children1, "children2":children2, "children3":children3, 
                                                "tendometriosis":tendometriosis, "fendometriosis":fendometriosis, "tpolycystic":tpolycystic, "fpolycystic":fpolycystic, 
                                                "thcontraception":thcontracepton, "fhcontraception":fhcontracepton, "thpregnancy":thpregnancy, "fhpregnancy":fhpregnancy, 
                                                "ncpregnancies0":ncpregnancies0, "ncpregnancieas1":ncpregnancies1, "ncpregnancies2":ncpregnancies2, 
                                                "current_user":current_user})
    
def shdata(response):
    current_user = response.user

    smoking = SocialHabits.objects.filter(smokingYears__gte = 1).count()
    nsmoking = SocialHabits.objects.filter(smokingYears = 0).count()

    pcigarettes0 = SocialHabits.objects.filter(numOfPacksOfCigarettes = 0).count()
    pcigarettes1 = SocialHabits.objects.filter(numOfPacksOfCigarettes__gte = 1).filter(numOfPacksOfCigarettes__lte = 4).count()
    pcigarettes2 = SocialHabits.objects.filter(numOfPacksOfCigarettes__gte = 5).filter(numOfPacksOfCigarettes__lte = 10).count()
    pcigarettes3 = SocialHabits.objects.filter(numOfPacksOfCigarettes__gte = 11).count()
    galcohol0 = SocialHabits.objects.filter(numOfAlcoholGlasses = 0).count()
    galcohol1 = SocialHabits.objects.filter(numOfAlcoholGlasses__gte = 1).filter(numOfAlcoholGlasses__lte = 4).count()
    galcohol2 = SocialHabits.objects.filter(numOfAlcoholGlasses__gte = 5).filter(numOfAlcoholGlasses__lte = 10).count()
    galcohol3 = SocialHabits.objects.filter(numOfAlcoholGlasses__gte = 11).count()

    return render(response, "main/shdata.html", {"smoking":smoking, "nsmoking":nsmoking, 
                                                "pcigarettes0":pcigarettes0, "pcigarettes1":pcigarettes1, "pcigarettes2":pcigarettes2, "pcigarettes3":pcigarettes3, 
                                                "galcohol0":galcohol0, "galcohol1":galcohol1, "galcohol2":galcohol2, "galcohol3":galcohol3, 
                                                "current_user":current_user})

def dcdata(response):
    general1 = DoctorsComments.objects.filter(general='E').count()
    general2 = DoctorsComments.objects.filter(general='M').count()
    general3 = DoctorsComments.objects.filter(general='C').count()
    general4 = DoctorsComments.objects.filter(general='U').count()
    hearing1 = DoctorsComments.objects.filter(hearing='E').count()
    hearing2 = DoctorsComments.objects.filter(hearing='M').count()
    hearing3 = DoctorsComments.objects.filter(hearing='C').count()
    hearing4 = DoctorsComments.objects.filter(hearing='U').count()
    vision1 = DoctorsComments.objects.filter(vision='E').count()
    vision2 = DoctorsComments.objects.filter(vision='M').count()
    vision3 = DoctorsComments.objects.filter(vision='C').count()
    vision4 = DoctorsComments.objects.filter(vision='U').count()
    respiratoryTract1 = DoctorsComments.objects.filter(respiratoryTract='E').count()
    respiratoryTract2 = DoctorsComments.objects.filter(respiratoryTract='M').count()
    respiratoryTract3 = DoctorsComments.objects.filter(respiratoryTract='C').count()
    respiratoryTract4 = DoctorsComments.objects.filter(respiratoryTract='U').count()
    heart1 = DoctorsComments.objects.filter(heart='E').count()
    heart2 = DoctorsComments.objects.filter(heart='M').count()
    heart3 = DoctorsComments.objects.filter(heart='C').count()
    heart4 = DoctorsComments.objects.filter(heart='U').count()
    chest1 = DoctorsComments.objects.filter(chest='E').count()
    chest2 = DoctorsComments.objects.filter(chest='M').count()
    chest3 = DoctorsComments.objects.filter(chest='C').count()
    chest4 = DoctorsComments.objects.filter(chest='U').count()
    lungs1 = DoctorsComments.objects.filter(lungs='E').count()
    lungs2 = DoctorsComments.objects.filter(lungs='M').count()
    lungs3 = DoctorsComments.objects.filter(lungs='C').count()
    lungs4 = DoctorsComments.objects.filter(lungs='U').count()
    abdomen1 = DoctorsComments.objects.filter(abdomen='E').count()
    abdomen2 = DoctorsComments.objects.filter(abdomen='M').count()
    abdomen3 = DoctorsComments.objects.filter(abdomen='C').count()
    abdomen4 = DoctorsComments.objects.filter(abdomen='U').count()
    myoskeleticalSystem1 = DoctorsComments.objects.filter(myoskeleticalSystem='E').count()
    myoskeleticalSystem2 = DoctorsComments.objects.filter(myoskeleticalSystem='M').count()
    myoskeleticalSystem3 = DoctorsComments.objects.filter(myoskeleticalSystem='C').count()
    myoskeleticalSystem4 = DoctorsComments.objects.filter(myoskeleticalSystem='U').count()
    limbs1 = DoctorsComments.objects.filter(limbs='E').count()
    limbs2 = DoctorsComments.objects.filter(limbs='M').count()
    limbs3 = DoctorsComments.objects.filter(limbs='C').count()
    limbs4 = DoctorsComments.objects.filter(limbs='U').count()
    skin1 = DoctorsComments.objects.filter(skin='E').count()
    skin2 = DoctorsComments.objects.filter(skin='M').count()
    skin3 = DoctorsComments.objects.filter(skin='C').count()
    skin4 = DoctorsComments.objects.filter(skin='U').count()
    nervousSystem1 = DoctorsComments.objects.filter(nervousSystem='E').count()
    nervousSystem2 = DoctorsComments.objects.filter(nervousSystem='M').count()
    nervousSystem3 = DoctorsComments.objects.filter(nervousSystem='C').count()
    nervousSystem4 = DoctorsComments.objects.filter(nervousSystem='U').count()
    current_user = response.user
    return render(response, "main/dcdata.html", {"general1":general1, "general2":general2, "general3":general3, "general4":general4, "hearing1":hearing1, "hearing2":hearing2, "hearing3":hearing3, "hearing4":hearing4,
                                                "vision1":vision1, "vision2":vision2, "vision3":vision3, "vision4":vision4, "respiratoryTract1":respiratoryTract1, "respiratoryTract2":respiratoryTract2, "respiratoryTract3":respiratoryTract3, "respiratoryTract4":respiratoryTract4, 
                                                "heart1":heart1, "heart2":heart2, "heart3":heart3, "heart4":heart4, "chest1":chest1, "chest2":chest2, "chest3":chest3, "chest4":chest4, "lungs1":lungs1, "lungs2":lungs2, "lungs3":lungs3, "lungs4":lungs4, 
                                                "abdomen1":abdomen1, "abdomen2":abdomen2, "abdomen3":abdomen3, "abdomen4":abdomen4, "myoskeleticalSystem1":myoskeleticalSystem1, "myoskeleticalSystem2":myoskeleticalSystem2, "myoskeleticalSystem3":myoskeleticalSystem3, "myoskeleticalSystem4":myoskeleticalSystem4, 
                                                "limbs1":limbs1, "limbs2":limbs2, "limbs3":limbs3, "limbs4":limbs4, "skin1":skin1, "skin2":skin2, "skin3":skin3, "skin4":skin4, "nervousSystem1":nervousSystem1, "nervousSystem2":nervousSystem2, "nervousSystem3":nervousSystem3, "nervousSystem4":nervousSystem4, 
                                                 "current_user":current_user})

def chart(response):
    active = Tuberculosis.objects.filter(typeOfTB='A').count()
    latend = Tuberculosis.objects.filter(typeOfTB='L').count()
    trueV = Tuberculosis.objects.filter(vaccinationForTB='True').count()
    falseV = Tuberculosis.objects.filter(vaccinationForTB='False').count()
    trueA = Tuberculosis.objects.filter(antibioticConsumption='True').count()
    falseA = Tuberculosis.objects.filter(antibioticConsumption='False').count()
    return render(response, "main/chart.html", {"active": active, "latend": latend, "trueV": trueV, "falseV": falseV, "trueA": trueA, "falseA": falseA})

def home(response):
    current_user = response.user
    return render(response, "main/home.html", {"current_user":current_user})

def pdview(response):
    current_user = response.user
    return render(response, "main/pdview.html", {"current_user":current_user})

def mhview(response):
    current_user = response.user
    return render(response, "main/mhview.html", {"current_user":current_user})

def ceview(response):
    current_user = response.user
    return render(response, "main/ceview.html", {"current_user":current_user})

def vview(response):
    current_user = response.user
    return render(response, "main/vview.html", {"current_user":current_user})

def ctview(response):
    current_user = response.user
    print(current_user)
    return render(response, "main/ctview.html", {"current_user":current_user})

def dcview(response):
    current_user = response.user
    return render(response, "main/dcview.html", {"current_user":current_user})

def tview(response):
    current_user = response.user
    return render(response, "main/tview.html", {"current_user":current_user})

def ghview(response):
    current_user = response.user
    return render(response, "main/ghview.html", {"current_user":current_user})

def shview(response):
    current_user = response.user
    return render(response, "main/shview.html", {"current_user":current_user})

def pd(response):
    current_user = response.user
    if response.method == "POST":
        form = PerData(response.POST)
        if form.is_valid():
            ln = form.cleaned_data["lastName"]
            fn = form.cleaned_data["firstName"]
            g = form.cleaned_data["gender"]
            d = form.cleaned_data["dateOfBirth"]
            t = form.cleaned_data["telephone"]
            e = form.cleaned_data["email"]
            f = form.cleaned_data["familySituation"]
            n = form.cleaned_data["nationality"]
            r = form.cleaned_data["race"]
            l = form.cleaned_data["language"]
            o = form.cleaned_data["occupation"]
            ed = form.cleaned_data["education"]
            hi = form.cleaned_data["healthInsurance"]
            dateOfUpdate = datetime.now()
            if response.user.personaldata.exists():
                p = {'lastName': ln, 'firstName': fn, 'gender': g, 'dateOfBirth': d, 'telephone': t, 'email': e, 'familySituation': f, 'nationality': n, 'race': r, 'language': l, 'occupation': o, 'education': ed, 'healthInsurance': hi, 'dateOfUpdate': dateOfUpdate}
                response.user.personaldata.update(**p)
            else:
                p = PersonalData(lastName=ln, firstName=fn, gender=g, dateOfBirth=d, telephone=t, email=e, familySituation=f, nationality=n, race=r, language=l, occupation=o, education=ed, healthInsurance=hi)
                p.save()
                response.user.personaldata.add(p)
            return HttpResponseRedirect("/pdview")
    else:
        form = PerData()
    return render(response, "main/pd.html", {"form":form, "current_user":current_user})

def mh(response):
    current_user = response.user
    if response.method == "POST":
        form = MedHist(response.POST)
        if form.is_valid():
            d = form.cleaned_data["diseses"]
            dm = form.cleaned_data["dailyMedication"]
            cot = form.cleaned_data["cancerOrTumor"]
            bt = form.cleaned_data["bloodTransfusions"]
            a = form.cleaned_data["allergies"]
            s = form.cleaned_data["surgeries"]

            if response.user.medicalhistory.exists():
                medhist = {'diseses': d, 'dailyMedication': dm, 'cancerOrTumor': cot, 'bloodTransfusions': bt, 'allergies': a, 'surgeries': s}                                                                  
                response.user.medicalhistory.update(**medhist)
            else:
                medhist = MedicalHistory(diseses=d, dailyMedication=dm, cancerOrTumor=cot, bloodTransfusions=bt, allergies=a, surgeries=s)                                                                        
                medhist.save()
                response.user.medicalhistory.add(medhist)
            return HttpResponseRedirect("/mhview")
    else:
        form = MedHist()
    return render(response, "main/mh.html", {"form":form, "current_user":current_user})

def t(response):
    current_user = response.user
    if response.method == "POST":
        form = Tb(response.POST)
        if form.is_valid():
            totb = form.cleaned_data["typeOfTB"]
            vftb = form.cleaned_data["vaccinationForTB"]
            ac = form.cleaned_data["antibioticConsumption"]
            nopwtb = form.cleaned_data["numberOfPeopleWithTB"]
            dmu = form.cleaned_data["diagnosticMethodUndertaken"]
            if response.user.tuberculosis.exists():
                tb = {'typeOfTB': totb, 'vaccinationForTB': vftb, 'antibioticConsumption': ac, 'numberOfPeopleWithTB': nopwtb, 'diagnosticMethodUndertaken': dmu}
                response.user.tuberculosis.update(**tb)
            else:
                tb = Tuberculosis(typeOfTB=totb,  vaccinationForTB=vftb, antibioticConsumption=ac, numberOfPeopleWithTB=nopwtb, diagnosticMethodUndertaken=dmu)
                tb.save()
                response.user.tuberculosis.add(tb)
            return HttpResponseRedirect("/tview")
    else:
        form = Tb()
    return render(response, "main/t.html", {"form":form, "current_user":current_user})

def ce(response):
    current_user = response.user
    if response.method == "POST":
        form = ClinicEx(response.POST)
        if form.is_valid():
            h = form.cleaned_data["height"]
            w = form.cleaned_data["weight"]
            wl = form.cleaned_data["weistline"]
            bmi = form.cleaned_data["bmi"]
            sys = form.cleaned_data["systolic"]
            dia = form.cleaned_data["diastolic"]
            p = form.cleaned_data["pulse"]
            rr = form.cleaned_data["respiratoryRythm"]
            t = form.cleaned_data["temperature"]
            hosp = form.cleaned_data["hospital"]
            if response.user.clinicalexamination.exists():
                clinex = {'height': h, 'weight': w, 'weistline': wl, 'bmi': bmi, 'systolic': sys, 'diastolic': dia, 'pulse': p, 'respiratoryRythm': rr, 'temperature': t, 'hospital': hosp}
                response.user.clinicalexamination.update(**clinex)
            else:
                clinex = ClinicalExamination(height=h, weight=w, weistline=wl, bmi=bmi, systolic=sys, diastolic=dia, pulse=p, respiratoryRythm=rr, temperature=t, hospital=hosp)
                clinex.save()
                response.user.clinicalexamination.add(clinex)
            return HttpResponseRedirect("/ceview")
    else:
        form = ClinicEx()
    return render(response, "main/ce.html", {"form":form, "current_user":current_user})

def v(response):
    current_user = response.user
    if response.method == "POST":
        form = Vaccines(response.POST)
        if form.is_valid():
            chickenpox = form.cleaned_data["chickenpox"]
            dt = form.cleaned_data["dt"]
            dtap = form.cleaned_data["dtap"]
            td = form.cleaned_data["td"]
            tdap = form.cleaned_data["tdap"]
            flu = form.cleaned_data["flu"]
            hav = form.cleaned_data["hav"]
            hbv = form.cleaned_data["hbv"]
            hib = form.cleaned_data["hib"]
            hpv = form.cleaned_data["hpv"]
            mmr = form.cleaned_data["mmr"]
            meningococcal = form.cleaned_data["meningococcal"]
            pcv13 = form.cleaned_data["pcv13"]
            ppsv23 = form.cleaned_data["ppsv23"]
            ipv = form.cleaned_data["ipv"]
            opv = form.cleaned_data["opv"]
            rotavirus = form.cleaned_data["rotavirus"]
            rzv = form.cleaned_data["rzv"]
            bcg = form.cleaned_data["bcg"]
            tyfoidFever = form.cleaned_data["tyfoidFever"]
            yellowFever = form.cleaned_data["yellowFever"]
            covid19 = form.cleaned_data["covid19"]


            chickenpoxD = form.cleaned_data["chickenpoxD"]
            dtD = form.cleaned_data["dtD"]
            dtapD = form.cleaned_data["dtapD"]
            tdD = form.cleaned_data["tdD"]
            tdapD = form.cleaned_data["tdapD"]
            fluD = form.cleaned_data["fluD"]
            havD = form.cleaned_data["havD"]
            hbvD = form.cleaned_data["hbvD"]
            hibD = form.cleaned_data["hibD"]
            hpvD = form.cleaned_data["hpvD"]
            mmrD = form.cleaned_data["mmrD"]
            meningococcalD = form.cleaned_data["meningococcalD"]
            pcv13D = form.cleaned_data["pcv13D"]
            ppsv23D = form.cleaned_data["ppsv23D"]
            ipvD = form.cleaned_data["ipvD"]
            opvD = form.cleaned_data["opvD"]
            rotavirusD = form.cleaned_data["rotavirusD"]
            rzvD = form.cleaned_data["rzvD"]
            bcgD = form.cleaned_data["bcgD"]
            tyfoidFeverD = form.cleaned_data["tyfoidFeverD"]
            yellowFeverD = form.cleaned_data["yellowFeverD"]
            covid19D = form.cleaned_data["covid19D"]

            dateOfUpdate = datetime.now()
            if response.user.vaccinations.exists():
                vaccines = {'chickenpox': chickenpox,'dt': dt, 'dtap': dtap, 'td': td, 'tdap': tdap, 'flu': flu, 'hav': hav, 'hbv': hbv, 'hib': hib, 'hpv': hpv, 'mmr': mmr, 'meningococcal': meningococcal, 'pcv13': pcv13, 'ppsv23': ppsv23, 'ipv': ipv, 'opv': opv, 'rotavirus': rotavirus, 'rzv': rzv, 'bcg': bcg, 'tyfoidFever': tyfoidFever, 'yellowFever': yellowFever, 'dateOfUpdate': dateOfUpdate,
                'chickenpoxD': chickenpoxD,'dtD': dtD, 'dtapD': dtapD, 'tdD': tdD, 'tdapD': tdapD, 'fluD': fluD, 'havD': havD, 'hbvD': hbvD, 'hibD': hibD, 'hpvD': hpvD, 'mmrD': mmrD, 'meningococcalD': meningococcalD, 'pcv13D': pcv13D, 'ppsv23D': ppsv23D, 'ipvD': ipvD, 'opvD': opvD, 'rotavirusD': rotavirusD, 'rzvD': rzvD, 'bcgD': bcgD, 'tyfoidFeverD': tyfoidFeverD, 'yellowFeverD': yellowFeverD}
                response.user.vaccinations.update(**vaccines)
            else:
                vaccines = Vaccinations(chickenpox=chickenpox, dt=dt, dtap=dtap, td=td, tdap=tdap, flu=flu, hav=hav, hbv=hbv, hib=hib, hpv=hpv, mmr=mmr, meningococcal=meningococcal, pcv13=pcv13, ppsv23=ppsv23, ipv=ipv, opv=opv, rotavirus=rotavirus, rzv=rzv, bcg=bcg, tyfoidFever=tyfoidFever, yellowFever=yellowFever, dateOfUpdate=dateOfUpdate,
                chickenpoxD=chickenpoxD, dtD=dtD, dtapD=dtapD, tdD=tdD, tdapD=tdapD, fluD=fluD, havD=havD, hbvD=hbvD, hibD=hibD, hpvD=hpvD, mmrD=mmrD, meningococcalD=meningococcalD, pcv13D=pcv13D, ppsv23D=ppsv23D, ipvD=ipvD, opvD=opvD, rotavirusD=rotavirusD, rzvD=rzvD, bcgD=bcgD, tyfoidFeverD=tyfoidFeverD, yellowFeverD=yellowFeverD)
                vaccines.save()
                response.user.vaccinations.add(vaccines)
            return HttpResponseRedirect("/vview")
    else:
        form = Vaccines()
    return render(response, "main/v.html", {"form":form, "current_user":current_user})

def ct(response):
    current_user = response.user
    if response.method == "POST":
        form = CurTreatment(response.POST)
        if form.is_valid():
            t = form.cleaned_data["text"]
            if response.user.currenttreatment.exists():
                curtreat = {'text': t}
                response.user.currenttreatment.update(**curtreat)
            else:
                curtreat = CurrentTreatment(text=t)
                curtreat.save()
                response.user.currenttreatment.add(curtreat)
            return HttpResponseRedirect("/ctview")
    else:
        form = CurTreatment()
    return render(response, "main/ct.html", {"form":form, "current_user":current_user})

def dc(response):
    current_user = response.user
    if response.method == "POST":
        form = DocComments(response.POST)
        if form.is_valid():
            g = form.cleaned_data["general"]
            h = form.cleaned_data["hearing"]
            v = form.cleaned_data["vision"]
            rt = form.cleaned_data["respiratoryTract"]
            heart = form.cleaned_data["heart"]
            c = form.cleaned_data["chest"]
            lu = form.cleaned_data["lungs"]
            a = form.cleaned_data["abdomen"]
            li = form.cleaned_data["limbs"]
            m = form.cleaned_data["myoskeleticalSystem"]
            s = form.cleaned_data["skin"]
            ns = form.cleaned_data["nervousSystem"]
            if response.user.doctorscomments.exists():
                doccom = {'general': g, 'hearing': h, 'vision': v, 'respiratoryTract': rt, 'heart': heart, 'chest': c, 'lungs': lu, 'abdomen': a, 'limbs': li, 'myoskeleticalSystem': m, 'skin': s, 'nervousSystem': ns}
                response.user.doctorscomments.update(**doccom)
            else:
                doccom = DoctorsComments(general=g, hearing=h, vision=v, respiratoryTract=rt, heart=heart, chest=c, lungs=lu, abdomen=a, limbs=li, myoskeleticalSystem=m, skin=s, nervousSystem=ns)
                doccom.save()
                response.user.doctorscomments.add(doccom)
            return HttpResponseRedirect("/dcview")
    else:
        form = DocComments()
    return render(response, "main/dc.html", {"form":form, "current_user":current_user})

def gh(response):
    current_user = response.user
    if response.method == "POST":
        form = GynHist(response.POST)
        if form.is_valid():
            sa = form.cleaned_data["startAge"]
            ea = form.cleaned_data["endAge"]
            noc = form.cleaned_data["numOfChildren"]
            e = form.cleaned_data["endometriosis"]
            pos = form.cleaned_data["polycysticOvarySyndrome"]
            hct = form.cleaned_data["hormonalContraceptiveTherapy"]
            htp = form.cleaned_data["hormoneTherapyPregnancy"]
            ncp = form.cleaned_data["notCompletedPregnancies"]

            if response.user.gynecologicalhistory.exists():
                gynhist = {'startAge': sa, 'endAge': ea, 'numOfChildren': noc, 'endometriosis': e, 'polycysticOvarySyndrome': pos, 'hormonalContraceptiveTherapy': hct, 'hormoneTherapyPregnancy': htp, 'notCompletedPregnancies': ncp}                                                                  
                response.user.gynecologicalhistory.update(**gynhist)
            else:
                gynhist = GynecologicalHistory(startAge=sa, endAge=ea, numOfChildren=noc, endometriosis=e, polycysticOvarySyndrome=pos, hormonalContraceptiveTherapy=hct, hormoneTherapyPregnancy=htp, notCompletedPregnancies=ncp)                                                                        
                gynhist.save()
                response.user.gynecologicalhistory.add(gynhist)
            return HttpResponseRedirect("/ghview")
    else:
        form = GynHist()
    return render(response, "main/gh.html", {"form":form, "current_user":current_user})

def sh(response):
    current_user = response.user
    if response.method == "POST":
        form = SocHab(response.POST)
        if form.is_valid():
            sa = form.cleaned_data["startAge"]
            ea = form.cleaned_data["endAge"]
            sy = form.cleaned_data["smokingYears"]
            npc = form.cleaned_data["numOfPacksOfCigarettes"]
            nag = form.cleaned_data["numOfAlcoholGlasses"]

            if response.user.socialhabits.exists():
                sochab = {'startAge': sa, 'endAge': ea, 'smokingYears': sy, 'numOfPacksOfCigarettes': npc, 'numOfAlcoholGlasses': nag}                                                                  
                response.user.socialhabits.update(**sochab)
            else:
                sochab = SocialHabits(startAge=sa, endAge=ea, smokingYears=sy, numOfPacksOfCigarettes=npc, numOfAlcoholGlasses=nag)                                                                        
                sochab.save()
                response.user.socialhabits.add(sochab)
            return HttpResponseRedirect("/shview")
    else:
        form = SocHab()
    return render(response, "main/sh.html", {"form":form, "current_user":current_user})
