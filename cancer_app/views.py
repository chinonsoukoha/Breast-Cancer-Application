from operator import mod
import re
from django.forms.fields import EmailField
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from tensorflow.python.client.session import Session
from tensorflow.python.eager.context import context
from tensorflow.python.framework.ops import Graph
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .models import Assess, Patient_data
import pickle
from keras.models import load_model
from keras.preprocessing import image
import json
import numpy as np
import tensorflow as tf
# Create your views here.
def landing(request):
    return render(request, 'cancer_app/landingpage.html')

def about(request):
    return render(request, 'cancer_app/about.html')

def instructions(request):
    return render(request, 'cancer_app/instructions.html')

def insights(request):
    return render(request, 'cancer_app/insights.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'cancer_app/signup.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Your details are incorrect. Please confirm or create an account.')
        context = {}
        return render(request, 'cancer_app/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'cancer_app/homepage.html')


@login_required(login_url='login')
def diagnosis(request):
    context = {'a': 1}
    
    return render(request, 'cancer_app/diagnose.html', context)


img_height, img_width = 224, 224


model_graph = Graph()
with model_graph.as_default():
    tf_session = Session()
    with tf_session.as_default():
        model = load_model('/Users/chinonsoukoha/Final Year Project/Breast_Cancer_App/mobilenet.h5')

def predict(x):
    with model_graph.as_default():
        with tf_session.as_default():
            predi = model.predict(x)[0]
            print(predi)
            return predi

@login_required(login_url='login')
def diagResult(request):
    print(request)
    print(request.POST.dict())
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage(location="media/")
    filePathName = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    print(filePathName)
    testImage = './'+ filePathName
    img = image.load_img(testImage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x = x.reshape(1, img_height, img_width, 3)
    x = tf.keras.applications.mobilenet.preprocess_input(x)
    diagnosis = predict(x)
    print(diagnosis)
    def dataStore(value):
        if value [0] < value[1]:
            predi = 'malignant'
        elif value [0] > value[1]:
            predi = 'benign'
        else:
            predi = 'error'
        return predi
    result = dataStore(diagnosis)
    ben = (diagnosis[0] * 100) 
    ben = (format(ben, ".2f"))
    print(ben)
    mal = (diagnosis[1] * 100) 
    mal = (format(mal, ".2f"))
    print(mal) 
    print(result)
    context = {'filePathName' : filePathName, 'diagnosis' : diagnosis, 'image': x, 'benign': ben, 'malignant': mal, 'result': result}
    id = request.POST.get ('id')
    full_name = request.POST.get ('full_name')
    if Patient_data.objects.filter(patient_id = id).exists():
        messages.info(request, "This patient has already been diagnosed")
        return render(request, 'cancer_app/diagnose.html', context)
    else:
        data = Patient_data(patient_name = full_name, patient_id = id, hist_image = fileObj.name, diagnosis_result = result, pathologist=request.user)
        data.save()
        return render(request, 'cancer_app/diagnoseResult.html', context)

@login_required(login_url='login')
def risk(request):
    patient_db = Patient_data.objects.filter(pathologist=request.user)

    return render(request, 'cancer_app/assess.html', {"patients": patient_db})


def do_classify (features): 
    features = {k: int (v) for k, v in features.items () }
    model = pickle.load (open  ("/Users/chinonsoukoha/Final Year Project/Breast_Cancer_App/logistic_regression.sav", 'rb'))
    row =  (list (features.values ()))
    print (row)
    prediction = model.predict_proba ([ row ])[0]
    print (prediction)
    return prediction



@login_required(login_url='login')
def riskResult(request):
    context = {} 
    pid = request.POST.get ('pid')
    
    menopause = request.POST.get ('menopause') 
    context['menopause'] = menopause

    agegrp = request.POST.get ('agegrp') 
    context['agegrp'] = agegrp

    density = request.POST.get ('density') 
    context['density'] = density

    bmi = request.POST.get ('bmi') 
    context['bmi'] = bmi

    agefirst = request.POST.get ('agefirst') 
    context['agefirst'] = agefirst

    nrelbc = request.POST.get ('nrelbc') 
    context['nrelbc'] = nrelbc

    brstproc = request.POST.get ('brstproc') 
    context['brstproc'] = brstproc

    lastmamm = request.POST.get ('lastmamm') 
    context['lastmamm'] = lastmamm

    surgmeno = request.POST.get ('surgmeno') 
    context['surgmeno'] = surgmeno

    hrt = request.POST.get ('hrt') 
    context['hrt'] = hrt

    invasive = request.POST.get ('invasive') 
    context['invasive'] = invasive

    assessment = do_classify (context)
    context['assessment'] = assessment
    print(assessment)
    def dataStore(value):
        if value [0] < value[1]:
            predi = 'high risk'
        elif value [0] > value[1]:
            predi = 'low risk'
        else:
            predi = 'error'
        return predi
    result = dataStore(assessment)
    ben = (assessment[0] * 100) 
    ben = (format(ben, ".2f"))
    context['benign'] = ben
    print(ben)
    mal = (assessment[1] * 100) 
    mal = (format(mal, ".2f"))
    context['malignant'] = mal
    print(mal) 
    context['result'] = result
    print(result)
    data = Assess.objects.all()
    data = Assess(patient_id = Patient_data.objects.get(patient_id=pid), menopause= menopause, age = agegrp, density = density, bmi = bmi, agefirst = agefirst, nrelbc = nrelbc, brstproc = brstproc, lastmamm=lastmamm, surgmeno=surgmeno, hrt=hrt, invasive=invasive, risk_result = result, pathologist = request.user)
    data.save()

    return render(request, 'cancer_app/riskResult.html', context) 

def history(request):
    patients = Patient_data.objects.filter(pathologist=request.user)
    return render(request, 'cancer_app/history.html', {'patients': patients})

def historyRisk(request):
    risk_data = Assess.objects.filter(pathologist=request.user) 
    return render(request, 'cancer_app/historyRisk.html', {'risk_data': risk_data})                                                  