from fastapi import FastAPI
from pydantic import BaseModel
from src.crud.ai_data_extract import get_filters

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/filter/")
def filter_data(req: QueryRequest):
    filters = get_filters(req.query)
    df = get_data_from_filters(filters)
    return df.to_dict(orient="records")