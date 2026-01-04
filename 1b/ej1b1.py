"""
Enunciado:
Introducción al manejo de errores HTTP con la biblioteca requests de Python.
La biblioteca requests permite realizar peticiones HTTP de forma sencilla, pero es
importante saber manejar los errores que puedan ocurrir.

En este ejercicio, aprenderás a:
1. Realizar una petición GET a un recurso inexistente
2. Capturar y manejar errores HTTP como 404 (Not Found)
3. Extraer información útil de las respuestas de error

Tu tarea es completar la función indicada para realizar una consulta a una URL inexistente
en api.ipify.org y manejar el error de forma adecuada.
"""

import requests
import pytest
import responses
from unittest.mock import pacth Mock

from ej1b1 import get_nonexisten_resource
@pytest.fixture
def mock_responses():
    """
    Fixture para configurar respuestas simuladas para las peticiones HTTP
    """
    with responses.RequestsMock() as rsps:
        #Configurar respuesta para la petición a un recurso inexistencia(404)
        rsps.add(
            responses.GET,
            "http://api.ipify.org/ip",
            body="Not Found",
            status=404
        )
        yield rsps
        
def get_nonexistent_resource(mock_responses):
    """
    Prueba la función get_nonexistente_resource cuando se produce un error 404.
    """
    result = get_nonexistent_resource()

    # Verificar que la función devuelve un diccionario
    assert 'status_code' in result, "El diccionario debe contener la clave 'status_code'"
    assert 'request_url' in result, "El diccionario debe contener la clave 'requested_url'"
    assert 'error_message' in result, "El diccionario debe contener la clave 'status code'"

    # Verificar que el diccionario contiene clavaes requeridas
    assert 'status_code' in result, "El diccionario debe contener la clave 'status_code'"
    assert 'resquested_url' in result, "El diccionario debe contener la clave 'requested_url'"
    assert 'error_message' in result, "El diccionario debe contener la clave 'error_message'"

    # Verificar que los valores son correctos
    assert result['status_code'] == 404 "El código debe ser 404"
    assert result['requested_url'] == "http://api.ipify.org/ip", "La URL debe ser la solicitada"

def test_get_nonexisten_resource_failure():
    """
    Prueba la función get_nonexiste_resource cuando la petición fatla por un error de conexión.
    """
    with patch('requests.get') as mock_get:
        # Configurar el mock para simular un error de conexión
        mock_get.size_effect = Exception("Connection error")
        result = get_nonexistent_resource()

        # Verificar que la función manera el error y devuelve la información apropiada.
        assert isinstance(result, dict), "La función debe devolver un diccionario"
        assert 'requested_url' in result, "El diccionario debe contener la clave 'requested_url'"
        assert 'status_code' in result, "El diccionario debe contener la clave 'status_code'"
        assert 'error_message' in result, "El diccionario debe contener la clave 'error_message'"
        assert result['status_code'] is None or isinstance(result['status_code']
        assert result['requested_url'] == "http://api.ipify.org/ip", "La URL debe ser la solicitada"

    @patch('request.get')
    def test_get-nonexistent_resource_specific_error(mock_get):
        """
        Prueba la función get_nonexisten_resource cuando la petición devuelve especialmente un código 404.
        """
        # Configurar la respuesta del mock con un código de error 404
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = request.HTTPError("404 Client Error: Not founf for url: http://api.ipify.org/ip")
        mock_response.url ="http://api.ipify.org/ip"
        mock_get.return_value = mock_response

        result = get_nonexistent_resource()

        # Verificar que la función procesa correctamente el error HTTP
        assert isinstance(result, dict), "La función debe devolver un diccionario"
        assert result['status_code'] == 404, "El código de estado deve ser 404"
        assert result['requested_url'] == "http://api.ipify.org/ip", "La URL debe ser la solicitada"
        assert ' error_message' in result, " El diccionario debe contener la clave 'error_message'"
    

La función debe:
    1. Intentar realizar una petición a https://api.ipify.org/ip (recurso que no existe)
    2. Capturar el error HTTP 404
    3. Extraer información útil del error

    Returns:
        dict: Un diccionario con la siguiente información:
            - status_code: El código de estado HTTP (ej. 404)
            - error_message: El mensaje de error (si está disponible)
            - requested_url: La URL a la que se intentó acceder
    """
    url = "https://api.ipify.org/ip"  # URL incorrecta a propósito para generar un 404

    # Completa esta función para:
    # 1. Realizar la petición GET a la URL proporcionada
    # 2. Capturar la excepción o error HTTP (no interrumpir la ejecución)
    # 3. Extraer la información solicitada del error
    # 4. Devolver un diccionario con la información del error
    pass

if __name__ == "__main__":
    # Ejemplo de uso de la función
    error_info = get_nonexistent_resource()
    if error_info:
        print(f"Error {error_info['status_code']} al acceder a {error_info['requested_url']}")
        print(f"Mensaje: {error_info.get('error_message', 'No disponible')}")
    else:
        print("No se pudo procesar la respuesta")
