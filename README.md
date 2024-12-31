# DJANGO-CGPA-CALCULATOR
This is an repository that include my first Django project a simple CGPA Calculator 

Starting the Project Folder
To start the project use this command

django-admin startproject tutorial
cd core

To start the app use this command

python manage.py startapp ktucal

Now add this app to the ‘settings.py’

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ktucal",
]

models.py : This Django model includes fields for user (linked to the built-in User model), 
name, grade (with predefined choices), and Roll no.


from django.db import models

# Create your models here.
class result(models.Model):
    Name = models.CharField(max_length=255)
    Rollno = models.CharField(max_length=255)
    Semester_1=models.FloatField(default=0)
    Semester_2=models.FloatField(default=0)
    Semester_3=models.FloatField(default=0)
    Semester_4=models.FloatField(default=0)
    Semester_5=models.FloatField(default=0)
    Semester_6=models.FloatField(default=0)
    Semester_7=models.FloatField(default=0)
    Semester_8=models.FloatField(default=0)
    Total_Credit=models.IntegerField(default=160)
    Total_CGPA=models.FloatField(default=0)


views.py : In below code, Django application includes views for a CGPA calculator, include semester grade, name, roll no etc.

from django.shortcuts import render,redirect
from ktucal.models import result

# Create your views here.
def home(request):
   return render(request,'home.html')
   

def calculate(request):
    if request.method=='POST':
      name=request.POST.get('name',None)
      rollno=request.POST.get('rollno',None)
      s1=float(request.POST.get('s1',None))
      s1sum=s1*17
      s2=float(request.POST.get('s2',None))
      s2sum=s2*21
      s3=float(request.POST.get('s3',None))
      s3sum=s3*22
      s4=float(request.POST.get('s4',None))
      s4sum=s4*22
      s5=float(request.POST.get('s5',None))
      s5sum=s5*23
      s6=float(request.POST.get('s6',None))
      s6sum=s6*23
      s7=float(request.POST.get('s7',None))
      s7sum=s7*15
      s8=float(request.POST.get('s8',None))
      s8sum=s8*17
      totalsemsum=float(s1sum+s2sum+s3sum+s4sum+s5sum+s6sum+s7sum+s8sum)
      cgpa=float(totalsemsum/160)
      temp = result.objects.create(
         Name=name,
         Rollno=rollno,
         Semester_1=s1,Semester_2=s2,Semester_3=s3,Semester_4=s4,
         Semester_5=s5,Semester_6=s6,Semester_7=s7,Semester_8=s8,
         Total_CGPA=cgpa)
      temp.save()
      final={'name':name,'rollno':rollno,'cgpa':cgpa,}
      return render(request,'suc.html',{'final':final})
    else:
      return render(request,'ktucal.html')

 
urls.py : The main `urls.py` file in this Django project includes paths for the admin interface and includes URLs from the 'ktucal.urls' module 
using the 'include' function, promoting modularity and organization in the project's URL configuration. 


from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('register.urls')),
    path('',include('diaryentry.urls')),
    path('',include('ktucal.urls'))
]


app/urls.py : The 'urls.py' file in the 'ktucal' app of this Django project includes paths for views like 'cgpa_calculator'       

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('ktucal/',views.calculate)
]


Creating GUI
home.html: This HTML file implements a simple intro of a CGPA Calculator web application

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>CGPA FINDER</title>
  </head>
  <body style="background-color: black;">
    

  <div class="container" style="display: flex; justify-content: center; align-items: center; height: 100vh;">
    <div class="col-md-12">
     <div class="row">
       <h1 style="text-align: center; font-style: Bold; color: white; font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;">EDGE ICT Project | MBSTU</h1>
     </div>
	<div class="row">
       <h2 style="text-align: center; font-style: Bold; color: white; font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;">CGPA Calculator</h2>
     </div>
     <div class="row">
       <form method="GET" action="/ktucal/" class="form-inline">
       {% csrf_token %}  
       <button type="submit" class="btn btn-primary" style="width: 100%;">Click Here</button>
       </form>
     </div> 
    </div>
  </div>
    

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    -->
	<footer>
            <p id="copyright" class="copyright">
                Copyright © 2024 All rights reserved | EDGE ICT | MBSTU
            </p>
        </footer>
  </body>
