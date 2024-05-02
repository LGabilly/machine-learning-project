import uvicorn
from fastapi import FastAPI

# from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRouter

from src.backend.config.iris import settings
from src.backend.routers.router_iris import router as iris_router

app = FastAPI(
    title=settings.API_NAME,
    version=settings.API_VERSION,
)

# If need be

# app.add_middleware(
#     CORSMiddleware,
#     allow_credentials=False,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/health", tags=["health check"])
async def root() -> dict[str, str]:
    return {"status": "ON"}


router = APIRouter()
router.include_router(iris_router)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=settings.API_PORT)
