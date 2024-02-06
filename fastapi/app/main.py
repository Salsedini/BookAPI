from fastapi import FastAPI
import model 
from config import Base, engine
import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def Home():
    return "Home sweet home"

app.include_router(router.router, prefix = "/book", tags = ["book"])