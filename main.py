from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items():
    return {"message": "This is a simple word counter API. Please provide text to count words."}
