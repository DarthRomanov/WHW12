from fastapi import FastAPI
from src.routes import contacts, users, auth, token



app = FastAPI()


app.include_router(contacts.router, prefix="/api")  # Можете додати префікс "/api"
app.include_router(users.router, prefix="/api")     # Можете додати префікс "/api"
app.include_router(auth.router, prefix="/api/auth") # Додайте маршрути з авторизацією
app.include_router(token.router, prefix="/api/token") # Додайте маршрути для токенів
@app.get("/")
def read_root():
    return {"message": "Hello World"}

app.include_router(auth.router)
app.include_router(token.router)

