from typing import Any, Dict
from vkbottle import Keyboard, GroupEventType, GroupTypes, KeyboardButtonColor, Text, Callback, GroupEventType, GroupTypes, BaseStateGroup, CtxStorage, ShowSnackbarEvent,  PhotoMessageUploader
from vkbottle.bot import  Message, MessageEvent
import os, json, random
from token_1 import token
import os
from vkbottle import Bot, Callback
import os
import json 
import requests
from io import BytesIO
from PIL import Image
from vkbottle.bot import rules
from vkbottle_types.objects import PhotosPhoto
from vkbottle.bot import Message, rules
from vkbottle_types.objects import MessagesKeyboard, MessagesKeyboardButton
import datetime
from datetime import date, timedelta, time, datetime
import time
from typing import List, Dict, Tuple
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import humanize, flask
from vkbottle.api import API
from vkbottle import Bot, PhotoMarketUploader, template_gen, TemplateElement
import asyncio
from flask import Flask, request, jsonify
def format_time(type, seconds):
    if type == 'час-минута-секунда':
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02d} часов {minutes:02d} минут {seconds:02d} секунд"
    if type == 'минута-секунда':
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{minutes:02d} минут {seconds:02d} секунд"
    

async def edit_message(peer_id, message_id, newtext=None, keyboard=None, attachment=None):
    await bot.api.messages.edit(
        peer_id=peer_id,
        conversation_message_id=message_id,
        message=newtext,
        keyboard=keyboard,
        attachment=attachment
    )


from flask import Flask, request
from vkbottle import Bot

app = Flask(__name__)

CONFIRMATION_CODE = "e4a9143e"  # Тот самый код из настроек Callback API

@app.route('/callback', methods=['POST', 'GET'])
def callback():
    if request.method == 'GET':
        # Подтверждение сервера
        return CONFIRMATION_CODE
    else:
        # Обработка событий от ВК
        data = request.json
        print(data)  # Для отладки
        return jsonify({"ok": True})
    



primary = KeyboardButtonColor.PRIMARY
positive = KeyboardButtonColor.POSITIVE
negative = KeyboardButtonColor.NEGATIVE
secondary = KeyboardButtonColor.SECONDARY


bot = Bot(token=token)
api = API(token=token)


photo_uploader = PhotoMessageUploader(bot.api)
def kazino_numbers(number):
    if number == 0:
        photo = 'photo-230806544_457239110'
    elif number == 1:
        photo = 'photo-230806544_457239072'
    elif number == 2:
        photo = 'photo-230806544_457239073'
    elif number == 3:
        photo = 'photo-230806544_457239074'
    elif number == 4:
        photo = 'photo-230806544_457239075'
    elif number == 5:
        photo = 'photo-230806544_457239076'
    elif number == 6:
        photo = 'photo-230806544_457239077'
    elif number == 7:
        photo = 'photo-230806544_457239078'
    elif number == 8:
        photo = 'photo-230806544_457239079'
    elif number == 9:
        photo = 'photo-230806544_457239080'
    elif number == 10:
        photo = 'photo-230806544_457239081'
    elif number == 11:
        photo = 'photo-230806544_457239082'
    elif number == 12:
        photo = 'photo-230806544_457239083'
    elif number == 13:
        photo = 'photo-230806544_457239084'
    elif number == 14:
        photo = 'photo-230806544_457239085'
    elif number == 15:
        photo = 'photo-230806544_457239086'
    elif number == 16:
        photo = 'photo-230806544_457239087'
    elif number == 17:
        photo = 'photo-230806544_457239088'
    elif number == 18:
        photo = 'photo-230806544_457239089'
    elif number == 19:
        photo = 'photo-230806544_457239090'
    elif number == 20:
        photo = 'photo-230806544_457239091'
    elif number == 21:
        photo = 'photo-230806544_457239092'
    elif number == 22:
        photo = 'photo-230806544_457239093'
    elif number == 23:
        photo = 'photo-230806544_457239094'
    elif number == 24:
        photo = 'photo-230806544_457239095'
    elif number == 25:
        photo = 'photo-230806544_457239096'
    elif number == 26:
        photo = 'photo-230806544_457239097'
    elif number == 27:
        photo = 'photo-230806544_457239098'
    elif number == 28:
        photo = 'photo-230806544_457239099'
    elif number == 29:
        photo = 'photo-230806544_457239100'
    elif number == 30:
        photo = 'photo-230806544_457239101'
    elif number == 31:
        photo = 'photo-230806544_457239102'
    elif number == 32:
        photo = 'photo-230806544_457239109'
    elif number == 33:
        photo = 'photo-230806544_457239104'
    elif number == 34:
        photo = 'photo-230806544_457239105'
    elif number == 35:
        photo = 'photo-230806544_457239106'
    elif number == 36:
        photo = 'photo-230806544_457239107'
    return photo
def go_money(money) -> int:
    money = humanize.intcomma(money).replace(',', ' ')
    return money
async def resolve_resources(pattern: str) -> int:
    user_id = None
    if "[id" in pattern:
        user_id = int(pattern.split("|")[0].replace("[id", ""))
    elif "vk.com/" in pattern:
        user_id = pattern.split("/")[-1]
    elif "https://" in pattern:
        user_id = pattern.split("/")[3]
    else:
        user_id = pattern

    user = await bot.api.users.get(user_ids=user_id)
    return user[0] if user else None

DB_PATH = Path("users_db.json")
DB_PATH2 = Path("clans.json")

# Загрузка базы данных из JSON
def load_db() -> dict:
    if not DB_PATH.exists():
        return {}
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# Сохранение базы данных в JSON
def save_db(db: dict):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=4)

def load_db_clans() -> dict:
    if not DB_PATH.exists():
        return {}
    with open(DB_PATH2, "r", encoding="utf-8") as f:
        return json.load(f)

# Сохранение базы данных в JSON
def save_db_clans(db: dict):
    with open(DB_PATH2, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=4)
# Проверка, зарегистрирован ли пользователь
def is_user_registered(user_id: int) -> bool:
    db = load_db()
    return str(user_id) in db
def get_balance_top(limit: int = 10) -> List[Tuple[str, Dict]]:
    db = load_db()
    
    # Получаем всех пользователей и фильтруем тех, у кого есть баланс
    users = [(user_id, user_data) for user_id, user_data in db.items() 
             if isinstance(user_data, dict) and 'balance' in user_data]
    
    # Сортируем по балансу (по убыванию)
    users.sort(key=lambda x: x[1]['balance'], reverse=True)
    
    return users[:limit]

def get_tiktok_top(limit: int = 10) -> List[Tuple[str, Dict]]:
    db = load_db()
    
    # Получаем всех пользователей и фильтруем тех, у кого есть баланс
    users = [(user_id, user_data) for user_id, user_data in db.items() 
            if isinstance(user_data, dict) and 'tiktok_subs' in user_data['tiktok_stats']]
    
    # Сортируем по балансу (по убыванию)
    users.sort(key=lambda x: x[1]['tiktok_stats']['tiktok_subs'], reverse=True)
    
    return users[:limit]
def get_piska_top(limit: int = 10) -> List[Tuple[str, Dict]]:
    
    db = load_db()
    
    # Получаем всех пользователей и фильтруем тех, у кого есть баланс
    users = [(user_id, user_data) for user_id, user_data in db.items() 
             if isinstance(user_data, dict) and 'piska' in user_data]
    
    # Сортируем по балансу (по убыванию)
    users.sort(key=lambda x: x[1]['piska'], reverse=True)
    
    return users[:limit]

def get_clan_kubki_top(limit: int = 4) -> List[Tuple[str, Dict]]:
    db = load_db_clans()
    clans = [(clan_id, clan_data) for clan_id, clan_data in db.items()
            if isinstance(clan_data, dict) and 'kubki' in clan_data]
    clans.sort(key=lambda x: x[1]['kubki'], reverse=True)
    return clans[:limit]

def get_clan_money_top(limit: int = 4) -> List[Tuple[str, Dict]]:
    db = load_db_clans()
    clans = [(clan_id, clan_data) for clan_id, clan_data in db.items()
            if isinstance(clan_data, dict) and 'money' in clan_data]
    clans.sort(key=lambda x: x[1]['money'], reverse=True)
    return clans[:limit]

def get_user_rank(user_id: int) -> int:
    
    top_users = get_balance_top(limit=1000)  # Берем большой лимит чтобы найти пользователя
    user_id = str(user_id)
    
    for index, (uid, _) in enumerate(top_users, 1):
        if uid == user_id:
            return index
    
    return '999+'

bot.labeler.vbml_ignore_case = True
def parse_amount(money: str, user_id: str = None) -> int:
    if not money or money.lower() == 'вб':
        if not user_id:
            return 0
        db = load_db()
        user = db.get(str(user_id))
        return user['balance'] if user else 0

    money = money.lower().replace(',', '.').replace(' ', '')

    # Разделяем число и множитель
    num_part = ''
    mult_part = ''
    
    for char in money:
        if char.isdigit() or char in {'.', '-'}:
            num_part += char
        else:
            mult_part += char.lower()

    if not num_part:
        return 0

    try:
        number = float(num_part)
    except ValueError:
        return 0

    # Определяем множитель
    multiplier = 1
    if mult_part:
        multipliers = {
            'к': 10**3,
            'кк': 10**6,
            'м': 10**6,
            'мк': 10**9,
            'мм': 10**12,
            'ммк': 10**15,
            'ккк': 10**9,
            'кккк': 10**12,
            'ккккк': 10**15,
            'т': 10**12,
            'трлн': 10**12,
            'а': 10**18,
            'аа': 10**36
        }
        
        # Проверяем все возможные комбинации
        for k in sorted(multipliers.keys(), key=len, reverse=True):
            if mult_part.startswith(k):
                multiplier = multipliers[k]
                break

    return int(number * multiplier)
# Обработчик сообщений
@bot.on.private_message(text=["Регистрация", "регистрация", "начать"])
async def register_handler(message: Message):
    user_id = message.from_id
    if is_user_registered(user_id):
        await message.answer("Вы уже зарегистрированы!")
        return

    # Получаем информацию о пользователе
    user_info = await bot.api.users.get(user_ids=user_id)
    username = f"{user_info[0].first_name} {user_info[0].last_name}"

    db = load_db()
    db[str(user_id)] = {
        'username': f'{username}',
        'balance': 100000000000,
        "bts": 0,
        'level': 1,
        "car": "Нет",
        'clan': 'Нет',
        'id_clan': 0,
        'inventory': [],
        'registred': True,
        'registered_at': f'{date.today()}',
        'banned': False,
        'piska': 0,
        'tiktok': "Нет",
        'status': 'player',
        'vip': 'Нет',
        'invite_status': False,
        'id_clan_to': 0,
        'role': 0,
        'stats': {
            'casino_wins': 0,
            'casino_losses': 0,
            'steals_success': 0,
            'steals_failed': 0,
            'tiktoks_made': 0,
            "last_piska": 0,
            "last_seyf": 0,
            "last_doors": 0,
            "last_vzlom": 0,
            "last_steal": 0,
            "last_pensia": 0,
            "skins_id": [],
            "audio": None,
            'points': 0,
            "замес": [],
            "кости": [],
            "taksi": False,
            "fish": False,
            "gruz": False,
            },
        'tiktok_stats': {
            'tiktok_kd': 3600,
            'tiktok_subs': 0,
            'tiktok_tosubs': 0,
            'tiktok_date': None,
            "last_tiktok": 0,
            "tiktok_views": 0
        },
        "farm": {
                "income": 0,
                "level": 0,
                "last_income": 0,
                "next_level": 0,
                "bank": 0
            }
            
            }
            
    
    save_db(db)
    await message.answer(f"✅ Регистрация прошла успешно, {username}! \nТакже ты получил бонус в виде 100мк!💸")
    await menu(message)
uploader = PhotoMessageUploader(api)
@bot.on.chat_message(text='регистрация')
async def no_reg_sorry(message: Message):
    user_id = message.from_id
    db = load_db()
    if db[str(user_id)]['registred'] == True:
        await message.answer('Вы уже зарегистрированы!')
    else:
        await message.answer('Регистрация возможна только в лс бота!')
