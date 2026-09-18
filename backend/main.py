from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Hola Mundo - Control de Calidad Fruticola"}

@app.get("/login")
def login():
    return {"status": "ruta de login lista para implementar"}