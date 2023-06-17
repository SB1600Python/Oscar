import logging

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
import aiogram.utils.markdown as md

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Site.settings")

import django
django.setup()

from django.contrib.auth.models import User
from blog.models import Profile
from asgiref.sync import sync_to_async

def chek_password(password):
    if len(password) <=8:
        return not password
    elif len(password) > 8 and len(password) < 26:
        if not password.istitle():
            return not password
        else:
            return password

API_TOKEN = '6200954862:AAF67JhXrUP5xYnyzHPNdiUOYdlqBuTpYS4'

bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

b1 = types.KeyboardButton('/Yes')
b2 = types.KeyboardButton('/No')
b3 = types.KeyboardButton('/login')
b4 = types.KeyboardButton('/Password')
b5 = types.KeyboardButton('/Cancle')

key_client_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
key_client_1.row(b1, b2)
register = types.ReplyKeyboardMarkup(resize_keyboard=True)
register.row(b3, b4)
cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add(b5)

class RegistrationForm(StatesGroup):
    login = State()
    password = State()

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    if message.text == '/start':
        await message.answer("Привет %s!\nЯ RegisterBot!\nТы хочешь зарегистрироваться?" % message.from_user.full_name,
            reply_markup=key_client_1)
    elif message.text == '/help':
        await message.answer("Напиши /start чтобы начать")

@sync_to_async
def check_user(username):
    try:
        profile = Profile.objects.get(username=username)
        if profile:
            return False
        else:
            return True
    except:
        return True

@dp.message_handler(commands=['Yes', 'No'])
async def check_answer(message: types.Message):
    if message.text == '/Yes':
        await RegistrationForm.login.set()
        await message.reply("Придумайте логин", reply_markup=cancel)
    elif message.text == '/No':
        await message.answer("%s Может зарегистрируешься?" % message.from_user.full_name, reply_markup=key_client_1)


@dp.message_handler(state="*", commands=["Cancle"])
@dp.message_handler(Text(equals="Cancle",ignore_case=True), state="*")
async def cancel_handler(message:types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return False
    
    logging.info("Cancelling state", current_state)
    await state.finish()
    await message.reply("Cancle", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=RegistrationForm.login)
async def process_login(messege: types , state: FSMContext):
    async with state.proxy() as data:
        data["login"]= messege.text

        await RegistrationForm.next()
        await messege.reply("Input password")

@dp.message_handler(lambda message: not chek_password[message.text], state=RegistrationForm.password)
async def process_password(messege: types):
    return await messege.reply(
        "Пароль должен бути  з великої букви і в паролі должно бути більше 8 символов"
    )




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)