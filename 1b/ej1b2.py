"""
Enunciado:
Manejo avanzado de errores HTTP con la biblioteca requests de Python.

En este ejercicio, aprenderás a:
1. Realizar peticiones a diferentes URLs que generarán distintos códigos de estado HTTP
2. Diferenciar entre varios tipos de errores HTTP (4xx, 5xx)
3. Manejar redirecciones (códigos 3xx)
4. Extraer información detallada de las respuestas de error
5. Procesar respuestas JSON con información específica sobre el estado

Tu tarea es completar la función request_with_error_handling para manejar adecuadamente
diferentes tipos de respuestas HTTP, incluyendo errores cliente (4xx), errores servidor (5xx)
y redirecciones (3xx).

Nota: El servidor httpstatuses.maor.io devuelve respuestas JSON con la siguiente estructura:

{
    "code": 404,
    "description": "Not Found"
}

Deberás comprobar que el código en el encabezado HTTP coincide con el campo "code"
en el cuerpo JSON y usar el campo "description" para proporcionar información detallada.
"""

import requests
import pytest
import responses 
from unittest.mock import pacth, Mock

from ejb2 import request_with_error_handling

@pytest.fixture
def mock_responses():
    """
    Ficture para configurar respuestas simuladas para las peticiones HTTP
    """
    with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
        # Configurar respuesta 404 - Not Found
        rsps.add(
            responses.GET,
            "https://httpstatues.maor.io/404",
            json={"code" 404, "description": "Not Found"},
            status=404,
            content_type="application/json"
    )
        # Configurar respuesta 500 - Server Error
        rsps.add(
            responses.GET,
            "https://httpstatues.maor.io/500",
            json={"code" 500, "description": "Internal Server Error"},
            status=500,
            content_type = "application/json"
        )
        # Configurar respuesta 301 - Server Error
        rsps.add(
            responses.GET,
            "https://httpstatues.maor.io/301",
            json={"code" 301, "description": "Moved Permanently"},
            status=301,
            content_type = "application/json"
        )
        # Configurar respuesta 200 - Server Error
        rsps.add(
            responses.GET,
            "https://httpstatues.maor.io/200",
            json={"code" 200, "description": "Description": "OK"},
            status=200,
            content_type = "application/json"
        )
        yield rsps

 def test_404_client_error(mock_responses):
     """
     Prueba la función request_with_error_handling cuando se produce un error 500(server error)
     """
     url = "https://httpstatues.maor.io/404"
     result = request_with_error_handling(url)
     
     # Verificaciones básicas 
     assert isinstance(result, dict) "La función debe devolver un diccionario"

     # Verificación de campos obligatorios
     assert 'success' in result, "El resultado debe contener el campo 'succes'"
     assert 'status_code' in result, "El resultado debe contener 'status code'"
     assert 'is_redirect' in result, "El resultado debe contener el campo 'is redirect'"
     assert 'message' in result, "El resultadodebe contener el campo 'message'"

     # Verificación de valores para el caso específico
     assert result['success'] is True, "Para un 404, 'success' debe ser True"
     assert result['status_code'] == 404, "El código de estado debe ser 404"
     assert result['is-redirect'] is False, "Para un 404, 'is_redirect debe ser False"
     assert 'error_type' in result, "El resultado debe contener el campo 'error_type' para errores"
     assert['error_type'] == 'client_error', "Para un 404, 'error_type' debe ser clien_error'"
 
def test_500_client_error(mock_responses):
     """
     Prueba la función request_with_error_handling cuando se produce un error 500(cliente error)
     """
     url = "https://httpstatues.maor.io/500"
     result = request_with_error_handling(url)
     
     # Verificaciones básicas 
     assert isinstance(result, dict) "La función debe devolver un diccionario"
     
     # Verificación de campos obligatorios
     assert 'success' in result, "El resultado debe contener el campo 'succes'"
     assert 'status_code' in result, "El resultado debe contener 'status code'"
     assert 'is_redirect' in result, "El resultado debe contener el campo 'is redirect'"
     assert 'message' in result, "El resultadodebe contener el campo 'message'"

    # Verificación de valores para el caso específico
     assert result['success'] is False, "Para un 500, 'success' debe ser False"
     assert result['status_code'] == 500, "El código de estado debe ser 500"
     assert result['is-redirect'] is False, "Para un 500, 'is_redirect debe ser False"
     assert 'error_type' in result, "El resultado debe contener el campo 'error_type' para errores"
     assert['error_type'] == 'server_error', "Para un 500, 'error_type' debe ser server_error'"


