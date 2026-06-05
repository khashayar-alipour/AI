
'''
        _____________________________
        \      inline keywords       \
         =============================   
'''

#(Inlinekeyboardbuttons)
# یک command جدید بنام /menu

# طراحی کردن گزینه


from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram import Update 
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler
from telegram.ext import filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup




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
    
    # متغیر zarf حاوی پیامی هست که کاربر داخل بات ارسال میکنه    
    zarf= update.message.text


    if zarf =='سلام':
        await update.message.reply_text('سلام خوبی؟')

    elif zarf =='خوبی':
        await update.message.reply_text('ممنون تو خوبی؟')

    else:
        await update.message.reply_text('من نمی فهمم چی می گی')
#______________________________________________________________________________






#____________________________[ echo ]__________________________________________
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    zarf= update.message.text
    # user message = "zarf"
    await update.message.reply_text(f'you said :{zarf}')
#______________________________________________________________________________







# ______________________[ Inline keywords ( /menu )  ]_________________________

async def menu_func(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        
        # اینجا میتونیک گزینه هارو طراحی کنیم و براشون اسم بزاریم        
        # برای هر گزینه نیازه که یک مخفف (مثلا opt1) هم بنویسیم        
        [InlineKeyboardButton("گزینه 1", callback_data="opt1")],
        [InlineKeyboardButton("گزینه 2", callback_data="opt2")],
        # میشه در ادامه هر تعداد خواستیم اضافه کنیم .....        
    ]
    
    
    reply_markup = InlineKeyboardMarkup(keyboard)


# اینجا میایم با استفاده از reply_text دو کار انجام میدیم    
# ورودی اول میاد یک text به user نمایش میده    
# ورودی دوم (Reply_markup) میاد گزینه هایی که درست کردیم نشون میده    
    await update.message.reply_text('لطفا یک گزینه انتخاب کن',reply_markup =reply_markup )
#______________________________________________________________________________
    



#____________________________[ error handler ]_________________________________
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")
#______________________________________________________________________________





# _____________________________________________________________________________

def main():

    TOKEN = '7595970797:AAHneoE0fNQrw1Uhn9_hgaxBYPMsHkr20cI'
    application = Application.builder().token(TOKEN).build()


    application.add_handler(CommandHandler('start',start_func))
    application.add_handler(CommandHandler('help',help_func))
    application.add_handler(CommandHandler('menu',menu_func))     # ایجاد دستور منو


    application.add_handler(MessageHandler(filters.TEXT,text_handler))


    application.add_error_handler(error_handler)
    application.run_polling()

# _____________________________________________________________________________




if __name__ == "__main__":
    main()