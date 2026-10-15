# claude-rpc

Discord Rich Presence со случайными «вайбкодерскими» статусами, например «Дебажит кэш браузера» или «Спит, пока Клод работает». Фраза меняется каждые 5 секунд, таймер идёт от запуска.

## Настройка

1. Создай приложение на https://discord.com/developers/applications
2. Скопируй Application ID в `CLIENT_ID` в `rpc.py`
3. В **Rich Presence → Art Assets** загрузи `claude_1024.png` (ключ ассета должен совпадать с `LARGE_IMAGE` в `rpc.py`)
4. Установи зависимости и запусти при открытом Discord:

```bash
pip install -r requirements.txt
python rpc.py
```

Для запуска без окна консоли используй `pythonw rpc.py`. Для автозагрузки положи ярлык на `pythonw.exe rpc.py` в `shell:startup`.

## Настройки

- `DETAILS` — верхняя строка статуса
- `VERBS` и `OBJECTS` — из них собираются фразы (12 × 12 вариантов)
- `STATE_INTERVAL` — как часто менять фразу в секундах. Discord ограничивает частоту обновлений, при застревании поставь 15–20.
