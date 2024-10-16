import sys
import asyncio
import uvicorn
import nest_asyncio
from starlette.middleware import Middleware
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse

from model_logic import model_predict, setup_model
from constants import ALLOWED_METHODS, ALLOWED_ORIGINS, TEMPORARY_IMAGE_FILE_PATH, PATH
from file_transfer import dowload_image_from_form_data
from authentication import get_user_details_from_google_code


nest_asyncio.apply()
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_methods=ALLOWED_METHODS,
    ),
]
templates = Jinja2Templates(directory="templates")
app = Starlette(middleware=middleware)
app.mount("/static", StaticFiles(directory="static"))

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(setup_model())]
model = loop.run_until_complete(asyncio.gather(*tasks))[0]


@app.route("/api/upload", methods=["POST"])
async def upload_api(request):
    data = await request.form()
    if "file" not in data:
        return JSONResponse({"error": "File is required!"})
    await dowload_image_from_form_data(data)
    label, _, code, accuracy = model_predict(TEMPORARY_IMAGE_FILE_PATH, model)
    return JSONResponse({"label": label, "accuracy": float(accuracy), "code": code})


@app.route("/upload", methods=["POST"])
async def upload(request):
    data = await request.form()
    await dowload_image_from_form_data(data)
    label, color, _, accuracy = model_predict(TEMPORARY_IMAGE_FILE_PATH, model)
    return templates.TemplateResponse(
        request,
        "result.html",
        {"accuracy": str(round(accuracy)), "color": color, "label": label},
    )


@app.route("/code", methods=["POST"])
async def code(request):
    code = request.headers.get("authorization", None)
    return (
        JSONResponse({"error": "Code cannot be none"})
        if not code
        else get_user_details_from_google_code(request, code)
    )


@app.route("/")
def form(_):
    return HTMLResponse((PATH / "static" / "index.html").open().read())


if __name__ == "__main__" and "serve" in sys.argv:
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")
