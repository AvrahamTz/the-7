from fastapi import FastAPI,File, UploadFile
import uvicorn
from datetime import datetime
import csv
from solider import Solider


app = FastAPI()
@app.get("/")
def get_root():
    return {"ts": datetime.now()}

@app.post("/assignWithCsv")
def get_file(file: UploadFile = File()):
    if not "csv" in file.content_type:
        return {"msg": f"content_type: `{file.content_type}` not allowed!"}
    text = file.file.read().decode()
   
   
    reader = csv.reader(text.splitlines())
    rows = [row for row in reader]
    columns = rows[0]
    rows = rows[1:]
    data = Solider.add_solider(Solider.to_dict(rows))

