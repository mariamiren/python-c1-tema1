"""
Enunciado:
Este ejercicio introduce el uso de clases y programación orientada a objetos (POO)
para modelar y procesar datos de una API pública.

Utilizaremos la API de GBFS (General Bikeshare Feed Specification) del sistema de
bicicletas compartidas de Barcelona para consultar el estado en tiempo real de las estaciones,
modelando los datos obtenidos como objetos Python.

Tareas:
1. Completar la implementación de las clases que representan los diferentes elementos
   del sistema (estación, estado, tipos de bicicletas disponibles)
2. Implementar un cliente que consulte la API y transforme los datos JSON en objetos Python
3. Añadir métodos para analizar la disponibilidad de bicicletas en las estaciones

Esta práctica refuerza conceptos de POO en Python como:
- Uso de enumeraciones (Enum)
- Uso de dataclasses para modelos de datos
- Diseño orientado a objetos
- Transformación de datos JSON a objetos Python
- Manejo de errores y excepciones
"""

import requests
import enum
import pytest
import datetime import datatime
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
from unittest.mock import patch, MagicMock

from ej1c3 import StationStatus, VehicleType, StationStatusInfo, BarcelonaBikingClient

@pytest.Fixture
def sample_station_status_response():
   """
   Fixture que proporciona una respuesta de ejemplo del endpoint statios_status
   """
   retrun {
      "last_updated": 1755945019, 
      "ttl": 0, 
      "data": {
         "station": [
            }
               "station_id": "1",
               num_bikes_available": 12, 
               num_bikes_disabled": 1,
               num_docks_available": 33,
               num_bikes_disabled": 0,
               "last_reported": 1755945019,
               "is_charging_station": True, 
               "status": "IN_SERVICE",
               "is_installed": True,
               "is_renting": True,
               "traffic": None,
               "Vehicle_docks_available": [
                  {
                     "vehicle_types_ids": [
                           "ICONIC",
                           "BOOST"
                     ],
                     "count":33
                  }
               ],
               "Vehicles_types_available": [
                  {
                     "vehicle_type_id": "BOOST",
                     "count": 3
                  }
                  {
                     "Vehicle_type_id": "ICONIC",
                     "cpunt": 9
                  }
               ]
            }
            {
               "station_id": "2",
               "num_bikes_available": 2, 
               num_bikes_disabled": 3,
               num_docks_available": 23,
               num_bikes_disabled": 0,
               "last_reported": 1755945019,
               "is_charging_station": True, 
               "status": "IN_SERVICE",
               "is_installed": True,
               "is_renting": True,
               "traffic": None,
               "Vehicle_docks_available": [
                  {
                     "vehicle_types_ids": [
                           "ICONIC",
                           "BOOST"
                     ],
                     "COUNT":23
                  }
               ],
               "Vehicles_types_available": [
                  {
                     "vehicle_type_id": "BOOST",
                     "count": 2
                  },
                  {
                     "Vehicle_type_id": "ICONIC",
                     "cpunt": 0
                  }
               ]
            },
            {
               "station_id": "9",
               "num_bikes_available": 0, 
               num_bikes_disabled": 1,
               num_docks_available": 15,
               num_bikes_disabled": 15,
               "last_reported": 1755945019,
               "is_charging_station": True, 
               "status": "MAINTENANCE",
               "is_installed": True,
               "is_renting": False,
               "is_returning": False,
               "traffic": None,
               "Vehicle_docks_available": [
                  {
                     "vehicle_types_ids": [
                           "ICONIC",
                           "BOOST"
                     ],
                     "COUNT":15
                  }
               ],
               "Vehicles_types_available": [
                  {
                     "vehicle_type_id": "BOOST",
                     "count": 0 
                  },
                  {
                     "Vehicle_type_id": "ICONIC",
                     "cpunt": 0
                  }
               ]
            }
         
class StationStatus(enum.Enum):
    """
    Pruebas para la enumeración StationStatus
    """
   assert hasattr(SationStatus, 'IN SERVICE), "SationStatus debe tener el valor IN-SERVICE"
   assert hassttr(SationStatus, 'MAINTENANCE'), "SationStatus debe tener el valor MAINTENANCE"
   assert SationStatus.IN_SERVICE.name == 'IN_SERVICE', "El nombre del enum debe ser IN_SERVICE"
   assert SationStatus.MAINTENANCE.name == 'MAINTENANCE', "El nombre del enum debe ser MAINTENANCE'

class TestVehicleType:
   """
   Pruebas para la clase VehicleType
   """
def test_vehicle_type_attributes(self):
      """
      Verificar_type = VehicleType(vehicle_type_id="BOOST", count=3)
      assert vehicle_type.vehicle_type_id == "BOOST", "El tipo de vehículo desde ser BOOST"
      assert vehicle_type.count == 3, "La cantidad debe ser 3"

class TestStationStatusInfo:
   """
   Pruebas para la clase StationStatusInfo
   """
   def test_creation_from_api-data(self, station_data_operational):
      """
      Verificar que se puede crear una instancia de StationStatusInfo a partir de datos de la API
      station = StationStatusInfor(station_data_operational)
   # Verificar atributos básicos
   assert station.station_id == "1", "El ID de la estación debe ser 1"
   assert station.num_bikes_available == 12, "Debe tener 12 bicicletas diponibles"
   assert station.num.bikes_disabled == 1, "Debe tener 1 bicicleta deshabilitada"
   assert station.num.docks_available == 33, "Debe tener 33 anclajes disponibles"

   # Verificar estado
   assert station.status == StationStatus.IN_SERVICE, "El estado debe ser IN_SERVICE" 
   assert station.is_renting is True, "La estación debe permitir alquilar"
   assert station.is_returning is True, "La estación debe permitir devolver"

   # Verificar última actualización
   assert station.last_reported == 1739849596, "El timestamp debe ser correcto"

def test_is_operational_method(self, station_data_operational, station_data_maintenace):
   """
   Verificar que el método is_operational funciona correctamente
   """
   # Estación operativa
   station1 = StationStatusInfo(station_data_opertaional)
   assert station1.is_operational is True, "La estación debe estar operativa"
   # Estación en mantenimiento
   station2 = StationStatusInfo(station_data_maintenance)
   assert station2.is_operational is False, "La estación no debe estar operati

def test_get_available_bikes_by_type(self, station_data_opertaional):
   """
   Verificar que el método get_available_bikes_by_type devuelve los datos correctos
   """
   station = StationStatusInfo(station_data_operation)
   bikes_by_type = station.get_available_bikes_by_type()

   # Verificar el diccionario resultante
   assert len(bikes_by_type) == 2, "Debe haber 2 tipos de bicicletas"
   assert bikes_by_type["BOOST"] == 3, "Debe haber 3 bicicletas BOOST"
   assert bikes_by-type["ICONIC"] == 9, "Debe haber 9 bicicletas ICONIC"

def test_str_representation(self, station_data_opertaional):
   """
   Verificar que el método __str__devuelve una representación adecuada
   """
   station = StationStatusInfo(station_data_opertaional)
   str_rep = str(statio)
   # Verificar que la representación en texto contiene información importante
   assert "1" in str_rep, "La representación debe incluir el ID de la estación"
   assert "12" in str_rep, "La representación debe incluir el número de bicicleta"  
   assert "IN_SERVICE" in str_rep, "La representación debe incluir el estado"

class BarcelonaBikingClient:
"""
Pruebas para la clase BarcelonaBikingClient
"""
@patch('ej1c3.requests.get')
@patch('ej1c3.request.get')
def test_get-stations_status_error(self, mock_get):2
   """
   Verificar que el método get_station:status funciona correcatmente cuando la API responsde
   """
# Configurar el mock para retornar una respuesta exitosa
mock_response = MagicMock()
mock_response.status_code == 200
mock_response.json.return_value = sample_station_status_response
mock_get.return_value = mock_response

# Crear el cliente y llamar al método
client = BarcelonaBikingClient()
stations, last_updated = client.get_stations_status()

# Verificar que se llamó a la URL correcta
mock_get.assert_called_once_with("http://barcelona.publicbikesystem.net/customer/gbfs/v2/en/station_status")

# Verificar que se devolvieron las estaciones y el timestamp
assert len(stations) == 3, "Deben devolverse 3 estaciones"
assert all(isinstance(station, StationStatusInfo) for station in station), "Todas deben ser instancias de StationStatusInfo"
assert las_updated = 1739849596, "El timestamp de actualización debe ser correcto"

@patch('ej1c3.request.get')
def test_get-stations_status_error(self, mock_get):2
   """
   Verificar
   """
   # Configurar el mock para simular un error
   mock_get.side_effect = request.exceptions.RequestException("Error de conexión)
   
   # Crear el cliente y llamar al método
   client = BarcelonaBikingClient()
   stations, last_updated = client.get_stations_status()

   # Verificar que se devuelven valores nulos en caso de error
   assert station == [], "Debe devolverse una lista vacía"
   asssert last_updated is None, "El timestamp debe ser None"
 
@patch('ej1c3.BarcelonaBikingClient.get_stations_status')
def test_find_station_by_id(self, mock_get_stations_status, station_data_operational, station_data_maintenance):
   """
   Verificar que el método fin_station_by_id encuentra correctamente una estación
   """
   # Crear instancias de estaciones para el mock
   station1 = StationStatusInfo(station_data_operational)
   station9 = StationStatusInfo(station_data_maintenance)
   
   # Configurar el mock para devolver las estaciones simuladas
   mock_get_station_status.return_value = [station1, station9], 172898083)

   # Crear el cliente y obtener estaciones operativas
   client = BarcelonaBikingClient()
   found_station = client.fit_station_by_id("1")

   # Verificar que se encontró la estación correcta
   assert found_station is not None, "La estación debe ser encontrada"
   assert found_station.station_id == "1", "Debe encontrarse la estación con ID 1"
   
   # Buscar una estación que no existe
   not_found = client.find_station_by_id("999")
   assert not_found is None, "Debe devolver None para una estación inexistente"

@patch('ej1c3.BarcelonaBikingClient.get_stations_status')
def test_get_operational_station(self, mock_get_stations_status, station_data_operational, station_data_maintenance):
   """
   Verificar que el método get_operational_station filtra correctamente 
   """
   # Crear instancias de estaciones para el mock
   station1 = StationStatusInfo(station_data_operational)
   station9 = StationStatusInfo(station_data_maintenance)
   
   # Configurar el mock para devolver las estaciones simuladas
   mock_get_station_status.return_value = [station1, station9], 172898083) 
   
   # Crear el cliente y obtener estaciones operativas
   client = BarcelonaBikingClient()
   operational = client.get_operational_stations()

   # Verificar que solo se devuelven las estaciones operativas
   assert len(operational) == 1, "Solo debe haber 1 estación operativa"
   assert operational[0].station_id == "1", "La estación operativa debe ser la ID 1"

     
    @patch('ej1c3.BarcelonaBikingClient.get_stations_status')
    def test_get_stations_with_available_bikes(self, mock_get_stations_status, station_data_operational, station_data_maintenance):
        """
        Verificar que el método get_stations_with_available_bikes filtra correctamente
        """
        # Crear instancias de estaciones para el mock
        station1 = StationStatusInfo(station_data_operational)
        station9 = StationStatusInfo(station_data_maintenance)
        
        # Configurar el mock para devolver las estaciones simuladas
        mock_get_stations_status.return_value = ([station1, station9], 1759835019)
        
        # Crear el cliente y obtener estaciones con bicicletas disponibles
        client = BarcelonaBikingClient()
        with_bikes = client.get_stations_with_available_bikes(min_bikes=5)
        
        # Verificar que solo se devuelven estaciones con suficientes bicicletas
        assert len(with_bikes) == 1, "Solo debe haber 1 estación con más de 5 bicicletas"
        assert with_bikes[0].station_id == "1", "La estación con bicicletas debe ser la ID 1"
        
        # Probar con un umbral diferente
        with_any_bike = client.get_stations_with_available_bikes(min_bikes=1)
        assert len(with_any_bike) == 1, "Solo debe haber 1 estación con bicicletas"







class VehicleType:
    """
    Clase que representa un tipo de vehículo y su cantidad disponible.
    """
    # Añade aquí los atributos necesarios: tipo de vehículo (vehicle_type_id) y cantidad (count)
    pass


class StationStatusInfo:
    """
    Clase que representa el estado de una estación de bicicletas compartidas.
    
    Atributos:
        station_id: Identificador único de la estación
        status: Estado actual de la estación (enum StationStatus)
        num_bikes_available: Número total de bicicletas disponibles
        num_bikes_disabled: Número de bicicletas fuera de servicio
        num_docks_available: Número de anclajes disponibles
        is_renting: Indica si la estación permite alquilar bicicletas
        is_returning: Indica si la estación permite devolver bicicletas
        last_reported: Timestamp del último reporte de estado
        vehicle_types: Lista de tipos de vehículos disponibles
    """
    
    def __init__(self, station_data):
        """
        Inicializa una instancia de StationStatusInfo a partir de los datos
        de la estación proporcionados por la API.
        
        Args:
            station_data: Diccionario con los datos de la estación obtenidos de la API
        """
        # Implementa aquí la inicialización de todos los atributos
        # a partir del diccionario station_data
        pass
    
    @property
    def is_operational(self) -> bool:
        """
        Indica si la estación está completamente operativa
        (en servicio y permite alquilar y devolver bicicletas)
        
        Returns:
            bool: True si la estación está operativa, False en caso contrario
        """
        # Implementa aquí la lógica para determinar si la estación está operativa
        pass
    
    def get_available_bikes_by_type(self) -> Dict[str, int]:
        """
        Devuelve un diccionario con la cantidad de bicicletas disponibles por tipo.
        
        Returns:
            Dict[str, int]: Diccionario donde la clave es el tipo de bicicleta
                            y el valor es la cantidad disponible
        """
        # Implementa aquí la lógica para devolver un diccionario
        # con la cantidad de bicicletas disponibles por tipo
        pass
    
    def __str__(self) -> str:
        """
        Devuelve una representación en string de la estación con su estado actual.
        
        Returns:
            str: Representación en texto del estado de la estación
        """
        # Implementa aquí la lógica para devolver una representación en texto
        # de la estación y su estado actual
        pass


class BarcelonaBikingClient:
    """
    Cliente para consultar el estado de las estaciones de bicicletas de Barcelona.
    """
    
    def __init__(self):
        """
        Inicializa el cliente con la URL base de la API.
        """
        self.base_url = "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en"
        self.station_status_url = f"{self.base_url}/station_status"
    
    def get_stations_status(self) -> Tuple[List[StationStatusInfo], Optional[datetime]]:
        """
        Obtiene el estado actual de todas las estaciones de bicicletas.
        
        Returns:
            Tuple[List[StationStatusInfo], Optional[datetime]]:
                - Lista de objetos StationStatusInfo, uno por cada estación
                - Timestamp de la última actualización de los datos, o None si hay error
        """
        # Implementa aquí la lógica para:
        # 1. Realizar una petición GET a la URL de station_status
        # 2. Verificar que la respuesta sea correcta (código 200)
        # 3. Crear objetos StationStatusInfo para cada estación en la respuesta
        # 4. Extraer el timestamp de last_updated de la respuesta
        # 5. Manejar posibles errores (conexión, formato, etc.)
        pass
    
    def find_station_by_id(self, station_id: str) -> Optional[StationStatusInfo]:
        """
        Busca una estación específica por su ID.
        
        Args:
            station_id: ID de la estación a buscar
            
        Returns:
            Optional[StationStatusInfo]: Objeto con la información de la estación,
                                         o None si no se encuentra
        """
        # Implementa aquí la lógica para buscar y devolver una estación por su ID
        pass
    
    def get_operational_stations(self) -> List[StationStatusInfo]:
        """
        Obtiene la lista de estaciones que están completamente operativas.
        
        Returns:
            List[StationStatusInfo]: Lista de estaciones operativas
        """
        # Implementa aquí la lógica para filtrar y devolver solo las estaciones operativas
        pass
    
    def get_stations_with_available_bikes(self, min_bikes: int = 1) -> List[StationStatusInfo]:
        """
        Obtiene la lista de estaciones que tienen al menos min_bikes disponibles.
        
        Args:
            min_bikes: Número mínimo de bicicletas requeridas (por defecto 1)
            
        Returns:
            List[StationStatusInfo]: Lista de estaciones con bicicletas disponibles
        """
        # Implementa aquí la lógica para filtrar y devolver las estaciones
        # con al menos min_bikes disponibles
        pass


if __name__ == "__main__":
    # Ejemplo de uso del cliente
    client = BarcelonaBikingClient()
    
    # Obtener el estado de todas las estaciones
    stations, last_updated = client.get_stations_status()
    
    if stations:
        # Mostrar información sobre el conjunto de datos
        print(f"Datos actualizados: {datetime.fromtimestamp(last_updated) if last_updated else 'Desconocido'}")
        print(f"Total de estaciones: {len(stations)}")
        
        # Mostrar estaciones operativas
        operational = client.get_operational_stations()
        print(f"\nEstaciones operativas: {len(operational)} de {len(stations)}")
        
        # Mostrar estaciones con bicicletas disponibles
        with_bikes = client.get_stations_with_available_bikes(min_bikes=5)
        print(f"\nEstaciones con al menos 5 bicicletas: {len(with_bikes)}")
        
        # Mostrar detalles de algunas estaciones
        if stations:
            print("\nDetalle de algunas estaciones:")
            for station in stations[:3]:  # Mostrar solo las primeras 3
                print(f"\n{station}")
                bikes_by_type = station.get_available_bikes_by_type()
                for bike_type, count in bikes_by_type.items():
                    print(f"  - {bike_type}: {count} disponibles")
    else:
        print("No se pudieron obtener los datos de las estaciones.")
