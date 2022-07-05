from email.policy import default
from tarfile import PAX_NAME_FIELDS
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import BooleanField
from sqlalchemy import null
# Create your models here.


class Applications(models.Model):
    id = models.AutoField(primary_key=True)
    upiid = models.CharField(max_length=200, null=True)
    amount = models.IntegerField(null=True)
    paymentdate = models.DateField(null=True)
    Paymentss = models.FileField(null=True)
    cname = models.CharField(max_length=200, null=True)
    fname = models.CharField(max_length=200, null=True)
    caste = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    photo = models.ImageField(null=True)
    mob = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.TextField(max_length=500, null=True)
    tsubmit = models.CharField(max_length=200, null=True)
    ftsubmit = models.CharField(max_length=200, null=True)
    equalexam = models.CharField(max_length=200, null=True)
    university = models.CharField(max_length=200, null=True)
    monthyear = models.CharField(max_length=200, null=True)
    supname = models.CharField(max_length=200, null=True)
    supdept = models.CharField(max_length=200, null=True)
    supwadd = models.CharField(max_length=200, null=True)
    admissionorder = models.FileField(null=True)
    supreport = models.FileField(null=True)
    titlethesis = models.CharField(null=True, max_length=200)
    tthesis = models.FileField(null=True)
    yearofadd = models.CharField(max_length=200,null=True)
    time = models.CharField(max_length=200, null=True)
    ptime = models.CharField(max_length=90, null=True)
    onTime = models.CharField(max_length=200, null=True)
    onTimef = models.FileField(null=True)
    prephd = models.FileField(null=True)
    prephdmonthandyear = models.CharField(max_length=200, null=True)
    article = models.FileField(null=True)
    synopsis = models.FileField(null=True)
    fullthesis = models.FileField(null=True)
    dateofsubmission = models.DateField(null=True)
    sem1 = models.FileField(null=True)
    sem2 = models.FileField(null=True)
    pc = models.FileField(null=True)
    noc = models.FileField(null=True)
    myDate = models.CharField(max_length=200,null=True)
    sign = models.FileField(null=True)
    transactionstatus = models.CharField(null=True, max_length=200, default='Pending')
    plagiarismStatus = models.CharField(max_length=200, null=True, default='Pending')
    status = models.CharField(max_length=200, null=True, default='Pending')
    S_Reason = models.TextField(
        max_length=500, null=True, default="Checking transaction")

    def __str__(self):
        return str(self.id)+" "+self.cname


class Approved(models.Model):
    id = models.AutoField(primary_key=True)
    upiid = models.CharField(max_length=200, null=True)
    amount = models.IntegerField(null=True)
    paymentdate = models.DateField(null=True)
    Paymentss = models.FileField(null=True)
    cname = models.CharField(max_length=200, null=True)
    fname = models.CharField(max_length=200, null=True)
    caste = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    photo = models.ImageField(null=True)
    mob = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    address = models.TextField(max_length=500, null=True)
    tsubmit = models.CharField(max_length=200, null=True)
    ftsubmit = models.CharField(max_length=200, null=True)
    equalexam = models.CharField(max_length=200, null=True)
    university = models.CharField(max_length=200, null=True)
    monthyear = models.CharField(max_length=200, null=True)
    supname = models.CharField(max_length=200, null=True)
    supdept = models.CharField(max_length=200, null=True)
    supwadd = models.CharField(max_length=200, null=True)
    admissionorder = models.FileField(null=True)
    supreport = models.FileField(null=True)
    titlethesis = models.CharField(null=True, max_length=200)
    tthesis = models.FileField(null=True)
    yearofadd = models.CharField(max_length=200,null=True)
    time = models.CharField(max_length=200, null=True)
    ptime = models.CharField(max_length=90, null=True)
    onTime = models.CharField(max_length=90, null=True)
    onTimef = models.FileField(null=True)
    prephd = models.FileField(null=True)
    prephdmonthandyear = models.CharField(max_length=200, null=True)
    article = models.FileField(null=True)
    synopsis = models.FileField(null=True)
    fullthesis = models.FileField(null=True)
    dateofsubmission = models.DateField(null=True)
    sem1 = models.FileField(null=True)
    sem2 = models.FileField(null=True)
    pc = models.FileField(null=True)
    noc = models.FileField(null=True)
    myDate = models.CharField(max_length=20, null=True)
    sign = models.FileField(null=True)
    status = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)+" "+self.cname


