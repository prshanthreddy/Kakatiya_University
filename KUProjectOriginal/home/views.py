import email
from operator import methodcaller
from os import P_NOWAIT
from pickletools import read_uint1
import re
from sre_parse import State
from unicodedata import name
from django.core.files.storage import FileSystemStorage
from django.db.models.fields import EmailField
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from psutil import users
from home.models import Applications, Approved, Authenticate, BOSFill, Examiner, OfficeAuthenticates
from django.contrib import messages
import datetime

def sample(request):
    return render(request,'sample1.html')
def getExaminars(obj):
    l = []
    obj1 = Examiner.objects.get(mobile=obj.examiner1)
    if(obj1.selected == True):
        l.append(obj1)
    obj1 = Examiner.objects.get(mobile=obj.examiner2)
    if(obj1.selected == True):
        l.append(obj1)
    obj1 = Examiner.objects.get(mobile=obj.examiner3)
    if(obj1.selected == True):
        l.append(obj1)
    obj1 = Examiner.objects.get(mobile=obj.examiner4)
    if(obj1.selected == True):
        l.append(obj1)
    obj1 = Examiner.objects.get(mobile=obj.examiner5)
    if(obj1.selected == True):
        l.append(obj1)
    obj1 = Examiner.objects.get(mobile=obj.examiner6)
    if(obj1.selected == True):
        l.append(obj1)
    obj1 = Examiner.objects.get(mobile=obj.examiner7)
    if(obj1.selected == True):
        l.append(obj1)
    obj1 = Examiner.objects.get(mobile=obj.examiner8)
    if(obj1.selected == True):
        l.append(obj1)
    obj1 = Examiner.objects.get(mobile=obj.examiner9)
    if(obj1.selected == True):
        l.append(obj1)
    return l


def getAllExaminars(obj):
    l = []
    e1 = Examiner.objects.get(mobile=obj.examiner1)
    l.append(e1)
    e2 = Examiner.objects.get(mobile=obj.examiner2)
    l.append(e2)
    e3 = Examiner.objects.get(mobile=obj.examiner3)
    l.append(e3)
    e4 = Examiner.objects.get(mobile=obj.examiner4)
    l.append(e4)
    e5 = Examiner.objects.get(mobile=obj.examiner5)
    l.append(e5)
    e6 = Examiner.objects.get(mobile=obj.examiner6)
    l.append(e6)
    e7 = Examiner.objects.get(mobile=obj.examiner7)
    l.append(e7)
    e8 = Examiner.objects.get(mobile=obj.examiner8)
    l.append(e8)
    e9 = Examiner.objects.get(mobile=obj.examiner9)
    l.append(e9)
    return l


def getTwoDiffExaminars(obj):
    l = []
    l1 = []
    e1 = Examiner.objects.get(mobile=obj.examiner1)
    l.append(e1)
    e2 = Examiner.objects.get(mobile=obj.examiner2)
    l.append(e2)
    e3 = Examiner.objects.get(mobile=obj.examiner3)
    l.append(e3)
    e4 = Examiner.objects.get(mobile=obj.examiner4)
    l1.append(e4)
    e5 = Examiner.objects.get(mobile=obj.examiner5)
    l1.append(e5)
    e6 = Examiner.objects.get(mobile=obj.examiner6)
    l1.append(e6)
    e7 = Examiner.objects.get(mobile=obj.examiner7)
    l1.append(e7)
    e8 = Examiner.objects.get(mobile=obj.examiner8)
    l1.append(e8)
    e9 = Examiner.objects.get(mobile=obj.examiner9)
    l1.append(e9)
    return l, l1


def instruction(request):
    if request.session['var'] == 0:
        request.session['var'] = 1
        return render(request, 'instruction.html')
    return HttpResponseRedirect("/")


def register(request):
    return render(request, 'register.html')


def login(request):
    if(request.session['var'] == 1 or request.session['var'] == 2):
        request.session['var'] = 2
        return render(request, 'login.html', {'andy': request.session['phno1']})
    return HttpResponseRedirect("/")


