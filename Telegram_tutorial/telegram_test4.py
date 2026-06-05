

# callbackqueryhandler --> هندل کردن گزینه ها



from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram import Update 
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler
from telegram.ext import filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler



#___________________________[ /start ]_________________________________________

async def start_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('سلام به ربات فناوری مهندسی اینگلیسی خوش آمدید .')
#______________________________________________________________________________




#____________________________[ /help ]_________________________________________

async def help_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
    سلام به بخش کمک بات خوش امدید
    دستورات موجود:

    استارت : /start
    کمک : /help
    منو : /menu
    """
    await update.message.reply_text(text)
#______________________________________________________________________________





#______________________________[ /text handler ]_______________________________

async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        
    zarf= update.message.text

    if zarf =='سلام':
        await update.message.reply_text('سلام خوبی؟')
    elif zarf =='خوبی':
        await update.message.reply_text('ممنون تو خوبی؟')
    else:
        await update.message.reply_text('من نمی فهمم چی می گی')
#______________________________________________________________________________




#______________________________[ echo ]________________________________________
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    zarf= update.message.text
    await update.message.reply_text(f'you said :{zarf}')
#______________________________________________________________________________






# _____________________[ Inline keywords ( /menu ) ]___________________________

async def menu_func(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("گزینه 1", callback_data="opt1")],
        [InlineKeyboardButton("گزینه 2", callback_data="opt2")],   
    ]  
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('لطفا یک گزینه انتخاب کن',reply_markup =reply_markup )
#______________________________________________________________________________





# ____________________________[ callback_func ]________________________________
async def callback_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
 
    # وقتی کاربر یه message میفرسته برای گرفتن اون پیام update.message.text رو مینوشتیم    
    # ولی زمانیکه کاربر گزینه‌هارو انتخاب میکنه که دیگه پیام نمیفرسته! داره گزینه انتخاب میکنه!    
    # اینجا دیگه چیزی بنام update.message.text نداریم    
# بجاش مینویسیم:    
    query = update.callback_query
    query.answer()  # اینو مینویسیم که منتظر بمونه تا پاسخ رو دریافت کنه


# اینجا query داخلش یک data داره که همون گزینه‌ای هست که کاربر انتخاب کرده    
    
    if query.data=='opt1':
        #await update.message.reply_text('you selected option 1')  دیگه اینجا اینجوری نمینویسیم
        # کار reply_text اینه که به پیام کاربر پاسخ بده        
        await query.edit_message_text(text='شما گزینه یک رو انتخاب کردید')     # بجاش مینویسیم

    elif query.data=='opt2':
        await query.edit_message_text(text='شما گزینه دو رو انتخاب کردید')
#______________________________________________________________________________
    

    


# _________________________[ error_handler ]___________________________________
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")
#______________________________________________________________________________




#______________________________________________________________________________
def main():

    TOKEN = '7595970797:AAHneoE0fNQrw1Uhn9_hgaxBYPMsHkr20cI'
    application = Application.builder().token(TOKEN).build()


    application.add_handler(CommandHandler('start',start_func))
    application.add_handler(CommandHandler('help',help_func))
    application.add_handler(CommandHandler('menu',menu_func))
    application.add_handler(CallbackQueryHandler(callback_func))


    application.add_handler(MessageHandler(filters.TEXT,text_handler))


    application.add_error_handler(error_handler)
    application.run_polling()
#______________________________________________________________________________





if __name__ == "__main__":
    main()