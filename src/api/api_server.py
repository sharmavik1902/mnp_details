from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from datetime import datetime

from src.crud.update_db import insert_personal_details
from src.crud.update_db import insert_mmd_dpr

app = FastAPI()
'''---------------------------------------------------------------'''
class DailyDefect(BaseModel):
    unit_no: int
    area: str
    equipment: str
    dept: str
    work_description: str
    permit_no: int
    mp_deployed: int
    job_start: datetime
    job_stop: datetime
    consumables: str
    spares: str
    status: str
'''----------------------------------------------'''
class PersonalDetail(BaseModel):
    name: str
    age: int
    mobile_no: int
    address: str
'''----------------------------------------------------------------'''
@app.post("/mnp_detail/")
def save_mnp_details(detail: PersonalDetail = Body(...)):
    try:
        insert_personal_details(*detail.model_dump().values())  # Insert into DB
        return {"message": "Detail updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
'''-----------------------------------------------------------------------'''
@app.post("/mmd_dpr/")
def save_mmd_dpr(defect: DailyDefect = Body()):
    insert_mmd_dpr(*defect.model_dump().values())
    if not defect:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summery from the database")

    return {"massage": "Expense updated successfully"}

# Run FastAPI Server Properly (No direct function calls)
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8080)

