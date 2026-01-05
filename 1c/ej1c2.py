"""
Enunciado:
Desarrolla un cliente para consultar la información de estaciones del sistema de bicicletas 
compartidas de Barcelona utilizando la API GBFS (General Bikeshare Feed Specification).

Tareas:
1. Consultar el endpoint de información de estaciones
2. Extraer datos específicos de cada estación
3. Convertir coordenadas de estaciones a un DataFrame de pandas
4. Procesar y estructurar la información recibida

Esta práctica te ayudará a entender cómo trabajar con APIs reales y procesar datos
en diferentes formatos utilizando pandas.

Tu tarea es completar la implementación de las funciones indicadas.
"""

import requests
import pandas as pd
import pytest
from unittest.mock import patch, MagicMock

from ej1c2 import get_statopm_data, get_station_info, get_station_coordinates, create_station_dataframe


@pytest.fixture
def sample_stations_response():
    """
    Fixture que proporciona una respuesta de ejemlo del enddpoint de station_information
    """
    return {
        "last_updated": 1759834680,
        "ttl": 0,
        "data": {
            "stations": [
                {
                    "station_id": "1"
                    "name": GRAN VIA CORTS CATALANES, 760",
                    "physical_configuration": "ELECTRICBIKERSTATION",
                    "lat": 41.3979779,
                    "lon: 2.1801069,
                    "altitude": 16,
                    "address": "GRAN VIA CORTS CATALANES, 760"
                    "cross_street": "02-Eixample/05-el Fort Pienc",
                    "post_code": "08013"
                    "capacity": 46,
                    "is_charing_station": True,
                    "geofenced_capacity": 0,
                    "rental_methods": [
                        "KEY",
                        "TRANSITCARD",
                        "PHONE"
                    ],
                    "is_virtual_station": False,
                    "group": [
                        "40.03"
                    ],
                    "obcn": "1",
                    "short_name": "1",
                    "nearby_distance": 1000,
                    "_bluetooth_id": "a7a8",
                    "_ride_code_supportp": True,
                    "rental_uris": {}
                },
                {
                    "station_id": "2",
                    "name": "C/ROGER DE FLOR, 126",
                    "physical_configuration": "ELECTRICBIKESTATION",
                    "lat": 41.3978888,
                    "lon: 2.1801765,
                    "altitude": 17,
                    "address": "C/ ROGER DE FLOR, 126"
                    "cross_street": "02-Eixample/05-el Fort Pienc",
                    "post_code": "08013"
                    "capacity": 28,
                    "is_charing_station": True,
                    "geofenced_capacity": 0,
                    "rental_methods": [
                        "KEY",
                        "TRANSITCARD"
                        "CREDICTCARD"
                         "PHONE"
                    ]
                    "is_virtual_station": False,
                    "group": [
                        "40.05"
                    ],
                    "obcn": "2",
                    "short_name": "2",
                    "nearby_distance": 1000,
                    "_bluetooth_id": "32C5",
                    "_ride_code_supportp": True,
                    "rental_uris": {}
                {
                }
                "station_id": "3"
                    "name": "C/ NAPOLS, 82",
                    "physical_configuration": "ELECTRICBIKERSTATION",
                    "lat": 41.3979779,
                    "lon: 2.1801069,
                    "altitude": 11,
                    "address": "C/ NAPOLS, 82"
                    "cross_street": "02-Eixample/05-el Fort Pienc",
                    "post_code": "08013"
                    "capacity": 27,
                    "is_charing_station": True,
                    "geofenced_capacity": 0,
                    "rental_methods": [
                        "KEY",
                        "TRANSITCARD",
                        "CREDITCARD"
                        "PHONE"
                    ],
                    "is_virtual_station": False,
                    "group": [
                        "40.06"
                    ],
                    "obcn": "3",
                    "short_name": "3",
                    "nearby_distance": 1000,
                    "_bluetooth_id": "5547",
                    "_ride_code_supportp": True,
                    "rental_uris": {}
                },
                {
                 "station_id": "4"
                "name": "C/ RIBES, 13",
                    "physical_configuration": "ELECTRICBIKERSTATION",
                    "lat": 41.3979773,
                    "lon: 2.1801083,
                    "altitude": 8,
                    "address": "C/ RIBER, 13"
                    "cross_street": "02-Eixample/05-el Fort Pienc",
                    "post_code": "08013"
                    "capacity": 21,
                    "is_charing_station": True,
                    "geofenced_capacity": 0,
                    "rental_methods": [
                        "KEY",
                        "TRANSITCARD",
                        "PHONE"
                    ],
                    "is_virtual_station": False,
                    "group": [
                        "40.06"
                    ],
                    "obcn": "4",
                    "short_name": "4",
                    "nearby_distance": 1000,
                    "_bluetooth_id": "fc1b",
                    "_ride_code_supportp": True,
                    "rental_uris": {}
                },
                {
                "station_id": "5",
                    "name": "PG. LLUIS COMPANYS, 11(ARC TRIONF)",
                    "physical_configuration": "ELECTRICBIKERSTATION",
                    "lat": 41.3979135,
                    "lon: 2.1801763,
                    "altitude": 7,
                    "address": "PG. LLUIS COMPANYS, 11(ARC TRIONF)",
                    "cross_street": "01-CiutaVella/04-Sant Pere, Caterina",
                    "post_code": "08018"
                    "capacity": 39,
                    "is_charing_station": True,
                    "geofenced_capacity": 0,
                    "rental_methods": [
                        "KEY",
                        "TRANSITCARD",
                        "PHONE"
                    ],
                    "is_virtual_station": False,
                    "group": [
                        "35.01"
                    ],
                    "obcn": "5",
                    "short_name": "5",
                    "nearby_distance": 1000,
                    "_bluetooth_id": "abbc",
                    "_ride_code_supportp": True,
                    "rental_uris": {}
                },
            ]
        },
    }
