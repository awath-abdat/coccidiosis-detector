import numpy as np
from keras.api.saving import load_model
from keras.api.preprocessing import image
from keras.src.applications.imagenet_utils import preprocess_input

from file_transfer import download_file_from_url
from constants import MODEL_FILE_URL, MODEL_PATH


async def setup_model():
    # Download cocci model
    await download_file_from_url(MODEL_FILE_URL, MODEL_PATH)

    # Load the model and make the predict function
    model = load_model(MODEL_PATH)
    if not model:
        return

    getattr(model, "make_predict_function")()

    # Return the model
    return model


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    x = preprocess_input(np.expand_dims(image.img_to_array(img), axis=0))
    prediction = model.predict(x)[0]
    healthy, cocci, _, _ = prediction
    label = "Coccidiosis" if cocci > healthy else "Healthy"
    color = "red" if cocci > healthy else "green"
    accuracy = max(cocci, healthy)*100
    code = int(cocci > healthy)
    return (label, color, code, accuracy)
