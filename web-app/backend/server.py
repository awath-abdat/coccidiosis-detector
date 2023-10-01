from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Route
import asyncio
import uvicorn
import sys
import nest_asyncio

from file_transfer import dowload_image_from_form_data
from constants import TEMPORARY_IMAGE_FILE_PATH, PATH
from model_logic import model_predict, setup_model

nest_asyncio.apply()
app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount('/static', StaticFiles(directory='static'))

# Asynchronous Steps
loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(setup_model())]
model = loop.run_until_complete(asyncio.gather(*tasks))[0]

@app.route("/api/upload", methods=["POST"])
async def upload(request):
    data = await request.form()
    if 'file' not in data:
        return JSONResponse({'error': 'File is required!'})
    await dowload_image_from_form_data(data)
    label, _, code, accuracy = model_predict(TEMPORARY_IMAGE_FILE_PATH, model)
    return JSONResponse({'label': label, 'accuracy': float(accuracy), 'code': code})

@app.route("/upload", methods=["POST"])
async def upload(request):
    data = await request.form()
    await dowload_image_from_form_data(data)
    label, color, _, accuracy = model_predict(TEMPORARY_IMAGE_FILE_PATH, model)
    result_html1 = PATH/'static'/'result1.html'
    result_html2 = PATH/'static'/'result2.html'
    result_html = str(result_html1.open().read() + '<span style=\"color: ' + color + ';\">' + label + '</span>' + ' at <span style=\"color: blue;\">' + str(round(accuracy*100, 2)) + '%</span> accuracy' + result_html2.open().read())
    return HTMLResponse(result_html)

@app.route("/")
def form(request):
    index_html = PATH/'static'/'index.html'
    return HTMLResponse(index_html.open().read())

if __name__ == "__main__":
    if "serve" in sys.argv: uvicorn.run(app, host="127.0.0.1", port=8080)
