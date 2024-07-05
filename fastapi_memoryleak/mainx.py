from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def background_task(message: str):
    # This function simulates a background task
    with open("background_tasks_log.txt", mode="a") as log:
        log.write(message + "\n")

@app.get("/send-notification/{message}")
async def send_notification(message: str, background_tasks: BackgroundTasks):
    # This endpoint will accept a message and send it as a notification in the background
    background_tasks.add_task(background_task, message)
    return {"message": "Notification sent in the background"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=9999)