def validate(request):
    if(request.session['var'] != 2):
        return HttpResponseRedirect("/")
    if request.method == "POST":
        request.session['var'] = 2
        request.session['upiid'] = request.POST.get('upiid')
        request.session['amount'] = request.POST.get('amount')
        request.session['paymentdate'] = request.POST.get('paymentdate')
        payss = request.FILES['payss']
        fs = FileSystemStorage()
        file = fs.save(payss.name, payss)
        request.session['payss'] = file
        request.session['cname'] = request.POST.get('cname')
        request.session['fname'] = request.POST.get('fname')
        request.session['caste'] = request.POST.get('caste').upper()
        request.session['dob'] = request.POST.get('dob')
        photo = request.FILES['photo']
        file = fs.save(photo.name, photo)
        request.session['photo'] = file
        request.session['mob'] = request.POST.get('mob')
        request.session['email'] = request.POST.get('email')
        request.session['address'] = request.POST.get('address')
        request.session['ftsubmit'] = request.POST.get('ftsubmit')
        request.session['equalexam'] = request.POST.get('equalexam')
        request.session['university'] = request.POST.get('university')
        request.session['monthyear'] = request.POST.get('monthyear')
        request.session['supname'] = request.POST.get('supname')
        request.session['supdept'] = request.POST.get('supdept')
        request.session['supwadd'] = request.POST.get('supwadd')
        admissionorder = request.FILES['admissionorder']
        file = fs.save(admissionorder.name, admissionorder)
        request.session['ador'] = file
        supreport = request.FILES['supreport']
        file = fs.save(supreport.name, supreport)
        request.session['supre'] = file
        tthesis = request.FILES['tthesis']
        file = fs.save(tthesis.name, tthesis)
        request.session['th'] = file
        request.session['titlethesis'] = request.POST.get(
            'titlethesis').upper()
        request.session['yearofadd'] = request.POST.get('yearofadd')
        request.session['prephdmonthandyear'] = request.POST.get('prephdmonthandyear')
        request.session['time'] = request.POST.get('time')
        request.session['ptime'] = ptime = request.POST.get('ptime')
        request.session['otf'] = onTimef = 0
        request.session['onTime'] = onTime = request.POST.get('onTime')
        
        if(ptime == 'false' and onTime == 'true'):
            onTimef = request.FILES['onTimef']
            file = fs.save(onTimef.name, onTimef)
            request.session['otf'] = file
        prephd = request.FILES['prephd']
        file = fs.save(prephd.name, prephd)
        request.session['prephd'] = file
        article = request.FILES['article']
        file = fs.save(article.name, article)
        request.session['article'] = file
        synopsis = request.FILES['synopsis']
        file = fs.save(synopsis.name, synopsis)
        request.session['syn'] = file
        uploadthesis = request.FILES['uploadthesis']
        file = fs.save(uploadthesis.name, uploadthesis)
        request.session['fthesis'] = file
        
        sem1 = request.FILES['sem1']
        file = fs.save(sem1.name, sem1)
        request.session['sem1'] = file
        
        sem2 = request.FILES['sem2']
        file = fs.save(sem2.name, sem2)
        request.session['sem2'] = file
        
        pc = request.FILES['pc']
        file = fs.save(pc.name, pc)
        request.session['pc'] = file
        request.session['dateofsubmission'] = request.POST.get(
            'dateofsubmission')
        noc = request.FILES['noc']
        file = fs.save(noc.name, noc)
        request.session['noc'] = file
        request.session['myDate'] = request.POST.get('myDate')
        Sign = request.FILES['Sign']
        file = fs.save(Sign.name, Sign)
        request.session['sign'] = file

    return render(request, 'validate.html', {'sign': request.session['sign'], 'mydate': request.session['myDate'],'sem1':request.session['sem1'],'sem2':request.session['sem2'], 'pc': request.session['pc'], 'noc': request.session['noc'], 'date': request.session['dateofsubmission'], 'fthesis': request.session['fthesis'], 'syn': request.session['syn'], 'article': request.session['article'], 'yearofadd': request.session["yearofadd"], 'prephd': request.session['prephd'], 'otf': request.session['otf'], 'otime': request.session['onTime'], 'ptime': request.session['ptime'], 'time': request.session['time'], 'photo': request.session['photo'], 'th': request.session['th'],'prephdmonthandyear':request.session['prephdmonthandyear'], 'supre': request.session['supre'], 'ador': request.session['ador'], 'supname': request.session['supname'], 'supdept': request.session['supdept'], "supwadd": request.session["supwadd"], 'monthyear': request.session['monthyear'], 'university': request.session['university'], 'equalexam': request.session['equalexam'], 'ftsubmit': request.session['ftsubmit'],  'addr': request.session['address'], 'mail': request.session['email'], 'mob': request.session['mob'], 'dob': request.session['dob'], 'caste': request.session['caste'], 'fname': request.session['fname'], 'cname': request.session['cname'], 'payss': request.session['payss'], 'paymt': request.session['paymentdate'], 'amount': request.session['amount'], 'upiid': request.session['upiid'], 'titlethesis': request.session['titlethesis'], 'photo': request.session['photo']})


