from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CurrentTreatment, Tuberculosis, Vaccinations, MedicalHistory, ClinicalExamination, DoctorsComments, PersonalData, GynecologicalHistory, SocialHabits

# Register your models here.

admin.site.unregister(Group)
admin.site.register(CurrentTreatment)
admin.site.register(Tuberculosis)
admin.site.register(Vaccinations)
admin.site.register(MedicalHistory)
admin.site.register(ClinicalExamination)
admin.site.register(DoctorsComments)
admin.site.register(PersonalData)
admin.site.register(GynecologicalHistory)
admin.site.register(SocialHabits)
