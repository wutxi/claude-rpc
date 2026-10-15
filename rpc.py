import random
import time
from pypresence import Presence

# 1. Создай приложение на https://discord.com/developers/applications , назови его "Claude"
# 2. Скопируй Application ID сюда
CLIENT_ID = "1559215312409464876"

# 3. В разделе Rich Presence -> Art Assets загрузи картинку и задай ей имя "claude"
LARGE_IMAGE = "claude_1024"

DETAILS = "Claude Desktop открыт"

# Фразы собираются из глаголов и объектов: 12 x 12 = 144 варианта
VERBS = [
    "Дебажит",
    "Анимирует",
    "Медитирует над",
    "Переписывает",
    "Ищет",
    "Гладит",
    "Тестирует",
    "Удаляет",
    "Перечитывает",
    "Чинит",
    "Пьёт кофе над",
    "Гуглит",
]
OBJECTS = [
    "стектрейсом",
    "код, который вчера работал",
    "изображения",
    "точку с запятой",
    "баг в проде",
    "README без картинок",
    "тесты, которые падают",
    "кэш браузера",
    "console.log",
    "чужой легаси-код",
    "пиксели в 4K",
    "конфиг на 300 строк",
]
STATES = [f"{verb} {obj}" for verb in VERBS for obj in OBJECTS]
STATES += ["Спит, пока Клод работает", "Клод работает, я сплю"]

STATE_INTERVAL = 5  # меняем фразу каждые 5 секунд


def connect():
    while True:
        try:
            rpc = Presence(CLIENT_ID)
            rpc.connect()
            return rpc
        except Exception:
            # Discord не запущен - ждём и пробуем снова
            time.sleep(10)


rpc = connect()
start_time = time.time()

while True:
    state = random.choice(STATES)
    try:
        rpc.update(
            details=DETAILS,
            state=state,
            large_image=LARGE_IMAGE,
            large_text="Claude",
            start=start_time,
        )
    except Exception:
        # Discord закрыли или перезапустили - переподключаемся
        rpc = connect()
        continue
    time.sleep(STATE_INTERVAL)
