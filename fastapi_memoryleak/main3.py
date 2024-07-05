from fastapi import FastAPI, BackgroundTasks
from memory_profiler import profile
import time
import numpy as np
import pandas as pd
from bson import ObjectId

app = FastAPI()

def get_mappings_category(
    code_unique_size: int, value_unique_size: int, value_unique_first: str
) -> str:
    if code_unique_size == 1 and value_unique_size > 1:
        return "cat-1"
    if code_unique_size == 1 and value_unique_size == 1:
        return "cat-2"
    if code_unique_size > 1 and value_unique_size == 1 and value_unique_first == "0-1":
        return "cat-3"


def get_mappings_values(df: pd.DataFrame):
    import pdb
    pdb.set_trace()
    df["_id"] = df.Text.apply(lambda x: str(ObjectId()))
    df.rename(columns={"Text": "text", "values": "value"}, inplace=True)
    return df[["_id", "text", "value"]].replace(np.nan, None).to_dict(orient="records")


@profile
def create_studies_mappings(df: pd.DataFrame):
    output = []
    for dp in df.groupby(by="Question"):
        question = dp[0]
        grouped_df = dp[1]

        code_unique = grouped_df["code"].unique().tolist()
        value_unique = grouped_df["values"].unique().tolist()
        value_unique_first = grouped_df["values"].unique().tolist()[0]

        output.append(
            dict(
                name=question,
                colName=code_unique,
                category=get_mappings_category(
                    len(code_unique), len(value_unique), value_unique_first
                ),
                values=get_mappings_values(grouped_df),
            )
        )

    return output

@profile
def read_excel_sheet(filepath, sheet_name):
    df = pd.read_excel(filepath, sheet_name=sheet_name)
    # df = df.fillna(0)
    # result = create_studies_mappings(df=df)
    dict_reocord = df.to_dict(orient="records")
    df.close()
    del df
    
    return dict_reocord
@profile
def process_excel(file_path):
    file_path = "fastapi_memoryleak/output_61.xlsx"
    # print(file_path)
    try:
        xl = pd.ExcelFile(file_path)
        sheet_names = xl.sheet_names
        # print("Sheet names:", sheet_names)
        dict_record = read_excel_sheet(file_path,sheet_names[0])
        # print(dict_record)
        dict_record = read_excel_sheet(file_path,sheet_names[1])
        # print(dict_record)
        
    except Exception as e:
        print("Error processing Excel file:", e)

@profile
def time_consuming_operation():
    file_path = "fastapi_memoryleak/output_61.xlsx"
    process_excel(file_path=file_path)
    return "Operation completed"

def background_task():
    result = time_consuming_operation()
    # with open("background_tasks_log.txt", mode="a") as log:
    #     log.write(result + "\n")

@app.get("/perform-background-task")
async def perform_background_task(background_tasks: BackgroundTasks):
    background_tasks.add_task(background_task)
    return {"message": "Background task accepted"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)
