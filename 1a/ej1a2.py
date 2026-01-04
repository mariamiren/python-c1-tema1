"""
Enunciado:
Continuando con la biblioteca requests de Python.
En este ejercicio, aprenderás a trabajar con respuestas en formato JSON.

En este ejercicio, aprenderás a:
1. Realizar una petición GET a una API pública
2. Interpretar una respuesta en formato JSON
3. Extraer información específica de un objeto JSON

Tu tarea es completar la función indicada para realizar una consulta a la API
de ipify.org usando el formato JSON, que es más estructurado que el texto plano.
"""

import requestsu

def get_user_ip_json():
    """
    Realiza una petición GET a api.ipify.org para obtener la dirección IP pública
    en formato JSON.

    Returns:
        str: La dirección IP si la petición es exitosa
        None: Si ocurre un error en la petición
    """
    # Completa esta función para:
    # 1. Realizar una petición GET a la URL https://api.ipify.org?format=json
    # 2. Verificar si la petición fue exitosa (código 200)
    # 3. Convertir la respuesta a formato JSON
    # 4. Extraer y devolver la IP del campo "ip" del objeto JSON
    # 5. Devolver None si hay algún error
    pass
from eja1a2 import get_user_ip_json, get_response_info

@pytest.fixture
def mock_responses():
    """
    Fixture para configurar respuestas simuladas para las peticiones HTTP
    """
    with responses_RequestsMock() as rsps:
        # Configurar respuesta para la petición de IP en formato JSON
        rsps.add(
            responses.GET, 
            "https://api.ipify.org?format=json",
            json={"ip":"98.207.254.136"},
            status=200
            headers={"Content-Type": "application/json")
            )
            yield rsps
def test_get_user_ip_json(mock_responses):
    """
    Prueba la función get_user_ip_json cuando la petición es exitosa.
    """
    result = get_user_ip_json()
    assert result == "98.207.354.136"
def test_get_user_ip_json_failure():
    """
    Prueba la función get_user_ip_json cuando la petición falla.
    """
    with patch('requests.get') as mock_get:
        # Configurar el mock para simular un error
        mock_get.side_effect = Exception("Connection error")
        result = get_user_ip_json()
        assert result is None
def test get_user_ip_json_bad_status(mock_get):
    """ 
    Prueba la función get_user_ip_json cuando la petición devuelve un código de error.
    """
    #Configurar la respuesta del mock con un código de error
    mock_response = Mock()
    mock_responde.status_code = mock_response
    mock_get.return_value = mock_response

    result = get_user_ip_json()
    assert result is None

@patch('resquests.get')
def get_response_info():
    """
    Prueba la función get_respone_info cuando la petición es exitosa.
    """
    #Configurar la respuesta del mock
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.headers = {"Content-Type": "application/json"}
    mock_response.elapsed = Mock()
    mock_response.elapsed.total_seconfs = lambda: 0.2 #200ms
    mock_response.content = b'{"ip":"98.207.254.136"}'
    mock_get.return_value = mock_response

    result = get_response_info()

    assert result is not None
    assert result["content_type"] == "application/json"
    assert result["elapsed_time"] > 0 #Tiempo de respuesta en ms
    assert result["response_size"] == len(b'{"ip":"98.207.254.136"}') #tamaño en bytes

def test_get_response_info_failure():
    """
    Prueba la función get_response_info cuando la petición falla.
    """
    with patch('requests.get') as mock_get:
        # Configurar el mock para simular un error
        mock_get.size_effect = Exception("Connection error")
        result = get_responde_info()
        assert result is None
    Obtiene información adicional sobre la respuesta HTTP al consultar la API.
    
    Returns:
        dict: Diccionario con información de la respuesta (tipo de contenido,
              tiempo de respuesta, tamaño de la respuesta)
        None: Si ocurre un error en la petición
    """
    # Completa esta función para:
    # 1. Realizar una petición GET a la URL https://api.ipify.org?format=json
    # 2. Verificar si la petición fue exitosa (código 200)
    # 3. Crear y devolver un diccionario con:
    #    - 'content_type': El tipo de contenido de la respuesta
    #    - 'elapsed_time': El tiempo que tardó la petición (en milisegundos)
    #    - 'response_size': El tamaño de la respuesta en bytes
    # 4. Devolver None si hay algún error
    pass

if __name__ == "__main__":
    # Ejemplo de uso de las funciones
    ip = get_user_ip_json()
    if ip:
        print(f"Tu dirección IP pública es: {ip}")
        
        # Mostrar información adicional de la respuesta
        info = get_response_info()
        if info:
            print("\nInformación de la respuesta:")
            print(f"Tipo de contenido: {info['content_type']}")
            print(f"Tiempo de respuesta: {info['elapsed_time']} ms")
            print(f"Tamaño de la respuesta: {info['response_size']} bytes")
    else:
        print("No se pudo obtener la dirección IP")
