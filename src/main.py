# src/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
import os
from dotenv import load_dotenv

# Import only what's needed for the app instance itself initially
# We'll call setup_logging and initialize_sql_agent inside lifespan
from src.utils.logger import logger # Keep logger here for FastAPI logs before lifespan
from src.api.v1.api import api_router


# Load environment variables first (before any other imports that might use them)
load_dotenv()

# Setup logging once here at the top level, so it's configured for FastAPI itself
from src.utils.logger import setup_logging # Import the setup function
setup_logging() # Call it immediately to configure logging for the entire app


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager for application startup and shutdown events.
    Used to initialize the SQL agent once when the API starts.
    """
    logger.info("Application starting up...")
    try:
        # Import initialize_sql_agent ONLY here, inside the lifespan function.
        # This guarantees that src.core.agent has been fully loaded.
        from src.core.agent import initialize_sql_agent
        initialize_sql_agent() # This initializes the singleton agent
        logger.info("SQL agent pre-loaded successfully.")
    except Exception as e:
        logger.error(f"Failed to pre-load SQL agent on startup: {e}")
        raise RuntimeError("Failed to initialize core services on startup.") from e

    yield # Application will run here

    logger.info("Application shutting down...")
    # Add any cleanup code here if necessary


app = FastAPI(
    title="SQL AI Agent API",
    description="An API to convert natural language questions into SQL queries and retrieve results.",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    logger.info("Starting Uvicorn server...")
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True, log_level=os.getenv("LOG_LEVEL", "info").lower())