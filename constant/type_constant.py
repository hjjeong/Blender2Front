from enum import Enum, auto

class TypeConstant(Enum):
    MESH = 'mesh'
    FURNITURE = 'furniture'
    EXTENSION = 'extension'
    MATERIAL = 'material'

class RoomTypeConstant(Enum):
    LIVING_ROOM = 'LivingDiningRoom'
    BEDROOM = 'BedRoom'
    LIVING_BEDROOM = 'LivingBedRoom'
    OFFICE_ROOM = 'OfficeRoom'