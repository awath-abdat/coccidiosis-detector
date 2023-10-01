from keras.applications.imagenet_utils import preprocess_input
from keras.preprocessing import image
from keras.models import load_model
from file_transfer import download_file_from_url
from constants import MODEL_FILE_URL, MODEL_PATH
import numpy as np

async def setup_model():
    # Download cocci model
    await download_file_from_url(MODEL_FILE_URL, MODEL_PATH)

    # Load the model and make the predict function
    model = load_model(MODEL_PATH)
    model.make_predict_function()

    # Return the model
    return model

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    x = preprocess_input(np.expand_dims(image.img_to_array(img), axis=0))
    prediction = model.predict(x)[0]
    cocci, healthy = prediction
    label = "Coccidiosis" if cocci > healthy else "Healthy"
    color = "red" if cocci > healthy else "green"
    accuracy = max(cocci, healthy)
    code = int(cocci > healthy)
    return (label, color, code, accuracy)