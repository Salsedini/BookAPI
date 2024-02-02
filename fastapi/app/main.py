from fastapi import FastAPI
import model 
from config import engine 
import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def Home():
    return "Que dicen mis chavales"

app.include_router(router.router, prefix = "/book", tags = ["book"])