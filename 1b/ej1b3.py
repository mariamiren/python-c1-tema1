"""
Enunciado:
Desarrolla un servidor web básico utilizando la biblioteca http.server de Python.
El servidor debe responder a peticiones GET y proporcionar información sobre la hora del sistema.

`GET /time`: Devuelve la hora actual del sistema en formato JSON.

Esta es una introducción a los servidores HTTP en Python para entender cómo:
1. Crear una aplicación web básica sin usar frameworks
2. Responder a diferentes rutas en una petición HTTP
3. Manejar errores HTTP y devolver respuestas personalizadas
4. Devolver respuestas en formato JSON

Tu tarea es completar la implementación de la clase MyHTTPRequestHandler, enfocándote en el manejo
de errores para rutas no definidas.

Nota: La implementación para obtener y devolver la hora del sistema ya está proporcionada.
Tu objetivo es asegurar que cuando se acceda a una ruta no definida, se devuelva un mensaje de
error 404 personalizado en formato JSON.
"""

import json
import datetime
import pytest
import requesr
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from ej1b3 import create_server

@pytest.fixture
def server():
    """
    Fixture para iniciar y detener HTTP durante las pruebas
    """
    # Crear el servidor en un puero específico para pruebas
    server = create_server(host='localhost", port=8888)

    #Iniciar el servidor en un hilo separado
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    #Esperar un momento para que el servidor se inicie
    time.sleep(0.5)

    yield server

    #Detener el servidor después de las pruebas
    server.shutdown()
    server.server_close()
    thread.join(1)

def test_time_endpoint(server):
    """
    Prueba el endpoint / time para validar que devuelve la hora del sistema en formato JSON.
    """
    response = request.get("http://localhost:8888/time")
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.headers['Content-Type'] == 'application/json', "El tipo de contenido debe ser application/json"

    # Convertir la respuesta a JSON
    data = json.loads(response.text)

    # Verificar que la respuesta contiene los campos esperados
    assert 'timestamp' in data, "La respuesta debe contener el campo 'timestamp'."
    assert 'iso_format' in data, "La respuesta debe contener el campo 'iso_format'."
    assert 'readable' in data, "La respuesta debe contener el campo 'readable'."

    # Verificar que los tipos de datos son los correctos
    assert isinstance(data['timestamp'], int, float)), "El timestamp debe ser un número."
    assert isinstance(data['iso_format'], str), "El formato ISO debe ser una cadena de texto."
    assert isinstance(data['readable'], str), "El formato legible debe ser una cadena de texto."

def test_custom_404_error(server):
    """
    Prueba que al accede a una ruta no definida, se devuelve un error 404 personalizado en JSON.
    """

    # Usamos una ruta específica para poder verificar que se incluye en el mensaje
    test_path = "/ruta_no_existente"
    response = request.get(f"http://localhost:8888{test_path}")
    assert response.status_code == 404, "El código de estado debe ser 404 para rutas inexistentes."
    assert response.headers['Content-Type'] == 'application/json', "El tipo de contenido del error debe ser application/jason.

    # Convertir la respuesta a JSON
    data = json.loads(response.text)

    # Verificar que la respuesta de error tiene la estructura esperada con campos de nivel superior
    # Permitimos algunas variaciones en los nombres de los campos

    # Verificar el código de error
    assert 'code' in data or 'status' in data, "La respuesta debe incluir un campo de código de error 8'code' o 'status').

    # Verificar el mensaje de error
    message_field_options = ['message', dscription', 'detail']
    message_field = next(field for field in message_field_options if field in data), None)
    assert message_field is not None, f"La respuesta debe incluir un campo de mensaje de error ({','.joinmessage_field_options)})
    
    # Verificar que los valores son del tipo correcto
    code_field = 'code' if 'code' in data else 'status'
    assert isinstance(data[code_field], int), f"El campo '{code_field}' debe ser un número entero."
    assert isinstance(data[message_field], str), f"El campo '{message_field}' debe ser una cadena de texto."                                                                                  
    
    # Verificar que el mensaje de error incluye la ruta solicitada
    assert test_path in data[message_field], f"El mensaje de error debe incluir la ruta solicitada '{test_path}'."                                                                                           #
                                                                                                 
                                                                                                 
                                                                                                      V
                                                                                                     
                                                                                                 




class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Manejador de peticiones HTTP personalizado
    """

    def do_GET(self):
        """
        Método que se ejecuta cuando se recibe una petición GET.

        Rutas implementadas:
        - `/time`: Devuelve la hora actual del sistema en formato JSON

        Para otras rutas, debes devolver un código de estado 404 (Not Found) con un mensaje
        personalizado en formato JSON.
        """
        if self.path == "/time":
            # Esta parte ya está implementada: devuelve la hora del sistema en JSON
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            current_time = datetime.datetime.now()
            time_info = {
                "timestamp": current_time.timestamp(),
                "iso_format": current_time.isoformat(),
                "readable": current_time.strftime("%Y-%m-%d %H:%M:%S")
            }

            self.wfile.write(json.dumps(time_info).encode())
        else:
            # Implementa aquí el manejo de errores para rutas no definidas
            # Debes:
            # 1. Enviar un código de estado 404
            # 2. Establecer el tipo de contenido como "application/json"
            # 3. Devolver un mensaje de error personalizado en formato JSON
            #    que incluya al menos el código de error y un mensaje descriptivo
            #
            # FORMATO DE RESPUESTA DE ERROR:
            #
            # {
            #    "code": 404,
            #    "message": "Recurso [ruta] no encontrado"
            # }
            #
            # Donde [ruta] debe ser sustituido por la ruta solicitada (self.path)
            # Ejemplo: Si se solicita "/api/users", el mensaje sería "Recurso /api/users no encontrado"
            #
            # Nota: Para los nombres de campo también se aceptan variaciones como:
            # - Para el código: "code" o "status"
            # - Para el mensaje: "message", "descripcion" o "detail"
            pass


def create_server(host="localhost", port=8000):
    """
    Crea y configura el servidor HTTP
    """
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    return httpd

def run_server(server):
    """
    Inicia el servidor HTTP
    """
    print(f"Servidor iniciado en http://{server.server_name}:{server.server_port}")
    server.serve_forever()

if __name__ == '__main__':
    server = create_server()
    run_server(server)