def success(request):
    if(request.session['var'] == 2):
        app = Applications(
            upiid=request.session['upiid'],
            amount=request.session['amount'],
            paymentdate=request.session['paymentdate'],
            Paymentss=request.session['payss'],
            cname=request.session['cname'],
            fname=request.session['fname'],
            caste=request.session['caste'],
            dob=request.session['dob'],
            photo=request.session['photo'],
            mob=request.session['mob'],
            email=request.session['email'],
            address=request.session['address'],
            ftsubmit=request.session['ftsubmit'],
            equalexam=request.session['equalexam'],
            university=request.session['university'],
            monthyear=request.session['monthyear'],
            prephdmonthandyear=request.session['prephdmonthandyear'],
            supname=request.session['supname'],
            supdept=request.session['supdept'],
            supwadd=request.session['supwadd'],
            admissionorder=request.session['ador'],
            supreport=request.session['supre'],
            titlethesis=request.session['titlethesis'],
            tthesis=request.session['th'],
            yearofadd=request.session['yearofadd'],
            time=request.session['time'],
            ptime=request.session['ptime'],
            onTime=request.session['onTime'],
            onTimef=request.session['otf'],
            prephd=request.session['prephd'],
            article=request.session['article'],
            synopsis=request.session['syn'],
            fullthesis=request.session['fthesis'],
            sem1=request.session['sem1'],
            sem2=request.session['sem2'],
            pc=request.session['pc'],
            dateofsubmission=request.session['dateofsubmission'],
            noc=request.session['noc'],
            myDate=request.session['myDate'],
            sign=request.session['sign']
        )
        app.save()
        request.session['var'] = 0
        return render(request, 'success.html', {'cname': app.cname, 'id': app.id})
    return HttpResponseRedirect("/")


def check(request):
    if request.method == "POST":
        phno = request.POST.get('mob')
        passwd = request.POST.get('password')
        sq = request.POST.get('sq')
        try:
            obj = Authenticate.objects.get(mob=phno)
            return HttpResponseRedirect("/")
        except:
            authenticate = Authenticate(
                mob=phno,
                password=passwd,
                sq=sq
            )
            authenticate.save()
    request.session['var'] = 0
    return render(request, 'check.html', {'message': ""})


def status(request):
    if request.method == "POST":
        if request.session['var'] == 0:
            phno = request.POST.get('phno')
            count = 0
            for i in phno:
                if(i < '0' or i > '9'):
                    break
                count += 1
            if(count != 10):
                return render(request, 'check.html', {'message': "Enter Valid Mobile Number"})
            request.session['phno1'] = phno
            password = request.POST.get('password')
            try:
                obj = Authenticate.objects.get(mob=phno)
            except:
                return render(request, 'check.html', {'message': "Create New User"})
            try:
                if obj.password == password:
                    obj = Applications.objects.get(mob=phno)
                    name = getattr(obj, 'cname')
                    fname = getattr(obj, 'fname')
                    mobile = getattr(obj, 'mob')
                    photo = getattr(obj, 'photo')
                    sta = getattr(obj, 'status')
                    tsta = getattr(obj, 'transactionstatus')
                    bsta = rej = False
                    tstabool = False
                    if sta == 'Approved':
                        request.session['fmobile'] = mobile
                        bsta = True
                    elif sta == 'Rejected':
                        request.session['fmobile'] = mobile
                        rej = True
                    if tsta == "Approved":
                        tstabool = True
                    srea = getattr(obj, 'S_Reason')
                    return render(request, 'status.html', {'paystatus': tstabool, 'photo': photo, 'cname': name, 'fname': fname, 'mobile': mobile, 'bstatus': bsta, 'status': sta, 'Sreason': srea, 'Rstatus': rej})
                return render(request, 'check.html', {'message': "Incorrect Password"})
            except:
                return HttpResponseRedirect("/instruction")
        else:
            return HttpResponseRedirect("/")
    return HttpResponseRedirect("/")


def forgot(request):
    return render(request, 'forgot.html')


def change(request):
    if request.method == "POST":
        mob = request.POST.get("mob")
        sq = request.POST.get("sq")
        passwd = request.POST.get("password")
    try:
        obj = Authenticate.objects.get(mob=mob)
        print(obj.password)
        if obj.sq == sq:
            Authenticate.objects.filter(mob=mob).update(password=passwd)
        else:
            return render(request, 'forgot.html', {"andy": "Invalid Security Answer"})
        return render(request, 'check.html', {"message": "Password Changed Succesfully..!"})
    except:
        return HttpResponseRedirect('/register')


def certificate(request):
    mobile = request.session['fmobile']
    obj = Approved.objects.get(mob=mobile)
    return render(request, 'certify.html', {'obj': obj})


def delete(request):
    Applications.objects.get(mob=request.session['fmobile']).delete()
    return HttpResponseRedirect("/instruction")


def paylogin(request):
    if request.method == "POST":
        user = request.POST.get('user')
        password = request.POST.get('pass')
        newpassword = request.POST.get('newpass')
        try:
            obj = OfficeAuthenticates.objects.get(username=user)
            if obj.password == password:
                obj.password = newpassword
                obj.save()
                return HttpResponseRedirect("paylogin")
            else:
                return render(request, 'ponewpassword.html', {"andy": 'Invalid Password'})
        except:
            return render(request, 'ponewpassword.html', {"andy": 'Invalid Username'})
    request.session['var'] = 1
    return render(request, 'paylogin.html')


