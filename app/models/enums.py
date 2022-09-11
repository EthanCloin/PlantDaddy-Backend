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
