import fastapi
import uvicorn
from typing import Optional

api = fastapi.FastAPI()


@api.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return fastapi.Response(content='{"erro": "z não pode ser zero"}',
                                media_type="application/json",
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