from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from src.crud.update_db import insert_personal_details

app = FastAPI()

class PersonalDetail(BaseModel):
    name: str
    age: int
    mobile_no: int
    address: str

@app.post("/mnp_detail/")
def save_mnp_details(detail: PersonalDetail = Body(...)):
    try:
        insert_personal_details(*detail.model_dump().values())  # Insert into DB
        return {"message": "Detail updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# Run FastAPI Server Properly (No direct function calls)
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8080)