</html>


ktucal.html contain,

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>CGPA FINDER</title>
  </head>
  <body style="background-color: black;">
    

  <div class="container" style="display: flex; justify-content: center; align-items: center; height: 100vh;">
    

    <form method="POST" action="/ktucal/">
        {% csrf_token %}
        <div class="row" style="gap:50px; color: white; font-style: italic; font-size: larger;">
          <h1>CGPA FINDER</h1>
        <div class="row">
          <div class="form-group col-md-6">
            <label for="inputEmail4">Name</label>
            <input type="text" class="form-control" id="name" placeholder="Name" name="name">
          </div> 
          <div class="form-group col-md-6">
            <label for="inputPassword4">Roll No</label>
            <input type="text" class="form-control" id="rollno" placeholder="roll no" name="roll no">
          </div>
        </div>
        <div class="row">
         <div class="form-group col-md-3">
           <label for="inputAddress">Semester 1</label>
           <input type="number" class="form-control" id="s1" name="s1" step="any">
         </div>
         <div class="form-group col-md-3">
           <label for="inputAddress2">Semester 2</label>
           <input type="number" class="form-control" iid="s2" name="s2" step="any">
         </div>
         <div class="form-group col-md-3">
            <label for="inputAddress2">Semester 3</label>
            <input type="number" class="form-control" id="s3" name="s3" step="any">
          </div>
          <div class="form-group col-md-3">
            <label for="inputAddress2">Semester 4</label>
            <input type="number" class="form-control" id="s4" name="s4" step="any">
          </div>
        </div>
        <div class="row">
            <div class="form-group col-md-3">
              <label for="inputAddress">Semester 5</label>
              <input type="number" class="form-control" id="s5" name="s5" step="any">
            </div>
            <div class="form-group col-md-3">
              <label for="inputAddress2">Semester 6</label>
              <input type="number" class="form-control" id="s6" name="s6" step="any">
            </div>
            <div class="form-group col-md-3">
               <label for="inputAddress2">Semester 7</label>
               <input type="number" class="form-control" id="s7" name="s7" step="any">
             </div>
             <div class="form-group col-md-3">
               <label for="inputAddress2">Semester 8</label>
               <input type="number" class="form-control" id="s8" name="s8" step="any">
             </div>
           </div>
        
        <button type="submit" class="btn btn-primary">Enter to Database</button>
      </div>
      </form>
   
    </div>
    


    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    -->
	<footer>
            <p id="copyright" class="copyright">
                Copyright © 2024 All rights reserved | EDGE ICT | MBSTU
            </p>
        </footer>
  </body>
</html>


suc.html contain,

<html>
  <head>
    <link href="https://fonts.googleapis.com/css?family=Nunito+Sans:400,400i,700,900&display=swap" rel="stylesheet">
  </head>
    <style>
      body {
        text-align: center;
        padding: 40px 0;
        background: #EBF0F5;
      }
        h1 {
          color: #88B04B;
          font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
          font-weight: 900;
          font-size: 40px;
          margin-bottom: 10px;
        }
        p {
          color: #404F5E;
          font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
          font-size:20px;
          margin: 0;
        }
      i {
        color: #9ABC66;
        font-size: 100px;
        line-height: 200px;
        margin-left:-15px;
      }
      .card {
        background: white;
        padding: 60px;
        border-radius: 4px;
        box-shadow: 0 2px 3px #C8D0D8;
        display: inline-block;
        margin: 0 auto;
      }
    </style>
    <body>
      <div class="card">
      <div style="border-radius:200px; height:200px; width:200px; background: #F8FAF5; margin:0 auto;">
        <i class="checkmark">✓</i>
      </div>
        <h1>Success</h1> 
        <p>Data has Entered in to the database;<br/>{{final.name}} ; Roll No: {{final.rollno}} has a CGPA of {{final.cgpa}}</p>
      </div>
	<footer>
            <p id="copyright" class="copyright">
                Copyright © 2024 All rights reserved | EDGE ICT | MBSTU
            </p>
        </footer>
    </body>
</html>



#Deployment of the Project

Run these commands to apply the migrations:

python3 manage.py makemigrations
python3 manage.py migrate

Run the server with the help of following command:

python3 manage.py runserver