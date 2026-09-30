#!/usr/bin/env python3
import argparse
import requests


class WeatherError(Exception):
    pass


def get_weather(city: str) -> dict:
    url = f"https://wttr.in/{city}"
    params = {
        "format": "j1",
        "lang": "ru",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.RequestException as e:
        raise WeatherError(f"Ошибка сети: {e}")

    if response.status_code != 200:
        raise WeatherError(f"Сервис вернул {response.status_code}")

    try:
        data = response.json()
    except ValueError:
        raise WeatherError(
            "wttr.in вернул не JSON. Скорее всего, город не найден."
        )

    current = data["current_condition"][0]

    return {
        "city": city,
        "temp": float(current["temp_C"]),
        "feels_like": float(current["FeelsLikeC"]),
        "wind": float(current["windspeedKmph"]) / 3.6,  # км/ч → м/с
        "description": current["lang_ru"][0]["value"]
            if "lang_ru" in current else current["weatherDesc"][0]["value"],
    }

def main():
    parser = argparse.ArgumentParser(description="Утилита вывода прогноза погоды в выбранном городе")
    parser.add_argument("city", help="Название города, например: Москва")
    args = parser.parse_args()
    try:
        weather = get_weather(args.city)
    except WeatherError as e:
        print(f"Ошибка {e}")
        return

    print(f"Погода в {weather['city']}:")
    print(f"  Температура: {weather['temp']:.1f}°C")
    print(f"  Ощущается как: {weather['feels_like']:.1f}°C")
    print(f"  Ветер: {weather['wind']:.1f} м/с")
    print(f"  Описание: {weather['description']}")

if __name__ == "__main__":
    main()