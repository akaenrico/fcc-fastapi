from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


# Status route
@app.get("/status", status_code=200)
def get_status():
    return {
        "status": "ok",
        "version": "1.0.0"
    }