@bot.on.message(text=['я', 'проф', 'профиль', 'стата', '/я'])
async def prof(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    username = db[str(message.from_id)]['username']
    if db[str(message.from_id)]['banned'] == True:
        await message.answer("🤡 Вы заблокированы в боте! Ожидайте разблокировки, чтобы снова играть в бота.")
    if db[str(message.from_id)]['banned'] == False:
        if user['vip'] == 'Нет':
            pr = f'👤 Профиль @id{message.from_id}({username}): \n'
            pr += f'\n'
            pr += f'💸 Баланс: {"{:,}".format(user['balance']).replace(',', ' ')}$\n'
            pr += f'🍌 Писька: {user['piska']}\n'
            pr += f'🏡 Клан: {user['clan']}\n'
            pr += f'🎥 Тикток: {user['tiktok']}\n'
            pr += f'📆 Дата регистрации: {user['registered_at']}\n\n'
        else:
            pr = f'👤 Профиль @id{message.from_id}({username}): \n'
            pr += f'PREMIUM 💎\n'
            pr += f'💸 Баланс: {"{:,}".format(user['balance']).replace(',', ' ')}$\n'
            pr += f'🍌 Писька: {user['piska']}\n'
            pr += f'🏡 Клан: {user['clan']}\n'
            pr += f'🎥 Тикток: {user['tiktok']}\n'
            pr += f'📆 Дата регистрации: {user['registered_at']}\n\n'
        if user['status'] == 'moder':
            pr += '👺 Модератор'
        if user['status'] == 'gl.moder':
            pr += '👺 Главный Модератор'
        if user['status'] == 'zam':
            pr += '👺 Заместитель основателя'
        if user['status'] == 'owner':
            pr += '👺 Основатель бота'
        if user['stats']['audio'] != None:
            audio_attachment = f"audio{user['stats']['audio']['owner_id']}_{user['stats']['audio']['id']}"
        else:
            audio_attachment = None

        if user['level'] == 1:
            await message.answer(pr, attachment=["photo-230806544_457239021", audio_attachment], disable_mentions=True)
            #обычный
        if user['level'] == 2:
            await message.answer(pr, attachment=["photo-230806544_457239022", audio_attachment], disable_mentions=True)
            #светлый нефор
        if user['level'] == 3:
            await message.answer(pr, attachment=["photo-230806544_457239023", audio_attachment], disable_mentions=True)
            #чёрный нефор
        if user['level'] == 4:
            await message.answer(pr, attachment=["photo-230806544_457239024", audio_attachment], disable_mentions=True)
            #чёрная кепка
        if user['level'] == 5:
            await message.answer(pr, attachment=["photo-230806544_457239025", audio_attachment], disable_mentions=True)
            #gold anonymous
        if user['level'] == 6:
            await message.answer(pr, attachment=["photo-230806544_457239032", audio_attachment], disable_mentions=True)
            #скинруана
        if user['level'] == 7:
            await message.answer(pr, attachment=["photo-230806544_457239031", audio_attachment], disable_mentions=True)
            #скин месси
            
@bot.on.message(text='+аудио')
async def audio(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    audio = message.attachments[0].audio
    if user['vip'] == 'Нет':
        await message.answer('Данная функция доступна только пользователям с VIP подпиской')
    else:
        # Сохраняем в переменную (можно сохранять ссылку или metadata)
        user['stats']['audio'] = {
        'owner_id': audio.owner_id,
        'id': audio.id,
        'artist': audio.artist,
        'title': audio.title
    }
        save_db(db)
        await message.answer("✅ Аудио сохранено!")

@bot.on.message(text='-аудио')
async def no_audio(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    if user['vip'] == 'Нет':
        await message.answer('Данная функция доступна только пользователям с VIP подпиской!')
    else:
        await message.answer('✅ Аудио успешно удалено!')
        user['stats']['audio'] = None
        save_db(db)

@bot.on.message(text=['казино <bet_type> <money>', 'рулетка <bet_type> <money>', 'рул <bet_type> <money>'])
async def kazino(message: Message, bet_type: str = None, money: str = None):
    db = load_db()
    user_id = str(message.from_id)
    user = db.get(user_id)
    
    if not user:
        await message.answer("❌ Пользователь не найден!")
        return

    amount = parse_amount(money, user_id=user_id)
    if amount <= 0:
        await message.answer("❌ Неверная сумма ставки!")
        return

    if user['balance'] < amount:
        await message.answer("❌ Недостаточно средств на балансе!")
        return

    # Генерация выигрышного числа
    win_num = random.randint(0, 36)
    black_numbers = {2, 4, 6, 7, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35 }
    is_black = win_num in black_numbers
    is_even = win_num % 2 == 0 if win_num != 0 else False  # 0 — ни чётный, ни нечётный
    photo = kazino_numbers(win_num)
    # Определение выигрыша
    multiplier = 1
    

    bet_type = bet_type.lower()
    if bet_type in ['чёрное', 'черное', 'чёр', 'чер']:
       
        multiplier = 2 if is_black else 1

    elif bet_type in ['красное', 'крас']:
        multiplier = 2 if not is_black else 1

    elif bet_type == 'чёт' or bet_type == 'чет':
        
        multiplier = 2 if is_even else 1

    elif bet_type == 'нечёт' or bet_type == 'нечет':
        
        multiplier = 2 if not is_even else 1

    elif bet_type == '1-12':
        
        multiplier = 3 if 1 <= win_num <= 12 else 1

    elif bet_type == '12-24':
        
        multiplier = 3 if 12 <= win_num <= 24 else 1

    elif bet_type == '24-36':
        multiplier = 3 if 24 <= win_num <= 36 else 1

    elif bet_type == '0':
        multiplier = 36 if win_num == 0 else 1

    elif bet_type.isdigit() and 0 <= int(bet_type) <= 36:
        if win_num == int(bet_type):
            multiplier = 14

    if bet_type is None:
        await message.answer(
            "❌ Неправильный тип ставки! Доступные варианты:\n\n"
            "• Красное/Чёрное (х2)\n"
            "• Чёт/Нечёт (х2)\n"
            "• 1-12/12-24/24-36 (х3)\n"
            "• 0 (х36)\n"
            "• Конкретное число (1-36, х14)\n\n"
            "🎰 Пример: «казино чёт 100к» или  «рул 12-24 вб»"
        )
        return

    # Обновление баланса
    if multiplier > 1:
        win_amount = amount * multiplier
        user['balance'] += win_amount
        result = f"\n🥳 Вы выиграли {go_money(win_amount)}$!(x{multiplier})"
        user['stats']['casino_wins'] += 1
    else:
        user['balance'] -= amount
        result = f"\n😭 Вы проиграли {go_money(amount)}!$ (x0)"
        user['stats']['casino_losses'] += 1

    result += f"\n💸 Баланс: {go_money(user['balance'])}"
    save_db(db)
    await message.answer(result, attachment=photo)
    
   

@bot.on.message(text='тт создать <name>')
async def create_tiktok(message: Message, name: str = None):
    db = load_db()
    user = db[str(message.from_id)]
    if user['tiktok'] == 'Нет':
        if name != None:
            await message.answer(f'✅ {user['username']}, ты создал свой тикток под названием: {name}')
            user['tiktok'] = f'{name}'
            user['tiktok_stats']['tiktok_date'] = f'{date.today()}'
            user['tiktok_stats']['tiktok_subs_persons'] = []
            user['tiktok_stats']['tiktok_tosubs_persons'] = []

            save_db(db)
        if name == None:
            await message.answer('❌ Не правильно! тт создать (текст)')

    if user['tiktok'] != 'Нет':
        await message.answer('❌ У тебя уже есть аккаунт в тиктоке! Если тебе не нравится название, то переименуй его командой: тт имя (текст)')
@bot.on.message(text='тт имя <name>')
async def recreate_tiktok(message: Message, name: str = None):
    db = load_db()
    user = db[str(message.from_id)]
    if user['tiktok'] != 'Нет':
        if name == None:
            await message.answer('❌ Не так! тт имя (текст)')
        if name != None:
            await message.answer('✅ Ты успешно поменял название своего аккаунта в тиктоке!')
            user['tiktok'] = f'{name}'
            save_db(db)
    if user['tiktok'] == 'Нет':
        if name != None:
            await message.answer('😊 У тебя нет аккаунта в тиктоке! Но сегодня я добрый и создал сам тебе аккаунт)')
            user['tiktok'] = f'{name}'
            user['tiktok_stats']['tiktok_date'] = f'{date.today()}'
            save_db(db)



@bot.on.message(text='тт снять')
@bot.on.message(payload={'tiktok': 'create'})
async def create_video(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    if user['tiktok'] == 'Нет':
        await message.answer('❌ У тебя нет аккаунта в тиктоке!')
    if user['tiktok'] != 'Нет':
        now = int(time.time())
        if now - user['tiktok_stats']["last_tiktok"] < 3600:
            wait_time = 3600 - (now - user['tiktok_stats']['last_tiktok'])
            formatted = format_time('час-минута-секунда', wait_time)
            await message.answer(f"⏳ Вы можете снять следующее видео через {formatted}!")
            return
    
        else:
            if user['tiktok_stats']['tiktok_subs'] == 0:
                earnings = random.randint(100000000000, 200000000000)
            else:
                earnings = (random.randint(100000000000, 200000000000)*(user['tiktok_stats']['tiktok_subs']))/2
            
            user['tiktok_stats']["last_tiktok"] = now
            rand = random.randint(20,100)
            if user['vip'] != 'Нет':
                rand = rand * 2
                earnings = earnings * 2
            user['tiktok_stats']['tiktok_views'] += rand
            user['balance'] += earnings
            save_db(db)

            await message.answer(
                f"📱 Вы сняли видео в TikTok и заработали {go_money(earnings)} монет!\n"
                f"💰 Теперь ваш баланс: {go_money(user['balance'])}\n"
                f"👀 Просмотры: {rand} \n\n"
                f"⏳ Следующее видео можно будет снять через 1 час"
            )

@bot.on.message(text=['тт', 'тикток'])
async def tiktok(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    if user['tiktok'] == 'Нет':
        await message.answer('❌ У тебя нет тиктока!')
    if user['tiktok'] != 'Нет':
        pr = f'👤 Тикток @id{message.from_id}({user['username']})\n'
        pr += '\n'
        pr += f'🔥 Название: {user['tiktok']}\n'
        pr += f'👥 Подписчики: {user['tiktok_stats']['tiktok_subs']}\n'
        pr += f'🧸 Подписки: {user['tiktok_stats']['tiktok_tosubs']}\n'
        pr += f'👀 Просмотры: {user['tiktok_stats']['tiktok_views']}\n'
        pr += f'📆 Создан: {user['tiktok_stats']['tiktok_date']}\n'
        keyboard = (Keyboard(inline=True)
        .add(Text('📸 Снять видео', payload={'tiktok': 'create'}), color=KeyboardButtonColor.POSITIVE)
        ).get_json()
        await message.answer(pr, keyboard=keyboard)


@bot.on.message(text='кик <mention>')
async def kick(message: Message, mention: str = None):
    db = load_db()
    user = db[str(message.from_id)]
    target_id = await resolve_resources(mention)
    if user['status'] not in ['admin', 'owner', 'zam', 'moder', 'gl.moder']:
        await message.answer('❌ Данная команда вам не доступна!')
    if user['status'] in ['admin', 'owner', 'zam', 'moder', 'gl.moder']:
        if mention != None:
            try:
                await bot.api.messages.remove_chat_user(message.chat_id, target_id.id)
                await message.answer(f'✅ @id{target_id.id}(Пользователь) кикнут из чата.')
            except:
                await message.answer('❌Введите корректную ссылку или упоминание!')
        if message.reply_message:
            try:
                await bot.api.messages.remove_chat_user(message.chat_id, message.reply_message.from_id)
                await message.answer(f'✅ @id{message.reply_message.from_id}(Пользователь) кикнут из чата.')
            except:
                await message.answer('❌ Перешлите сообщение или укажите упоминание, чтобы я кикнул юзера.')
@bot.on.message(text='клан создать <name>')
async def create_clan(message: Message, name: str = None):
    db = load_db()
    db_clan = load_db_clans()

    user = db[str(message.from_id)]

    if user['clan'] != 'Нет':
        await message.answer('❌ У вас уже есть клан, выйдите из него или удалите.')
    else:
        if user['balance'] < 10000000000000:
            await message.answer('❌ Создать клан стоит 10мм$')
        if user['balance'] >= 10000000000000:
            if name == None:
                await message.answer('❌ Не так! клан создать (текст)')
            if name != None:
                if len(name) > 15:
                    await message.answer('❌ Название не должно превышать 15 символов!')
                if len(name) <= 15:
                    await message.answer(f'✅ Вы успешно создали клан под названием "{name}"')
                    id = db['819016396']['ids_clans'] = db['819016396']['ids_clans'] + 1
                    user['clan'] = f'{name}'
                    db_clan[str(id)] = {
                        'users': 1,
                        'kubki': 0,
                        'money': 0,
                        'leader': f'{message.from_id}',
                        'last_reyd': 0,
                        'nickname': f'{user['username']}',
                        'clan': f'{name}',
                        'role': 'Лидер',
                        'users_ids': [f"{message.from_id}"],
                        'max_users': 50,
                        'photo': None,
                        'level': [],
                        'photo': None
                    }
                    user['balance'] = user['balance'] - 10000000000000
                    user['id_clan'] = f'{id}'
                    user['role'] = 'Лидер'
                    save_db(db)
                    save_db_clans(db_clan)

@bot.on.message(text=['клан приглос', 'клан приглос <mention>'])
async def priglos(message: Message, mention: str):
    if message.reply_message:
        touser = message.reply_message.from_id
    else:
        touser1 = await resolve_resources(mention)
        touser = touser1.id
    db = load_db()
    db_clan = load_db_clans()
    user = db[str(message.from_id)]
    if user['clan'] != 'Нет':
        if user['role'] in ['Лидер', 'Заместитель']:
            user2 = db[str(touser)]
            
            if mention != None:    
                if user2['clan'] != 'Нет':
                    await message.answer('❌ Пользователь в вашем клане или в другом клане!')
                if user2['clan'] == 'Нет':
                    id_clan = user['id_clan']
                    if db_clan[id_clan]['users'] == db_clan[id_clan]['max_users']:
                        await message.answer('❌ В вашем клане не хватает мест!')
                    if db_clan[id_clan]['users'] < db_clan[id_clan]['max_users']:
                        await message.answer('✅ Приглашение пользователю отправлено!')
                        keyboard = (Keyboard(inline=True).add(Callback('✅', payload={'clan': id_clan}), color=KeyboardButtonColor.POSITIVE)
                                    .add(Callback('❌', payload={'clan_no': id_clan}), color=negative)
                                    ).get_json()
                        await bot.api.messages.send(user_id=touser, message=f'Вас пригласили в клан "{user['clan']}"', keyboard=keyboard, random_id=0)
                        save_db(db)
                        save_db_clans(db_clan)
            if message.reply_message:
                user2 = db[str(message.reply_message.from_id)]
                if user2['clan'] != 'Нет':
                    await message.answer('❌ Пользователь в вашем клане или в другом клане!')
                if user2['clan'] == 'Нет':
                    id_clan = user['id_clan']
                    if db_clan[id_clan]['users'] == db_clan[id_clan]['max_users']:
                        await message.answer('❌ В вашем клане не хватает мест!')
                    if db_clan[id_clan]['users'] < db_clan[id_clan]['max_users']:
                        await message.answer('✅ Приглашение пользователю отправлено!')
                        keyboard = (Keyboard(inline=True).add(Callback('✅', payload={'clan': id_clan}), color=KeyboardButtonColor.POSITIVE).add(Callback('❌', payload={'clan_no': 'disinvite'}), color=KeyboardButtonColor.NEGATIVE)).get_json()
                        await bot.api.messages.send(user_id=message.reply_message.from_id, message=f'Вас пригласили в клан "{user['clan']}"', keyboard=keyboard, random_id=0)
                        save_db(db)
                        save_db_clans(db_clan)
           
        else:
            await message.answer('❌ Вы не являетесь лидером или заместителем клана!')
    else:
        await message.answer('❌ У вас нет клана!')
        



@bot.on.message(text='клан')
async def clan(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    if user['clan'] == 'Нет':
        await message.answer('❌ У вас нет клана!')
    if user['clan'] != 'Нет':
        clan = load_db_clans()
        clan2 = user['id_clan']
        clan_user = clan[clan2]
        members = []
        for member_id in clan_user['users_ids']:
            member = db[str(member_id)]
            if member:
                members.append(f'@id{member_id}({member['username']})')
        
        if clan_user['photo'] != None:
            photo_url = clan_user["photo"]
            response = requests.get(photo_url)
            img_bytes = BytesIO(response.content)

            # Используем PhotoMessageUploader для загрузки
            uploader = PhotoMessageUploader(bot.api)
            photo = await uploader.upload(img_bytes)
        else:
            photo = None 
        

        pr = f'🏡 Профиль клана {user['clan']}\n'
        pr += f'\n'
        pr += f'👑 Лидер: @id{clan_user['leader']}({clan_user['nickname']})\n'
        pr += f'🏆 Кубки: {clan_user['kubki']}\n'
        pr += f'💰 Казна: {go_money(clan_user['money'])}\n'
        pr += f'👥 Участников: {clan_user['users']}/{clan_user['max_users']}\n'
        pr += f'🛡️ Роль: {user['role']}\n'
        pr += f'Участники:\n'
        pr += f'\n'.join(members)
        await message.answer(pr, attachment=photo ,disable_mentions = True)


@bot.on.message(text='give <role>')
async def give_role(message: Message, role: str = None):
    db = load_db()
    user = db[str(message.from_id)]
    user_to = db[str(message.reply_message.from_id)]
    if user['status'] in ['owner', 'zam', 'gl.moder']:
        if user_to['status'] in ['owner']:
            await message.answer('Этому человеку нельзя менять статус.')
        if user['status'] == 'owner':
            await message.answer('Вы успешно поменяли юзеру роль')
            user_to['status'] = f'{role}'
        if user['status'] == 'zam' and user_to['status'] not in ['owner', 'zam']:
            await message.answer('Вы успешно поменяли роль юзеру')
            user_to['status'] = f'{role}'
        if user['status'] not in ['owner', 'zam', 'gl.moder']:
            await message.answer('Вы не можете менять роль юзерам!')
    else:
        await message.answer('У вас нет полномочий менять роль юзерам!')
    save_db(db)

@bot.on.message(text='клан рейд')
async def reyd(message: Message):
    db = load_db()
    db_clan = load_db_clans()
    user = db[str(message.from_id)]
    id_clan = user['id_clan']
    if user['clan'] == 'Нет':
        await message.answer('У вас нет клана!')
    if user['clan'] != 'Нет':
        now = int(time.time())
        if "3" in db_clan[id_clan]['level']:
            num = 300
        else:
            num = 600
        if now - db_clan[id_clan]["last_reyd"] < num:
            wait_time = num - (now - db_clan[id_clan]['last_reyd'])
            formatted = format_time('час-минута-секунда', wait_time)
            await message.answer(f"⏳ Вы можете рейдить через {formatted}!")
            return
        else:
            rand = random.choice(["выигрыш", "проигрыш", "ничья", "выигрыш", "проигрыш"])

            potential_victims = [
            uid for uid, u in db_clan.items()
            if uid != user['id_clan']]
        
            if not potential_victims:
                await message.answer("Нет подходящих кланов для рейда.")
            
            victim_id = random.choice(potential_victims)
            victim = db_clan[victim_id]['clan']
            victim_owner_id = db_clan[victim_id]['leader']
            id_clan = user['id_clan']
            db_clan[id_clan]["last_reyd"] = now

            if rand == "выигрыш":
                rand1 = random.randint(1,3)
                if "2" in db_clan[id_clan]['level']:
                    rand1 = rand1 * 2
                    score = f'{rand1} (x2)'
                else:
                    score = f'{rand1}'
                await message.answer(f'Вы зарейдили клан "{victim}" и получили {score} кубков.')
                db_clan[id_clan]['kubki'] += rand1
                await bot.api.messages.send(user_id=victim_owner_id, message=f'Ваш клан зарейдил клан "{user['clan']}" и вы потеряли {score} кубков.', random_id=0)
                db_clan[victim_id]['kubki'] -= rand1
            if rand == "проигрыш":
                rand1 = random.randint(1,3)
                await message.answer(f'Попытка зарейдить клан "{victim}" провалилась! Вы потеряли {rand1} кубков.')
                db_clan[id_clan]['kubki'] -= rand1
                db_clan[victim_id]['kubki'] += rand1
                await bot.api.messages.send(user_id=victim_owner_id, message=f'Попытка зарейдить ваш клан кланом "{user['clan']}" провалилась! Вы получили {rand1} кубков.', random_id=0)
            if rand == "ничья":
                await message.answer(f'Вы зарейдили клан "{victim}" и между вами ничья! Вы ничего не потеряли.')
                await bot.api.messages.send(user_id=victim_owner_id, message=f'Ваш клан зарейдил клан "{user['clan']}" и между вами ничья! Вы ничего не потеряли.', random_id=0)
        save_db_clans(db_clan)

@bot.on.message(text='рандом клан')
async def rand_clan(message: Message):
    db = load_db()
    db_clan = load_db_clans()
    user = db[str(message.from_id)]
    id_clan = user['id_clan']
    potential_victims = [
            uid for uid, u in db_clan.items() 
            if u != user['id_clan']]
    victim_id = random.choice(potential_victims)
    victim_owner_id = db_clan[victim_id]['leader']
    victim_owner_name = db[victim_owner_id]['username']

    await message.answer(f'Айди клана: {victim_id}\n'
                         f'Айди лидера: {victim_owner_id}\n'
                         f'Имя лидера: {victim_owner_name}'
                         )


@bot.on.message(text='тт подписаться <mention>')
async def sub(message: Message, mention: str = None):
    db = load_db()
    user = db[str(message.from_id)]
    if user['tiktok'] == 'Нет':
        await message.answer('У вас нет тиктока!')
    else:
        if message.reply_message:
            id_to = message.reply_message.from_id
        else:
            id_to = await resolve_resources(mention)
        
        user_to = db[str(id_to.id)]
        if user_to['tiktok'] == 'Нет':
            await message.answer('У юзера нет тиктока!')
        else:
            if f'{message.from_id}' in user_to['tiktok_stats']['tiktok_subs_persons']:
                await message.answer('Вы уже подписаны на него.')
            else:
                user_id = str(message.from_id)
                user_to_id = str(id_to.id)
                if user_id in user_to['tiktok_stats']['tiktok_subs_persons'] or message.from_id == id_to.id:
                    await message.answer(f'Вы уже подписаны на этого @id{id_to.id}(юзера)!')
                else:
                    # Увеличиваем счётчик подписчиков у пользователя, на которого подписываются
                    user_to["tiktok_stats"]["tiktok_subs"] += 1

                    # Добавляем user_id в список подписчиков (если список не существует, создаём его)
                    if "tiktok_subs_persons" not in user_to["tiktok_stats"]:
                        user_to["tiktok_stats"]["tiktok_subs_persons"] = []
                    user_to["tiktok_stats"]["tiktok_subs_persons"].append(user_id)

                    # Увеличиваем счётчик подписок у текущего пользователя
                    user["tiktok_stats"]["tiktok_tosubs"] += 1

                    # Добавляем user_to_id в список подписок (если список не существует, создаём его)
                    if "tiktok_tosubs_persons" not in user["tiktok_stats"]:
                        user["tiktok_stats"]["tiktok_tosubs_persons"] = []
                    user["tiktok_stats"]["tiktok_tosubs_persons"].append(user_to_id)
                    await message.answer(f'Вы подписались на тикток @id{id_to.id}(юзера)', disable_mentions=True)
                    await bot.api.messages.send(user_id=id_to.id, message=f'На ваш тикток подписался @id{message.from_id}(этот юзер)', random_id=0)
                    save_db(db)
                


@bot.on.message(text='клан помощь')
async def help_clans(message: Message):
    await message.answer('🏡 Помощь по командам связанных с кланом:\n\n'
                         '1. Клан - окно клана.\n'
                         '2. Клан рейд - рейд других кланов для получения кубков.\n'
                         '3. Клан выйти - выход из клана.\n'
                         '4. Клан создать [текст] - создать собственный клан (стоит 500.000)\n'
                         '5. Клан приглос [@username] - пригласить пользователя в клан (доступно только Лидеру и Заместителю.)\n'
                         '6. Клан кик [@username] - кикнуть пользователя из клана.\n'
                         '5. Клан вывод [деньги] - вывод денег из казны клана.\n',
                         '6. Клан герб - устанавливает герб клана.\n'
                         '7. Клан магаз - магазин кланов.'
                         )

@bot.on.message(text=['писька', 'писюн'])
async def piska(message: Message):
    db = load_db()
    user = db[str(message.from_id)]

    now = int(time.time())
    if now - int(user['stats']['last_piska']) < 1800:
        wait_time = 1800 - (now - int(user['stats']['last_piska']))
        formatted = format_time('час-минута-секунда', wait_time)
        await message.answer(f"⏳ Вы можете растить письку через {formatted}!")
    else:
        if user['vip'] != 'Нет':
            rand = (random.randint(1,6))*2
            user['piska'] += rand
            await message.answer(f'🍌 Вы вырастили письку на {rand} (x2) см!\n😎 Писька: {user['piska']} см')
        if user['vip'] == 'Нет':
            rand = random.randint(1,6)
            user['piska'] += rand
            await message.answer(f'🍌 Вы вырастили письку на {rand} см!\n😎 Писька: {user['piska']} см')
        user['stats']['last_piska'] = now
    save_db(db)

@bot.on.message(text='сейф')
async def seyf(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    now = int(time.time())
    if now - user['stats']['last_seyf'] < 3600:
        wait_time = 3600 - (now - user['stats']['last_seyf'])
        formatted = format_time('час-минута-секунда', wait_time)
        await message.answer(f"⏳ Вы можете взламывать сейф через {formatted}!")
    else:
        rand = random.randint(1,3)
        if rand == 1:
            keyboard = (Keyboard(inline=True).add(Callback('2341', payload={'seyf': '1'})).add(Callback('5901', payload={'seyf': '1'}))).get_json()
            await message.answer('🔑 Отгадайте код от сейфа.', keyboard=keyboard)
        if rand == 2:
            keyboard = (Keyboard(inline=True).add(Callback('5657', payload={'seyf': '1'})).add(Callback('8189', payload={'seyf': '1'}))).get_json()
            await message.answer('🔑 Отгадайте код от сейфа.', keyboard=keyboard)
        if rand == 3:
            keyboard = (Keyboard(inline=True).add(Callback('6273', payload={'seyf': '1'})).add(Callback('0020', payload={'seyf': '1'}))).get_json()
            await message.answer('🔑 Отгадайте код от сейфа.', keyboard=keyboard)
            
@bot.on.message(text='двери')
async def doors(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    now = int(time.time())
    if now - user['stats']['last_doors'] < 3600:
        wait_time = 3600 - (now - user['stats']['last_doors'])
        formatted = format_time('час-минута-секунда', wait_time)
        await message.answer(f"⏳ Вы можете угадывать дверь через {formatted}!")
    else:
        keyboard = (Keyboard(inline=True)
                    .add(Callback('🚪', payload={'doors': '1'}))
                    .add(Callback('🚪', payload={'doors': '1'}))
                    .add(Callback('🚪', payload={'doors': '1'}))).get_json()
        await message.answer('🚪 Попробуйте угадать дверь, за ней спрятан приз.', keyboard=keyboard)

@bot.on.message(text='взлом')
async def vzlom(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    now = int(time.time())
    if now - user['stats']['last_vzlom'] < 3600:
        wait_time = 3600 - (now - user['stats']['last_vzlom'])
        formatted = format_time('минута-секунда', wait_time)
        await message.answer(f'⏳ Вы можете взламывать через {formatted}!')
    else:
        rand = random.randint(1,2)
        if rand == 1:
            await message.answer(f'🚨 Пока ты взламывал {'Интернет магазин' or 'Сервер майнкрафта' or 'Сына маминой подруги'} тебя спалили!')
        else:
            rand2 = random.randint(3500000000000, 4000000000000)
            if user['vip'] != 'Нет':
                rand2 = rand2 * 2

            await message.answer(f'🥳 Ты успешно взломал {'Интернет магазин' or 'Сервер майнкрафта' or 'Сына маминой подруги'} и получил {humanize.intcomma(rand2)}$')
            if user['vip'] == 'Нет':
                user['balance'] += rand2
            else:
                user['balance'] += rand2 * 2
        user['stats']['last_vzlom'] = now
        save_db(db)

@bot.on.message(text='украсть <mention>')
async def steal_piska(message: Message, mention: str = None):
    db = load_db()
    user = db[str(message.from_id)]
    now = int(time.time())
    if now - user['stats']['last_steal'] < 3600:
        wait_time = 7200 - (now - user['stats']['last_steal'])
        formatted = format_time('час-минута-секунда', wait_time)
        await message.answer(f'⏳ Вы можете красть письку через {formatted}!')
    else:
        if mention != None:
            try:
                user_to = await resolve_resources(mention)
            except:
                await message.answer('Введите корректную ссылку.')
                return
            
            userto = db[str(user_to.id)]
            if userto['vip'] != 'Нет':
                await message.answer('👺 У юзера стоит защита на кражу письки!')
            else:
                if userto['piska'] < 0:
                    await message.answer('🫣 Нельзя украсть письку у данного юзера! Глубже некуда)')
                else:
                    rand = random.randint(1,5)
                    await message.answer(f'😅 Вы украли {rand} см!')
                    userto['piska'] -= rand
                    user['piska'] += rand
                    await bot.api.messages.send(user_id=user_to.id, message=f'🙄 @id{message.from_id}({user['username']}) украл у вас {rand} см письки!', random_id=0)
                user['stats']['last_steal'] = now
                save_db(db)
        elif message.reply_message:
            try:
                user_to = message.reply_message.from_id
            except:
                await message.answer('Ответьте на сообщение или напишите ссылку')
                return
            userto = db[str(user_to.id)]
            if userto['vip'] != 'Нет':
                await message.answer('👺 У юзера стоит защита на кражу письки!')
            else:
                if userto['piska'] < 0:
                    await message.answer('🫣 Нельзя украсть письку у данного юзера! Глубже некуда)')
                else:
                    rand = random.randint(1,5)
                    await message.answer(f'😅 Вы украли {rand} см!')
                    userto['piska'] -= rand
                    user['piska'] += rand
                    await bot.api.messages.send(user_id=user_to.id, message=f'🙄 @id{message.from_id}({user['username']}) украл у вас {rand} см письки!', random_id=0)
                user['stats']['last_steal'] = now
                save_db(db)

@bot.on.message(text=['топ баланс', 'топ по балансу'])
@bot.on.message(payload={'top': 'balance'})
async def show_balance_top(message: Message):
    top_users = get_balance_top(limit=10)
    db = load_db()
    
    if not top_users:
        await message.answer("📊 Топ пуст. Начните зарабатывать баланс!")
        return
    
    response = [f"🏆 Топ пользователей по балансу:\n\nВы на {get_user_rank(message.from_id)} месте\n\n"]
    
    for index, (user_id, user_data) in enumerate(top_users, 1):
        balance = user_data['balance']
        name = user_data.get('name', f'@id{user_id}({db[str(user_id)]['username']})')
        
        # Форматирование баланса (1500 → 1 500)
        formatted_balance = "{:,}".format(balance).replace(',', ' ')
        
        # Добавляем эмодзи для первых трех мест
        if index == 1:
            place_emoji = "🥇"
        elif index == 2:
            place_emoji = "🥈"
        elif index == 3:
            place_emoji = "🥉"
        else:
            place_emoji = "🔹"
        
        response.append(f"{place_emoji} {name} - {formatted_balance} $")
    
    await message.answer(f"\n".join(response), disable_mentions=True)

@bot.on.message(text=['топ тикток', 'топ по тиктоку'])
@bot.on.message(payload={'top': 'tiktok'})
async def show_tiktok_top(message: Message):
    top_users = get_tiktok_top(limit=10)
    db = load_db()
    
    if not top_users:
        await message.answer("📊 Топ пуст. Начните зарабатывать подписчиков!")
        return
    
    response = [f"🏆 Топ пользователей по подписчикам в ТТ :\n\n"]
    
    for index, (user_id, user_data) in enumerate(top_users, 1):
        tiktok = user_data['tiktok_stats']['tiktok_subs']
        name = user_data.get('name', f'@id{user_id}({db[str(user_id)]['username']})')
        
        # Форматирование баланса (1500 → 1 500)
        formatted_balance = "{:,}".format(tiktok).replace(',', ' ')
        
        # Добавляем эмодзи для первых трех мест
        if index == 1:
            place_emoji = "🥇"
        elif index == 2:
            place_emoji = "🥈"
        elif index == 3:
            place_emoji = "🥉"
        else:
            place_emoji = "🔹"
        
        response.append(f"{place_emoji} {name} - {formatted_balance} ")
    
    await message.answer(f"\n".join(response), disable_mentions=True)
@bot.on.message(text='топ клан')
@bot.on.message(payload={'top': 'clan'})
async def top_clan(message: Message):
    top_clans = get_clan_kubki_top(limit=4)
    db = load_db_clans()
    if not top_clans:
        await message.answer('📊 Топ пуст.')
        return
    response = ['🏆 Топ кланов по кубкам:\n']
    for index, (clan_id, clan_data) in enumerate(top_clans, 1):
        kubki = clan_data['kubki']
        name = clan_data.get('name', f'@id{db[str(clan_id)]['leader']}({db[str(clan_id)]['clan']})')
        
        # Форматирование баланса (1500 → 1 500)
        formatted_balance = "{:,}".format(kubki).replace(',', ' ')
        
        # Добавляем эмодзи для первых трех мест
        if index == 1:
            place_emoji = "🥇"
        elif index == 2:
            place_emoji = "🥈"
        elif index == 3:
            place_emoji = "🥉"
        else:
            place_emoji = "🔹"
        
        response.append(f"{place_emoji} {name} - {formatted_balance} шт")
    
    await message.answer("\n".join(response), disable_mentions=True)
@bot.on.message(text=['топ писька', 'топ по письке'])
@bot.on.message(payload={'top': 'piska'})
async def show_piska_top(message: Message):
    top_users = get_piska_top(limit=10)
    db = load_db()
    if not top_users:
        await message.answer("📊 Топ пуст. Начните зарабатывать письку!")
        return
    
    response = ["🏆 Топ пользователей по письке:\n"]
    
    for index, (user_id, user_data) in enumerate(top_users, 1):
        piska = user_data['piska']
        name = user_data.get('name', f'@id{user_id}({db[str(user_id)]['username']})')
        
        # Форматирование баланса (1500 → 1 500)
        formatted_balance = "{:,}".format(piska).replace(',', ' ')
        
        # Добавляем эмодзи для первых трех мест
        if index == 1:
            place_emoji = "🥇"
        elif index == 2:
            place_emoji = "🥈"
        elif index == 3:
            place_emoji = "🥉"
        else:
            place_emoji = "🔹"
        
        response.append(f"{place_emoji} {name} - {formatted_balance} см")
    
    await message.answer("\n".join(response), disable_mentions=True)

@bot.on.message(text='топ')
async def show_top(message: Message):
    keyboard = (Keyboard(inline=True)
    .add(Text('Деньги', payload={'top': 'balance'}))
    .add(Text('Кланы', payload={'top': 'clan'}))
    .row()
    .add(Text('Писька', payload={'top': 'piska'}))
    .add(Text('Тикток', payload={'top': 'tiktok'}))
    ).get_json()
    await message.answer('🙂 Какой топ вам нужен?', keyboard=keyboard)

from typing import Optional
from vkbottle.dispatch.rules import ABCRule
MUTE_DATA_PATH = Path("mute_data.json")
MUTE_DURATIONS = {
    "мьют": 60,  # 1 минута
    "мут": 60,
    "mute": 60,
    "мут1": 60,
    "мут1ч": 3600,  # 1 час
    "мутч": 3600,
    "мут1д": 86400,  # 1 день
    "мутд": 86400,
}

class IsMutedRule(ABCRule[Message]):
    async def check(self, message: Message) -> bool:
        data = load_mute_data()
        chat_id = str(message.peer_id)
        user_id = str(message.from_id)
        
        if chat_id in data and user_id in data[chat_id]:
            mute_time = datetime.fromisoformat(data[chat_id][user_id])
            return datetime.now() < mute_time
        return False

def load_mute_data() -> Dict[str, Dict[str, str]]:
    try:
        if not MUTE_DATA_PATH.exists():
            return {}
        with open(MUTE_DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_mute_data(data: Dict[str, Dict[str, str]]):
    with open(MUTE_DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_mute(chat_id: int, user_id: int, duration: int) -> datetime:
    data = load_mute_data()
    mute_end = datetime.now() + timedelta(seconds=duration)
    
    if str(chat_id) not in data:
        data[str(chat_id)] = {}
    
    data[str(chat_id)][str(user_id)] = mute_end.isoformat()
    save_mute_data(data)
    return mute_end

def remove_mute(chat_id: int, user_id: int):
    data = load_mute_data()
    chat_id = str(chat_id)
    user_id = str(user_id)
    
    if chat_id in data and user_id in data[chat_id]:
        del data[chat_id][user_id]
        save_mute_data(data)

async def cleanup_mutes():
    data = load_mute_data()
    now = datetime.now()
    changed = False
    
    for chat_id in list(data.keys()):
        for user_id in list(data[chat_id].keys()):
            if now >= datetime.fromisoformat(data[chat_id][user_id]):
                del data[chat_id][user_id]
                changed = True
        
        if not data[chat_id]:
            del data[chat_id]
            changed = True
    
    if changed:
        save_mute_data(data)

@bot.on.message(text=["/мут <user> <duration>", "/mute <user> <duration>"])
async def mute_cmd(message: Message, user: Optional[str] = None, duration: str = "60"):
    db = load_db()
    try:
        # Проверка прав
        members = await api.messages.get_conversation_members(peer_id=message.peer_id)
        admins = ['moder', 'gl.moder', 'zam', 'owner']
        
        if db[str(message.from_id)]['status'] not in admins:
            return "🚫 Недостаточно прав!"
        
        # Получаем ID цели
        target_id = None
        if message.reply_message:
            target_id = message.reply_message.from_id
        elif user and user.isdigit():
            target_id = int(user)
        elif user and "[id" in user:
            target_id = int(user.split("|")[0].replace("[id", ""))
        
        if not target_id:
            return "❌ Укажите пользователя (reply/ID/упоминание)"
        
        # Парсим длительность
        duration_sec = MUTE_DURATIONS.get(duration.lower(), None)
        if duration_sec is None:
            try:
                duration_sec = int(duration)
            except ValueError:
                return "❌ Неверная длительность. Примеры: 60, 1ч, 1д"
        
        mute_end = add_mute(message.peer_id, target_id, duration_sec)
        return f"🔇 Пользователь [id{target_id}|замьючен] до {mute_end.strftime('%d.%m.%Y %H:%M')}"
    
    except Exception as e:
        return f"⚠ Ошибка: {e}"

@bot.on.message(text=["/размут <user>", "/unmute <user>"])
async def unmute_cmd(message: Message, user: Optional[str] = None):
    db = load_db()
    try:
        # Проверка прав
        members = await api.messages.get_conversation_members(peer_id=message.peer_id)
        admins = ['moder', 'gl.moder', 'zam', 'owner']
        
        if db[str(message.from_id)]['status'] not in admins:
            return "🚫 Недостаточно прав!"
        
        # Получаем ID цели
        target_id = None
        if message.reply_message:
            target_id = message.reply_message.from_id
        elif user and user.isdigit():
            target_id = int(user)
        elif user and "[id" in user:
            target_id = int(user.split("|")[0].replace("[id", ""))
        
        if not target_id:
            return "❌ Укажите пользователя (reply/ID/упоминание)"
        
        remove_mute(message.peer_id, target_id)
        return f"🔊 Пользователь [id{target_id}|размучен]"
    
    except Exception as e:
        return f"⚠ Ошибка: {e}"

@bot.on.message(IsMutedRule())
async def mute_handler(message: Message):
        # Удаляем сообщение
        await api.messages.delete(
            peer_id=message.peer_id,
            cmids=message.conversation_message_id,
            delete_for_all=True
        )
        

async def task_cleanup():
    while True:
        await cleanup_mutes()
        await asyncio.sleep(3600)


@bot.on.private_message(text=['магазин', 'магаз', 'shop'])
async def shop_show(message: Message):
    db = load_db()
    keyboard = (Keyboard(inline=True).add(Text('👔 Одежда', payload={'shop': 'clothes'}), color=KeyboardButtonColor.POSITIVE).row().add(Text('🚘 Машины', payload={'shop': 'cars'}), color=KeyboardButtonColor.NEGATIVE).add(Text('💎 Донат', payload={'shop': 'donat'}))).get_json()
    username = db[str(message.from_id)]['username']
    await message.answer(f'🛍️ Привет, {username}, ты попал в магазин "Rodrigo"', keyboard=keyboard, attachment='photo-230806544_457239028')

@bot.on.chat_message(text=['магазин', 'магаз', 'shop'])
async def now_shop_show(message: Message):
    await message.answer('Только в лс бота')

@bot.on.private_message(payload={"shop": "clothes"})
async def show_clothes(message: Message):
    db = load_db()
    await message.answer(f'Привет, {db[str(message.from_id)]['username']} выбери себе одежду тут: vk.com/@rodrigobot-allskins')
    await message.answer('Когда выбрал, посмотри айди вещи. Чтобы купить, напиши "купить [айди вещи]"')
    
@bot.on.private_message(text='//modershop')
async def moder_shop(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    if user['status'] not in ['owner', 'zam', 'gl.moder', 'moder']:
        return
    else:
        keyboard1 = Keyboard(inline=True).add(Text('Обменять', payload={'moder_shop': 'деньги'}))
        keyboard2 = Keyboard(inline=True).add(Text('Получить', payload={'moder_shop': 'вип'}))
        keyboard3 = Keyboard(inline=True).add(Text('Сменить', payload={'moder_shop': 'ник'}))
        # Генерируем шаблон карусели
        template = template_gen(
    TemplateElement(
        buttons=keyboard1,  title = 'Деньги', description='1мм = 1 очко'
    ),
    TemplateElement(
        buttons=keyboard2,  title = 'Вип на 7 дней', description = '50 очков'
    ),
    TemplateElement(
        buttons=keyboard3,  title = 'Смена ника', description = '10 очков'
    )
)

        await message.answer(f'Ваш баланс: {user['stats']['points']} очков', template=template)
@bot.on.private_message(payload={'moder_shop': 'деньги'})
async def moder_shop_money(message: Message):
    db = load_db()
    await message.answer('Напишите: //обменять [кол-во]')
@bot.on.private_message(text='//обменять <points_to>')
async def obmen(message: Message, points_to: str = None):
    db = load_db()
    user = db[str(message.from_id)]
    points = user['stats']['points']
    try:
        points_to = int(points_to)
    except:
        await message.answer('Не могу понять сколько это..')
    if points < points_to:
        await message.answer('Не хватает очков.')
    else:
        user['stats']['points'] -= points_to
        user['balance'] += 1000000000000 * points_to
        save_db(db)
        await message.answer(f'Вы потрали {points_to}(остаток: {user['stats']['points']})\nБаланс: {go_money(user['balance'])}$')

@bot.on.private_message(payload={'moder_shop': 'вип'})
async def vip_for_moders(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    if user['stats']['points'] < 50:
        await message.answer('Вам не хватает очков.')
    else:
        await message.answer('-50 очков, обратись к @id819016396(Денису Бисекееву), чтобы получить свой вип.')
        user['stats']['points'] -= 50
        save_db(db)
        
@bot.on.message(payload={'moder_shop': 'ник'})
async def nick(message: Message):
    await message.answer('Чтобы сменить ник, напиши: //сменить ник [ник]')

@bot.on.message(text='//сменить ник <nick>')
async def change_nick(message: Message, nick: str = None):
    db = load_db()
    user = db[str(message.from_id)]
    dbc = load_db_clans()
    if user['stats']['points'] < 10:
        await message.answer('Вам не хватает очков.')
    else:
        if len(nick) > 16:
            await message.answer('Ник не должен превышать 16 символов. ')
        else:
            user['stats']['points'] -= 10
            if user['role'] != 'Лидер':
                user['username'] = nick
            else:
                id_clan = user['id_clan']
                dbc[id_clan]['nickname'] = nick
            save_db_clans(dbc)
            save_db(db)
            await message.answer('Успешно!')

@bot.on.private_message(text='купить <id_s>')
async def buy_skin(message: Message, id_s: str = None):
    db = load_db()
    user = db[str(message.from_id)]
    id = int(id_s)
    if id == None:
        await message.answer('Не так! Купить [id вещи]')
    if id == 1:
        await message.answer('Вы успешно надели этот скин на себя.')
        user['level'] = 1
    if id == 2:
        if user['balance'] >= 100000000000:
            await message.answer('Вы успешно купили этот скин!')
            user['balance'] -= 100000000000
            user['stats']['skins_id'].append("2")
        else:
            await message.answer('Вам не хватает денег!')
    if id == 3:
        if user['balance'] >= 100000000000:
            await message.answer('Вы успешно купили этот скин!')
            user['balance'] -= 100000000000
            user['stats']['skins_id'].append("3")
        else:
            await message.answer('Вам не хватает денег!')
    if id == 4:
        if user['balance'] >= 500000000000:
            await message.answer('Вы успешно купили этот скин!')
            user['balance'] -= 500000000000
            user['stats']['skins_id'].append("4")
        else:
            await message.answer('Вам не хватает денег!')
    if id == 5:
        if user['vip'] != 'Нет':
            await message.answer('Вы успешно получили этот скин!')
            user['stats']['skins_id'].append("5")
        else:
            await message.answer('Это доступно только пользователям с подпиской VIP!')
    if id == 7:
        if user['balance'] >= 10000000000000:
            await message.answer('Вы успешно купили этот скин!')
            user['balance'] -= 10000000000000
            user['stats']['skins_id'].append("7")
        else:
            await message.answer('Вам не хватает денег!')
    if id > 7:
        await message.answer('Вещь с таким айди не найдена.')
    save_db(db)
        
@bot.on.message(text='+ник <text>')
async def add_nick(message: Message, text: str = None):
    db = load_db()
    db_clan = load_db_clans()
    user = db[str(message.from_id)]
    id_clan = user['id_clan']
    
    user_clan = db_clan[id_clan]

    if user['vip'] == 'Нет':
        await message.answer('Данная команда доступна только пользователям с подпиской вип!')
    else:
        if len(text) > 15:
            await message.answer('Текст не должен превышать 15 символов!')
        if len(text) <= 16:
            await message.answer(f'Вы успешно сменили ник на: {text}')
            user['username'] = f'{text}'
            save_db(db)
            if user['role'] == 'Лидер':
                user_clan['nickname'] = f'{text}'
                save_db_clans(db_clan)


@bot.on.message(text='надеть <id_s>')
async def add_clothes_on_user(message: Message, id_s: str = None):
    db = load_db()
    user = db[str(message.from_id)]
    id = int(id_s)
    if id == None:
        await message.answer('Не так! Надеть [id вещи]')
    if id == 1:
        await message.answer('✅ Вы успешно надели этот скин')
        user['level'] = 1
    if id == 2:
        if '2' in user['stats']['skins_id']:
            await message.answer('✅ Вы успешно надели этот скин.')
            user['level'] = 2
        else:
            await message.answer('У вас нет вещи с таким айди.')
    if id == 3:
        if '3' in user['stats']['skins_id']:
            await message.answer('✅ Вы успешно надели этот скин.')
            user['level'] = 3
        else:
            await message.answer('У вас нет вещи с таким айди.')
    if id == 4:
        if '4' in user['stats']['skins_id']:
            await message.answer('✅ Вы успешно надели этот скин.')
            user['level'] = 4
        else:
            await message.answer('У вас нет вещи с таким айди.')
    if id == 5:
        if '5' in user['stats']['skins_id']:
            await message.answer('✅ Вы успешно надели этот скин.')
            user['level'] = 5
        else:
            await message.answer('У вас нет вещи с таким айди.')
    if id == 6:
        if '6' in user['stats']['skins_id']:
            await message.answer('✅ Вы успешно надели этот скин.')
            user['level'] = 6
        else:
            await message.answer('У вас нет вещи с таким айди.')
    if id == 7:
        if '7' in user['stats']['skins_id']:
            await message.answer('✅ Вы успешно надели этот скин.')
            user['level'] = 7
        else:
            await message.answer('У вас нет вещи с таким айди.')
    if id > 7:
        await message.answer('☠️ Странный айди')
    save_db(db)
    
@bot.on.message(text='тт отписаться <mention>')
async def remove_sub(message: Message, mention: str = None):
    db = load_db()
    user = db[str(message.from_id)]
    if user['tiktok'] == 'Нет':
        await message.answer('У вас нет тиктока!')
    else:
        try:
            user_to = await resolve_resources(mention)
        except:
            await message.answer('Странный айди..')
            prof()
        if user_to.id == message.from_id:
            await message.answer('😂 Вы рил хотите от себя отписаться?')
        else:
            if str(user_to.id) not in user['tiktok_stats']['tiktok_tosubs_persons']:
                await message.answer(f'Вы не подписаны на @id{user_to.id}(юзера)')
            else:
                await message.answer(f'Вы отписались от тиктока @id{user_to.id}(юзера).', disable_mentions=True)
                await bot.api.messages.send(user_id=user_to.id, message=f'От вашего тиктока отписался @id{message.from_id}(этот юзер)', random_id=0)
                user['tiktok_stats']['tiktok_tosubs'] -= 1
                user['tiktok_stats']['tiktok_tosubs_persons'].remove(str(user_to.id))
                user_todb = db[str(user_to.id)]
                user_todb['tiktok_stats']['tiktok_subs'] -= 1
                user_todb['tiktok_stats']['tiktok_subs_persons'].remove(str(message.from_id))
            
    save_db(db)

@bot.on.message(text='ответь')
async def reply(message: Message):
    await bot.api.messages.send(peer_id=message.peer_id, message='Ответил', random_id=0, reply_to=message.from_id)

@bot.on.message(text='помощь')
async def help(message: Message):
    await message.answer("Основные команды бота: \n\n"
    "1. я - просмотр профиля\n"
    "2. клан - окно профиля клана\n"
    "3. писька - растить письку\n"
    "4. тт - окно аккаунта в тикток\n"
    "5. магаз - магазин бота\n"
    "6. двери - отгадать дверь\n"
    "7. казино [ставка] [красное/чёрное/зеленое] - игра в казино\n"
    "8. взлом - взломать что-то\n"
    "9. сейф - отгадать код от сейф\n"
    )

@bot.on.private_message(text='меню')
@bot.on.private_message(payload={'command': 'menu'})
async def menu(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    keyboard = (Keyboard(inline=False)
    .add(Text('Донат', payload={'shop': 'donat'}), color=KeyboardButtonColor.POSITIVE)
    .add(Text('Профиль', payload={'command': 'profile'}))
    .add(Text('Тикток', payload={'command': 'tiktok'}), color=KeyboardButtonColor.NEGATIVE)
    .row()
    .add(Text('Помощь', payload={'command': 'help'}), color=KeyboardButtonColor.PRIMARY)
    .add(Text('Магазин', payload={'command': 'shop'}))
    .add(Text('Клан'), color=KeyboardButtonColor.POSITIVE)
    .row()
    .add(Text('Заработок'))
    .add(Text('Работы'))
    ).get_json()
    await message.answer(f'{user['username']}, ты попал в меню бота.', keyboard=keyboard, attachment='photo-230806544_457239029')

@bot.on.private_message(text='заработок')
async def zarabotok(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    keyboard = (Keyboard(inline=True)
    .add(Text('Взлом'))
    .row()
    .add(Text('Сейф'))
    .row()
    .add(Text('Двери'))
    .row()
    .add(Text('Снять тикток', payload={'tiktok': 'create'}))
    ).get_json()
    await message.answer(f'{user['username']}, кнопки внизу:', keyboard=keyboard)

@bot.on.message(text='клан выйти')
async def clan_resign(message: Message):
    db = load_db()
    db_clan = load_db_clans()
    user = db[str(message.from_id)]
    if user['clan'] == 'Нет':
        await message.answer('У вас нет клана.')
    else:
        id_clan = user['id_clan']
        clan = db_clan[id_clan]
        if user['role'] == 'Лидер':
            await message.answer('☠️ Вы лидер клана.')
        else:
            await message.answer(f'Вы вышли из клана "{user['clan']}"')
            user['clan'] = 'Нет'
            user['id_clan'] = 0
            user['role'] = 0
            clan['users'] -= 1
            clan['users_ids'].remove(str(message.from_id))
            save_db(db)
            save_db_clans(db_clan)

@bot.on.message(text='клан кик <mention>')
async def kicker_clan(message: Message, mention: str = None):
    db = load_db()
    db_clan = load_db_clans()
    user = db[str(message.from_id)]
    if user['clan'] == 'Нет' or user['role'] not in ['Лидер', 'Заместитель']:
        await message.answer('Вы не в клане или у вас нет доступа.')
    if user['clan'] != 'Нет' and user['role'] in ['Лидер', 'Заместитель']:
        id_clan = user['id_clan']
        clan = db_clan[id_clan]
        a = await resolve_resources(mention)
        id_user = a.id
        user2 = db[str(id_user)]
        if user2['id_clan'] != user['id_clan']:
            await message.answer(f'@id{a.id}(Пользователь) не в вашем клане!')
        else:
            if user2['role'] in ['Лидер', 'Заместитель']:
                await message.answer('Вы не можете кикнуть данного юзера.')
            else:
                await message.answer(f'@id{a.id}(Пользователь) кикнут из клана.')
                user2['clan'] = 'Нет'
                user2['id_clan'] = 0
                user2['role'] = 0
                db_clan[str(id_clan)]['users'] -= 1
                save_db(db)
                save_db_clans(db_clan)
                await bot.api.messages.send(user_id=a.id, message=f'Вас кикнули из клана. Согласен, это жёстко(', random_id=0)


@bot.on.private_message(text='работы')
@bot.on.private_message(payload={'command': 'works'})
async def works(message: Message):
    db = load_db()
    keyboard = (Keyboard()
                .add(Text('Грузчик'))
                .add(Text('Такси'))
                .row()
                .add(Text('Мусорщик'))
                .add(Text('Рыбалка'))
                .row()
                .add(Text('Назад', payload={'command': 'menu'}), color=KeyboardButtonColor.NEGATIVE)
                ).get_json()

    await message.answer(f'{db[str(message.from_id)]['username']}, выбери работу:', keyboard=keyboard, attachment='photo-230806544_457239030')

@bot.on.private_message(text='грузчик')
async def gruz(message: Message):
    keyboard = (Keyboard()
                .add(Text('Начать таскать'), color=positive)
                .add(Text('Назад', payload={'command': 'works'}), color=negative)).get_json()
    await message.answer('Список действий', keyboard=keyboard)

@bot.on.message(text='начать таскать')
async def taskaty(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    if user['stats']['gruz'] == False:
        user['stats']['gruz'] = True
        save_db(db)
        await message.answer('Вы потащили коробку..')
        await asyncio.sleep(30)
        if user['vip'] == 'Нет':
            rand = random.randint(200000000000, 500000000000)
        else:
            rand = (random.randint(200000000000, 500000000000))*2
        user['balance'] += rand
        user['stats']['gruz'] = False
        save_db(db)
        await message.answer(f'Вы притащили коробку и заработали: {str(humanize.intcomma(rand).replace(",", "."))}$\n\nВаш баланс: {str(humanize.intcomma(user['balance']).replace(",", "."))}$')
    else:
        await message.answer('Вы не притащили ещё ту коробку!')

@bot.on.message(text='перевод <mention> <sum1>')
async def perevod(message: Message, mention: str = None, sum1: str = None):
    db = load_db()
    user = db[str(message.from_id)]
    try:
        user2 = await resolve_resources(mention)
    except:
        await message.answer('Странный айди.')
    try:
        sum = parse_amount(sum1, message.from_id)
    except:
        await message.answer('Странная ставка.')
    if message.from_id == user2.id:
        await message.answer('Ты как себе собрался переводить?')
    else:
        if sum > user['balance']:
            await message.answer('У вас нет столько денег -_-')
        if sum <= user['balance']:
            user['balance'] -= sum
            db[str(user2.id)]['balance'] += sum
            await message.answer(f'Вы успешно перевели @id{user2.id}(пользователю) сумму в размере: {humanize.intcomma(sum).replace(',', ' ')}')
            await bot.api.messages.send(user_id=user2.id, message=f'"@id{message.from_id}({user['username']}) перевёл вам {humanize.intcomma(sum).replace(',', ' ')}$', random_id=0)
            save_db(db)

@bot.on.message(text='баланс')
async def balans(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    if message.reply_message:
        user = db[str(message.reply_message.from_id)]
        await message.answer(f'💸 Баланс @id{message.reply_message.from_id}({user['username']}) - {humanize.intcomma(user['balance']).replace(',', ' ')}')
    else:
        await message.answer(f'💸 Баланс: {humanize.intcomma(user['balance']).replace(',', ' ')}')


@bot.on.message(text='выдать бабло <money>')
async def give_money_adm(message: Message, money: str = None):
    db = load_db()
    user = db[str(message.from_id)]
    if user['status'] == 'player':
        await message.answer('❌')
    else:
        money = parse_amount(money, message.from_id)
        user['balance'] += int(money)
        save_db(db)
        await message.answer('✅')

@bot.on.message(text='клан пожертвовать <money>')
async def send_money_to_clan(message: Message, money: str = None):
    db = load_db()
    db_clan = load_db_clans()
    user = db[str(message.from_id)]
    if user['clan'] == 'Нет':
        await message.answer('У тебя нет клана!')
    else:
        try:
            amount = parse_amount(money, user_id=message.from_id)
        except:
            await message.answer('Странная сумма..')
        if user['balance'] >= amount:
            await message.answer(f'Вы успешно положили в казну клана -- {humanize.intcomma(amount).replace(',', ' ')}')
            id = str(user['id_clan'])
            clan = db_clan[id]
            clan_leader = clan['leader']
            await bot.api.messages.send(user_id=int(clan_leader), message=f'@id{message.from_id}({user['username']}) положил в казну -- {humanize.intcomma(amount).replace(',', ' ')}', random_id=0)
            clan['money'] += amount
            user['balance'] -= amount
            save_db(db)
            save_db_clans(db_clan)
        else:
            await message.answer('Вам не хватает денег!')


@bot.on.message(text='клан магаз')
async def clan_shop(message: Message):
    db = load_db()
    db_clan = load_db_clans()
    user = db[str(message.from_id)]
    if user['clan'] == 'Нет':
        await message.answer('У тебя нет клана!')
    else:
        keyboard = (Keyboard(inline=True)
        .add(Text('1', payload={'clan_shop': 1}))
        .add(Text('2', payload={'clan_shop': 2}))
        .row()
        .add(Text('3', payload={'clan_shop': 3}))
        .add(Text('4', payload={'clan_shop': 4}))
        ).get_json()
        await message.answer(f'''
🛒 *Магазин для кланов* 🏰

Товары в наличии:

1️⃣ *Увеличение мест в клане* 
   ➕ +1 место для участников
   💰 Стоимость: 60мм$
   ━━━━━━━━━━━━━━━━━━━

2️⃣ *х2 кубки при победе* 🏆 
   🔥 Удвоенная награда за победы
   ⏳ Действует: 3 дня
   💎 Стоимость: 100мм$
   ━━━━━━━━━━━━━━━━━━━

3️⃣ *Быстрые рейды* ⚡ 
   🎯 Рейдите каждые 5 минут
   ⏳ Действует: 3 дня
   💰 Стоимость: 100мм$
   ━━━━━━━━━━━━━━━━━━━

4️⃣ *Эксклюзивный герб клана* 🛡️ 
   🎨 Уникальная эмблема для вашего клана
   ⏳ Действует: НАВСЕГДА
   💎 Стоимость: 300мм$
   ━━━━━━━━━━━━━━━━━━━

💡 Баланс клана: {go_money(db_clan[str(user['id_clan'])]['money'])}
''', keyboard=keyboard)

@bot.on.message(payload={'clan_shop': 1})
async def clan_shop1(message: Message):
    db = load_db()
    db_clan = load_db_clans()
    clan = str(db[str(message.from_id)]['id_clan'])
    clan_id = db_clan[clan]
    if db[str(message.from_id)]['role'] in ['Лидер', 'Заместитель']:
        if clan_id['money'] <= 600000000000000:
            await message.answer('В казне клана не достаточно денег.')
        else:
            await message.answer('Места в клане увеличены на 1.')
            clan_id['money'] -= 600000000000000
            clan_id['max_users'] += 1
            save_db_clans(db_clan)
    else:
        await message.answer('У вас недостаточно полномочий или у вас вовсе нет клана.')
@bot.on.message(payload={'clan_shop': 2})
async def clan_shop2(message: Message):
    db = load_db()
    db_clan = load_db_clans()
    clan = str(db[str(message.from_id)]['id_clan'])
    clan_id = db_clan[clan]
    if db[str(message.from_id)]['role'] in ['Лидер', 'Заместитель']:
        if clan_id['money'] <= 1000000000000000:
            await message.answer('В казне клана не достаточно денег.')
        else:
            if "2" not in clan_id['level']:
                await message.answer('Буст "х2 кубки" активирован!')
                await bot.api.messages.send(user_id=int(clan_id['leader']), message=f'Ваш клан купил буст "х2 кубки" на 3 дня.', random_id=0)
                clan_id['level'].append("2")
                clan_id['money'] -= 1000000000000000
                save_db_clans(db_clan)
                await asyncio.sleep(259200)
                await bot.api.messages.send(user_id=int(clan_id['leader']), message=f'Буст "х2 кубки" закончен.', random_id=0)
                clan_id['level'].remove("2")
                save_db_clans(db_clan)
            else:
                await message.answer('Этот буст уже активирован.')
    else:
        await message.answer('У вас недостаточно полномочий или у вас вовсе нет клана.')
@bot.on.message(payload={'clan_shop': 3})
async def clan_shop3(message: Message):
    db = load_db()
    db_clan = load_db_clans()
    clan = str(db[str(message.from_id)]['id_clan'])
    clan_id = db_clan[clan]
    if db[str(message.from_id)]['role'] in ['Лидер', 'Заместитель']:
        if clan_id['money'] >= 100000000000000:
            if "3" not in clan_id['level']:
                clan_id['level'].append("3")
                clan_id['money'] -= 100000000000000
                save_db_clans(db_clan)
                await bot.api.messages.send(user_id=int(clan_id['leader']), message=f'Ваш клан купил буст "рейд каждые 5 минут" на 3 дня.', random_id=0)
                await asyncio.sleep(259300)
                clan_id['level'].remove("3")
                bot.api.messages.send(user_id=int(clan_id['leader']), message=f'Буст "рейд каждые 5 минут" закончился', random_id=0)
                save_db_clans(db_clan)
            else:
                await message.answer('У вас уже куплен этот буст.')
        else:
            await message.answer('В казне клана не достаточно денег!')
    else:
        await message.answer('Вам не хватает полномочий или у вас вовсе нет клана.')
@bot.on.message(payload={'clan_shop': 4})
async def clan_shop4(message: Message):
    db = load_db()
    db_clan = load_db_clans()
    clan = str(db[str(message.from_id)]['id_clan'])
    clan_id = db_clan[clan]
    if db[str(message.from_id)]['role'] in ['Лидер', 'Заместитель']:
        if "4" not in clan_id['level']:
            if clan_id['money'] >= 300000000000000:

                await message.answer('Способность ставить герб клана активирована!\nЧтобы поставить, используй команду: "клан герб" и прикрепи фото.')
                clan_id['level'].append("4")
                await bot.api.messages.send(user_id=int(clan_id['leader']), message=f'Ваш клан купил способность ставить герб клана! Используй команду: "клан герб" и прикрепи фото', random_id=0)
                save_db_clans(db_clan)
            else:
                await message.answer('Недостаточно денег в казне клана!')
        else:
            await message.answer('Эта способность уже активирована.')
    else:
        await message.answer('Вам не хватает полномочий или у вас вовсе нет клана!')

@bot.on.message(text='клан герб')
async def photo_for_clan(message: Message):
    db = load_db()
    db_clan = load_db_clans()
    id_clan = db[str(message.from_id)]['id_clan']
    clan = db_clan[str(id_clan)]
    if db[str(message.from_id)]['role'] in ['Лидер']:
        if "4" in clan['level']:
            photo = message.attachments[0].photo
            photo_url = max(photo.sizes, key=lambda x: x.width).url
            await message.answer('Герб клана установлен.')
            clan['photo'] = photo_url
            save_db_clans(db_clan)
        else:
            await message.answer('У вашего клана нет этой способности!')
    else:
        await message.answer('Вам не хватает полномочий или у вас вовсе нет клана!')



@bot.on.message(text='фото')
async def photo_for_cln(message: Message):
    db = load_db()
    photo = message.attachments[0].photo
    photo_url = max(photo.sizes, key=lambda x: x.width).url
    await message.answer('Yes')
    db['photo'] = photo_url
    save_db(db)

@bot.on.message(text='покажи фото')
async def show(message: Message):
    db = load_db()
    photo_url = db["photo"]
    response = requests.get(photo_url)
    img_bytes = BytesIO(response.content)

    # Используем PhotoMessageUploader для загрузки
    uploader = PhotoMessageUploader(bot.api)
    photo = await uploader.upload(img_bytes) 
    
    await message.answer("Вот ваше фото:", attachment=photo)

@bot.on.message(text='клан вывод <mon>')
async def give_me_my_money(message: Message, mon: str = None):
    db = load_db()
    db_clan = load_db_clans()
    user = db[str(message.from_id)]
    clan_id = user['id_clan']
    clan = db_clan[str(clan_id)]
    if user['clan'] == 'Нет':
        await message.answer('У вас нет клана!')
    else:
        if user['role'] not in ['Лидер', 'Заместитель']:
            await message.answer('Вы не можете выводить деньги из клана!')
        else:
            try:
                money = parse_amount(mon, message.from_id)
            except:
                await message.answer('Странная сумма..')
            if money <= clan['money']:
                await message.answer(f'Вы вывели из клана {go_money(money)}$\nЕсли сумма не корректная, то не используй "вб"')
                clan['money'] -= money
                user['balance'] += money
                save_db_clans(db_clan)
                save_db(db)
            else:
                await message.answer('В клане недостаточно средств!')
            
@bot.on.message(text='клан ранг <mention> <rang>')
async def rang(message: Message, mention: str = None, rang: str = None):
    db = load_db()
    db_clan = load_db_clans()
    user = db[str(message.from_id)]
    id_clan = user['id_clan']
    clan = db_clan[id_clan]
    rang = int(rang)
    if user['role'] in ['Лидер', 'Заместитель']:
        if message.reply_message:
            try:
                target_id = message.reply_message.from_id
            except:
                await message.answer('Не могу найти пользователя!')
            if str(target_id) in clan['users_ids']:
                if rang is None:
                    await message.answer('Не правильный ввод ранга! Доступные ранги:\n\n1 - Новичок\n2 - Старейшина\n3 - Заместитель')
                else:
                    if user['role'] == 'Лидер':
                        await message.answer(f'Вы успешно поменяли роль @id{target_id}(юзеру)', disable_mention=True)
                        if rang == 1 or rang < 1:
                            db[str(target_id)]['role'] = 'Новичок'
                        if rang == 2:
                            db[str(target_id)]['role'] = 'Старейшина'
                        if rang == 3 or rang > 3:
                            db[str(target_id)]['role'] = 'Заместитель'
                    if user['role'] == 'Заместитель' and db[str(target_id)]['role'] in ['Заместитель', 'Лидер']:
                        await message.answer(f'У вас нет прав менять роль этому @id{target_id}(юзеру)', disable_mention=True)
                    if user['role'] == 'Заместитель' and db[str(target_id)]['role'] not in ['Заместитель', 'Лидер']:
                        if rang == 1 or rang < 1:
                            db[str(target_id)]['role'] = 'Новичок'
                        if rang == 2 or rang > 2:
                            db[str(target_id)]['role'] = 'Старейшина'
                        await message.answer(f'Вы успешно поменяли роль @id{target_id}(юзеру)!', disable_mentions=True)
        else:
            try:
                targ = await resolve_resources(mention)
                target_id = targ.id
            except:
                await message.answer('Не удалось найти пользователя!')
            if str(target_id) in clan['users_ids']:
                if rang is None:
                    await message.answer('Не правильный ввод ранга! Доступные ранги:\n\n1 - Новичок\n2 - Старейшина\n3 - Заместитель')
                else:
                    if user['role'] == 'Лидер':
                        await message.answer(f'Вы успешно поменяли роль @id{target_id}(юзеру)', disable_mention=True)
                        if rang == 1 or rang < 1:
                            db[str(target_id)]['role'] = 'Новичок'
                        if rang == 2:
                            db[str(target_id)]['role'] = 'Старейшина'
                        if rang == 3 or rang > 3:
                            db[str(target_id)]['role'] = 'Заместитель'
                    if user['role'] == 'Заместитель' and db[str(target_id)]['role'] in ['Заместитель', 'Лидер']:
                        await message.answer(f'У вас нет прав менять роль этому @id{target_id}(юзеру)', disable_mention=True)
                    if user['role'] == 'Заместитель' and db[str(target_id)]['role'] not in ['Заместитель', 'Лидер']:
                        if rang == 1 or rang < 1:
                            db[str(target_id)]['role'] = 'Новичок'
                        if rang == 2 or rang > 2:
                            db[str(target_id)]['role'] = 'Старейшина'
                        await message.answer(f'Вы успешно поменяли роль @id{target_id}(юзеру)!', disable_mentions=True)
    else:
        await message.answer('Вы не можете менять роль юзерам!')
    save_db(db)
@bot.on.raw_event(GroupEventType.LIKE_ADD, dataclass=GroupTypes.LikeAdd)
async def handle_like_add(event: GroupTypes.LikeAdd):
    db = load_db()
    user_id = event.object.liker_id
    
    await bot.api.messages.send(
        user_id=user_id,
        message=f"Спасибо за лайк! Ты заработал 1мм",
        random_id=0
    )
    db[str(user_id)]['balance'] += 1000000000000
    save_db(db)

@bot.on.raw_event(GroupEventType.LIKE_REMOVE, dataclass=GroupTypes.LikeRemove)
async def handle_like_remove(event: GroupTypes.LikeRemove):
    db = load_db()
    user_id = event.object.liker_id
    
    await bot.api.messages.send(
        user_id=user_id,
        message=f"Жаль, что вы убрали лайк с поста :(\nВы потеряли 1мм$",
        random_id=0
    )
    db[str(user_id)]['balance'] -= 1000000000000
    save_db(db)


@bot.on.message(text='//givepoints <mention> <points>')
async def give_points(message: Message, mention: str = None, points: str = None):
    db = load_db()
    if db[str(message.from_id)]['status'] in ['owner', 'zam', 'gl.moder']:
        try:
            user_id = await resolve_resources(mention)
            user_id = user_id.id
        except Exception as e:
            await message.answer('Ошибка: ' + e)
        if db[str(user_id)]['status'] in ['moder', 'zam', 'owner', 'gl.moder']:
            try:
                points = int(points)
            except Exception as e:
                await message.answer('Ошибка: ' + e)
            db[str(user_id)]['stats']['points'] += points
            await message.answer('Готово')
            save_db(db)

@bot.on.message(text='кости <mon>')
async def kosti(message: Message, mon: str = None):
    db = load_db()
    try:
        target_id = message.reply_message.from_id
        target = db[str(target_id)]
        user = db[str(message.from_id)]
    except:
        return await message.answer('Ответьте на сообщение юзера, с которым хотите играть.')
    
    try:
        money = parse_amount(mon, message.from_id)
    except:
        return await message.answer('Введите корректную ставку')
    
    if user['balance'] < money:
        return await message.answer('Вам не хватает денег!')
    
    if target['balance'] < money:
        return await message.answer('Сопернику не хватает денег!')
    
    keyboard = (Keyboard(inline=True)
               .add(Callback(f'Согласиться'))
               ).get_json()
    
    await message.answer(
        f"@id{target_id}({target['username']}), @id{message.from_id}({user['username']}) "
        f"предлагает вам сыграть в кости на {go_money(money)}$",
        keyboard=keyboard
    )
from PIL import Image, ImageDraw, ImageFont
import os

def generate_meme(user1: str, user2: str, result: str):
    # Загружаем шаблон изображения
    template = Image.open("template.jpg")  # Ваш шаблон для мема
    
    # Настройки шрифта
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    draw = ImageDraw.Draw(template)
    
    # Рисуем текст на изображении
    draw.text((50, 50), f"{user1} vs {user2}", font=font, fill="black")
    draw.text((150, 300), f"Результат: {result}", font=font, fill="red")
    
    # Сохраняем результат
    output_path = "result.jpg"
    template.save(output_path)
    return output_path
@bot.on.message(text='замес <sm>')
async def zames(message: Message, sm: str = None):
    db = load_db()
    try:
        target_id = message.reply_message.from_id
        target = db[str(target_id)]
        user = db[str(message.from_id)]
    except KeyError:
        return await message.answer('Ответьте на сообщение пользователя, с которым хотите сделать замес.')
    
    try:
        sm = int(sm)
    except ValueError:
        return await message.answer('Укажите корректное количество см (число)')
    
    if sm > user['piska']:
        return await message.answer('Недостаточно письки для замеса.')
    
    if sm > target['piska']:
        return await message.answer('У соперника недостаточно письки!')
    
    db['игра']['замесы']['ID'] += 1
    save_db(db)
    ID = db['игра']['замесы']['ID']
    keyboard = (
        Keyboard(inline=True)
        .add(Callback("Согласиться", payload={
            "zames": f"zames_{ID}"
        }), color=KeyboardButtonColor.POSITIVE)
        .get_json()
    )
    
    db['игра']['замесы'][str(ID)] = {
        "1": message.from_id,
        "2": target_id,
        "sm": sm,
        "time": time.time()
    }
    user['stats']['замес'].append(str(ID))
    target['stats']['замес'].append(str(ID))
    save_db(db)

    await message.answer(
        f"@id{target_id}({target['username']}), @id{message.from_id}({user['username']}) "
        f"предлагает вам замес на {sm} см письки.",
        keyboard=keyboard
    )


# Элементы и их веса (чем больше вес - тем чаще появляется)
ITEMS: Dict[str, int] = {
    "🧻": 1000000000,
    "🛢️": 2000000000,
    "⚽": 3000000000,
    "🩳": 5000000000,
    "🧨": 8000000000,
    "📃": 10000000000,
    "💳": 20000000000,
    "💰": 25000000000,
    "💎": 100000000000
}
    
ROWS = 3          # Количество рядов
BUTTONS_PER_ROW = 3  # Кнопок в ряду

# Генератор клавиатуры
def generate_trash_keyboard() -> str:
    keyboard = Keyboard(inline=True)
    
    # Создаем взвешенный список (чем дешевле предмет - тем чаще он встречается)
    weighted_items = []
    for item, price in ITEMS.items():
        # Чем выше цена, тем меньше шанс выпадения (обратная зависимость)
        weight = max(1, 1000 // price)  # Формулу можно настроить
        weighted_items.extend([(item, price)] * weight)
    
    # 3 ряда по 3 кнопки (9 предметов)
    for _ in range(3):
        row_buttons = []
        for _ in range(3):
            item, price = random.choice(weighted_items)
            row_buttons.append(
                Callback(f"{item}", payload={"item": item, "price": price})
            )
        
        # Добавляем ряд кнопок
        for btn in row_buttons:
            # Цвет кнопки зависит от цены (дешевые - серые, дорогие - зеленые/золотые)
            color = (
                KeyboardButtonColor.PRIMARY if btn.payload["price"] > 500
                else KeyboardButtonColor.POSITIVE if btn.payload["price"] > 100
                else KeyboardButtonColor.SECONDARY
            )
            keyboard.add(btn, color=color)
        keyboard.row()  # Новый ряд
    
    # Кнопка "Закрыть"
    keyboard.add(
        Text("❌ Закрыть", payload={"command": 'menu'}),
        color=KeyboardButtonColor.NEGATIVE
    )
    
    return keyboard.get_json()

# Пример обработчика команды
@bot.on.private_message(text="мусорщик")
async def trash_handler(message: Message):
    keyboard = generate_trash_keyboard()
    await message.answer("🎰 Мусорщик готов к работе!\nСобирай ценные вещи.", keyboard=keyboard)

@bot.on.private_message(text='такси')
async def taksi_handler(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    keyboard = (Keyboard(inline=True)
    .add(Callback('Начать рейс', payload={'taksi': 'start'}), color=positive)
    ).get_json()
    await message.answer(f'🚕 Вы попали в меню таксиста\n💰 Баланс: {go_money(user['balance'])}$', keyboard=keyboard)
def is_eligible(user_id):
    db = load_db()
    user_data = db.get(str(user_id))
    
    if not user_data:
        return False
    
    first_seen = datetime.strptime(user_data["registered_at"], "%Y-%m-%d")
    return (datetime.now() - first_seen) >= timedelta(days=30)

# Команда /пенсия
@bot.on.message(text="пенсия")
async def pension(message: Message):
    user_id = message.from_id
    db = load_db()
    user = db[str(user_id)]
    now = int(time.time())
    if now - user['stats']['last_pensia'] < 86400:
        wait_time = 86400 - (now - user['stats']['last_pensia'])
        formatted_time = format_time('час-минута-секунда', wait_time)
        await message.answer(f'До следующей пенсии осталось {formatted_time}')
    else:
        # Проверка стажа
        if is_eligible(user_id):
            db[str(user_id)]["balance"] += 6000000000000  # Начисляем пенсию
            user['stats']['last_pensia'] = now
            save_db(db)
            await message.answer("🎉 Вам начислена пенсия: 6.000.000.000.000 монет!")
        else:
            first_seen = datetime.strptime(db[str(user_id)]["registered_at"], "%Y-%m-%d")
            days_left = 30 - (datetime.now() - first_seen).days
            await message.answer(f"⏳ До пенсии осталось: {days_left} дней.")

def get_btc_price():
    try:
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        data = response.json()
        return data["bitcoin"]["usd"]*1000000000  
    except:
        return 100000000000000  # Дефолтное значение
import matplotlib.pyplot as plt
import requests
import io
from datetime import datetime, timedelta
import locale
import pytz  # Библиотека для работы с часовыми поясами

# Устанавливаем локаль и часовой пояс
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
MOSCOW_TZ = pytz.timezone('Europe/Moscow')

def get_btc_chart():
    # Текущее время в Москве
    end_date = datetime.now(MOSCOW_TZ)
    start_date = end_date - timedelta(days=1)
    
    # Получаем данные
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from={int(start_date.timestamp())}&to={int(end_date.timestamp())}"
    response = requests.get(url)
    data = response.json()
    
    # Конвертируем timestamp в московское время
    timestamps = [datetime.fromtimestamp(point[0]/1000).astimezone(MOSCOW_TZ) for point in data['prices']]
    prices = [point[1] * 1000000000 for point in data['prices']]  # Умножаем для больших чисел

    # Настройка графика
    plt.figure(figsize=(12, 6), facecolor='#1e1e1e')
    ax = plt.axes()
    ax.set_facecolor('#1e1e1e')
    
    # Форматирование оси X (даты)
    plt.plot(timestamps, prices, color="#00ff0d", linewidth=2)
    plt.title("BTC Rodrigo Bot (MSK)", color='white', fontsize=16, pad=20)
    plt.xlabel("Time", color='white')
    plt.ylabel("Price ($)", color='white')
    
    # Настройка отображения времени
    ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M', tz=MOSCOW_TZ))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)).replace(",", ".")))
    
    # Стили осей
    ax.tick_params(colors='white', axis='both')
    ax.grid(color="#292929", linestyle='--')
    
    # Сохранение
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=120, facecolor='#1e1e1e', bbox_inches='tight')
    buf.seek(0)
    plt.close()
    return buf
# Команда /курс
@bot.on.message(text="биткоин")
async def show_rate(message: Message):
    price = get_btc_price()
    photo = get_btc_chart()
    photo_uploader = PhotoMessageUploader(bot.api)
    photo = await photo_uploader.upload(photo)
    db = load_db()
    user = db[str(message.from_id)]
    bts = user['bts']*price
    keyboard = (Keyboard(inline=True).add(Text('Команды для управления BTC', payload={'command': 'bts_command'}), color=positive)).get_json()
    await message.answer(f"📊 Курс BTC: 1 BTC = {go_money(price)}$\n\n"
    f"🪙 На вашем счету: {user['bts']} = {go_money(bts)}$"
    , keyboard=keyboard, attachment=photo)

@bot.on.message(payload={'command': 'bts_command'})
async def bts_commans(message: Message):

    await message.answer('Команды для управления BTC:\n\n'
    '1. Биткоин - меню биткоина\n'
    '2. Перевести биткоин [@username] [биткоины]\n'
    '3. Ферма - ферма биткоинов\n'
    '4. Купить биткоин [кол-во]\n'
    '5. Продать биткоин [кол-во]'
    )

@bot.on.private_message(text='ферма')
async def farm(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    if user['farm']['income'] == 0:
        keyboard = (Keyboard(inline=True).add(Callback('💰 Купить ферму за 10мм', payload={'farm': 'buy'}), color=positive)).get_json()
        await message.answer('❌ У вас нет фермы!', keyboard=keyboard)
    else:
        keyboard = (Keyboard(inline=True)
                    .add(Callback('Улучшить ферму', payload={'farm': 'up_level'}), color=positive)
                    .row()
                    .add(Text('Включить ферму', payload={'farm': 'start'}))
                    .row()
                    .add(Text('Собрать доход', payload={'farm': 'income'}), color=primary)
                    ).get_json()
        await message.answer(f'💻 Ферма {user['username']}\n\n'
                            f'🪙 Доход: {user['farm']['income']} btc/5 часов\n'
                            f'🔥 Уровень: {user['farm']['level']}\n'
                            f'💵 Следующее улучшение стоит: {go_money(user['farm']['next_level'])}$\n\n'
                            f'💰 Заработано: {user['farm']['bank']} BTC'
                            , keyboard=keyboard
                            )
@bot.on.chat_message(text='ферма')
async def no_farm(message: Message):
    await message.answer('Только в лс бота.')
@bot.on.private_message(payload={'farm': 'start'})
async def farm_start(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    if user['farm']['income'] == 0:
        await message.answer('У вас нет фермы.')
    else:
        if user['farm']['status'] == 'on':
            await message.answer('❌ Ферма уже включена.')
        if user['farm']['status'] == 'off':
            await message.answer('⏳ Вы запустили ферму на 5 часов!')
            user['farm']['status'] = 'on'
            user['farm']['last_income'] = int(time.time())
            save_db(db)
       
@bot.on.private_message(payload={'farm': 'income'})
async def income(message: Message):
        db = load_db()
        user = db[str(message.from_id)]
        last_claim = user["farm"]["last_income"]
        current_time = int(time.time())
        hours_passed = (current_time - last_claim) / 3600
        
        if hours_passed < 5:
            await message.answer("⏳ Доход ещё не накоплен! Попробуйте позже.")
            return
        else:
            btc_earned = user["farm"]["income"]
            user['bts'] += btc_earned
            user['farm']['status'] = 'off'
            save_db(db)
            await message.answer(f'🪙Вы собрали {btc_earned} btc \n😎 Запустите ферму, чтобы заработать ещё')

@bot.on.message(text='продать биткоин <btc>')
async def sale_btc(message: Message, btc: str):
    db = load_db()
    user = db[str(message.from_id)]
    price = get_btc_price()
    if btc == None:
        await message.answer('❌ Не так! Продать биткоин [кол-во]')
    else:
        try:
            btc = float(btc)
        except Exception as e:
            await message.answer(f'❌ Ошибка: {e}')
        
        btc_user = user['bts']
        if btc_user < btc:
            await message.answer('❌ Вам не хватает биткоинов для продажи.')
        else:
            await message.answer(f'✅ Вы продали {btc} BTC')
            user['bts'] -= btc
            user['balance'] += btc*price
            save_db(db)

@bot.on.message(text='купить биткоин <btc>')
async def buy_btc(message: Message, btc: str):
    db = load_db()
    user = db[str(message.from_id)]
    price = get_btc_price()
    if btc == None:
        await message.answer('❌ Не так! Купить биткоин [кол-во]')
    else:
        try:
            btc = float(btc)
        except Exception as e:
            await message.answer(f'❌ Ошибка: {e}')
        balance = user['balance']
        btc_price = btc*price
        if balance < btc_price:
            await message.answer('❌ Вам не хватает денег!')
        else:
            user['balance'] -= btc_price
            user['bts'] += btc
            save_db(db)
            await message.answer(f'✅ Вы купили {btc} BTC!')

@bot.on.message(text='перевести биткоин <mention> <btc>')
async def perevbit(message: Message, mention: str, btc: str):
    db = load_db()
    user = db[str(message.from_id)]
    try:
        id1 = await resolve_resources(mention)
        id_user = id1.id
    except:
        await message.answer('❌ Я не смог найти пользователя.')
    if str(id_user) not in db:
        await message.answer('❌ Данный юзер не играет в бота.')
    else:
        try:
            btc = float(btc)
        except Exception as e:
            await message.answer(f'❌ Ошибка: {e}')
        if btc > user['bts']:
            await message.answer('❌ Вам не хватает биткоинов для перевода')
        else:
            db[str(id_user)]['bts'] += btc
            user['bts'] -= btc
            save_db(db)
            await message.answer(f'Вы успешно перевели @id{id_user}(юзеру) биткоины.', disable_mentions=True)
            await bot.api.messages.send(user_id=id_user, message=f'@id{message.from_id}({user['username']}) перевёл вам биткоины в размере {btc} BTC', random_id=0)

import yoomoney
YOOMONEY_TOKEN = "ваш_токен"
WALLET = "4100119211392665"  # Ваш номер кошелька
client = yoomoney.Client(YOOMONEY_TOKEN)
async def give_vip(user_id: int, days: int):
    db = load_db()
    user = db[str(user_id)]
    expire_time = int(time.time()) + days * 86400
    user['vip'] = expire_time
    save_db(db)
@bot.on.message(text="Донат")
@bot.on.message(payload={'shop': 'donat'})
async def buy_vip(message: Message):
    await message.answer(
        "💎 VIP статус на 1 месяц (100 руб)\n\n"
        "Как оплатить:\n"
        f"1. Переведите 100 руб на номер {WALLET}\n"
        f"2. В комментарии укажите: vip_{message.from_id}\n\n"
        "После оплаты статус активируется автоматически в течение 5 минут! На всякий случай сохраните скриншот перевода. Если не появится, то пришлите @id819016396\n"
        "Проверить: команда 'вип'"
    )
async def check_payments():
    while True:
        history = client.operation_history(label="vip_")  # Ищем платежи с меткой
        
        for operation in history.operations:
            if operation.status == "success":
                user_id = operation.label.split("_")[1]  # Извлекаем ID из метки
                await give_vip(int(user_id), 30)  # 30 дней VIP
                
        await asyncio.sleep(300)  # Проверка каждые 5 минут

@bot.on.message(text='рыбалка')
async def fishing(message: Message):
    db = load_db()
    user = db[str(message.from_id)]
    keyboard = (Keyboard(inline=True)
    .add(Callback('Начать ловлю', payload={'fishing': 'start'}), color=positive)
    ).get_json()
    await message.answer('🐟 Приветствуем тебя на такой чудесной работе! Вам предстоит ловить рыбу!', keyboard=keyboard)
    await message.answer(sticker_id=109405)

@bot.on.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=GroupTypes.MessageEvent)
async def handle_callback(event: GroupTypes.MessageEvent):
    payload = event.object.payload
    db = load_db()
    if 'fishing' in payload:
        if 'start' in payload['fishing']:
            if db[str(event.object.user_id)]['stats']['fish'] == False:
                db[str(event.object.user_id)]['stats']['fish'] = True
                save_db(db)
                await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=f'Вы начали ловить рыбу. Ожидайте..')
                await asyncio.sleep(30)
                await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=f'Так, что-то там плещется.. Готовьтесь подсекать.')
                await asyncio.sleep(5)
                keyboard = (Keyboard(inline=True).add(Callback('Подсечь', payload={'fishing': 'подсечь'}), color=negative)).get_json()
                await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=f'ПОДСЕКАЙ', keyboard=keyboard)
            else:
                await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext='Вы уже ловите рыбу!')
        if 'подсечь' in payload['fishing']:
            keyboard = (Keyboard(inline=True).add(Callback('вытащить', payload={'fishing': 'вытащить'}), color=negative)).get_json()
            await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=f'ВЫТАСКИВАЙ', keyboard=keyboard)
        if 'вытащить' in payload['fishing']:
            fish = random.choice(['сом', 'лещ', 'плотва', 'щука', 'провал'])
            if fish == 'сом':
                photo = "photo-230806544_457239147"
                income = 100000000000
                text = '🎣 Ты поймал сома и получил 100.000.000$'
            if fish == 'лещ':
                photo = "photo-230806544_457239148"
                income = 200000000000
                text = '🎣 Ты поймал леща и получил 200.000.000$'
            if fish == 'плотва':
                photo = "photo-230806544_457239149"
                income = 300000000000
                text = '🎣 Ты поймал леща и получил 300.000.000$'
            if fish == 'щука':
                photo = "photo-230806544_457239150"
                income = 400000000000
                text = '🎣 Ты поймал леща и получил 400.000.000$'
            if fish == 'провал':
                photo = None
                income = 0
                text = '😭 Леска оборвалась и вы ничего не получили('
            db[str(event.object.user_id)]['balance'] += income
            db[str(event.object.user_id)]['stats']['fish'] = False
            save_db(db)
            keyboard = (Keyboard(inline=True).add(Callback('Ловить ещё', payload={'fishing': 'start'}), color=positive)).get_json()
            
            await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=f'{text}', attachment=photo, keyboard=keyboard)
    if 'farm' in payload:
        if 'buy' in payload['farm']:
            user = db[str(event.object.user_id)]
            if user['balance'] < 10000000000000:
                keyboard = (Keyboard(inline=True).add(Callback('Купить ферму за 10мм', payload={'farm': 'buy'}), color=positive)).get_json()
                await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=f'Вам не хватает денег!', keyboard=keyboard) 
            else:
                user['farm']['income'] = 0.0001
                user['farm']['level'] = 1
                user['farm']['next_level'] = 500000000000
                save_db(db)
                keyboard = (Keyboard(inline=True).add(Callback('Улучшить ферму', payload={'farm': 'up_level'}), color=positive)).get_json()
                await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=f'Ферма {user['username']}\n\n'
                            f'Доход: {user['farm']['income']} bts/час\n'
                            f'Уровень: {user['farm']['level']}\n'
                            f'Следующее улучшение стоит: {go_money(user['farm']['next_level'])}$', keyboard=keyboard)
        if 'up' in payload['farm']:
            user = db[str(event.object.user_id)]
            cost = user['farm']['next_level']
            if user['balance'] < cost:
                keyboard = (Keyboard(inline=True).add(Callback('Улучшить ферму', payload={'farm': 'up_level'}), color=positive)).get_json()
                await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=
                            'Вам не хватает денег!\n\n'
                            f'Ферма {user['username']}\n\n'
                            f'Доход: {user['farm']['income']} bts/час\n'
                            f'Уровень: {user['farm']['level']}\n'
                            f'Следующее улучшение стоит: {go_money(user['farm']['next_level'])}$', keyboard=keyboard)
            else:
                user['farm']['next_level'] += 15000000000000
                user['farm']['level'] += 1
                user['farm']['income'] += 0.09
                user['balance'] -= cost
                save_db(db)
                keyboard = (Keyboard(inline=True).add(Callback('Улучшить ферму', payload={'farm': 'up_level'}), color=positive)).get_json()
                await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=
                            'Вы купили улучшение!\n\n'
                            f'Ферма {user['username']}\n\n'
                            f'Доход: {user['farm']['income']} bts/час\n'
                            f'Уровень: {user['farm']['level']}\n'
                            f'Следующее улучшение стоит: {go_money(user['farm']['next_level'])}$', keyboard=keyboard)
                
    if 'zames' in payload:
        print(payload)
        zames_id = payload['zames'].split("_")[1]
        try:
            zames = db['игра']['замесы'][str(zames_id)]
        except KeyError:
            return await bot.api.messages.send_message_event_answer(
                event_id=event.object.event_id,
                user_id=event.object.user_id,
                peer_id=event.object.peer_id,
                event_data={"type":"show_snackbar", "text":"Замес не найден!"})
            
        now = int(time.time())
        zames_time = int(zames['time'])  # теперь точно int
        if now - zames_time > 300:  # Исправлено условие
            await edit_message(
                peer_id=event.object.peer_id,
                message_id=event.object.conversation_message_id,
                newtext='Вы не успели принять предложение..'
            )
            del db['игра']['замесы'][str(zames_id)]  # Удаляем из базы
            save_db(db)
            return
            
        user_id = zames['1']
        target_id = zames['2']
        
        if event.object.user_id != int(target_id):
            await bot.api.messages.send_message_event_answer(
                event_id=event.object.event_id,
                user_id=event.object.user_id,
                peer_id=event.object.peer_id,
                event_data={"type":"show_snackbar", "text":"Эта кнопка не для вас!"})
            return
            
        
            
        sm = zames['sm']
        target = db[str(target_id)]
        user = db[str(user_id)]

        
    
    
        
        rand = random.choice(['1', '2', '1', '2'])
        if rand == '1':
            message_text = (f"@id{user_id}({user['username']}) победил @id{target_id}({target['username']})\n"
                            f"Ему достаётся {sm} см")
            user['piska'] += sm
            target['piska'] -= sm
            result = f'Победил {user['username']}'
            target['stats']['замес'].remove(str(zames_id))
            user['stats']['замес'].remove(str(zames_id))
            
        if rand == '2':
            message_text = (f"@id{target_id}({target['username']}) победил @id{user_id}({user['username']})\n"
                            f"Ему достаётся {sm} см")
            result = f'Победил {target['username']}'
            target['piska'] += sm
            user['piska'] -= sm
            target['stats']['замес'].remove(str(zames_id))
            user['stats']['замес'].remove(str(zames_id))
        meme_path = generate_meme(user['username'], target['username'], result)
        uploader = PhotoMessageUploader(bot.api)
        photo = await uploader.upload(meme_path)
        await edit_message(
            peer_id=event.object.peer_id,
            message_id=event.object.conversation_message_id,
            newtext=message_text,
            keyboard=None,
            attachment=photo
        )
        del db['игра']['замесы'][str(zames_id)]  # Удаляем из базы
        save_db(db)
    if 'seyf' in payload:
        user_id = event.object.user_id
        db = load_db()
        user = db[str(user_id)]
        now = int(time.time())
        rand = random.randint(1,2)
        if rand == 1:
            rand2 = random.randint(1000000000000, 3000000000000)
            if user['vip'] != 'Нет':
                rand2 = rand2 * 2
            user['balance'] += rand2
            await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=f'🥳 Вы отгадали код от сейфа и получили {go_money(rand2)}$')
        if rand == 2:
            await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext='😭 Отгадать код от сейфа не получилось.')
            user['stats']['last_seyf'] = now
        save_db(db)
    if 'doors' in payload:
        user_id = event.object.user_id
        db = load_db()
        user = db[str(user_id)]
        now = int(time.time())
        
        rand = random.randint(1,3)
        if rand == 1:
            rand2 = random.randint(5000000000000, 7000000000000)
            if user['vip'] == 'Нет':
                user['balance'] += rand2
            else:
                user['balance'] += rand2 * 2
            
            await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=f'🥳 Вы отгадали дверь и нашли за ней {go_money(rand2)}$')
            
        if rand == 2:
            await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=f'😱😱😱 Вы открыли дверь и нашли за ней 200.000.000.000.000$! ОМАГАД! СУПЕР ВЫИГРЫШ! \n🫠 Ладно, я пошутил)')
        if rand == 3:
            await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=f'🐶🐶 Вы открыли дверь, а там миленькие собачки). Вы на них засмотрелись и у вас стащили деньги.')
        user['stats']['last_doors'] = now
        save_db(db)
    if 'item' in payload:
        item = payload['item']
        price = payload['price']
        user = db[str(event.object.user_id)]
        user['balance'] += price
        save_db(db)
        keyboard = generate_trash_keyboard()
        await edit_message(peer_id=event.object.peer_id, message_id = event.object.conversation_message_id, newtext=f'💸 Вы заработали {go_money(price)}$\n💰 Баланс: {go_money(user['balance'])}$\nПродолжайте дальше собирать..', keyboard=keyboard)
    if 'taksi' in payload:
        user = db[str(event.object.user_id)]
        if user['stats']['taksi'] == False:
            user['stats']['taksi'] = True
            save_db(db)
            await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=f'Вы повезли пассажира.\n⏳ Ориентировочное время: 40 секунд')
            await asyncio.sleep(40)
            rand = random.randint(100000000000, 500000000000)
            user['balance'] += rand
            save_db(db)
            keyboard = (Keyboard(inline=True)
            .add(Callback('Продолжать', payload={'taksi': 'start'}), color=positive)).get_json()
            await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=f'Вы привезли пассажира. Вы заработали: {go_money(rand)}$\nВаш баланс: {go_money(user['balance'])}', keyboard=keyboard)
        else:
            await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext='Вы уже везёте пассажира')
    if 'clan' in payload:
        user_id = event.object.user_id
        user = db[str(event.object.user_id)]
        db_clan = load_db_clans()
        id_clan = payload['clan']
        clan = db_clan[str(id_clan)]
        await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext=f'🥳 Вы вступили в клан "{clan['clan']}"')
        user['clan'] = clan['clan']
        user['id_clan'] = str(id_clan)
        user['role'] = 'Новичок'
        clan['users'] += 1
        clan['users_ids'].append(str(user_id))
        save_db(db)
        save_db_clans(db_clan)
        await bot.api.messages.send(user_id=int(clan['leader']), message=f'🥳 @id{user_id}({user['username']}) вступил в ваш клан!', random_id=0)
    if 'clan_no' in payload:
        db_clan = load_db_clans()
        user_id = event.object.user_id
        id_clan = payload['clan_no']
        clan = db_clan[str(id_clan)]
        await edit_message(peer_id=event.object.peer_id, message_id=event.object.conversation_message_id, newtext='😢 Вы отказались вступить в клан.')
        await bot.api.messages.send(user_id=int(clan['leader']), message=f'😢 @id{user_id}({user['username']}) отказался в ваш клан!', random_id=0)


@bot.on.message(text='магазин домов')
async def shop_houses(message: Message):
    keyboard1 = (Keyboard(inline=True).add(Text('Купить', payload={'shop_houses': '1'})))
    template  = template_gen(
    TemplateElement(
        buttons=keyboard1,  title = 'Дом бомжа', description='1.000.000.000.000$', photo_id='photo-230806544_457239170', action={'type': 'open'}
    ))
    await message.answer('Магазин домов:', template=template)

        
if __name__ == "__main__":    
    loop = asyncio.get_event_loop()
    loop.create_task(task_cleanup())
    loop.create_task(check_payments())
    print("Бот запущен...")
    bot.run_forever()