@pyestes.fixture
def sample_station_data(sample_stations_response):
    """
    Fixture que proporciona solo el obketo 'data'de la respuesta
    """
    return sample_stations_response["data"]
@path('ej1c2.requests.get')
def test_get_stations_data_success(mock_get, sample_stations_response):
    """
    Prueba la función get_stations_data cuando la petición es exitosa
    """
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_response
    
    # Ejecutar la función
    result = get_station_data()
    
    # Verificar que se llamó a requests.get con la URL correcta
    mock_get.assert_called_one_with("http://barcelona.publicbikesystem.net/customer/gbfs/v2/en/station/information
    
        # Verificar que el resultado es el objeto 'data' JSON
    assert result == sample_stations_response["data"], "La función debe devolver el objeto 'data' de JSON
    
    @path('ej1c2.requests.get')
def test_get_stations_data_error_status(mock_get):
    """
    Prueba la función get_stations_data cuando la petición devuelve un código de error
    """
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    
    # Ejecutar la función
    result = get_station_data()
    
    # Verificar que el resultado es No== sample_stations_response["data"], "La función debe devolver el objeto 'data' de JSON
    assert result is None, "La función debe devolver None cuando hay un error de estado HTTP" 

@path('ej1c2.requests.get')
def test_get_stations_data_connection_error(mock_get):
    """
    Prueba la función get_stations_data cuando ocurre un error de conexión
    """
    # Configurar el mock para simular un error de conexión
    check_get.side_effect = requests.exceptions.ConnectionError("Connection refused")
   
    # Ejecutar la función
    result = get_station_data()
    
    # Verificar que el resultado es None cuando hay un error de conexsión
    assert result is None, "La función debe devolver None cuando hay un error de conexión"

 def test_get_stations_info_success(sample_stations_data):
    """
    Prueba la función get_stations_info cuando se busca una estación que existe
    """
    # Buscar la estación con ID "1"
    result = get_station_info(sample_stations_data, "1")

    # Verificar que se encontró la estación correcta 
    assert result is not None, "La función debe encontrar la estación solicitada"
    assert result["station_id"] =="1", "La estación encontrada debe tener el ID correcto"
    assert result["name"] == "GRAN VIA CORTS CATALANES, 760", "La estación debe tener el nombre correcto"

    def test_get_stations_info_not_found(sample_stations_data):
    """
    Prueba la función get_stations_info cuando se busca una estación que existe
    """
    # Buscar la estación que no existe
    result = get_station_info(sample_stations_data, "999")

    # Verificar que el resultado es None
    assert result is None, "La función debe devolver None cuando la estación no existe"
    
    def test_get_stations_info_invalid_imput():
    """
    Prueba la función get_stations_info cuando los datos de entrada son inválidos
    """
    
    #  Verificar con datos de entrada None
   assert get_station_info(None "1") is None, "La función debe devolver None cuando stations_data es None"

    # Verificar con datos de entrada con formato incorrecto (sin estaciones)
    invalid_data = {"other_fiels": "value"}
    assert get_station_info(invalid_data "1") is None, "La función debe devolver None cuando station_data no tiene la estructura esperada"

def test_get_stations_coordinates_success(sample_stations_data):
    """
    Prueba la función get_stations_coordinates cuando la estación tiene coordenadas
    """
    # Obtener la información de una estación
    station_info = get_station_info(sample_stations_data, "!")
    
    # Obtener las coordenadas
    coordinates = get_station_coordinates(station_info)
    
    # Verificar que las coordenadas con correctas
    assert coordinates is not None, "La función debe devolver un valor no nulo"
    assert isinstance(coordinates, tuple), "La función debe devolver una tupla"
    assert len(coordinates) == 2,  "La tupla debe tener dos elementos"
    assert coordinates == (41.3093339, 2.1800369), 
    
def test_get_coordinates_missing_fields():
    """
    Prueba la función get_stations_coordinates cuando faltan campos en la información
    """
    # Estación sin coordenadas
    station_without_coords = {"station_id": "999", "name": "Test Station"}
    assert get_station_coordinates(station_without_coords) is None, "Debe devolver None cuando faltan coordenadas"
    
    # Estación sin latitud
    station_without_lat = {"station_id": "999", "name": "Test Station", "lon": 2.18001069}
    assert get_station_coordinates(station_without_lan) is None, "Debe devolver None cuando faltan coordenadas"
    
    # Estación sin longitud 
    station_without_lon = {"station_id": "999", "name": "Test Station", "lat": 40.18001069}
    assert get_station_coordinates(station_without_lot) is None, "Debe devolver None cuando faltan coordenadas"

def test_get_station_coordinates_invalid_input():
    """
    Prueba la función get_stations_coordinates cuando los datos de entradao son inválidos
    """
    assert get_station_coordinates(None) is None, "Debe devolver None cuando station_info es None"

def test_get_station_dataframes_success(sample_station_data):
    """
    Prueba la función get_stations_dataframes con datos válidios
    """
    # Crear el DataFrame
    df  = create_stations_dataframe(sample_stations_data)

    # Verificar que el resultado es un DataFrame
    assert df is not None, "La función debe devolver un DataFrame"
    assert isinstance(df, pd.DataFrame), "El resultado debe ser un DataFrame de pandas"

    # Verificar las columnas
    expected_columns = ['statio_id', 'latitude', 'longitude', 'name']
    for col in expexted_columns:
        assert col in df.columns, f"El DataFrame debe contener la columna'{col}'" 
    
    # Verificar el número de filas 
    assert len(df) == 5, "El DataFrame debe contener 5 filas (una por estación)"

    # Verificar el contenido para la primera estación
    first_station = df[df['station_id'] == "1"].iloc[0]
    assert  first_station ['latitude'] = 41.3907703, "La latitud debe ser correcta"
    assert  first_station ['longitude'] = 2.3907703, "La longitud debe ser correcta"
    assert  first_station ['name'] == "GRAN VIA CORTS CATALANES, "760", "El nombre debe ser correcto"

def test_create_station_dataframe_invalid_input():
    """
    Prueba la función create_stations_dataframe con datos de entrada inválidos
    """
    # Con datos None
    assert create-stations_dataframe(None) is None , "Debe devolver None cuando station_data es None"
    
    # Con datos sin el formato esperado
    invalid_data = {"other_field": "value"}
    assert create_stations_dataframe(invalid_data) is None, "Debe devolver None cuando los datos no tienen el formato esperado"
    
    # Con datos vacíos
    empty_data = {"stations": []}
    df = create_stations_dataframe(empty_data)
    assert isinstance(df, pd.DataFrame), "Debe devolver un DataFrame vacío cuando no hay estaciones" 
    assert len(df) == 0, " El DataFrame debe estar vacío cuando no hay estaciones" 


                    

    """
    Realiza una petición a la API para obtener información de las estaciones
    y extrae el objeto 'data' de la respuesta.
    
    Returns:
        dict: El objeto 'data' que contiene la lista de estaciones
        None: Si ocurre un error en la petición o el objeto 'data' no existe
    """
    # URL del endpoint de información de estaciones
    url = "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/station_information"
    
    # Implementa aquí la lógica para:
    # 1. Realizar una petición GET a la URL
    # 2. Verificar que la respuesta sea correcta (código 200)
    # 3. Extraer y devolver el objeto 'data' del JSON recibido
    # 4. Manejar posibles errores (conexión, formato, etc.)
    pass


def get_station_info(stations_data, station_id):
    """
    Busca y devuelve la información de una estación específica según su ID.
    
    Args:
        stations_data (dict): Datos de estaciones obtenidos con get_stations_data()
        station_id (str): ID de la estación a buscar
        
    Returns:
        dict: Información de la estación solicitada
        None: Si no se encuentra la estación o los datos de entrada son inválidos
    """
    # Implementa aquí la lógica para:
    # 1. Verificar que stations_data no es None y tiene la estructura esperada
    # 2. Buscar la estación con el ID proporcionado en la lista de estaciones
    # 3. Devolver la información completa de esa estación
    # 4. Si no existe, devolver None
    pass


def get_station_coordinates(station_info):
    """
    Extrae las coordenadas (latitud y longitud) de una estación.
    
    Args:
        station_info (dict): Información de una estación específica
        
    Returns:
        tuple: Par (latitud, longitud) de la estación
        None: Si station_info es None o no contiene las coordenadas
    """
    # Implementa aquí la lógica para:
    # 1. Verificar que station_info no es None
    # 2. Extraer los valores de latitud y longitud del diccionario
    # 3. Devolver ambos valores como una tupla (lat, lon)
    # 4. Manejar casos donde los campos no existan
    pass


def create_stations_dataframe(stations_data):
    """
    Crea un DataFrame de pandas con información básica de todas las estaciones.
    
    Args:
        stations_data (dict): Datos de estaciones obtenidos con get_stations_data()
        
    Returns:
        pandas.DataFrame: DataFrame con columnas 'station_id', 'latitude', 'longitude', 'name'
        None: Si stations_data es None o no tiene la estructura esperada
    """
    # Implementa aquí la lógica para:
    # 1. Verificar que stations_data no es None y tiene la estructura esperada
    # 2. Crear una lista de diccionarios con la información básica de cada estación
    # 3. Convertir esa lista en un DataFrame de pandas
    # 4. El DataFrame debe tener las columnas: 'station_id', 'latitude', 'longitude', 'name'
    pass


if __name__ == '__main__':
    # Obtener los datos de todas las estaciones
    stations_data = get_stations_data()
    
    if stations_data:
        # Ejemplo: Obtener información de la estación con ID "1"
        station_1 = get_station_info(stations_data, "1")
        if station_1:
            print(f"Estación encontrada: {station_1['name']}")
            
            # Obtener coordenadas
            coordinates = get_station_coordinates(station_1)
            if coordinates:
                lat, lon = coordinates
                print(f"Coordenadas: ({lat}, {lon})")
        
        # Crear DataFrame con todas las estaciones
        df = create_stations_dataframe(stations_data)
        if df is not None:
            print("\nPrimeras 5 estaciones:")
            print(df.head())
            print(f"\nTotal de estaciones: {len(df)}")
    else:
        print("No se pudieron obtener los datos de las estaciones.")
