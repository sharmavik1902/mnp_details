from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from datetime import datetime

from src.crud.db_defect import save_defect_report

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

    return {"massage": "Defect updated successfully"}

'''------------------------------------------------------'''
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8080)