from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = "KU Project"
admin.site.site_title = "KU Project PHD thesis"
admin.site.index_title = "KU Project PHD thesis"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instruction', views.instruction, name='2b'),
    path('login', views.login, name='3'),
    path('validate', views.validate, name='4'),
    path('success', views.success, name='5'),
    path('status', views.status, name='2a'),
    path('register', views.register),
    path('', views.check, name='1'),
    path('certificate', views.certificate, name="2a1"),
    path('delete', views.delete, name='2a2'),
    path('payverify', views.payverify, name='anonym'),
    path('paydetails', views.paydetails, name='anonym1'),
    path('paylogin', views.paylogin, name='flogin'),
    path('logverify', views.logverify, name='payverify'),
    path('verifydetails', views.verifydetails, name='verifydetails'),
    path('adminlogin', views.adminlogin),
    path('printform', views.printform, name='printform'),
    path('Approveds', views.ApprovedList, name='ApprovedList'),
    path('forgot', views.forgot),
    path('change', views.change),
    path('home', views.home),
    path('bcvdlogin', views.bcvdlogin),
    path('bcvdverify', views.bcvdverify),
    path('bosfill', views.bosfill),
    path('boslogin', views.boslogin),
    path('bosprint', views.bosprint),
    path('bosprintlist', views.bosprintlist),
    path('bosstatus', views.bosstatus),
    path('bosverify', views.bosverify),
    path('acoelogin', views.acoelogin),
    path('acoenote1', views.acoenote1),
    path('acoeverify1', views.acoeverify1),
    path('acoenote2', views.acoenote2),
    path('acoeverify2', views.acoeverify2),
    path('acoenote3', views.acoenote3),
    path('acoeverify3', views.acoeverify3),
    path('coelogin', views.coelogin),
    path('coenote1', views.coenote1),
    path('coeverify1', views.coeverify1),
    path('coenote2', views.coenote2),
    path('coeverify2', views.coeverify2),
    path('coenote3', views.coenote3),
    path('coeverify3', views.coeverify3),
    path('vclogin', views.vclogin),
    path('vcnote1', views.vcnote1),
    path('vcverify1', views.vcverify1),
    path('vcnote2', views.vcnote2),
    path('vcverify2', views.vcverify2),
    path('vcnote3', views.vcnote3),
    path('vcverify3', views.vcverify3),
    path('acoeprint1', views.acoeprint1),
    path('coeprint1', views.coeprint1),
    path('vcprint1', views.vcprint1),
    path('note1print', views.note1print),
    path('note2print', views.note2print),
    path('note3print', views.note3print),
    path('bosnewpassword',views.bosnewpassword),
    path('ponewpassword',views.ponewpassword),
    path('logout',views.logout),
    path('logout_PPV',views.logout_PPV),
    path('plagiarismcheck',views.plagiarismcheck),
    path('plagiarismverify',views.plagiarismverify),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handler404 = 'home.views.error_404'
# handler500 = 'home.views.error_500'