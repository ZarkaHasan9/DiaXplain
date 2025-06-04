from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('predict/', views.predict),
    path('predict/', views.predict, name='predict'),
    path('services/', views.services, name='services'), 
    path('about/', views.about, name='about'), 
    # path("predict/result", views.result)
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
]
