from loader import dp,bot
from aiogram import types
from random import randint as RI

goal = 28
candy = 0
mode = 0

@dp.message_handler(commands=['set'])
async def mes_set(message:types.Message):
    global candy
    count = message.text.split()[1]
    candy = int(count)
    await message.answer(f'Установили исходное количество конфет в размере {candy}')

@dp.message_handler(commands=['game'])
async def mes_set(message:types.Message):
    await message.answer(f' Игра в 28 конфет начинается!')
    global mode
    global candy
    global step
    global goal
    mode  = 1
    if candy < 28:
       candy = RI(58,113)   
     
    await message.answer(f' На столе {candy} конфет (ы)')
    active_player = RI(1,2)
    if active_player == 1:
        await message.answer(' Первый ход делает Гость:')
    else:
        await message.answer('Первый ход достается Боту:')
        if candy  > 2*goal:
                step = goal
        elif candy == goal+1:
                step = 1
        elif candy <= 2*goal:
                step = (candy-goal)-1
        candy-=step
        await message.answer(f"Бот забирает {step} конфет(ы), на столе остается {candy} конфет (ы)")
        await message.answer('Следующий ход достается Гостю:')
        
@dp.message_handler()
async def mes_all(message:types.Message):
    global candy
    global mode
    if mode == 1:    
        if message.text.isdigit() and (0 < int(message.text) <= 28):
            candy-= int(message.text)
            await message.answer(f'На столе осталось {candy} конфет')
            if candy <= goal:
                await message.answer('Игра завершена, все конфеты достаются Боту!')
                await message.answer('Для запуска новой игры введите /game, для установки исходного количества конфет, введите /set N ')
                mode = 0
            else:
                if candy  > 2*goal:
                    step = goal
                elif candy == goal+1:
                    step = 1
                elif candy <= 2*goal:
                    step = (candy-goal)-1
                candy-=step
                await message.answer(f"Бот забирает {step} конфет(ы),на столе остается {candy} конфет (ы)")
                
                if candy <= goal:
                    await message.answer('Игра завершена, все конфеты достаются Гостю!')
                    await message.answer('Для запуска новой игры введите /game, для установки исходного количества конфет, введите /set N')
                    mode = 0
                else:
                    await message.answer('Следующий ход делает Гость')    
        else:
            await message.answer('Так ходить в этой игре нельзя, введите количество конфет от 1 до 28')           
    elif mode ==0:
         await message.answer('Игра завершена, для запуска введите команду /game, для установки исходного количества конфет, введите /set N') 