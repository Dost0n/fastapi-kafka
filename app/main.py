from fastapi import FastAPI
import router
import asyncio


app = FastAPI()


@app.get('/')
async def home():
    return {'message':"hello world"}


app.include_router(router.route)
asyncio.create_task(router.consume())