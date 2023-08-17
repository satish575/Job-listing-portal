from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . import models
# Create your views here.

def loginpage(request):
    return render(request,'login.html')
def signuppage(request):
    return render(request,'signup.html')
 
def getAllJobs(request,username):
    jobs= models.Jobs.objects.all()
    
    joblistdata={
        "jobavaliable":jobs,
        "username":username
    }
    return render(request,'jobsListing.html',joblistdata)
def logout(request):
    return render(request,'login.html')
def getJobDetail(request,job_id,username):
   jobDetails=models.Jobs.objects.get(id=job_id)
   jobdata={
       "jobdetails":jobDetails,
       "username":username
   }
   return render(request,'jobdetails.html',jobdata)

    
def submitApplicationForm(request,job_id,username):
    if request.method=="POST":
       values={
           "fullname":request.POST['fullname'],
           "username":request.POST['username'],
           "email":request.POST['email'],
           "query":request.POST['queryanswer'],
           "cv":request.FILES['cv'],
           "jobid":job_id
       }
       if models.Applications.objects.create(fullname=values['fullname'],username=values['username'],email=values['email'],query=values['query'],cv=values['cv'],jobid=values['jobid']):
           return render(request,'applyfrom.html',{"success":"registeration successful","username":username})
    return HttpResponse(values['fullname'])
def getApplicationForm(request,job_id,username):
    data={
        "job_id":job_id,
        "username":username
    }
    return render(request,'applyfrom.html',data)
def getHomepage(request,username):
   return render(request,'home.html',{"username":username})
def loginuser(request):
    
    if models.User.objects.get(username=request.POST['username']):
     userdata=models.User.objects.get(username=request.POST['username'])
     if request.POST['password'] == userdata.password:
        userInfo={
           "username":userdata.username
        }
        
        return render(request,'home.html',userInfo)
    else:
     return HttpResponse(userdata.lastname);
def RegisterUser(request):
    
    if request.method=="POST":
        values={
        "firstnamevalue":"",
        "lastnamevalue":"",
        "emailvalue":"",
        "usernamevalue":"",
        "passwordvalue":"",
        "confirmpasswordvalue":""   
    }
        errors={
            "firstname":"",
            "lastname":"",
            "email":"",
            "username":"",
            "password":"",
            "confirmpassword":""  
        }
        if request.POST['firstname']=="":
            errors['firstname']="enter firstname"
        else:
            values['firstnamevalue']=request.POST['firstname']
        if request.POST['lastname']=="":
            errors['lastname']="enter lastname"
        else:
            values['lastnamevalue']=request.POST['lastname']
        if request.POST['email']=="":
            errors['email']="enter email"
        else:
            values['emailvalue']=request.POST['email']
        if request.POST['username']=="":
            errors['username']="enter username"
        else:
            values['usernamevalue']=request.POST['username']
        if request.POST['password']=="":
            errors['password']="enter password"
        else:
            values['passwordvalue']=request.POST['password']
        if request.POST['confirmpassword']=="":
            errors['confirmpassword']="enter valid confirm password"
        elif request.POST['password'] != request.POST['confirmpassword']:
            errors['confirmpassword']="password and confirm password should match"
        if errors['firstname'] or errors['lastname'] or errors['email'] or errors['username'] or errors['password'] or errors['confirmpassword']:
               combined_dict = {**errors, **values}
               return render(request,'signup.html',combined_dict)
        else:
           models.User.objects.create(firstname=values['firstnamevalue'],lastname=values["lastnamevalue"],username=values['usernamevalue'],email=values['emailvalue'],password=values['passwordvalue'])
           return HttpResponse("user registered successfully")
    return HttpResponse("user registeration failed")

def adminpanellogin(request):
    return render(request,"adminpanellogin.html")

def loginAdmin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if username=="satish" and password=="satish":
             return HttpResponseRedirect('/adminpanel')
def adminPanel(request):
       applicantsdata=models.Applications.objects.all()
       return render(request,'adminpanel.html',{"applicant":applicantsdata})
   
def addnewjob(request):
    return render(request,'addnewjob.html')
def addJob(request):
    
    models.Jobs.objects.create(jobTitle=request.POST['jobtitle'],jobDescription=request.POST['description'],jobRequirement=request.POST['requirement'],companyName=request.POST['companyname'])
    return render(request,'addnewjob.html',{"message":"job created"})
def viewjob(request):
    jobs=models.Jobs.objects.all()
    return render(request,'viewjobs.html',{"jobs":jobs}) 
def editjob(request,job_id):
    job_data=models.Jobs.objects.get(id=job_id)
    return render(request,'edit.html',{"jobdata":job_data})
def edit(request,job_id):
    job_data=models.Jobs.objects.get(id=job_id)
    job_data.jobTitle=request.POST['jobtitle']
    job_data.jobDescription=request.POST['description']
    job_data.jobRequirement=request.POST['requirement']
    job_data.companyName=request.POST['companyname']
    job_data.save()
    return HttpResponseRedirect('/viewjob')
    
def deleteJob(request,job_id):
    obj= models.Jobs.objects.get(id=job_id)
    obj.delete()
    return HttpResponseRedirect('/viewjob')

def Applicantdetails(request,applicantid,jobid):
    obj=models.Applications.objects.get(id=applicantid)
    obj2=models.Jobs.objects.get(id=jobid)
    
    objdata={
        "username":obj.username,
        "fullname":obj.fullname,
        "email":obj.email,
        "query":obj.query,
        "cvlink":obj.cv,
        "jobtitle":obj2.jobTitle
        
    }
    return render(request,'applicantdetailspage.html',objdata)
    