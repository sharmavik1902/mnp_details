from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from datetime import datetime

from src.crud.db_crud import insert_personal_details
from src.crud.db_crud import insert_mmd_dpr
from src.crud.db_crud import fetch_equip_maint_history
from src.crud.db_crud import fetch_distinct_equip_list
from src.crud.db_crud import fetch_distinct_eqi_wrt_area_list

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

'''-------------------------------------------------------------------------------'''
@app.get("/maint_history/{equipment_name}")
def fetch_maint_history(equipment_name: str):
    data = fetch_equip_maint_history(equipment_name)
    if not data:
        raise HTTPException(status_code=404, detail="No data found")
    return {"equipment_name": equipment_name, "history": data}


'''This API to to provide List of equipment to select box'''
@app.get("/distinct-eq_list/")
def fetch_distinct_equipment_list():
    data = fetch_distinct_equip_list()
    if not data:
        raise HTTPException(status_code=404, detail="No data found")
    return data


''' This API is to provide List of sub equipment wrt to filtered Area'''
@app.get("/distinct_sub_eqi_wrt_area_list/{selected_area}")
def fetch_distinct_subequip_wrt_area_list(selected_area: str):
    print("Hello API is fine")
    sub_eq_list = fetch_distinct_eqi_wrt_area_list(selected_area)
    if not sub_eq_list:
        raise HTTPException(status_code=404, detail="No data found")
    return {"selected_area": selected_area, "sub_equip": sub_eq_list}


'''--------------------------------------------------------------------------'''

# Run FastAPI Server Properly (No direct function calls)
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8080)

