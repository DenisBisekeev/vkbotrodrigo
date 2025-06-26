import vkbottle
from vkbottle.bot import Bot, Message
from vkbottle import Callback, Keyboard, KeyboardButtonColor, GroupEventType, GroupTypes, OpenLink
from token_1 import token2 as token
import json
from pathlib import Path

bot = Bot(token=token)

async def edit_message(peer_id, message_id, newtext=None, keyboard=None, attachment=None):
    await bot.api.messages.edit(
        peer_id=peer_id,
        conversation_message_id=message_id,
        message=newtext,
        keyboard=keyboard,
        attachment=attachment
    )

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

DB_PATH = Path("help.json")

def load_db() -> dict:
    if not DB_PATH.exists():
        return {'block': {'ids': []}, 'reports': {}}
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(db: dict):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=4)

db = load_db()

@bot.on.private_message()
async def report(message: Message):
    user_id = message.from_id
    if str(user_id) not in db['block']['ids']:
        if str(user_id) in db['reports']:
            if db['reports'][str(user_id)]['status'] == 'on':
                await bot.api.messages.send(
                    user_id=db['reports'][str(user_id)]['moder'],
                    message=f'Ответ от @id{user_id}',
                    forward_messages=[message.id],
                    random_id=0
                )
            else:
                return None
        else:
            keyboard = (
                Keyboard(inline=True)
                .add(Callback('Взять', payload={'id': f'id_{user_id}'}), color=KeyboardButtonColor.POSITIVE)
            ).get_json()
            await message.answer('Твой вопрос отправлен! Если хочешь что-то дополнить, то пиши.')
            await bot.api.messages.send(
                peer_id=2000000001,
                message=f'@online Новый репорт @id{user_id}',
                forward_messages=[message.id],
                keyboard=keyboard,
                random_id=0
            )
            db['reports'][str(user_id)] = {
                'status': 'off',
                'moder': None
            }
    else:
        await message.answer('🤡 Вы в блоке, вам нельзя отправлять репорты!')
    save_db(db)
@bot.on.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=GroupTypes.MessageEvent)
async def callback_event(event: GroupTypes.MessageEvent):
    payload = event.object.payload
    
    if 'id' in payload:
        user_id = event.object.user_id
        user_to = payload['id'].split('_')[1]
        db['reports'][user_to] = {
            'moder': user_id,
            'status': 'on'
        }
        keyboard = (
            Keyboard(inline=True)
            .add(OpenLink(label='Чат с юзером', link=f'https://m.vk.com/mail?act=show&peer={user_to}&community=231235093'))
            .row()
            .add(Callback('Вопрос решён', payload={'report': f'yes_{user_to}'}), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Callback('ЧС', payload={'report': f'block_{user_to}'}), color=KeyboardButtonColor.NEGATIVE)
            .add(Callback('Это флуд', payload={'report': f'flood_{user_to}'}), color=KeyboardButtonColor.PRIMARY)
            .row()
            .add(Callback('Передать разработчику', payload={'report': f'give_to_razrab_{user_to}'}))
        ).get_json()
        
        await bot.api.messages.send(
            user_id=int(user_to),
            message='🥳 Модератор начал решать ваш вопрос!',
            random_id=0
        )
        await edit_message(
            peer_id=event.object.peer_id,
            message_id=event.object.conversation_message_id,
            newtext=f'@id{user_id} начал решать вопрос @id{user_to}!',
            keyboard=keyboard
        )
    
    elif 'report' in payload:
        action, user_to = payload['report'].split('_', 1)
        
        if action == 'yes':
            await bot.api.messages.send(
                user_id=int(user_to),
                message='📍 Модератор поставил метку, что ваш вопрос решён! Если остались какие-то вопросы, то пиши:',
                random_id=0
            )
            await edit_message(
                peer_id=event.object.peer_id,
                message_id=event.object.conversation_message_id,
                newtext=f'Вопрос @id{user_to} решён!'
            )
            del db['reports'][user_to]
            
        elif action == 'block':
            db['block']['ids'].append(user_to)
            if user_to in db['reports']:
                del db['reports'][user_to]
            await edit_message(
                peer_id=event.object.peer_id,
                message_id=event.object.conversation_message_id,
                newtext=f'@id{user_to} добавлен в ЧС'
            )
            await bot.api.messages.send(
                user_id=int(user_to),
                message='🤡 Вам выдали ЧС репортов.',
                random_id=0
            )
            
        elif action == 'flood':
            if user_to in db['reports']:
                del db['reports'][user_to]
            await edit_message(
                peer_id=event.object.peer_id,
                message_id=event.object.conversation_message_id,
                newtext=f'Репорт @id{user_to} помечен как флуд'
            )
            await bot.api.messages.send(
                user_id=int(user_to),
                message='😡 Ваш репорт помечен как флуд! Если вы продолжите флудить, вам выдадут ЧС.',
                random_id=0
            )
            
        elif action == 'give_to_razrab':
            db['reports'][user_to]['moder'] = 819016396
            await bot.api.messages.send(
                peer_id=event.object.peer_id,
                message=f'Репорт @id{user_to} передан разработчику\n@id819016396',
                random_id=0
            )
    
    save_db(db)

@bot.on.message(text='вынести <mention>')
async def no_block(message: Message, mention: str = None):
    if message.from_id == 819016396:
        try:
            user = await resolve_resources(mention)
            db['block']['ids'].remove(str(user.id))
            await message.answer(f'Вынес @id{user.id} из списка заблокированных')
        except:
            await message.answer('Не смог найти пользователя!')
    save_db(db)
            
bot.run_forever()