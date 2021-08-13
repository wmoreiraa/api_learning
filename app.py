from typing import List

from fastapi import FastAPI

import models
from db import database
from db import models as models_table
from db import params as params_table

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/models", response_model=List[models.ModelList], tags=["Models"])
async def fetch_all_models():
    query = models_table.select()
    return await database.fetch_all(query)


@app.post("/models", response_model=List[models.ModelList], tags=["Models"])
async def register_model(model: models.ModelEntry):
    query = models_table.insert().values(
        id=model.mid, model_name=model.model_name, cod_params=model.cod_params
    )

    await database.execute(query)
    return {**model.dict()}
