from multiprocessing import context
from django.shortcuts import render , HttpResponse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from firstpage.models import Detail
from firstpage.models import student
#####  Experi ###########
import seaborn as sns
import matplotlib.pyplot as plt 

# Create your views here.

def index(request):
    return render(request,'index.html')
    #return HttpResponse("HomePage")


def predictions(request):
    predicted_status = Detail.objects.all()
    context = {
        'predicted_status' : predicted_status
    }
    return render(request,'predictions.html',context)
    #return render(request,'predictions.html',context)
    #return HttpResponse("HomePage")



def predictCovid(request):
    if request.method == 'POST':
        ######################### THESE ARE NOT USED FOR PREDICTION #######################
        name = request.POST['name']
        email = request.POST['email']
        phone1 =  request.POST['phone']
        city = request.POST['city']
        landmark = request.POST['landmark']
        ##################################################################################
        gender = int(request.POST['Gender'])
        Age = int(request.POST['Age'])
        fever = int(request.POST['fever'])
        cough = int(request.POST['cough'])
        runny_nose = int(request.POST['runny_nose'])
        muscle_soreness = int(request.POST['muscle_soreness'])
        pneumonia = int(request.POST['pneumonia'])
        diarrhea = int(request.POST['diarrhea'])
        lung_infection = int(request.POST['lung_infection'])
        travel_history = int(request.POST['travel_history'])
        isolation_treatment = int(request.POST['isolation_treatment'])

        filename="static\\raw_data2.csv" 
        trainfile=pd.read_csv(filename)
       
        x=trainfile.drop('SARS-CoV-2 Positive',axis=1)
        y=trainfile['SARS-CoV-2 Positive']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)   

        xgb_model = XGBClassifier(n_estimators=10,max_depth=4)
        xgb_model.fit(x_train,y_train)
        features =  np.array([[Age,fever,cough,runny_nose,muscle_soreness,pneumonia,diarrhea,lung_infection,travel_history,isolation_treatment,gender]])

        prediction = xgb_model.predict(features) 
        ###################################################################
        logistic_model = LogisticRegression(random_state=1)
        logistic_model  = LogisticRegression(solver='liblinear')
        logistic_model.fit(x_train,y_train)

        severity = logistic_model.predict(features) 
        s = logistic_model.predict_proba(features)[:,1]

        if s < 0.25:
            context={'b':' You Are Safe!'}
        elif s >= 0.25 and s < 0.5:
            context={'b':'Yor Are Having Mild Symptoms'}
        elif s >= 0.5 and s < 0.75:
            context={'b':'Yor Are Having Moderate Symptoms'}
        else:
            context={'b':'Yor Are Having Severe Symptoms'}  
        ######################################################################### 

        ######################## FOR STRING REPRESENTATION IN ALL PREDICTIONS #################
        if gender == 1:
            gen = "male"
        else:       
            gen = "female"
                                ####################################################
        if prediction==1:
            pred_status = "Positive"
        else:
            pred_status = "Negative"
                                #####################################################
        if s < 0.25:
            severity_status = "NA"
        elif s >= 0.25 and s < 0.5:
            severity_status = "Mild"
        elif s >= 0.5 and s < 0.75:
            severity_status = "Moderate"
        else:
            severity_status = "Severe"  
         ###################### ADDING DATA TO MODEL/DATABASE ##########################################
        ins = Detail(name=name,email=email,phone=phone1,city=city,landmark=landmark,gender=gen,Age=Age,fever=fever,cough=cough,runny_nose=runny_nose,muscle_soreness=muscle_soreness,pneumonia=pneumonia,diarrhea=diarrhea,lung_infection=lung_infection,travel_history=travel_history,isolation_treatment=isolation_treatment,prediction=pred_status,SeverityIndex=severity_status)
        ins.save()
        ################################################################################################  
        if prediction==1:
           #return render(request,'result.html',context) 
           return render(request,'result.html',context)   
        else:
            #return render(request,'result1.html',context)
            return render(request,'result1.html',context)  
           
    return render(request,'index.html')


###################### Experiment ######################################



    

