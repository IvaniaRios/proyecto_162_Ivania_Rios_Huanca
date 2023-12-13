from django.contrib import admin
from django.urls import path
from servicios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cerrar/', views.cerrar, name='cerrar'),
    path('singin/', views.singin, name='singin'),
    path('', views.home, name='home'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('agregarpaciente/', views.agregarpaciente, name='agregarpaciente'),
    path('editPaciente/<int:id>/', views.editPaciente, name='editPaciente'),
    path('medicos/', views.medicos, name='medicos'),
    path('agregarmedico/', views.agregarmedico, name='agregarmedico'),
    path('editmedico/<int:id>/', views.editmedico, name='editmedico'),
    path('especialidades/', views.especialidades, name='especialidades'),
    path('agregarespecialidad/', views.agregarespecialidad, name='agregarespecialidad'),
    path('editespecialidad/<int:id>/', views.editespecialidad, name='editespecialidad'),

    path('horarios/', views.horarios, name='horarios'),
    path('agregarhorario/', views.agregarhorario, name='agregarhorario'),
    path('edithorario/<int:id>/', views.edithorario, name='edithorario'),
    
    path('medicoHorarios/', views.medicoHorarios, name='medicoHorarios'),
    path('agregarhorario/', views.agregarhorario, name='agregarhorario'),
    path('edithorario/<int:id>/', views.edithorario, name='edithorario'),

    path('citasmedicas/', views.citasmedicas, name='citasmedicas'),
    path('agregarcitamedica/', views.agregarcitamedica, name='agregarcitamedica'),
    path('editcitamedica/<int:id>/', views.editcitamedica, name='editcitamedica'),

]
