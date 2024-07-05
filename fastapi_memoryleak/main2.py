from fastapi import FastAPI, BackgroundTasks
import asyncio
from memory_profiler import profile

app = FastAPI()

@profile
async def process_request(request_id: int):
    # Simulate processing request with asynchronous operations
    await asyncio.sleep(1)
    result = f"Processed request {request_id}"
    return result

async def background_task(request_id: int):
    result = await process_request(request_id)
    with open("background_tasks_log.txt", mode="a") as log:
        log.write(result + "\n")

@app.get("/process-request/{request_id}")
async def process_request_endpoint(request_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(background_task, request_id)
    return {"message": f"Request {request_id} accepted for processing"}
