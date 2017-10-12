# vehicle types: moto, car, bus
# taken space by vehicle:
# moto spot -> motocycle
# compact spot-> moto, car
# large spot->moto, car
# bus can park if 5 large spots in a row
# multiple levels

from enum import Enum
from abc import ABCMeta, abstractmethod

# my implementation
# class Vehicle(object):
#     pass
#
# class Moto(Vehicle):
#     def __init__(self):
#         self._type = "Moto"
#         super(Moto, self).__init__()
#
# class Car(Vehicle):
#     def __init__(self):
#         self._type = "Car"
#         super(Car, self).__init__()
#
# class Bus(Vehicle):
#     def __init__(self):
#         self._type = "Bus"
#         super(Bus, self).__init__()
#
# # my_implementation
# class SpotType(Enum):
#     MOTO = 0
#     COMPACT = 1
#     LARGE = 2
#
# class ParkingSpot:
#     def __init__(self, spotType):
#         if spotType is SpotType:
#             self._spot_type = spotType
#         else:
#             raise ValueError("the parking spot should be of a predefined type")
#
# class ParkingLot:
#     def __init__(self, total_moto_spots, total_compact_spots, total_large_spots):
#         # motocycle spots
#         self._occ_moto_spots = []
#         self._total_moto_spots = total_moto_spots
#         # compact spots
#         self._occ_compact_spots = []
#         self._total_compact_spots = total_compact_spots
#         # large spots
#         self._occ_large_spots = []
#         self._total_large_spots = total_large_spots
#
#     def _has_free_moto_spots(self):
#         return self._total_moto_spots > len(self._occ_moto_spots)
#
#     def _has_free_compact_spots(self):
#         self._total_compact_spots > len(self._occ_compact_spots)
#
#     def _has_free_large_spots(self):
#         self._total_large_spots > len(self._occ_large_spots)
#
#     def _has_free_spots_for_moto(self):
#         return self._has_free_moto_spots() or self._has_free_compact_spots() or self._has_free_large_spots()
#
#     def _has_free_spots_for_car(self):
#         return self._has_free_compact_spots() or self._has_free_large_spots()
#
#     def _has_free_spots_for_bus(self):
#         return self._total_large_spots > 4 + len(self._occ_large_spots)
#
#     def park_moto(self, moto):
#         if moto is Moto:
#             if self._has_free_spots_for_moto():
#                 if self._has_free_moto_spots():
#                     self._occ_moto_spots.append(moto)
#                     return "Moto parked at moto spot", len(self._occ_moto_spots)
#                 elif self._has_free_compact_spots():
#                     self._occ_compact_spots.append(moto)
#                     return "Moto parked at compact spot", len(self._occ_compact_spots)
#                 elif self._has_free_large_spots():
#                     self._occ_large_spots.append(moto)
#                     return "Moto parked at large spot", len(self._occ_large_spots)
#             else:
#                 return "no free spots"
#         else:
#             raise ValueError("you should be parking a motocycle")


# Anki implementation
class VehicleSize(Enum):
    MOTORCYCLE = 0
    COMPACT = 1
    LARGE = 2

class Vehicle(object):
    __metaclass__ = ABCMeta

    def __init__(self, vehicle_size, license_plate, spot_size):
        self.vehicle_size = vehicle_size
        self.license_plate = license_plate
        self.spot_size = spot_size
        self.spots_taken = []

    def clear_spots(self):
        for spot in self.spots_taken:
            spot.remove_vehicle(self)
        self.spots_taken = []

    def take_spot(self, spot):
        self.spots_taken.append(spot)

    @abstractmethod
    def can_fit_in_spot(self, spot):
        pass

class Motorcycle(Vehicle):
    def __init__(self, license_plate):
        super(Motorcycle, self).__init__(VehicleSize.MOTORCYCLE, license_plate, spot_size=1)

    def can_fit_in_spot(self, spot):
        return True

class Car(Vehicle):
    def __init__(self, license_plate):
        super(Car, self).__init__(VehicleSize.COMPACT, license_plate, spot_size=1)

    def can_fit_in_spot(self, spot):
        return True if (spot.size == LARGE or spot.size == COMPACT) else False

class Bus(Vehicle):
    def __init__(self, license_plate):
        super(Bus, self).__init__(VehicleSize.LARGE, license_plate, spot_size=5)

    def can_fit_in_spot(self, spot):
        return True if spot.size == LARGE else False

class ParkingLot(object):
    def __init__(self, num_levels):
        self.num_levels = num_levels
        self.levels = []

    def park_vehicle(self, vehicle):
        for level in levels:
            if level.park_vehicle(vehicle):
                return True
            else:
                return False

class Level(object):
    SPOTS_PER_ROW = 10
    def __init__(self, floor, total_spots):
        self.floor = floor
        self.total_spots = total_spots
        self.available_spots = 0
        self.parking_spots = []

    def spot_freed(self):
        self.available_spots += 1

    def park_vehicle(self, vehicle):
        spot = self._find_available_spot(vehicle)
        if spot is None:
            return None
        else:
            spot.park_vehicle(vehicle)
            return spot

    def _find_available_spot(self, vehicle):
        pass

    def _park_starting_at_spot(self, spot, vehicle):
        pass

class ParkingSpot(object):
    def __init__(self, level, row, spot_number, spot_size, vehicle_size):
        self.level = level
        self.row = row
        self.spot_number = spot_numebr
        self.spot_size = spot_size
        self.vehicle_size = vehicle_size
        self.vehicle = None

    def is_available(self):
        return True if self.vehicle is None else False

    def can_fit_vehicle(self, vehicle):
        if self.vehicle is not None:
            return False
        return vehicle.can_fit_in_spot(self)

    def park_vehicle(self, vehicle):
        pass

    def remove_vehicle(self):
        pass
