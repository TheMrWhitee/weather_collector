from fastapi import FastAPI

from project.api.resources import router

app = FastAPI()
app.include_router(router)


@app.get('/ping')
def ping():
    return {'ping': True}
