@'
Write-Host "Создание файлов проекта MedBook..." -ForegroundColor Cyan

# Массив всех файлов
$files = @(
    # Корневые файлы
    ".gitignore",
    "docker-compose.yml", 
    "README.md",
    
    # Backend
    "backend/requirements.txt",
    "backend/alembic.ini",
    "backend/.env.example",
    "backend/Dockerfile",
    "backend/app/__init__.py",
    "backend/app/main.py",
    
    # Core
    "backend/app/core/__init__.py",
    "backend/app/core/config.py",
    "backend/app/core/security.py",
    "backend/app/core/dependencies.py",
    
    # DB
    "backend/app/db/__init__.py",
    "backend/app/db/base.py",
    "backend/app/db/session.py",
    
    # API
    "backend/app/api/__init__.py",
    "backend/app/api/v1/__init__.py",
    "backend/app/api/v1/api.py",
    "backend/app/api/v1/endpoints/__init__.py",
    "backend/app/api/v1/endpoints/auth.py",
    "backend/app/api/v1/endpoints/users.py",
    "backend/app/api/v1/endpoints/doctors.py",
    "backend/app/api/v1/endpoints/appointments.py",
    
    # Models
    "backend/app/models/__init__.py",
    "backend/app/models/user.py",
    "backend/app/models/doctor.py",
    "backend/app/models/appointment.py",
    "backend/app/models/clinic.py",
    "backend/app/models/schedule.py",
    
    # Schemas
    "backend/app/schemas/__init__.py",
    "backend/app/schemas/user.py",
    "backend/app/schemas/doctor.py",
    "backend/app/schemas/appointment.py",
    
    # Frontend
    "frontend/package.json",
    "frontend/Dockerfile",
    
    # Telegram bot
    "telegram-bot/requirements.txt",
    "telegram-bot/Dockerfile",
    "telegram-bot/bot.py",
    "telegram-bot/__init__.py",
    "telegram-bot/handlers/__init__.py",
    "telegram-bot/handlers/start.py",
    "telegram-bot/handlers/appointments.py"
)

# Создаем каждый файл
foreach ($file in $files) {
    # Создаем директорию, если её нет
    $dir = Split-Path $file -Parent
    if ($dir -and !(Test-Path $dir)) {
        New-Item -ItemType Directory -Force -Path $dir | Out-Null
    }
    
    # Создаем файл
    New-Item -ItemType File -Force -Path $file | Out-Null
    Write-Host "✓ Создан: $file"
}

Write-Host "`n✅ Все файлы созданы успешно!" -ForegroundColor Green
Write-Host "Теперь можно заполнить их содержимым из инструкции." -ForegroundColor Yellow
'@ | Out-File -FilePath "setup-files.ps1" -Encoding UTF8