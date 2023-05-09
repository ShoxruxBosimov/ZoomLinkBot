import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text

import Kafedra1
import Kafedra2
import Kafedra3
import Kafedra4

API_TOKEN = '5876598104:AAEyPW6es57N8aHQd84In4oPwvh11Ku3kx0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

button_kafedra1 = KeyboardButton("Jismoniy tarbiya sport nazariyasi va uslubiyati kafedrasi")
button_kafedra2 = KeyboardButton("Pedagogika va psixologiya kafedrasi")
button_kafedra3 = KeyboardButton("Sport boshqaruvi kafedrasi")
button_kafedra4 = KeyboardButton("Ijtimoiy fanlar kafedrasi")

keyboard0 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_kafedra1).add(
    button_kafedra2).add(
    button_kafedra3).add(button_kafedra4)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text="Jismoniy tarbiya va sport bo'yicha mutaxassislari qayta tayyorlash va malakasini "
                              "oshirish instituti Kafedralari ", reply_markup=keyboard0)


@dp.message_handler(Text(equals="Jismoniy tarbiya sport nazariyasi va uslubiyati kafedrasi"))
async def send1(message: types.Message):
    await message.answer(text="Jismoniy tarbiya sport nazariyasi va uslubiyati kafedrasi o‘qituvchilari",
                         reply_markup=Kafedra1.keyboard1)
    await message.delete()


@dp.message_handler()
async def send11(message: types.Message):
    if message.text == "Ashur  Normuradov":
        await message.reply(
            "https://us04web.zoom.us/j/7570704239?pwd=M05Takx6WlgySnhvTU5xdTdEbmhJZz09 \n\n\n Идентификатор конференции"
            "757 070 4239 \n"
            "Код доступа 1111")
    elif message.text == "Talipjanov Asqar":
        await message.reply("https://us04web.zoom.us/j/5564798998?pwd=VG4yVytEak4zTTdQUmNrOVAyWDU1QT09 \n\n\n "
                            "Идентификатор конференции: 556 479 8998 \n Код доступа: 6BBsAb")
    elif message.text == "Галина Краснова":
        await message.reply(
            "https://us04web.zoom.us/j/73449660163?pwd=WmtMbHlZS093Nkc3SEdjMlhKMFdrUT09 \n\n\n Идентификатор "
            "конференции:"
            "734"
            "4966 0163 \n Код доступа: 1111")
    elif message.text == "Gayrat Horozov":
        await message.reply(
            "https://us05web.zoom.us/j/7362149007?pwd=bkhtRlNxL3E3SnZCTU1oSFNHcHJNQT09 \n\n\n Идентификатор "
            "конференции:"
            "736 214 9007 \n Код доступа: 1")
    elif message.text == "Ортуғмат Жуманов":
        await message.reply(
            "https://us04web.zoom.us/j/7407929643?pwd=bE0wNm11Y0FQY2hkdjlMWmdDTVZFQT09 \n\n\n Идентификатор "
            "конференции:"
            "740 792 9643 \n Код доступа: 19681203")
    elif message.text == "Ne'matov Bobirbek":
        await message.reply(
            "https://us05web.zoom.us/j/5625197826?pwd=N2svdFZGcFdYb0tBd3ZmTlVycTZlZz09 \n\n\n Идентификатор "
            "конференции:"
            "562 519 7826 \n Код доступа: 333444")
    elif message.text == "Isroilov Shoakrom":
        await message.reply(
            "https://us05web.zoom.us/j/5482597735?pwd=dTVreXJLQXFzdVNrTUp0aVpZUzdJUT09 \n\n\n Идентификатор "
            "конференции:"
            "548 259 7735 \n Код доступа: 1")
    elif message.text == "Boymatov Habibjon":
        await message.reply(
            "https://us04web.zoom.us/j/3640405337?pwd=STU3UzlOSEwyenAyWHkrZVQyaWgyZz09 \n\n\n Идентификатор "
            "конференции:"
            "364 040 5337 \n Код доступа: 88888")
    elif message.text == "Usmonov Aksam":
        await message.reply(
            "https://us04web.zoom.us/j/3845989513?pwd=dTk0NVJHNG9zRXN5TWdCVWVaOURrdz09 \n\n\n Идентификатор "
            "конференции:"
            "384 598 9513 \n Код доступа: 12")
    elif message.text == "Xo'jayev Faxriddin":
        await message.reply(
            "https://us04web.zoom.us/j/9559862049?pwd=RjA3d29CRkp0YlJ5bVFJSlUvMVRaUT09 \n\n\n Идентификатор "
            "конференции:"
            "955 986 2049 \n Код доступа: jB87MS")
    elif message.text == "Pulatovich Baxram":
        await message.reply(
            "https://us05web.zoom.us/j/9911326774?pwd=bTBmSnBPRjF3OExVejFEQUFIeEMrZz09 \n\n\n Идентификатор "
            "конференции:"
            "991 132 6774 \n Код доступа: 71977")
    elif message.text == "Orqaga":
        await message.reply(text="Jismoniy tarbiya va sport bo'yicha mutaxassislari qayta tayyorlash va malakasini "
                                 "oshirish instituti Kafedralari ", reply_markup=keyboard0)


