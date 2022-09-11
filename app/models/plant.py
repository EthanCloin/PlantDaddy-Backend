from sqlmodel import SQLModel, Field
from typing import Optional


# common attributes for all plant models
class PlantBase(SQLModel):
    nickname: str
    species: Optional[str] = "unknown"
    health: str


# sqlmodel reads this to create appropriate metadata for db table
class Plant(PlantBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


# additional information required for plant creation
class PlantCreate(PlantBase):
    pass


# additional information which can be expected when reading from db
class PlantRead(PlantBase):
    id: int
