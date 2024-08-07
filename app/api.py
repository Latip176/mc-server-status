from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from enum import Enum
from .server import Java, Bedrock
from fastapi.middleware.cors import CORSMiddleware

application = FastAPI()

application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Atur ini sesuai dengan daftar origin yang diizinkan
    allow_credentials=True,
    allow_methods=["*"],  # Atur ini sesuai dengan metode HTTP yang diizinkan
    allow_headers=["*"],  # Atur ini sesuai dengan header yang diizinkan
)

SERVER_TYPES = ["java", "bedrock"]


class ServerType(str, Enum):
    def __str__(self):
        return self.value

    JAVA = "java"
    BEDROCK = "bedrock"


@application.exception_handler(Exception)
async def internal_server_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )


@application.get("/api/{ServerTipe}")
async def handler_request(ServerTipe: ServerType, ip: str, port: int = 19132) -> dict:
    if ServerTipe not in SERVER_TYPES:
        raise HTTPException(status_code=422, detail="type server not found")
        # return {"msg": "type server is not found"}
    try:
        data = Java(ip) if ServerTipe.lower() == "java" else Bedrock(ip, port)
    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))

    return {"msg": "success", "data": data}


app = application
