
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as user_views 
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    # path('vote/', views.vote, name= 'vote')

    path('vote/', views.vote, name= 'vote'),
    # path('vote-details/<pk>/', views.GeneralCourseDetailView.as_view(), name='details'),
    # path('save-vote/<pk>', views.save_vote, name="save-vote"),
    path('result/<pk>/', views.result, name="result")

]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)