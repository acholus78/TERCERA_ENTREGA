from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader


def saludo(request):
	return HttpResponse('Hola Django - Coder')


def segundaVista (request):
	return HttpResponse ("<br><br>Ya entendí! :)")


def diaDeHoy (request):
	dia = datetime.datetime.now()
	texto = f'Hoy es día: <br> {dia}'
	return HttpResponse (texto)


def miNombre (self, nombre):
	texto = f"Mi nombre es: {nombre}"
	return HttpResponse(texto)


def probandoTemplate(self):

    nom = "Ariel"
    ape = "Solovey"
    dia = datetime.datetime.now()

    listaDeNotas = [2,3,8,9,10,9,10]

    diccionario = {'nombre': nom, 'apellido': ape, 'dia': dia, 'notas': listaDeNotas}

    miHtml = open("C:/PERSONAL/CURSO_PYTHON/CODERHOUSE/TRABAJOS/TERCERA_ENTREGA/PythonProyecto1/Proyecto1/Proyecto1/Plantillas/template1.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context(diccionario) #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)