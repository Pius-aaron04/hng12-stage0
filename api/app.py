#!/usr/bin/env pyhton3
'''FastAPI app that serves basic data'''

from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


# Response Structure
class Response(BaseModel):
    email: str = "piuschbz@gmail.com"
    current_datetime: str = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
    github_url: str = "https://github.com/Pius-aaron04/hng12-stage0"


app = FastAPI()


origins = [
    "*" # Allow all origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def get_root() -> Response:
    return Response()
