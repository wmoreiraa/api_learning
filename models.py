from typing import List, Optional

from pydantic import BaseModel, Field


# Model table
class ModelList(BaseModel):
    mid: int
    model_name: str
    cod_params: int


class ParamList(BaseModel):
    cod_params: int
    n_estimators: int
    learning_rate: Optional[float]


# Model entries
class ModelEntry(BaseModel):
    mid: int = Field(..., example="12")
    model_name: str = Field(..., example="xgbregressor")
    cod_params: int = Field(..., example="Insert the params code")


class ParameterEntry(BaseModel):
    n_estimators: int = Field(..., example="Enter value of param")
    learning_rate: Optional[float] = Field(..., example="Enter value of param")
