from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from memory_profiler import profile
import numpy as np
import cv2 
from net.mongodbcon import MongoDBConns

app = FastAPI()

@profile
def load_and_process_image(file_path):
    muri = "mongodb+srv://dce-qa2:jjsRpiadbyFLStNq@dce-qa2.mfhg2.mongodb.net/dce-qa2?retryWrites=true&w=majority&authMechanism=DEFAULT"
    mdb="dce-qa2"
    mongo = MongoDBConns(mongodb_uri=muri,mongodb_db=mdb)
    image = cv2.imread(file_path)

    resized_image = cv2.resize(image, (100, 100))  # Resize the image (modify as needed)
    return resized_image

@app.post("/process_image")
async def process_image(file: UploadFile = File(...)):
    
    # Save the uploaded file to the server
    file_path = f"fastapi_memoryleak/uploads/{file.filename}"
    with open(file_path, "wb") as image_file:
        image_file.write(file.file.read())

    # Process the image
    result_image = load_and_process_image(file_path)

    # Save the processed image
    processed_file_path = f"fastapi_memoryleak/uploads/processed_{file.filename}"
    cv2.imwrite(processed_file_path, result_image)

    # Return the processed image as a response
    return FileResponse(processed_file_path, media_type="image/png")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8888)