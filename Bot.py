
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
import Main_bot as Mb
from datetime import datetime as dt
import os


def bot_start (update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Тута, я тута, чего надобно?')

def bot_hello (update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}. Если вам нужна помощь, выполните команду /help')

def bot_bye  (update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Сладких снов {update.effective_user.first_name}. Текущее время {dt.now()}')

def bot_log  (update: Update, context: CallbackContext) -> None:
    with open('log.txt','r') as f:
        update.message.reply_text(f.read())

def bot_cleanlog  (update: Update, context: CallbackContext) -> None:
    os.remove('log.txt')
    update.message.reply_text('Логи почищены')
    
def bot_help (update: Update, context: CallbackContext) -> None:
    help_text = 'Для проведения расчетов введите ОДНОСЛОЖНОЕ выражение в следующем формате\n'\
                'calc#<первое число> <оператор> <второе число>\n'\
                'При вводе выражения в неверном формате (введено более одного оператора; вместо чисел введены буквы и т.д.) программа выдаст ошибку\n'\
                'Для просмотра логов требуется выполнить операцию /log'
    update.message.reply_text(f'Справка по работе калькулятора:\n{help_text}')

def answer (update: Update, context: CallbackContext) -> None:
    words = update.message.text.replace(' ','').split('#')
    if words[0] == 'calc':
        ans = Mb.main(update.message.text)
        update.message.reply_text(f'Результат вычисления: {ans}')
    else:
        update.message.reply_text(f'Yo no comprendo que es: {update.message.text}. Для работы с программой ознакомьтесь со справкой через команду /help')


updater = Updater('5786750473:AAEjBhZmd3bevTWncEueZ5-fb6AYtDp8PdM')
updater.dispatcher.add_handler(CommandHandler('start', bot_start))
updater.dispatcher.add_handler(CommandHandler('hello', bot_hello))
updater.dispatcher.add_handler(CommandHandler('help', bot_help))
updater.dispatcher.add_handler(CommandHandler('bye', bot_bye))
updater.dispatcher.add_handler(CommandHandler('log', bot_log))
updater.dispatcher.add_handler(CommandHandler('cleanlog', bot_cleanlog))
updater.dispatcher.add_handler(MessageHandler(callback=answer,filters=None))


updater.start_polling()
updater.idle()

