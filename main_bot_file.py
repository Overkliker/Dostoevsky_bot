from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler, CallbackContext,
)
from main import dost

bot = Bot('5209105577:AAFS0zwZHJ5ubtSO-eIVnemv2t19-dBj-RA')


#keyboard
def cups(name, one_time=False):
    list_with_cups = []
    for i in name:
        list_with_cups.append([i])

    markup = ReplyKeyboardMarkup(list_with_cups, one_time_keyboard=one_time)
    return markup


def start(update, context):
    rep_k = cups(['/analiz'], one_time=True)
    update.message.reply_text('Я бот, который проанализирут твой текст на эмоциональный окрас', reply_markup=rep_k)


#analizing text
def nach(update, context):
    rep_k = cups(['/stop_analiz'], one_time=True)
    update.message.reply_text('Введи сообщение, которое я должен буду проанализировать', reply_markup=rep_k)
    return 1


def analiz_mess(update, context):
    print(update.message.text)

    rep_k = cups(['/analiz'], one_time=True)
    dos = str(''.join([str(i) for i in dost(update.message.text)]))
    message = f'{update.message.text} -> {dos}'
    update.message.reply_text('Вот твой анализ')
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup=rep_k)
    return ConversationHandler.END


def stop_analiz(update, context):
    print('stop')
    rep_k = cups(['/analiz'], one_time=True)
    update.message.reply_text("Пока-пока...", reply_markup=rep_k)
    return ConversationHandler.END


def main():
    updater = Updater(token='5209105577:AAFS0zwZHJ5ubtSO-eIVnemv2t19-dBj-RA', use_context=True)
    dp = updater.dispatcher

    st = CommandHandler('start', start, pass_chat_data=True)
    analiz = ConversationHandler(
        entry_points=[CommandHandler('analiz', nach, pass_chat_data=True)],
        states={1: [MessageHandler(~ Filters.command, analiz_mess)]},
        fallbacks=[CommandHandler('stop_analiz', stop_analiz)]
    )

    dp.add_handler(st)
    dp.add_handler(analiz)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