def logverify(request):
    if(request.session['var'] == 1):
        request.session['var'] = 2
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            try:
                obj = OfficeAuthenticates.objects.get(username=user)
                print(obj)
                print(obj.nextpage)
                if obj.password == password:
                    return HttpResponseRedirect(obj.nextpage)
            except:
                pass
        return HttpResponseRedirect('paylogin')
    return HttpResponseRedirect('paylogin')


def payverify(request):
    if(request.session['var'] == 2):
        request.session['var'] = 3
        if request.method == "POST":
            val = request.POST.get('stat')
            obje = Applications.objects.get(mob=request.session['verfphno'])
            if(val != "Approved"):
                setattr(obje, 'status', val)
                setattr(obje, 'S_Reason', request.POST.get('rstat'))
            setattr(obje, 'transactionstatus', val)
            obje.save()
        obj = Applications.objects.filter(transactionstatus='Pending')
        return render(request, 'payverify.html', {'objs': obj})
    return HttpResponseRedirect('paylogin')


def paydetails(request):
    if(request.session['var'] == 3):
        request.session['var'] = 0
        if request.method == "POST":
            phno = request.POST.get('persel')
            try:
                obj = Applications.objects.get(mob=phno)
                request.session['verfphno'] = phno
                request.session['var'] = 2
                return render(request, 'payaproval.html', {'objs': obj})
            except:
                return HttpResponseRedirect('payverify')
        return render(request, "payverify")
    return HttpResponseRedirect('payverify')


def ponewpassword(request):
    return render(request, 'ponewpassword.html')


def test(request):
    if request.method == "POST":
        if request.POST.get('stat') == 'Approved':
            apprv = request.session['apprv']
            Applications.objects.filter(mob=apprv).update(status='Approved')
            try:
                obj = Approved.objects.get(mob=request.session['apprv'])
            except:
                obj = Applications.objects.get(mob=request.session['apprv'])
                approve = Approved(
                    upiid=obj.upiid,
                    amount=obj.amount,
                    paymentdate=obj.paymentdate,
                    Paymentss=obj.Paymentss,
                    cname=obj.cname,
                    fname=obj.fname,
                    caste=obj.caste,
                    dob=obj.dob,
                    photo=obj.photo,
                    mob=obj.mob,
                    email=obj.email,
                    address=obj.address,
                    ftsubmit=obj.ftsubmit,
                    equalexam=obj.equalexam,
                    university=obj.university,
                    monthyear=obj.monthyear,
                    prephdmonthandyear=obj.prephdmonthandyear,
                    supname=obj.supname,
                    supdept=obj.supdept,
                    supwadd=obj.supwadd,
                    admissionorder=obj.admissionorder,
                    supreport=obj.supreport,
                    titlethesis=obj.titlethesis,
                    tthesis=obj.tthesis,
                    yearofadd=obj.yearofadd,
                    time=obj.time,
                    ptime=obj.ptime,
                    onTime=obj.onTime,
                    onTimef=obj.onTimef,
                    prephd=obj.prephd,
                    article=obj.article,
                    synopsis=obj.synopsis,
                    fullthesis=obj.fullthesis,
                    sem1=obj.sem1,
                    sem2=obj.sem2,
                    pc=obj.pc,
                    dateofsubmission=obj.dateofsubmission,
                    noc=obj.noc,
                    myDate=obj.myDate,
                    sign=obj.sign,
                    status=obj.status
                )
                approve.save()
                return HttpResponseRedirect("/test")
        elif request.POST.get('stat') == 'Rejected':
            apprv = request.session['apprv']
            Applications.objects.filter(mob=apprv).update(status='Rejected')
            Applications.objects.filter(mob=apprv).update(
                S_Reason=request.POST.get('rstat'))
    a = []
    andy = Applications.objects.filter(
        status='Pending', transactionstatus='Approved')

    return render(request, 'test.html', {'andy': andy})


def adminlogin(request):
    if request.method == "POST":
        sandy = request.POST.get('nithin')
        try:
            obj = Applications.objects.get(mob=sandy)
            request.session['apprv'] = sandy
            return render(request, 'adminlogin.html', {'obj': obj})
        except:
            return HttpResponseRedirect('/test')
    return HttpResponseRedirect('/')


def printform(request):
    if request.method == "POST":
        mob = request.POST.get('nithin')
        obj = Approved.objects.get(mob=mob)
        return render(request, 'printform.html', {'obj': obj})
    return HttpResponseRedirect("paylogin")    


def ApprovedList(request):
    a = []
    obj = Approved.objects.all()

    return render(request, 'ApprovedList.html', {'andy': obj})


def home(request):
    return render(request, 'Home.html    ')


def bcvdlogin(request):
    return render(request, 'bcvdlogin.html')

loginses=""
acoeloginses=""
coeloginses=""
vcloginses=""

