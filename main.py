from fastapi import FastAPI

# Variable que va a contener nuestra aplicación
app = FastAPI()

#path decoration to a function
@app.get("/")
def home():
    # Return JSON=Dictionary -> Key: Hello y Value: World
    return {"Hello": "world"} 