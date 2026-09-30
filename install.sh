#!/bin/bash
set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT="$DIR/kh_weather.py"

if [ ! -f "$SCRIPT" ]; then
    echo "Не найден файл kh_weather.py рядом с install.sh"
    exit 1
fi

sudo cp "$SCRIPT" /usr/local/bin/kh_weather
sudo chmod +x /usr/local/bin/kh_weather

echo "----------------------------------------"
echo "Установка завершена успешно!"
echo "Теперь вы можете использовать команду: kh_weather"
echo "----------------------------------------"