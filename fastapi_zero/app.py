from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='FastAPI Zero')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get(
    '/landing-page', status_code=HTTPStatus.OK, response_class=HTMLResponse
)
def landing_page():
    return """
    <html>
        <head>
            <title>Landing Page</title>
        </head>
        <body>
            <h1>Welcome to the Landing Page</h1>
        </body>
    </html>
    """
