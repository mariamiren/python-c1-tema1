"""
Enunciado:
Este ejercicio introduce el uso de bibliotecas especializadas para acceder a APIs de forma
sencilla y estructurada. En concreto, utilizaremos la biblioteca pybikes que proporciona
wrappers para múltiples sistemas de bicicletas compartidas en todo el mundo.

En lugar de construir nuestro propio cliente HTTP y procesar manualmente los datos JSON,
aprenderemos a utilizar herramientas existentes que hacen este trabajo por nosotros.

Tareas:
1. Explorar los sistemas de bicicletas disponibles
2. Obtener información sobre el sistema de Barcelona (Bicing)
3. Analizar los datos de las estaciones

Esta práctica ilustra cómo las bibliotecas especializadas simplifican el acceso a APIs
y permiten concentrarse en el análisis de datos en lugar de en los detalles técnicos
de la comunicación con la API.
"""

import pybikes
import pandas as pd
import time
from typing import List, Dict, Any, Optional
import matplotlib.pyplot as plt
import pytest
from unittest.mock import patch, MagicMock

#Importar el módulo a probar
import sys
import os

from ej1d1 import (
    listar_sistemas_disponible, 
    buscar_sistema_por_ciudad, 
    obtener_info_sistema, 
    obtener_estaciones,
    crear_dataframe_estaciones,
    visualizat_estaciones
)

# Fixture para simular una estación
@pytest.fixture
def mock_stations():
    """Proporciona una lista de esatciones simuladas para pruebas."""
    station = []
    # Crear 5 estaciones simuladas
    for i in range(1, 6):
        station = MagicMock()
        station.name = f"Station {i}"
        station.latitude =  41.3 + (i / 100)
        station.longitude = 2.1 + (i / 100) 
        station.bikes = i * 5  # 5, 10, 15, 20, 25 
        station.free =  30 - (i * 5)  # 25, 20, 15, 10, 5
        station.append(station)
    return stations

def listar_sistemas_disponibles():
    """
    Prueba la función listar sistemas disponibles.
    Debe devolver una lista no vacía de sistemas.
    """
    sistemas = listar_sistemas_disponibles()
    assert isinstance(sistemas, list), La función debe devolver una lista" 
    assert len(sistemas) > 0, "La lista de sistemas no debe estar vacía"
    assert all(isinstance(s, str) for s in sistemas), "La lista de sistemas no debe estar vacía"

def test_buscar_sistema_pot_ciudad():
    """
    Prueba la función listar sistemas por ciudad.
    Debe encontrar al menos un sistema para Barcelona.
    """
    sistemas = buscar_sistemas_por_ciudad("Barcelona")
    assert isinstance(sistemas, list), "La función debe devolver una lista" 
    assert len(sistemas) > 0, "Debería haber al menos un sistema para Barcelona"
    assert "bicing" in sistemas, "El sistema 'bicing' debe estar entre los resulta

def test_obtener_info_sistema():
    """
    Prueba la función listar sistemas por ciudad.
    Debe encontrar al menos un sistema para Barcelona.
    """
    info = obtener_info_sistema("bicing")
    assert isinstance(info, dict) "La función debe devolver una diccionario"
    assert "name" in info, "Los metadatos deben incluir el nombre del sistema"
    assert "city" in info, "Los metadatos deben incluir el ciudad del sistema"
    assert "country" in info, "Los metadatos deben incluir el país del sistema"

@patch('pubykes.get')
def test_obtener_estaciones_error(mock_get):
    """
    Prueba la función obtener_estaciones cuando hay un error.
    """
    # Configurar el mock para lanzar una excpeción
    mock_get.side_effect = Exception("Error de prueba")

    # La función debe manejar el error de devolver None
    estaciones = obtener_estaciones("sistema_inexistente")
    assert estaciones is None, "Debe devolver None cuando hay un error"

def test_crear_dataframe_estaciones(mock_stations)
    """
    Prueba la función crear_dataframe_estaciones.
    """
    df = crear_dataframe_estaciones(mock_stations)
    # Verififcar que es un DataFrame
    assert isinstance(df, pd.DataFrame), "Debe devolver un DataFrame"

    # Verificar que tiene las columnas esperadas
    expected_columns = ['name', 'latitude', 'longitude', 'bikes', 'free']
    for col in expected_columns:
        assert col in df.columns, f"El DataFrame debe tener la columna '{col}'"

    # Verificar el número de filas 
    assert len(df) == 5, "El DataFrame debe tener 5 filas"

    # Verificar el contenido
    assert df.iloc[0]['name'] == "Station 1", "El nombre de la primera estación de debe ser 'Station 1'"
    assert df.iloc[0]['bikes'] == 5, "La primera estación debe tener 5 bicicletas"


@patch('matplotlib.pyplot.show')
@patch('matplotlib.pyplot.savefig')
def test_visualizar_estaciones
    """
    Prueba la función visualizar_estaciones.
    """
    # Crear un DataFrame para la prueba
    df = pd.DataFrame({
        'name': [station.name for station in mock_stations],
        'bikes': [station.bikes for station in mock_stations],
        'free': [station.free for station in mock_stations],
        'latitude': [station.latitude for station in mock_stations],
        'longitude': [station.longitude for station in mock_stations],
    })
    
    # Llamar a la función
    visualizar_estaciones(df)
    # Verificar que se llamó a la función show() para mostrar el gráfico
    # (o alternativamente, que se guardó el gráfico)
    assert mock_show.called or mock_savefig.called, "Debe mostrar o guardar una visualización"