def bcvdverify(request):
    if request.method == "POST":
        user = request.POST.get('user')
        password = request.POST.get('pass')
        try:
            obj = OfficeAuthenticates.objects.get(username=user)
            if obj.password == password:
                global loginses,acoeloginses,coeloginses,vcloginses
                if(user=="ACOEKU"):
                    acoeloginses=user
                    request.session['loginses']=acoeloginses
                elif(user=="COEKU"):
                    coeloginses=user
                    request.session['loginses']=coeloginses
                elif(user=="VCKU"):
                    vcloginses=user
                    request.session['loginses']=vcloginses
                else:
                    loginses=user
                    request.session['loginses']=loginses
                return HttpResponseRedirect( obj.nextpage)
            else:
                return render(request, 'bcvdlogin.html', {"andy": 'Invalid Credidentials'})
        except:
            return render(request, 'bcvdlogin.html', {"andy": 'Invalid Credidentials'})
    return HttpResponseRedirect('bcvdlogin')


def logout(request):
    global loginses,acoeloginses,coeloginses,vcloginses
    if (request.session['loginses']!=loginses  and request.session['loginses']!=acoeloginses and request.session['loginses']!=coeloginses and request.session['loginses']!=vcloginses ):
        return HttpResponseRedirect('bcvdlogin')
    if request.session['loginses']=="ACOEKU":
        user=acoeloginses
    elif request.session['loginses']=="COEKU":
        user=coeloginses
    elif request.session['loginses']=="VCKU":
        user=vcloginses
    else:
        user=loginses
    acoeloginses="hola"
    loginses="hola"
    coeloginses="hola"
    vcloginses="hola"
    request.session['loginses']='logedout'
    return render(request,'logout.html',{'user':user})

def bosnewpassword(request):
    if request.method == "POST":
        user = request.POST.get('user')
        password = request.POST.get('pass')
        newpassword = request.POST.get('newpass')
        try:
            obj = OfficeAuthenticates.objects.get(username=user)
            if obj.password == password:
                obj.password = newpassword
                obj.save()
                return HttpResponseRedirect("bcvdlogin")
            else:
                return render(request, 'bosnewpassword.html', {"andy": 'Invalid Password'})
        except:
            return render(request, 'bosnewpassword.html', {"andy": 'Invalid Username'})
    return render(request, 'bosnewpassword.html')


def bosfill(request):
    
    if (request.session['loginses']!=loginses):
        return HttpResponseRedirect('bcvdlogin')
    return render(request, 'bosfill.html')


def bosstatus(request):
    if (request.session['loginses']!=loginses):
        return HttpResponseRedirect('bcvdlogin')
    obj = BOSFill.objects.filter(acoeNote1Status="Rejected",bosuser=request.session['loginses'])
    return render(request, "bosstatus.html", {'andy': obj})


