from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def getItems():
    return ['Item 1', 'Item 2', 'Item 3']
