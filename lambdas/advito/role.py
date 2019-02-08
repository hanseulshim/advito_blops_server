from enum import Enum

class Role(Enum):
    """
    Different types of roles a user or application component can have.
    """
    HOTEL_SYSTEM = 1
    AIR_SYSTEM = 2
    I_AND_A_SYSTEM = 3
    ADMINISTRATOR = 4
    GENERAL = 5
    REPORTS = 6
