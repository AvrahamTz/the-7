from fastapi import FastAPI,File, UploadFile
import uvicorn
import csv
from solider import Solider
from rooms import Rooms


app = FastAPI()

@app.post("/assignWithCsv")
def get_file(file: UploadFile = File()):
    if not "csv" in file.content_type:
        return {"msg": f"content_type: `{file.content_type}` not allowed!"}
    text = file.file.read().decode()
   
   
    reader = csv.reader(text.splitlines())
    rows = [row for row in reader]
    columns = rows[0]
    rows = rows[1:]
    data = Solider(rows)
    Solider.add_solider(data)
    new = Solider.sorted_data()
    dormA =Rooms.to_buildings(new)
    dormB =Rooms.to_buildings(new)
    return {"assigned":(len(dormA)+len(dormB)),"waitinglist":[4553] }

if __name__ == "__main__":
    uvicorn.run(app)


