@echo off
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Пожалуйста, запустите этот файл от имени Администратора!
    pause
    exit /b
)

copy "%~dp0kh_weather.py" C:\Windows\kh_weather.py >nul

echo @python C:\Windows\kh_weather.py %%* > C:\Windows\kh_weather.bat

echo ----------------------------------------
echo Установка в Windows завершена успешно!
echo Теперь команда kh_weather доступна в cmd/PowerShell.
echo ----------------------------------------
pause