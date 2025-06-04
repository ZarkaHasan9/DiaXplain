import numpy as np
import joblib  
from django.shortcuts import render, redirect
from django.shortcuts import render,HttpResponse
from lime.lime_tabular import LimeTabularExplainer
from django.utils.safestring import mark_safe
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully')
        return redirect('login')

    return render(request, 'signup.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
def services(request):
    return render(request, 'services.html')
def about(request):
    return render(request, 'about.html')

  
import pandas as pd
 
def home(request):
    return render(request,'home.html')
    
from django.shortcuts import render
import numpy as np
import joblib
from lime.lime_tabular import LimeTabularExplainer
from django.utils.safestring import mark_safe

 
 
model = joblib.load("static/best_model.pkl")   
scaler = joblib.load("static/scaler.pkl")
xtrain_scaled = joblib.load("static/xtrain_scaled.pkl")   
feature_names = joblib.load("static/feature_names.pkl")
class_names = joblib.load("static/class_names.pkl")

def predict(request):
    if request.method == "POST":
        try:
            # Parse form inputs
            pregnancies = float(request.POST.get("pregnancies", 0))
            glucose = float(request.POST.get("glucose", 0))
            bloodpressure = float(request.POST.get("bloodpressure", 0))
            skinthickness = float(request.POST.get("skinthickness", 0))
            insulin = float(request.POST.get("insulin", 0))
            bmi = float(request.POST.get("bmi", 0))
            dpf = float(request.POST.get("dpf", 0))
            age = float(request.POST.get("age", 0))
            explain_flag = request.POST.get("explain", "") == "yes"

            # Prepare input and scale it
            input_data = np.array([[pregnancies, glucose, bloodpressure, skinthickness,
                                    insulin, bmi, dpf, age]])
            input_scaled = scaler.transform(input_data)

            # Make prediction
            prediction = model.predict(input_scaled)[0]
            result = "Diabetic" if prediction == 1 else "Non-Diabetic"

            influenced_features = []
            not_influenced_features = []

            if explain_flag:
                # Generate LIME explanation using scaled training data
                explainer = LimeTabularExplainer(
                    training_data=xtrain_scaled,
                    feature_names=feature_names,
                    class_names=class_names,
                    mode='classification'
                )
                explanation = explainer.explain_instance(
                    data_row=input_scaled[0],
                    predict_fn=model.predict_proba
                )

                # Format features by impact
                top_features = sorted(explanation.as_list(), key=lambda x: abs(x[1]), reverse=True)

                for feature, weight in top_features:
                    direction = "increases" if weight > 0 else "reduces"
                    if abs(weight) > 0.05:
                        influenced_features.append(
                            f"<strong>{feature}</strong> {direction} diabetes risk with a weight of {weight:.3f}"
                        )
                    else:
                        not_influenced_features.append(
                            f"<strong>{feature}</strong> had minimal impact on diabetes risk."
                        )

            return render(request, "result.html", {
                "result": result,
                "prediction": prediction,
                "influenced_features": influenced_features,
                "not_influenced_features": not_influenced_features
            })

        except Exception as e:
            return render(request, "result.html", {"result": f"Error: {e}"})

    return render(request, "predict.html")

 
from .forms import FeedbackForm

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('about')  # assuming 'about' is the name of your about page route
    return redirect('about')
