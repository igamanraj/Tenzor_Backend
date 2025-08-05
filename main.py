from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging
from constants import SERVER_URL, PORT, ENV
from apps.calculator.route import router as calculator_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI): 
    logger.info("Starting up the application...")
    yield
    logger.info("Shutting down the application...")

app = FastAPI(lifespan=lifespan)
app.add_middleware(CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health():
    """
    Health check endpoint to verify if the server is running.
    """
    return {"message": "Server is running", "status": "healthy"}

app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])


if __name__ == "__main__":
    try:
        logger.info(f"Starting server on {SERVER_URL}:{PORT}")
        uvicorn.run(app, host=SERVER_URL, port=PORT, log_level="info")
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        raise

# For Render deployment
app_for_render = app 