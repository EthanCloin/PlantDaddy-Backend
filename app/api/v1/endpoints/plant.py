# from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.dependencies import LocalSession, get_db
from app.db.connector import init_db
from app.models.plant import Plant, PlantCreate, PlantRead

# from sqlmodel import select

# from app.models.enums import Health

# TODO: move app instance and CORS handling into upper-level main.py file
#   replace this with an APIRouter and add it to higher-layer app
# api setup
app = FastAPI()

# needs to be the frontend server url
origins = ["http://localhost:3000", "localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    init_db()


# TODO: refactor all below paths to be more logical
@app.post("/plants/new/", response_model=PlantRead)
async def create_new_plant(plant: PlantCreate, db: LocalSession = Depends(get_db)):
    db_plant = Plant.from_orm(plant)
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)
    return db_plant


# @app.get("/nursery/")
# async def get_all_plants(
#     offset: int = 0, limit: int = Query(default=20, lte=100)
# ) -> list[Plant]:
#     with get_db() as db:
#         plants = db.exec(select(Plant).offset(offset).limit(limit)).all()
#         return plants


# @app.get("/plants/id/{plant_id}", response_model=PlantRead)
# async def get_plant_by_id(plant_id: int):
#     # TODO: move the actual db loging into a crud pkg and import complete
#     #       functions, use Depends obj and pass in the session
#     with get_db() as session:
#         plant = session.get(Plant, plant_id)
#         if not plant:
#             raise HTTPException(status_code=404, detail="Plant not found")
#         return plant


# @app.get("/plants/health/{plant_health}", response_model=list[Plant])
# async def get_plants_by_health(
#     plant_health: Health, offset: int = 0, limit: int = Query(default=10, lte=100)
# ):

#     with get_db() as session:
#         stmt = (
#             select(Plant)
#             .where(Plant.health == plant_health)
#             .offset(offset)
#             .limit(limit)
#         )
#         result = session.exec(stmt)
#         plants = result.all()
#         return plants
