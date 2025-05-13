# simple fast api app to retun a formated name
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from fastapi import Request

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World From backend"}

@app.get("/formatted_name")
async def formatted_name(request: Request):
    first_name = request.query_params.get("first_name")
    last_name = request.query_params.get("last_name")
    if first_name and last_name:
        formatted_name = f"{first_name} {last_name}"
        return JSONResponse(content={"formatted_name": formatted_name})
    else:
        return JSONResponse(content={"error": "Please provide both first and last name"}, status_code=400)