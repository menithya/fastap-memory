from fastapi import FastAPI, BackgroundTasks, File, UploadFile
import pandas as pd
import asyncio
import os
from memory_profiler import profile 

app = FastAPI()

@profile
def read_excel_sheet(filepath, sheet_name):
    df = pd.read_excel(filepath, sheet_name=sheet_name)
    df = df.fillna(0)
    return df.to_dict(orient="records")
@profile
async def process_excel(file_path):
    file_path = "fastapi_memoryleak/xl_read.py"
    print(file_path)
    try:
        xl = pd.ExcelFile(file_path)
        sheet_names = xl.sheet_names
        print("Sheet names:", sheet_names)
        dict_record = read_excel_sheet(file_path,sheet_names[0])
        print(dict_record)
        dict_record = read_excel_sheet(file_path,sheet_names[1])
        print(dict_record)
        
    except Exception as e:
        print("Error processing Excel file:", e)

@app.post("/upload/")
async def upload_excel(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    # os.makedirs("uploads", exist_ok=True)
    # file_path = f"uploads/{file.filename}"
    
    # with open(file_path, "wb") as buffer:
    #     buffer.write(await file.read())
    file_path = "fastapi_memoryleak/xl_read.py"
    background_tasks.add_task(process_excel, file_path)
    return {"message": "Excel file uploaded and processing started in the background."}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)
