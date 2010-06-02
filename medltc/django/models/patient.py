import django.contrib.auth.models
from django.db import models

class Patient(models.Model):
	lastname = models.CharField(max_length=13)
	firstname = models.CharField(max_length=12)
	midname = models.CharField(max_length=8)
	dob = models.DateField()
	address1 = models.CharField(max_length=30)
	city = models.CharField(max_length=15)
	state = models.CharField(max_length=2)
	zip = models.CharField(max_length=5)
	sex = models.CharField(max_length=1)
	phone = models.CharField(max_length=13)
	ss = models.CharField(max_length=11)
	medicare = models.CharField(max_length=13)
	coinsure1 = models.CharField(max_length=23)
	coinsure2 = models.CharField(max_length=27)
	billnote = models.TextField()
	coins_no = models.CharField(max_length=20)
	is_primary = models.CharField(max_length=1)
	facility = models.CharField(max_length=23)
	level = models.CharField(max_length=11)
	md = models.CharField(max_length=2)
	mncode = models.CharField(max_length=3)
	sub_lname = models.CharField(max_length=11)
	sub_fname = models.CharField(max_length=10)
	billto = models.CharField(max_length=30)
	billaddr1 = models.CharField(max_length=36)
	billaddr2 = models.CharField(max_length=36)
	billphone = models.CharField(max_length=13)
	newdx = models.CharField(max_length=50)
	dx1 = models.CharField(max_length=70)
	dx2 = models.CharField(max_length=70)
	dx3 = models.CharField(max_length=70)
	icd2 = models.CharField(max_length=35)
	icd3 = models.CharField(max_length=35)
	recordno = models.IntegerField(primary_key=True)
	note1 = models.CharField(max_length=32)
	note2 = models.CharField(max_length=32)
	ivdate = models.DateField()
	status = models.CharField(max_length=1)
	mccode = models.CharField(max_length=3)

	def __str__(self):
		return self.lastname+', '+self.firstname

	class Admin:
		pass
		search_fields = ['lastname', 'firstname']

	class Meta:
		db_table = 'PTRECORD'
		ordering = ('lastname', 'firstname')

class PatientFile(models.Model):
    # id is implicitly defined as integer primary key
    user = models.ForeignKey(django.contrib.auth.models.User)
    patient = models.ForeignKey(Patient)
    add_date = models.DateTimeField()
    filename = models.CharField(max_length=255)
    user_filename = models.CharField(max_length=255)
    file_date = models.DateField()
    file_size = models.IntegerField()
    summary = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=255)
    notes = models.TextField()

    class Meta:
        db_table = 'patient_files'
        ordering = ('-file_date',)

class PatientFileTemplate(models.Model):
    # id is implicitly defined as integer primary key
    name = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    notes = models.TextField()

    class Meta:
        db_table = 'patient_files_templates'
        ordering = ('name',)