@dp.message_handler(Text(equals="Pedagogika va psixologiya kafedrasi"))
async def send2(message: types.Message):
    await message.answer(text="Pedagogika va psixologiya kafedrasi o‘qituvchilari", reply_markup=Kafedra2.keyboard2)


@dp.message_handler(Text(equals="Sport boshqaruvi kafedrasi"))
async def send3(message: types.Message):
    await message.answer(text="Sport boshqaruvi kafedrasi o‘qituvchilari", reply_markup=Kafedra3.keyboard3)


@dp.message_handler(Text(equals="Ijtimoiy fanlar kafedrasi"))
async def send4(message: types.Message):
    await message.answer(text="Ijtimoiy fanlar kafedrasi o‘qituvchilari", reply_markup=Kafedra4.keyboard4)


executor.start_polling(dp)

""""@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Jismoniy tarbiya va sport bo'yicha mutaxassislari qayta tayyorlash va malakasini oshirish institutiga xush "
        "kelibsiz", reply_markup=keyboard0)


@dp.message_handler()
async def send_welcome1(message: types.Message):
    if message.text == 'Jismoniy tarbiya sport nazariyasi va uslubiyati kafedrasi':
        await bot.send_message(chat_id=message.from_id, text="Jismoniy tarbiya,sport nazariyasi va uslubiyati "
                                                             "kafedrasi O'qituvchilari",
                               reply_markup=Kafedra1.keyboard1)
    elif message.text == 'Pedagogika va psixologiya kafedrasi':
        await bot.send_message(chat_id=message.from_id, text="Pedagogika va psixologiya kafedrasi O'qituvchilari",
                               reply_markup=Kafedra2.keyboard2)
    elif message.text == 'Sport boshqaruvi kafedrasi':
        await bot.send_message(chat_id=message.from_id, text="Sport boshqaruvi kafedrasi O'qituvchilari",
                               reply_markup=Kafedra3.keyboard3)
    elif message.text == 'Ijtimoiy fanlar kafedrasi':
        await bot.send_message(chat_id=message.from_id, text="Ijtimoiy fanlar kafedrasi O'qituvchilari",
                               reply_markup=Kafedra4.keyboard4)


@dp.message_handler(Text(equals=""))
async def send1(message: send_welcome1):
    await message.answer(text='https://us04web.zoom.us/j/7570704239?pwd=M05Takx6WlgySnhvTU5xdTdEbmhJZz09')


@dp.message_handler()
async def send2(message: types.Message):
    if message.text == "Ashur  Normuradov":
        await message.reply(
            "https://us04web.zoom.us/j/7570704239?pwd=M05Takx6WlgySnhvTU5xdTdEbmhJZz09 // Идентификатор конференции "
            "757 070 4239 //"
            "Код доступа 1111")"""
