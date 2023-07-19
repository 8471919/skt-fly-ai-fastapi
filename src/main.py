from fastapi import FastAPI
import uvicorn

from src.api.index import api_router

app = FastAPI(docs_url="/api_docs", openapi_url="/open-api")

app.include_router(api_router, prefix="/api")


@app.get("/")
async def getHello():
    return "<h1>Hello! This is Fastapi Server</h1>\
            <div><a href='/api/v1/user' style='color:red'>Go to user</a></div>"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