# Pruebas adicionales para verificar comportamiento con valores borde

def test_buscar_sistema_por_ciudad_no_existente():
    """
    Prueba buscar_sistema_por_ciudad con una ciudad que no existe.
    """
    sistemas = buscar_sistema_por_ciudad("CiudadImaginaria123456")
    assert isinstance(sistemas, list), "La función debe devolver una lista"
    assert len(sistemas) == 0, "La lista debe estar vacía para una ciudad inexistente"

def test_obtener_info_existente_no_existente():
    """
    Prueba obtener info_sistema con un sistema que no existe.
    """
    info = obtener_info_sistema("sistema_inexistente_123456")
    assert info is None, "Debe devolver None para un sistema inexistente"

def test_crear_dataframe_estaciones_lista_vacíate:
     """
     Prueba la función crear_dataframe con una lista vacía.
     """
    df = crear_dataframe_estaciones([])
    assert isinstance(df, pd.DataFrame), "Debe devolver un DataFrame vacío"
    assert len(df) == 0, "El DataFrame debe estar vacío"
    


Returns:
        List[str]: Lista de identificadores de sistemas disponibles
    """
    # Implementa aquí la lógica para obtener y devolver la lista
    # de sistemas disponibles en pybikes
    pass


def buscar_sistema_por_ciudad(ciudad: str) -> List[str]:
    """
    Busca sistemas de bicicletas que contengan el nombre de la ciudad especificada.

    Args:
        ciudad (str): Nombre de la ciudad a buscar

    Returns:
        List[str]: Lista de sistemas que coinciden con la búsqueda
    """
    # Implementa aquí la lógica para buscar y devolver sistemas
    # que coincidan con la ciudad especificada
    pass


def obtener_info_sistema(tag: str) -> Dict[str, Any]:
    """
    Obtiene la información del sistema especificado.

    Args:
        tag (str): Identificador del sistema (por ejemplo, 'bicing')

    Returns:
        Dict[str, Any]: Metadatos del sistema o None si no existe
    """
    # Implementa aquí la lógica para obtener y devolver
    # los metadatos del sistema especificado
    pass


def obtener_estaciones(tag: str) -> Optional[List]:
    """
    Obtiene la lista de estaciones del sistema especificado.

    Args:
        tag (str): Identificador del sistema (por ejemplo, 'bicing')

    Returns:
        Optional[List]: Lista de objetos estación o None si hay error
    """
    # Implementa aquí la lógica para obtener y devolver
    # la lista de estaciones del sistema especificado
    pass


def crear_dataframe_estaciones(estaciones: List) -> pd.DataFrame:
    """
    Convierte la lista de estaciones en un DataFrame de pandas.

    Args:
        estaciones (List): Lista de objetos estación

    Returns:
        pd.DataFrame: DataFrame con la información de las estaciones
    """
    # Implementa aquí la lógica para convertir la lista de estaciones
    # en un DataFrame de pandas con al menos las columnas:
    # nombre, latitud, longitud, bicicletas disponibles, espacios libres
    pass


def visualizar_estaciones(df: pd.DataFrame) -> None:
    """
    Genera una visualización simple de la disponibilidad de bicicletas.

    Args:
        df (pd.DataFrame): DataFrame con la información de las estaciones
    """
    # Implementa aquí la lógica para crear un gráfico de barras que muestre
    # las 10 estaciones con más bicicletas disponibles
    pass


if __name__ == "__main__":
    # Listar sistemas disponibles
    print("\nSistemas de bicicletas disponibles:")
    sistemas = listar_sistemas_disponibles()
    print(f"Total: {len(sistemas)} sistemas")
    print(f"Algunos ejemplos: {sistemas[:5]}")

    # Buscar sistemas en Barcelona
    print("\nBuscando sistemas en Barcelona:")
    sistemas_barcelona = buscar_sistema_por_ciudad("Barcelona")
    print(f"Encontrados: {len(sistemas_barcelona)}")
    for sistema in sistemas_barcelona:
        print(f"- {sistema}")

    # Si se encuentra el sistema de Barcelona (Bicing), obtener información
    if "bicing" in sistemas:
        print("\nInformación del sistema Bicing de Barcelona:")
        info = obtener_info_sistema("bicing")
        for key, value in info.items():
            print(f"{key}: {value}")

        # Obtener estaciones
        print("\nObteniendo estaciones...")
        estaciones = obtener_estaciones("bicing")
        if estaciones:
            print(f"Obtenidas {len(estaciones)} estaciones")

            # Convertir a DataFrame
            print("\nConvirtiendo a DataFrame...")
            df = crear_dataframe_estaciones(estaciones)
            print(df.head())

            # Estadísticas básicas
            print("\nEstadísticas de bicicletas disponibles:")
            print(df['bikes'].describe())

            # Visualización
            print("\nVisualizando estaciones con más bicicletas disponibles...")
            visualizar_estaciones(df)
        else:
            print("No se pudieron obtener las estaciones.")
    else:
        print("El sistema 'bicing' no está disponible en pybikes.")

