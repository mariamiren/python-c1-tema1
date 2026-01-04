"""
Enunciado:
Introducción básica a la biblioteca requests de Python.
La biblioteca requests permite realizar peticiones HTTP de forma sencilla.

En este ejercicio, aprenderás a:
1. Realizar una petición GET a una API pública
2. Interpretar una respuesta en formato texto plano
3. Manejar errores en peticiones HTTP

Tu tarea es completar la función indicada para realizar una consulta básica
a la API de ipify.org, un servicio estable que proporciona la IP pública.
"""

Realiza una petición GET a api.ipify.org para obtener la dirección IP pública
en formato texto plano.

    Returns:
        str: La dirección IP si la petición es exitosa
        None: Si ocurre un error en la petición
    """
# Completa esta función para:

# 1. Realizar una petición GET a la URL https://api.ipify.org (sin parámetros)
@pytest.fixture
def mock_responses():
"""
Fixture para configurar respuestas simuladas para las peticiones HTTP
"""
with responses.RequestsMock() as rsps:
#configurar respuesta para la petición de IP en formato texto plano
    rsps.add(
        responses.GET, 
        "http://apli.ipify.org", 
        body="98.207.254.136",
        status=200
    )
    yield rsps
    
# 2. Verificar si la petición fue exitosa (código 200)
def get_user_ip(mock_responses):
"""
Prueba la función get_user_ip cuando la petición es exitosa.
"""
result = get_user_ip()
assert result == "98.207.254.136"
        
# 3. Devolver el texto de la respuesta directamente (contiene la IP)
def test_get_user_ip_failure():
"""
Prueba la función get_user_ip cuando la petición falla.
"""
    with patch('request.get') as mock_get:
#Configurar el mock para simular un error
    mock_get.side_effect = Exception("Connection error")
result = get_user_ip()
assert result is None
    
    # 4. Devolver None si hay algún error
    @patch('requests.get')
    def test_get_ip_bad_status(mock_get):
    """
    Prueba la función get_user_ip cuando la petición devuelve un código error
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

    result = get_user_ip()
    assert result is None

if __name__ == "__main__":
    # Ejemplo de uso de la función
    ip = get_user_ip()
    if ip:
        print(f"Tu dirección IP pública es: {ip}")
    else:
        print("No se pudo obtener la dirección IP")