def test_301_client_error(mock_responses):
     """
     Prueba la función request_with_error_handling cuando se produce una redirección 301.
     """
     url = "https://httpstatues.maor.io/301"
     result = request_with_error_handling(url)
     
     # Verificaciones básicas 
     assert isinstance(result, dict) "La función debe devolver un diccionario"
     
     # Verificación de campos obligatorios
     assert 'success' in result, "El resultado debe contener el campo 'succes'"
     assert 'status_code' in result, "El resultado debe contener 'status code'"
     assert 'is_redirect' in result, "El resultado debe contener el campo 'is redirect'"
     assert 'message' in result, "El resultadodebe contener el campo 'message'"
    
    # Verificación de valores para el caso específico
     assert result['success'] is True, "Para un 301, 'is_redirect' debe ser True"
     assert result['status_code'] == 301, "El código de estado debe ser 301"
     assert result['is-redirect'] is True, "Para un 301, 'is_redirect debe ser True"
     assert 'redirect_url' in result, "El resultado debe contener el campo 'redirect_url' para redirecciones"
     assert['redirect_url'] == "https://httpstatues.maor.io", "La URL de redirección debe ser correcta"
     
def test_200_success(mock_responses):
     """
     Prueba la función request_with_error_handling cuando se produce una redirección 301.
     """
     url = "https://httpstatues.maor.io/200"
     result = request_with_error_handling(url)
     
     # Verificaciones básicas 
     assert isinstance(result, dict) "La función debe devolver un diccionario"
     
     # Verificación de campos obligatorios
     assert 'success' in result, "El resultado debe contener el campo 'succes'"
     assert 'status_code' in result, "El resultado debe contener 'status code'"
     assert 'is_redirect' in result, "El resultado debe contener el campo 'is redirect'"
     assert 'message' in result, "El resultadodebe contener el campo 'message'"
    
     # Verificación de valores para el caso específico
     assert result['success'] is Trie, "Para un 200, 'success' debe ser False"
     assert result['status_code'] == 200, "El código de estado debe ser 200"
     assert result['is-redirect'] is False, "Para un 200, 'is_redirect debe ser False"
     assert'error_type' not in result, "No debe haber campo 'error_type' para respuestas exitosas"        

def test_conection_error():
     """
     Prueba la función request_with_error_handling cuando se produce una respuesta exitosa 200.
     """
     with patch('request.get') as mock_get:
        # Configurar el mock para simular un error de conexión
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection Refused")
     url = "https://httpstatues.maor.io/301"
     result = request_with_error_handling(url)

    # Verificaciones básicas 
     assert isinstance(result, dict) "La función debe devolver un diccionario"
     
     # Verificación de campos obligatorios
     assert 'success' in result, "El resultado debe contener el campo 'succes'"
     assert 'message' in result, "El resultado debe contener el campo 'message'"

     #Verificación de valores para el caso específico
     assert result['success] is False, "Para un error de conexión, 'success'debe ser False"
     assert 'connection_error' in str(result['message']).lower(), "El mensaje debe indicar que hubo un error de conexión"
    
    
    
    
    
    Realiza una petición GET a la URL proporcionada y maneja los diferentes tipos de
    respuestas HTTP que puedan ocurrir.

    Args:
        url (str): La URL a la que se realizará la petición

    Returns:
        dict: Un diccionario con la siguiente información:
            - success (bool): True si la petición fue exitosa (código 2xx), False en otro caso
            - status_code (int): El código de estado HTTP
            - is_redirect (bool): True si la respuesta es una redirección (código 3xx)
            - redirect_url (str, opcional): URL de redirección si is_redirect es True
            - error_type (str, opcional): "client_error" para 4xx, "server_error" para 5xx
            - message (str): Un mensaje descriptivo sobre el resultado de la petición
    """
    # Completa esta función para manejar diferentes tipos de respuestas HTTP
    # Debes gestionar al menos:
    # - Respuestas exitosas (códigos 2xx)
    # - Redirecciones (códigos 3xx)
    # - Errores del cliente (códigos 4xx)
    # - Errores del servidor (códigos 5xx)
    pass


if __name__ == "__main__":
    # Puedes probar tu función con estas URLs:

    # Para probar un error 404 (Not Found)
    print("Probando URL con error 404:")
    result = request_with_error_handling("https://httpstatuses.maor.io/404")
    print(f"Resultado: {result}")

    # Para probar un error 500 (Server Error)
    print("\nProbando URL con error 500:")
    result = request_with_error_handling("https://httpstatuses.maor.io/500")
    print(f"Resultado: {result}")

    # Para probar una redirección 301 (Moved Permanently)
    print("\nProbando URL con redirección 301:")
    result = request_with_error_handling("https://httpstatuses.maor.io/301")
    print(f"Resultado: {result}")

    # Para probar una respuesta exitosa
    print("\nProbando URL con respuesta exitosa:")
    result = request_with_error_handling("https://httpstatuses.maor.io/200")
    print(f"Resultado: {result}")
