"""
Enunciado:
Desarrolla un cliente HTTP básico utilizando la biblioteca requests de Python.
El cliente debe realizar peticiones a la API pública del sistema de bicicletas compartidas de Barcelona
que sigue el estándar General Bikeshare Feed Specification (GBFS).

Tareas:
1. Realizar una petición GET a la API de GBFS para obtener la lista de feeds disponibles
2. Procesar la respuesta JSON para extraer información relevante sobre los endpoints
3. Manejar posibles errores en las peticiones

Esta es una introducción a las peticiones HTTP en Python utilizando la biblioteca requests
para entender cómo interactuar con APIs web.

Tu tarea es completar la implementación de las funciones indicadas.
"""

import requests
import pytest
import json
import io
import sys
from unittest.mock import patch, MagicMock

from ej1c1 import get_gbfs_feeds, extract_feed_info, print_feeds_summary

@pytest.fixture
def sample_gbfs_response():
    """
    Fixture para proporcionar una respuesta de ejemplo de la API GBFS
    """
    return {
        ""last_updated": 1759834448,
        "ttl": 0, 
        "data": {
            "en": {
                "feeds": [
                    {"name: "geofencing_zones", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/geofencing_zones"}
                    {"name: "gbfs_versions", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/gbfs_versions"}
                    {"name: "station_information", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/station_information"}
                    {"name: "station_status", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/station_status"}
                    {"name: "system_regions", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/system_regions"}
                    {"name: "system_information", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/system_information"}
                    {"name: "system_pricing_plans", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/system_pricing_plans"}
                ]
            }
        },
        "Versión": "2.3"
    }
patch('ej1c1.requests.get')
def test_get_dbfs_feeds_success(mock_get, sample_gbfs_response):
    """
    Prueba la función get_gbfs_feeds cuando la petición es exitosa
    """
    #Configurar el mock para retornar una respuesta exitosa
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = sample_gbfs_response
    mock_get.return_value = mock_response

    # Ejecutar la función
    result = get_gbfs_feeds()

    # Verificar que se llamó a requests.get con la URL correcta
    mock_get.assert_called_once_with("https://barcelona-sp.publicbikesystem.net/customer/gbfs/v2/gbfs.json")

    # Verificar que el resultado es el esperado
    assert result == sample_gbfs_response, "La función debe devolver los datos de JSON de la respuesta"
    
    patch('ej1c1.requests.get')
def test_get_dbfs_feeds_error_status(mock_get):
    """
    Prueba la función get_gbfs_feeds cuando la petición devuelve un código error
    """
    #Configurar el mock para retornar un código error
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    # Ejecutar la función
    result = get_gbfs_feeds()

   # Verificar que el resultado es el esperado
    assert result is None, "La función debe devolver None cuando hay un error de estado HTTP"

patch('ej1c1.requests.get')
def test_get_dbfs_feeds_connection_error(mock_get):
    """
    Prueba la función get_gbfs_feeds cuando ocurre un error de conexión
    """
    #Configurar el mock para simular un error de conexión
    mock_get.size_effect = requests.exceptions.ConnectioneError("Connection refused")
    
    # Ejecutar la función
    result = get_gbfs_feeds()

    # Verificar que el resultado es el esperado
    assert result is None, "La función debe devolver None cuando hay un error de estado HTTP"
    
def test_extract_feeds_info_success(sample_gbfs_response).
    """
    Prueba la función extract_feeds_info cuando se proporciona una respuesta válida
    """
    # Ejecutar la función
    result = get_gbfs_feeds()

    # Verificar que el resultado es una lista
    assert isinstance(result, list), "La función debe extraer todos los feeds disponibles"

    # Verificar la estructura de los elementos
    for feed in result:
        asser "name" in feed, "Cada feed debe contener el campo 'name'"
        assert "url" in feed, "Cada feed debe contener el campo 'url'"

    # Verificar el contenifo del primer feed
    assert result[0]["name"] == "geofencing_zones", "El nombre del primer feed debe ser correcto"
    assert result[0]["url"] == "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/geofencing_zones"
    
