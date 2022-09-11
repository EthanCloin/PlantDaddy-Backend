from fastapi import FastAPI, HTTPException, Query
from app.models import Plant, PlantCreate, PlantRead, Health
from app.db import connector
from sqlmodel import Session, select
from fastapi.middleware.cors import CORSMiddleware

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
    # TODO: move engine into an upper level dependencies.py and use with Depends
    global engine
    engine = connector.get_engine()


# TODO: refactor all below paths to be more logical
@app.post("/plants/new/", response_model=PlantRead)
async def create_new_plant(plant: PlantCreate):
    with Session(engine) as session:
        db_plant = Plant.from_orm(plant)
        session.add(db_plant)
        session.commit()
        session.refresh(db_plant)
        return db_plant


@app.get("/nursery/")
async def get_all_plants(
    offset: int = 0, limit: int = Query(default=20, lte=100)
) -> list[Plant]:
    with Session(engine) as session:
        plants = session.exec(select(Plant).offset(offset).limit(limit)).all()
        return plants


@app.get("/plants/id/{plant_id}", response_model=PlantRead)
async def get_plant_by_id(plant_id: int):
    with Session(engine) as session:
        plant = session.get(Plant, plant_id)
        if not plant:
            raise HTTPException(status_code=404, detail="Plant not found")
        return plant


@app.get("/plants/health/{plant_health}", response_model=list[Plant])
async def get_plants_by_health(
    plant_health: Health, offset: int = 0, limit: int = Query(default=10, lte=100)
):

    with Session(engine) as session:
        stmt = (
            select(Plant)
            .where(Plant.health == plant_health)
            .offset(offset)
            .limit(limit)
        )
        result = session.exec(stmt)
        plants = result.all()
        return plants
