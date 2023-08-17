
from django.urls import path

from . import views
urlpatterns = [
    path('',views.loginpage),
    path('signup/',views.signuppage),
    path('RegisterUser/',views.RegisterUser),
    path('login/',views.loginuser),
    path('JobsAvaliable/<username>',views.getAllJobs),
    path('home/<username>',views.getHomepage),
    path('jobDetail/<int:job_id>/<username>',views.getJobDetail),
    path('applyApplication/<int:job_id>/<username>',views.getApplicationForm,name='applyApplication'),
    path('submitApplication/<int:job_id>/<username>',views.submitApplicationForm),
    path('adminpanel/',views.adminPanel),
    path('addnewjob/',views.addnewjob),
    path('viewjob/',views.viewjob),
    path('editjob/<int:job_id>',views.editjob),
    path('edit/<int:job_id>',views.edit),
    path('delete/<int:job_id>',views.deleteJob),
    path('addJob/',views.addJob),
    path('Applicantdetails/<int:applicantid>/<int:jobid>',views.Applicantdetails),
    path('logout/',views.logout),
    path("adminpanellogin/",views.adminpanellogin),
    path("loginAdmin/",views.loginAdmin)
    
    
   
]


