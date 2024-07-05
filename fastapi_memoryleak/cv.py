from memory_profiler import profile
import fastapi_memoryleak.cv22 as cv22

@profile
def load_and_process_image(file_path):
    image = cv22.imread(file_path)
    resized_image = cv22.resize(image, (100, 100))  # Resize the image (modify as needed)
    return resized_image

if __name__ == "__main__":
    file_path = "image.png"  # Provide the path to your image
    result_image = load_and_process_image(file_path)
