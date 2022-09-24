"""
represents various enumerations that are leveraged in db columns
to limit valid choices on a given property
"""

from enum import Enum


class Health(str, Enum):
    """the health status of a plant"""

    DYING = "dying"
    SURVIVING = "surviving"
    LIVING = "living"
    GROWING = "growing"
    THRIVING = "thriving"


class WateringFrequency(int, Enum):
    """the number of days between waterings for a plant"""

    MONTHLY = 30
    BIMONTHLY = 14
    WEEKLY = 7
    BIWEEKLY = 4
