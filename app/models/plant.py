"""
contains all db models for this project. separating them into different files 
causes nontrivial import issues. consider a refactor later if this becomes
bloated beyond reason
"""
from typing import Optional

from sqlmodel import Field, SQLModel

from app.models.enums import Health, WateringFrequency


# --- PLANTS --- #
# common attributes for all plant models
class PlantBase(SQLModel):
    nickname: str
    species: Optional[str] = "plantus mysterius"
    health: Optional[Health] = Health.LIVING
    watering_frequency: Optional[WateringFrequency]
    needs_watered: Optional[bool] = False
    last_watered: Optional[int]


# sqlmodel reads this to create appropriate metadata for db table
# likely the appropriate model to use for Update actions?
class Plant(PlantBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


# additional information required for plant creation
class PlantCreate(PlantBase):
    pass


# additional information which can be expected when reading from db
class PlantRead(PlantBase):
    id: int
