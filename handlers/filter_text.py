from aiogram import Bot, Dispatcher, Router, types, F, html
from aiogram.types import Message, CallbackQuery
from aiogram.types import InputFile, FSInputFile
from aiogram.methods.send_photo import SendPhoto
from aiogram.filters import Filter, Command
from aiogram import Bot, Dispatcher, types, F
import os
import random

router_filter = Router()

SAVOCHKIN_PHRASE = [
    'савочкин', 'savochkin', 'савочкину', 'савочкиным', 'савочкін', 'савочкіну', 'савочкіним',
    'владислав савочкін', 'владислав савочкин', 'владиславу савочкину', 'влад савочкин',
    'савочкин', 'савочкін', 'владислав савочкін', 'владислав савочкин', 'савочкину', 'савочкина',
    'савок'
]

SKAKUN_PHRASE = [
    'скакун', 'скакунчик', 'артем скакун', 'skakun', 'артём скакун', 'админ скакун'
]

RAZE_PHRASE = [
    'raze', 'рейз', 'рейзы'
]

MISA_PHRASE = [
    'миса', 'misa', 'люблю мису'
]


MISA_TO_SAVOCHKIN = [
    'Я чула що Савочкін син шл...? Це правда? 🤭', 'Савочкін? Тут всі кажуть що він га*дон 🤭',
    'Ооо.. я чула про Савочкіна, мені шкода його...', 'А правда що всі Рейзи були в гостях у Савочкіна? 🤭',
    'Знаєте, якщо обирати кого вбити: свиню чи Савочкіна? Я врятую свинку 🐷', 'Гидко від цієї людини 🤧',
    'Покійся з миром, мама Владислава Савочкіна 🤭'
]

MISA_TO_ANSWER = [
    'Сонечко, я тебе не розумію.', 'Не знаю про що ти..', 'Давай краще пограємо в /dick?🤭'
]

MISA_GO_PHOTO = [
    'миса покажи себя', 'миса фото', 'миса фотку', 'миса как ты выглядишь?', 'фото мисы', 'misa фото',
    'фотку скинь миса', 'миса скинь фотку', 'миса покажись', 'миса отправь фото', 'міса фото', 'міса фотку',
    'міса скинь фотку', 'міса відправ фото', 'міса покажи себе', 'фото міси', 'міса як ти виглядаєш?']

MISA_GO_MUR = [
    'мур', 'котик', 'киса', 'помурчи', 'киця']

MISA_PHOTO = ['https://cdn.kanobu.ru/editor/images/94/85d6b137-18cb-4996-8a1c-20518b6b8b01.webp',
              'https://cdn.kanobu.ru/editor/images/81/a8f42e62-7b0d-4dfc-aa4a-bf6ca665ac42.webp',
              'https://cdn.kanobu.ru/editor/images/52/21db48de-ad64-4101-afa8-74d14a28f98a.webp',
              'https://cdn.kanobu.ru/editor/images/17/6099d065-f5ae-41f0-b16b-3ea5cb3e561c.webp',
              'https://kalix.club/uploads/posts/2022-12/1671581774_kalix-club-p-misa-amane-oboi-krasivo-6.jpg',
              'https://foni.club/uploads/posts/2023-02/thumbs/1677583640_foni-club-p-tetrad-smerti-misa-art-5.jpg',
              'https://cybersport.metaratings.ru/storage/images/59/3a/593a95b3a540352108c58f96b012880a.jpg',
              'https://puzzleit.ru/files/puzzles/10/9836/_original.jpg',
              'https://pm1.aminoapps.com/6572/12b309a527b30c97bc180630826f5ceb4be56673_00.jpg',
              'https://static.wikia.nocookie.net/deathnote/images/7/74/260624untitled_3_large1.png/revision/latest?cb=20130903190907&path-prefix=ru']


@router_filter.message()
async def filter(message: types.Message):
    if any(word.lower() in message.text.lower() for word in SAVOCHKIN_PHRASE):
        message_misa = random.choice(MISA_TO_SAVOCHKIN)
        await message.reply(message_misa)

    elif any(word.lower() in message.text.lower() for word in SKAKUN_PHRASE):
        await message.reply("Скакун... це той у кого 5 см в штанах? 🤭")

    elif any(word.lower() in message.text.lower() for word in MISA_GO_MUR):
        voicee = FSInputFile("voice/voice_20-10-2023_00-37-03")
        await message.answer_voice(voicee)

    elif message.text.__contains__('@MisaAI_bot'):
        answer_misa = random.choice(MISA_TO_ANSWER)
        await message.reply(answer_misa)

    elif any(word.lower() in message.text.lower() for word in MISA_GO_PHOTO):
        random_photo = random.choice(MISA_PHOTO)
        await message.reply_photo(random_photo, caption='Це я 🤭')

    elif any(word.lower() in message.text.lower() for word in MISA_PHRASE):
        await message.reply("Я тут 💗")

    elif any(word.lower() in message.text.lower() for word in RAZE_PHRASE):
        await message.reply('❤️ Рейзы - 100 ❤️')