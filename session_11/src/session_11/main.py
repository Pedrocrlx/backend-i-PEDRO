from fastapi import FastAPI, HTTPException
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def read_root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to the FastAPI API!"}

@app.post("/items/")
async def create_item(item: dict):
    logger.info(f"Item received: {item}")
    # A simple validation example
    if "name" not in item:
        logger.error("Item does not contain 'name'")
        raise HTTPException(status_code=400, detail="Item must have a name")
    return {"item_id": item}