def test_extract_feeds_info_none_imput():
    """
    Prueba la función extract_feeds_info cuando nos proporciona None como entrada
    """
    # Ejecutar la función con None como entrada
    result = extract_feeds_info(None)

    # Verificar que el resultado es None
    assert result is None, "La función debe devolver None cuando la entrada es None"
 
 def test_extract_feeds_info_invalid_format():
    """
    Prueba la función extract_feeds_info cuando el formato de los datos es inválidos
    """
    # Datos con formato inválido(sin campo 'data')
    invalid_data = {"last_updated": 1759834448, "ttl": 0, "version": "2.3"}
    #Ejecutar la función
    result = extract_feeds_info(invalid_data)
    # Verificar que el resultado es None
    assert result is None, "La función debe devolcer None cuando el formato de datos es inválido"

def test_print_feeds_summary_(sample_gbfs_response, capsys):
    ""
    Prueba la función print_feeds_summary cuando se proporciona feed válidos
    """
    # Extraer los feeds de ejemplo
    feeds_info = extract_feeds_info(sample_gbfs_response)
    #Ejecutar la función
    print_feeds_summary(feeds_info)
    # Capturar la salida estándar
    captured = capsys.readoutter()
    # Verificar que la salida contiene la información esperada
    assert "Barcelona Bike-Sharing System" in captured.out, " La salida debe contener el título del sistema"
    assert f"Available Feeds: {len(feeds_info)}" in captured.out,"La salida debe indicar el número de feeds disponibles"
    assert "geofencing_zones" in captured, "La salida debe contener el nombre del primer feed"
    assert "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/geofencing_zones"
    
def test_print_feeds_summary_none(capsys):
    """
    Prueba la función print_feeds_summary cuando nos proporciona None como entrada
    """
    # Ejecutar la función con None
    print_feeds_summary(None)
    #Capturar la salida estándar
    captured = capsys.readoutter()
    #Verificar que la salida contiene un mensaje error
    assert "Error" in captured.out, "La salida debe contener un mensaje de error"
    
    
    Realiaza una petición GET a la API de GBFS de Barcelona para obtener
    la lista de feeds (endpoints) disponibles.

    Returns:
        dict: Datos de la respuesta si se obtiene correctamente
        None: Si ocurre un error en la petición
    """
    # La URL base de la API de GBFS de Barcelona
    base_url = "https://barcelona-sp.publicbikesystem.net/customer/gbfs/v2/gbfs.json"

    # Debes completar la función:
    # 1. Realizar una petición GET a la URL
    # 2. Verificar que la respuesta sea correcta (código 200)
    # 3. Devolver los datos en formato JSON
    # 4. Manejar posibles errores (conexión, formato, etc.)
    pass


def extract_feeds_info(feeds_data):
    """
    Extrae la información de los feeds disponibles a partir de los datos recibidos.

    Args:
        feeds_data (dict): Datos de los feeds obtenidos de la API

    Returns:
        list: Lista de diccionarios con los campos 'name' y 'url' de cada feed
        None: Si los datos de entrada son None o no tienen el formato esperado
    """
    # Debes completar la función:
    # 1. Verificar que feeds_data no es None
    # 2. Extraer la lista de feeds para el idioma inglés (en)
    # 3. Crear y devolver una lista con la información relevante de cada feed
    # 4. Manejar posibles errores en la estructura de los datos
    pass

def print_feeds_summary(feeds_info):
    """
    Imprime un resumen formateado de los feeds disponibles.

    Args:
        feeds_info (list): Lista de feeds con los campos 'name' y 'url'
    """
    if feeds_info is None:
        print("Error: No feeds information available")
        return

    # Imprimir título y cantidad de feeds
    print("=" * 50)
    print("Barcelona Bike-Sharing System - GBFS Feeds")
    print("=" * 50)
    print(f"Available Feeds: {len(feeds_info)}")
    print("-" * 50)

    # Imprimir información de cada feed
    for feed in feeds_info:
        print(f"Name: {feed['name']}")
        print(f"URL: {feed['url']}")
        print("-" * 50)


if __name__ == '__main__':
    # Obtener los datos de los feeds disponibles
    feeds_data = get_gbfs_feeds()

    # Extraer la información relevante
    feeds_info = extract_feeds_info(feeds_data)

    # Imprimir el resumen
    print_feeds_summary(feeds_info)
