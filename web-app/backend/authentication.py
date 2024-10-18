from starlette.responses import JSONResponse

from constants import GOOGLE_CREDENTIALS_FILE

# (Receive auth_code by HTTPS POST)


def get_user_details_from_google_code(request, auth_code):
    return JSONResponse({})
