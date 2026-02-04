from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Создаем экземпляр приложения FastAPI
app = FastAPI(
    title="MedBook API",
    description="API для системы онлайн-записи к врачам",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Настройка CORS (для работы с фронтендом)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все домены (в продакшене укажите конкретные)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все HTTP методы
    allow_headers=["*"],  # Разрешить все заголовки
)

# Маршрут для главной страницы
@app.get("/")
def read_root():
    return {
        "message": "Добро пожаловать в MedBook API!",
        "description": "Система онлайн-записи к врачам",
        "endpoints": {
            "docs": "/api/docs",
            "health": "/health",
            "api_v1": "/api/v1"
        },
        "version": "1.0.0"
    }

# Маршрут для проверки здоровья приложения
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "medbook-api",
        "timestamp": "2024-01-01T12:00:00Z"
    }

# Пример маршрута для API v1
@app.get("/api/v1")
def api_v1_info():
    return {
        "api": "MedBook API v1",
        "available_endpoints": [
            "/api/v1/auth",
            "/api/v1/users",
            "/api/v1/doctors",
            "/api/v1/appointments"
        ]
    }

# Пример маршрута с параметром
@app.get("/api/v1/hello/{name}")
def say_hello(name: str):
    return {
        "message": f"Привет, {name}!",
        "service": "MedBook",
        "tip": "Используйте /api/docs для документации API"
    }

# Маршрут для информации о проекте
@app.get("/api/v1/info")
def project_info():
    return {
        "project_name": "MedBook",
        "description": "Система онлайн-записи к врачам с напоминаниями",
        "stack": ["FastAPI", "PostgreSQL", "SQLAlchemy", "React", "Telegram Bot"],
        "features": [
            "Запись к врачам",
            "Управление расписанием",
            "Telegram-уведомления",
            "Парсинг сайтов поликлиник"
        ]
    }

# Этот блок нужен для запуска через python main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)