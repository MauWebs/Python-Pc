import getpass
import platform
import socket

import psutil
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PC
from .serializers import PCSerializer


def pcData():
    sistema_operativo = platform.system()
    version_sistema = platform.version()
    arquitectura_sistema = platform.architecture()

    nombre_usuario = getpass.getuser()

    nombre_host = socket.gethostname()
    direccion_ip = socket.gethostbyname(nombre_host)

    info_cpu = platform.processor()
    num_cores = psutil.cpu_count(logical=False)
    num_cores_logicos = psutil.cpu_count(logical=True)

    memoria_total = psutil.virtual_memory().total
    memoria_disponible = psutil.virtual_memory().available

    dataPc = {
        "sistema_operativo": sistema_operativo,
        "version_sistema": version_sistema,
        "arquitectura_sistema": arquitectura_sistema,
        "nombre_usuario": nombre_usuario,
        "nombre_host": nombre_host,
        "direccion_ip": direccion_ip,
        "info_cpu": info_cpu,
        "num_cores_fisicos": num_cores,
        "num_cores_logicos": num_cores_logicos,
        "memoria_total": memoria_total,
        "memoria_disponible": memoria_disponible,
    }

    return dataPc

@api_view(['POST'])
def savePcData(request):
    if request.method == 'POST':
        data = pcData()
        pc = PC.objects.create(**data)
        serializer = PCSerializer(pc, many=False)
        return Response(serializer.data)
    

@api_view(['GET'])
def getAllPcData(request):
    if request.method == 'GET':
        pc = PC.objects.all()
        serializer = PCSerializer(pc, many=True)
        return Response(serializer.data)