class Authenticate(models.Model):
    id = models.AutoField(primary_key=True)
    mob = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=200, null=True)
    sq = models.CharField(max_length=200, null=True)


class Examiner(models.Model):
    name = models.CharField(max_length=200, null=True)
    dept = models.CharField(max_length=200, null=True)
    nameOfUniv = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    selected = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.name


class BOSFill(models.Model):
    cid = models.IntegerField(null=True)
    bosuser = models.CharField(max_length=200, null=True)
    nameOfSchlr = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    topic = models.CharField(max_length=200, null=True)
    nameOfSprvsr = models.CharField(max_length=200, null=True)
    s4 = models.CharField(max_length=100, null=True)
    s5 = models.CharField(max_length=100, null=True)
    s6 = models.DateField(max_length=100, null=True)
    s8 = models.DateField(max_length=100, null=True)
    s9 = models.TimeField(max_length=100, null=True)

    acoeNote1Status = models.CharField(max_length=200, null=True, default='Pending')
    acoeNote1Reason = models.CharField(max_length=100, null=True, default="Accepted")
    acoeNote1Date = models.DateField(max_length=100, null=True)
    # acoeNote1File = models.FileField(null=True)

    acoeNote2Status = models.CharField(max_length=200, null=True, default='Pending')
    acoeNote2Date = models.DateField(max_length=100, null=True)
    # acoeNote2File = models.FileField(null=True)

    acoeNote3Status = models.CharField(max_length=200, null=True, default='Pending')
    acoeNote3Date = models.DateField(max_length=100, null=True)
    # acoeNote3File = models.FileField(null=True)

    coeNote1Status = models.CharField(max_length=200, null=True, default='Pending')
    coeNote1Date = models.DateField(max_length=100, null=True)
    # coeNote1File = models.FileField(null=True)

    coeNote2Status = models.CharField(max_length=200, null=True, default='Pending')
    coeNote2Date = models.DateField(max_length=100, null=True)
    # coeNote2File = models.FileField(null=True)

    coeNote3Status = models.CharField(max_length=200, null=True, default='Pending')
    coeNote3Date = models.DateField(max_length=100, null=True)
    # coeNote3File = models.FileField(null=True)

    vcNote1Status = models.CharField(max_length=200, null=True, default='Pending')
    vcNote1Date = models.DateField(max_length=100, null=True)
    # vcNote1File = models.FileField(null=True)

    vcNote2Status = models.CharField(max_length=200, null=True, default='Pending')
    vcNote2Date = models.DateField(max_length=100, null=True)
    vcNote2File = models.FileField(null=True)

    vcNote3Status = models.CharField(max_length=200, null=True, default='Pending')
    vcNote3Date = models.DateField(max_length=100, null=True)
    # vcNote3File = models.FileField(null=True)

    panel = models.FileField(null=True)
    f1 = models.FileField(null=True)
    f2 = models.FileField(null=True)
    f3 = models.FileField(null=True)
    f4 = models.FileField(null=True)
    examiner1 = models.CharField(max_length=200, null=True)
    examiner2 = models.CharField(max_length=200, null=True)
    examiner3 = models.CharField(max_length=200, null=True)
    examiner4 = models.CharField(max_length=200, null=True)
    examiner5 = models.CharField(max_length=200, null=True)
    examiner6 = models.CharField(max_length=200, null=True)
    examiner7 = models.CharField(max_length=200, null=True)
    examiner8 = models.CharField(max_length=200, null=True)
    examiner9 = models.CharField(max_length=200, null=True)
    bfile = models.FileField(null=True)
    bname = models.CharField(max_length=100, null=True)
    mode = models.CharField(max_length=100,null=True)
    def __str__(self):
        return str(self.cid)


class OfficeAuthenticates(models.Model):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    nextpage = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.username)
