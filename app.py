from flask import Flask
from vkbottle import Bot
from token_1 import token
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
bot = Bot(token=token)  # Замените на свой токен

# Функция, которая будет вызываться каждые 5 минут
def send_request():
    print("Отправляю запрос в ВК...")
    # Пример: отправка сообщения себе
    bot.api.messages.send(user_id=819016396, message="Проверка работы бота!", random_id=0)

# Настройка периодического выполнения
scheduler = BackgroundScheduler()
scheduler.add_job(send_request, 'interval', minutes=5)
scheduler.start()

# Маршрут для Flask (проверка работы сервера)
@app.route('/')
def home():
    return "Flask + VKBottle бот работает!\nНаш бот: https://vk.com/rodrigobot \nВладелец: https://vk.com/deniska_bisekeev"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
