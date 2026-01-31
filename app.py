from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Use app_working.py instead"}

if __name__ == "__main__":
    print("⚠️  Use app_working.py for the main application")
    uvicorn.run(app, host="0.0.0.0", port=8001)