from fastapi import FastAPI
from pydantic import BaseModel
from src.crud.ai_data_extract import get_filters

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

