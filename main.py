from handler import dp

from aiogram import Bot, Dispatcher, types, executor
async def on_start(_):
    print('Бот запущен')
    
executor.start_polling(dp, skip_updates = True, on_startup = on_start)
