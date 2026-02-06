from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import users, doctors, appointments

app = FastAPI(title="MedBook Platform API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Роутеры
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(doctors.router, prefix="/api/v1/doctors", tags=["doctors"])
app.include_router(appointments.router, prefix="/api/v1/appointments", tags=["appointments"])

@app.get("/")
def read_root():
    return {"message": "MedBook Platform API"}