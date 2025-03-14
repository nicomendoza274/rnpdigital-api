from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse


from routers import vehicle

app = FastAPI()

app.title = "rnpdigital API"
app.description = "Registro Nacional Republica de Costa Rica"
app.version = "0.1.0"

app_prefix = "/api"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vehicle.router, prefix=app_prefix)


@app.get("/", include_in_schema=False)
def main():
    return RedirectResponse(url="/docs/")
