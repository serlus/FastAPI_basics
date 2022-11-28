import fastapi
import uvicorn
from typing import Optional


api = fastapi.FastAPI()


@api.get('/')
def index():
    body = "<html>"\
            "<body style='padding: 10px;'>"\
            "<h1>Welcome to the API</h1>"\
            "<div>"\
            "Try it: <a href='/api/calculate?x=76&y=11'>/api/calculate?x=76&y=11</a>" \
            "</div>" \
            "</body>" \
            "</html>"
    return fastapi.responses.HTMLResponse(content=body)


@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return fastapi.responses.JSONResponse(
                                            content={"erro": "z não pode ser zero"},
                                            status_code=400
                                            )
    value = x + y
    if z is not None:
        value = value / z

    return {
        'x': x,
        'y': y,
        'z': z,
        'value': value
    }


uvicorn.run(api, port=8001, host="127.0.0.1", loop="auto")
