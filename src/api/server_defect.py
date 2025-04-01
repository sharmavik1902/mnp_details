from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from datetime import datetime

from src.crud.db_defect import save_defect_report
from src.crud.db_defect import get_all_defects
from src.crud.db_defect import get_distinct_defect,get_distinct_part,get_distinct_eqp

app = FastAPI()
'''-------------------------------------------------------------'''
class ReportDefect(BaseModel):
    equipment_id: str
    part_id: str
    defect_description: str
    reported_by: str


'''--------------------------------------------------------------'''

@app.post("/report_defect/")
def save_mmd_dpr(report: ReportDefect = Body()):
    save_defect_report(*report.model_dump().values())
    if not report:
        raise HTTPException(status_code=500, detail="Failed to retrieve defect summery from the database")

    return {"message": "Defect updated successfully"}

'''------------------------------------------------------'''
@app.get("/defect_list/{defect_status}")
def defect_list(defect_status: str):
    data = get_all_defects(defect_status)
    if not data:
        raise HTTPException(status_code=404, detail="No data found")
    return {"defect_status": defect_status, "defect_list": data}

@app.get("/equipment_list/{defect_status}")
def distinct_equipment_list(defect_status: str):
    data = get_distinct_eqp(defect_status)
    if not data:
        raise HTTPException(status_code=404, detail="No data found")
    return {"defect_status": defect_status, "equipment_list": data}

@app.get("/part_list/{equipment_list}")
def distinct_part_list(equipment_list: str):
    data = get_distinct_part(equipment_list)
    if not data:
        raise HTTPException(status_code=404, detail="No data found")
    return {"equipment_list": equipment_list, "part_list": data}

@app.get("/distinct_defect/{part_list}")
def distinct_part_list(part_list: str):
    data = get_distinct_defect(part_list)
    if not data:
        raise HTTPException(status_code=404, detail="No data found")
    return {"part_list": part_list, "distinct_defect": data}

'''-------------------------------------------------------------------------'''
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)