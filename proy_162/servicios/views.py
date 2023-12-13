from django.shortcuts import render, redirect
from .models import Paciente,Medico,Especialidad,Horario,HorarioMedico,EspecialidadMedico,CitaMedica
from django.urls import reverse
from django.contrib.auth import  logout 
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'home.html')
#---------Cita Medica
def citasmedicas(request):
    citasmedicas = CitaMedica.objects.all()
    detalle_cita=[]
    for cita in citasmedicas:      
        medico = cita.medico
        paciente = cita.paciente
        detalle_cita.append([cita,medico,paciente])               
    total = len(citasmedicas)
    return render(request, 'citasmedicas.html', {
        'citas': detalle_cita,
        'total': total,
    })

def editcitamedica(request, id):
    rr = reverse('admin:servicios_citamedica_change', args=[id])
    return redirect(rr)
def agregarcitamedica(request):
    return redirect(reverse('admin:servicios_citamedica_add'))
#-----------------------
def pacientes(request):
    pacientes = Paciente.objects.filter()
    return render(request, 'pacientes.html', {
        'pacientes': pacientes,
        'total':len(pacientes)
    }) 
#---------Medicos
def medicos(request):
    medicos = Medico.objects.all()
    medicos_detalle = []
    for medico in medicos:
        horarios_del_medico = HorarioMedico.objects.filter(medico=medico)
        especialidades = EspecialidadMedico.objects.filter(medico=medico)
        especialidades_detalle = [especialidad.especialidad.nombre for especialidad in especialidades]
        horarios_detalle = [horario.horario for horario in horarios_del_medico]
        medicos_detalle.append([medico, horarios_detalle, especialidades_detalle])       
    total_medicos = len(medicos)
    return render(request, 'medicos.html', {
        'medicos': medicos_detalle,
        'total': total_medicos,
    })
def editmedico(request, id):
    urleditmedico = reverse('admin:servicios_medico_change', args=[id])
    return redirect(urleditmedico)
def agregarmedico(request):
    return redirect(reverse('admin:servicios_medico_add'))
#---- ESPECIALIDAD
def especialidades(request):
    especialidades = Especialidad.objects.filter()
    return render(request, 'especialidades.html', {
        'especialidades': especialidades,
        'total':len(especialidades)
    }) 
def editespecialidad(request, id):
    urleditmedico = reverse('admin:servicios_especialidad_change', args=[id])
    return redirect(urleditmedico)
def agregarespecialidad(request):
    return redirect(reverse('admin:servicios_especialidad_add'))
#-------------------------------------
#---- HORARIO
def horarios(request):
    horarios = Horario.objects.filter()
    return render(request, 'horarios.html', {
        'horarios': horarios,
        'total':len(horarios)
    }) 
def edithorario(request, id):
    rr = reverse('admin:servicios_horario_change', args=[id])
    return redirect(rr)
def agregarhorario(request):
    return redirect(reverse('admin:servicios_horario_add'))
#-------------------------------------
#---- MEDICO - HORARIO
def medicoHorarios(request):
    medicoHorarios = HorarioMedico.objects.filter()
    return render(request, 'medicoHorarios.html', {
        'medicoHorarios': medicoHorarios,
        'total':len(medicoHorarios)
    }) 
def editmedicoHorario(request, id):
    rr = reverse('admin:servicios_horarioMedico_change', args=[id])
    return redirect(rr)
def agregarmedicoHorario(request):
    return redirect(reverse('admin:servicios_horarioMedico_add'))
#-------------------------------------

def editPaciente(request, id):
    url_admin_editar = reverse('admin:servicios_paciente_change', args=[id])
    return redirect(url_admin_editar)
def agregarpaciente(request):
    return redirect(reverse('admin:servicios_paciente_add'))



@login_required
def cerrar(request):
    logout(request)
    return redirect('home')
def singin(request):
   return redirect(reverse('admin:login'))