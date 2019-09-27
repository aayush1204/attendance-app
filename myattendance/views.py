from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime
from myattendance.models import StudentEntries
from django.contrib.auth.decorators import login_required
from accounts.views import *
# Create your views here.

@login_required
def dashboard(request):
    
    # st=StudentEntries.objects.create(idn="2",student_name=request.user,subject_name="DLDA",total_lectures="4",attended_lectures="2",missed_lectures="1")
    # st.save()
    # text= {"student_name":request.user,"subject_name":"ECCF","total_lectures":"3","attended_lectures":"2","missed_lectures":"1"} 
    
    # testsave= StudentEntries.objects.create(**text)
    # testsave.save()
    db = StudentEntries.objects.all()
    return render(request,"dash.html",{'db':db})

# def add_btn(request):
#     if request.GET.get('add_btn'):
#         db= StudentEntries.objects.get(subject_name="ECCF")
#         # for i in db:

#         #     i.total_lectures=i.total_lectures+1
#         #     # i.save()
#         db.total_lectures= "10"
#         db.save(['total_lectures'])    
#         # db= StudentEntries.objects.all()
#     return render_to_response(request,"dash.html",{'db':db})

def updateinfo(request, p):
    
    tlec=request.GET['totallectures']
    mlec=request.GET['missedlectures']
    alec=request.GET['attendedlectures'] #querydict object

    
    StudentEntries.objects.filter(idn=p).filter(student_name=request.user).update(total_lectures=tlec,missed_lectures=mlec,attended_lectures=alec)

    db=StudentEntries.objects.all()
    
    return render(request,"dash.html",{'db':db})    

def editinfo(request, sb):
    
    dm=StudentEntries.objects.get(idn=sb)
        

    return render(request,"Edit.html",{'dm':dm})

def deletesubject(request, sb):
    dm=StudentEntries.objects.filter(idn=sb).delete()
    # dm.save()

    db=StudentEntries.objects.all()
    return render(request,"dash.html",{'db':db})


def addsubject(request):
    return render(request,"AddSubject.html")

def addsubjecttodatabase(request):        
    tlec=request.GET['totallectures']
    mlec=request.GET['missedlectures']
    alec=request.GET['attendedlectures'] #querydict object
    sname=request.GET['subjectname']

    am=StudentEntries.objects.all().last()
    q=am.idn
    q=q+1
    db = StudentEntries.objects.create(idn=q,total_lectures=tlec,missed_lectures=mlec,attended_lectures=alec,subject_name=sname,student_name=request.user)
    db.save()
    db=StudentEntries.objects.all()
    
    return render(request,"dash.html",{'db':db})    