def bosverify(request):
    if (request.session['loginses']!=loginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        id = request.POST.get("nithin")
        obj = BOSFill.objects.get(id=id)
        request.session['acoethroughid'] = id
        return render(request, "bosverify.html", {'andy': obj, 'vicky': getAllExaminars(obj)})


def boslogin(request):
    if (request.session['loginses']!=loginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        e1 = Examiner(
            name=request.POST.get("e1name"),
            dept=request.POST.get("e1dep"),
            nameOfUniv=request.POST.get("e1uni"),
            state=request.POST.get("e1add"),
            mobile=request.POST.get("e1mob"),
            email=request.POST.get("e1mail"),
        )
        try:
            Examiner.objects.get(mobile=e1.mobile)
        except:    
            e1.save() 
        e2 = Examiner(
            name=request.POST.get("e2name"),
            dept=request.POST.get("e2dep"),
            nameOfUniv=request.POST.get("e2uni"),
            state=request.POST.get("e2add"),
            mobile=request.POST.get("e2mob"),
            email=request.POST.get("e2mail"),
        )
        try: 
            Examiner.objects.get(mobile=e2.mobile)
        except:    
            e2.save()
        e3 = Examiner(
            name=request.POST.get("e3name"),
            dept=request.POST.get("e3dep"),
            nameOfUniv=request.POST.get("e3uni"),
            state=request.POST.get("e3add"),
            mobile=request.POST.get("e3mob"),
            email=request.POST.get("e3mail"),
        )
        try:
            Examiner.objects.get(mobile=e3.mobile)
        except:    
            e3.save()
        e4 = Examiner(
            name=request.POST.get("e4name"),
            dept=request.POST.get("e4dep"),
            nameOfUniv=request.POST.get("e4uni"),
            state=request.POST.get("e4add"),
            mobile=request.POST.get("e4mob"),
            email=request.POST.get("e4mail"),
        )
        try:
            Examiner.objects.get(mobile=e4.mobile)
        except:    
            e4.save()
        e5 = Examiner(
            name=request.POST.get("e5name"),
            dept=request.POST.get("e5dep"),
            nameOfUniv=request.POST.get("e5uni"),
            state=request.POST.get("e5add"),
            mobile=request.POST.get("e5mob"),
            email=request.POST.get("e5mail"),
        )
        try:
            Examiner.objects.get(mobile=e5.mobile)
        except:    
            e5.save()
        e6 = Examiner(
            name=request.POST.get("e6name"),
            dept=request.POST.get("e6dep"),
            nameOfUniv=request.POST.get("e6uni"),
            state=request.POST.get("e6add"),
            mobile=request.POST.get("e6mob"),
            email=request.POST.get("e6mail"),
        )
        try:
            Examiner.objects.get(mobile=e6.mobile)
        except:    
            e6.save()
        e7 = Examiner(
            name=request.POST.get("e7name"),
            dept=request.POST.get("e7dep"),
            nameOfUniv=request.POST.get("e7uni"),
            state=request.POST.get("e7add"),
            mobile=request.POST.get("e7mob"),
            email=request.POST.get("e7mail"),
        )
        try:
            Examiner.objects.get(mobile=e7.mobile)
        except:    
            e7.save()
        e8 = Examiner(
            name=request.POST.get("e8name"),
            dept=request.POST.get("e8dep"),
            nameOfUniv=request.POST.get("e8uni"),
            state=request.POST.get("e8add"),
            mobile=request.POST.get("e8mob"),
            email=request.POST.get("e8mail"),
        )
        try:
            Examiner.objects.get(mobile=e8.mobile)
        except:    
            e8.save()
        e9 = Examiner(
            name=request.POST.get("e9name"),
            dept=request.POST.get("e9dep"),
            nameOfUniv=request.POST.get("e9uni"),
            state=request.POST.get("e9add"),
            mobile=request.POST.get("e9mob"),
            email=request.POST.get("e9mail"),
        )
        try:
            Examiner.objects.get(mobile=e9.mobile)
        except:    
            e9.save()
        fs = FileSystemStorage()
        photo = request.FILES['bfile']
        b1 = BOSFill(
            cid=request.POST.get('cid'),
            bosuser = request.session['loginses'],
            nameOfSchlr=request.POST.get('cname'),
            subject=request.POST.get('subject'),
            topic=request.POST.get('topic').upper(),
            nameOfSprvsr=request.POST.get('sname'),
            examiner1=e1.mobile,
            examiner2=e2.mobile,
            examiner3=e3.mobile,
            examiner4=e4.mobile,
            examiner5=e5.mobile,
            examiner6=e6.mobile,
            examiner7=e7.mobile,
            examiner8=e8.mobile,
            examiner9=e9.mobile,
            bname=request.POST.get('bname'),
            bfile=fs.save(photo.name, photo)
        )
        b1.save()
    return render(request, 'boslogin.html')

def acoelogin(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    return render(request, 'acoelogin.html')


def coelogin(request):
    if (request.session['loginses']!=coeloginses):
        return HttpResponseRedirect('bcvdlogin')
    return render(request, 'coelogin.html')


def vclogin(request):
    if (request.session['loginses']!=vcloginses):
        return HttpResponseRedirect('bcvdlogin')
    return render(request, 'vclogin.html')


def acoenote1(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        obj = BOSFill.objects.get(cid=request.session['acoethroughid'])
        obj.acoeNote1Status = request.POST.get("stat1")
        obj.acoeNote1Reason = request.POST.get("rstat")
        fs = FileSystemStorage()
        photo = request.FILES['myfile']
        obj.panel = fs.save(photo.name, photo)
        obj.acoeNote1Date = datetime.date.today()
        obj.save()
    obj = BOSFill.objects.filter(acoeNote1Status='Pending')
    return render(request, 'acoenote1.html', {'andy': obj})


def acoeverify1(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        id = request.POST.get('persel')
        obj = BOSFill.objects.get(cid=id)
        andy = Approved.objects.get(id=id)
        print(obj)
        request.session['acoethroughid'] = id
        l, l1 = getTwoDiffExaminars(obj)
        return render(request, 'acoeverify1.html', {'andy': obj, 'obj': andy, 'vicky': l, 'vicky1': l1})
    return render(request, 'acoeverify1.html', {'andy': obj, 'obj': andy, 'vicky': l, 'vicky1': l1})


def coenote1(request):
    if (request.session['loginses']!=coeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        obj = BOSFill.objects.get(cid=request.session['coethroughid'])
        obj.coeNote1Status = "Approved"
        obj.coeNote1Date = datetime.date.today()
        obj.save()
    obj = BOSFill.objects.filter(
        acoeNote1Status='Approved', coeNote1Status='Pending')
    return render(request, 'coenote1.html', {'andy': obj})


def coeverify1(request):
    if (request.session['loginses']!=coeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        id = request.POST.get('nithin')
        obj = BOSFill.objects.get(cid=id)
        andy = Approved.objects.get(id=id)
        request.session['coethroughid'] = id
        l, l1 = getTwoDiffExaminars(obj)
    return render(request, 'coeverify1.html', {'obj': andy, 'andy': obj, 'vicky': l, 'vicky1': l1, 'objs': obj})


def vcnote1(request):
    if (request.session['loginses']!=vcloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        obj = BOSFill.objects.get(cid=request.session['vcthroughid'])
        obj.vcNote1Status = "Approved"
        obj.vcNote1Date = datetime.date.today()
        obj.save()
        s1 = int(request.POST.get('s1'))
        s2 = int(request.POST.get('s2'))
        s3 = int(request.POST.get('s3'))
        if(s1 == 1 or s2 == 1 or s3 == 1):
            obj1 = Examiner.objects.get(mobile=obj.examiner1)
            obj1.selected = True
            obj1.save()
        if(s1 == 2 or s2 == 2 or s3 == 2):
            obj1 = Examiner.objects.get(mobile=obj.examiner2)
            obj1.selected = True
            obj1.save()
        if(s1 == 3 or s2 == 3 or s3 == 3):
            obj1 = Examiner.objects.get(mobile=obj.examiner3)
            obj1.selected = True
            obj1.save()
        if(s1 == 4 or s2 == 4 or s3 == 4):
            obj1 = Examiner.objects.get(mobile=obj.examiner4)
            obj1.selected = True
            obj1.save()
        if(s1 == 5 or s2 == 5 or s3 == 5):
            obj1 = Examiner.objects.get(mobile=obj.examiner5)
            obj1.selected = True
            obj1.save()
        if(s1 == 6 or s2 == 6 or s3 == 6):
            obj1 = Examiner.objects.get(mobile=obj.examiner6)
            obj1.selected = True
            obj1.save()
        if(s1 == 7 or s2 == 7 or s3 == 7):
            obj1 = Examiner.objects.get(mobile=obj.examiner7)
            obj1.selected = True
            obj1.save()
        if(s1 == 8 or s2 == 8 or s3 == 8):
            obj1 = Examiner.objects.get(mobile=obj.examiner8)
            obj1.selected = True
            obj1.save()
        if(s1 == 9 or s2 == 9 or s3 == 9):
            obj1 = Examiner.objects.get(mobile=obj.examiner9)
            obj1.selected = True
            obj1.save()
    obj = BOSFill.objects.filter(
        coeNote1Status='Approved', vcNote1Status='Pending')
    return render(request, 'vcnote1.html', {'andy': obj})


def vcverify1(request):
    if (request.session['loginses']!=vcloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        id = request.POST.get('nithin')
        obj = BOSFill.objects.get(cid=id)
        andy = Approved.objects.get(id=id)
        request.session['vcthroughid'] = id
        l, l1 = getTwoDiffExaminars(obj)
    return render(request, 'vcverify1.html', {'obj': andy, 'andy': obj, 'vicky': l, 'vicky1': l1, 'objs': obj})


def acoenote2(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        obj = BOSFill.objects.get(cid=request.session['acoethroughid2'])
        obj.acoeNote2Status = "Approved"
        obj.acoeNote2Date = datetime.date.today()
        obj.s4 = request.POST.get('s4')
        obj.s5 = request.POST.get('s5')
        obj.s6 = request.POST.get('s6')
        fs = FileSystemStorage()
        photo = request.FILES['f1']
        obj.f1 = fs.save(photo.name, photo)
        photo = request.FILES['f2']
        obj.f2 = fs.save(photo.name, photo)
        photo = request.FILES['f3']
        obj.f3 = fs.save(photo.name, photo)
        obj.save()
    obj = BOSFill.objects.filter(
        vcNote1Status='Approved', acoeNote2Status='Pending')
    return render(request, 'acoenote2.html', {'andy': obj})


def acoeverify2(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        request.session['acoethroughid2'] = request.POST.get('persel')
        obj = BOSFill.objects.get(cid=request.POST.get('persel'))
    return render(request, 'acoeverify2.html', {'vicky': getExaminars(obj), "andy": obj})


def coenote2(request):
    if (request.session['loginses']!=coeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        obj = BOSFill.objects.get(cid=request.session['coethroughid2'])
        obj.coeNote2Status = "Approved"
        obj.coeNote2Date = datetime.date.today()
        obj.save()
    obj = BOSFill.objects.filter(
        acoeNote2Status='Approved', coeNote2Status='Pending')
    return render(request, 'coenote2.html', {'andy': obj})


def coeverify2(request):
    if (request.session['loginses']!=coeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        request.session['coethroughid2'] = request.POST.get('persel')
        obj = BOSFill.objects.get(cid=request.POST.get('persel'))
        return render(request, 'coeverify2.html', {'vicky': getExaminars(obj), "andy": obj})


def vcnote2(request):
    if (request.session['loginses']!=vcloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        sel = int(request.POST.get('s7'))
        mode = request.POST.get('onof')
        obj = BOSFill.objects.get(cid=request.session['vcthroughid2'])
        obj.vcNote2Status = "Approved"
        obj.vcNote2Date = datetime.date.today()
        obj.mode = mode
        obj.save()
        obj1 = getExaminars(obj)
        for i in range(0, 3):
            if(i == sel-1):
                continue
            obj1[i].selected = False
            obj1[i].save()
    obj = BOSFill.objects.filter(
        coeNote2Status='Approved', vcNote2Status='Pending')
    return render(request, 'vcnote2.html', {'andy': obj})


def vcverify2(request):
    if (request.session['loginses']!=vcloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        request.session['vcthroughid2'] = request.POST.get('persel')
        obj = BOSFill.objects.get(cid=request.POST.get('persel'))
        return render(request, 'vcverify2.html', {'vicky': getExaminars(obj), "andy": obj})


def acoenote3(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        obj = BOSFill.objects.get(cid=request.session['acoethroughid3'])
        obj.acoeNote3Status = "Approved"
        obj.acoeNote3Date = datetime.date.today()
        obj.s8 = request.POST.get('s8')
        obj.s9 = request.POST.get('s9')
        fs = FileSystemStorage()
        photo = request.FILES['f4']
        obj.f4 = fs.save(photo.name, photo)
        obj.save()
    obj = BOSFill.objects.filter(
        vcNote2Status='Approved', acoeNote3Status='Pending')
    return render(request, 'acoenote3.html', {'andy': obj})


def acoeverify3(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        request.session['acoethroughid3'] = request.POST.get('persel')
        obj = BOSFill.objects.get(cid=request.POST.get('persel'))
        return render(request, 'acoeverify3.html', {'vicky': getExaminars(obj)[0], 'andy': obj})


def coenote3(request):
    if (request.session['loginses']!=coeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        obj = BOSFill.objects.get(cid=request.session['coethroughid3'])
        obj.coeNote3Status = "Approved"
        obj.coeNote3Date = datetime.date.today()
        obj.save()
    obj = BOSFill.objects.filter(
        acoeNote3Status='Approved', coeNote3Status='Pending')
    return render(request, 'coenote3.html', {'andy': obj})


def coeverify3(request):
    if (request.session['loginses']!=coeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        request.session['coethroughid3'] = request.POST.get('persel')
        obj = BOSFill.objects.get(cid=request.POST.get('persel'))
        return render(request, 'coeverify3.html', {'vicky': getExaminars(obj)[0], "andy": obj})


def vcnote3(request):
    if (request.session['loginses']!=vcloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        obj = BOSFill.objects.get(cid=request.session['vcthroughid3'])
        obj.vcNote3Status = "Approved"
        obj.vcNote3Date = datetime.date.today()
        obj.save()
    obj = BOSFill.objects.filter(
        coeNote3Status='Approved', vcNote3Status='Pending')
    return render(request, 'vcnote3.html', {'andy': obj})


def vcverify3(request):
    if (request.session['loginses']!=vcloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        request.session['vcthroughid3'] = request.POST.get('persel')
        obj = BOSFill.objects.get(cid=request.POST.get('persel'))
        return render(request, 'vcverify3.html', {'vicky': getExaminars(obj)[0], "andy": obj})


def bosprintlist(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    obj = BOSFill.objects.all()
    obj = obj[::-1]
    return render(request, 'bosprintlist.html', {'andy': obj})


def bosprint(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        id = request.POST.get('persel')
        obj = BOSFill.objects.get(cid=id)
        request.session['bosthroughid'] = id
    return render(request, 'bosprint.html', {'andy': obj, 'vicky': getAllExaminars(obj)})


def acoeprint1(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        id = request.POST.get('persel')
        obj = BOSFill.objects.get(cid=id)
        andy = Approved.objects.get(id=id)
        request.session['acoethroughid'] = id
        l, l1 = getTwoDiffExaminars(obj)
    return render(request, 'acoeprint1.html', {'andy': obj, 'vicky': l, 'vicky1': l1, 'obj': andy})


def coeprint1(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        request.session['coethroughid2'] = request.POST.get('persel')
        obj = BOSFill.objects.get(cid=request.POST.get('persel'))
        return render(request, 'coeprint1.html', {'vicky': getExaminars(obj), "andy": obj})


def vcprint1(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    if request.method == "POST":
        request.session['vcthroughid2'] = request.POST.get('persel')
        obj = BOSFill.objects.get(cid=request.POST.get('persel'))
        return render(request, 'vcprint1.html', {'vicky': getExaminars(obj)[0], "andy": obj})


def note1print(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    obj = BOSFill.objects.all()
    return render(request, 'note1print.html', {"objs": obj})


def note2print(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    obj = BOSFill.objects.filter(vcNote1Status='Approved')
    return render(request, 'note2print.html', {"objs": obj})


def note3print(request):
    if (request.session['loginses']!=acoeloginses):
        return HttpResponseRedirect('bcvdlogin')
    obj = BOSFill.objects.filter(vcNote2Status='Approved')
    return render(request, 'note3print.html', {"objs": obj})
