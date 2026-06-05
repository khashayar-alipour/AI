
'''     _______________________________________
        \    template  -  /start  -  /help     \
         =======================================
'''
# در این فایل template اصلی رو در قالب main میسازیم.
# همچنین اینجا دستورات /start و /help رو در ابتدا تعریف کردیم.



from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram import Update 
from telegram.ext import ContextTypes



#_______________________________[ /start ]_____________________________________

# وقتی کاربر زد روی /start فلان متن رو واسش بفرست.
async def start_func(update: Update, context: ContextTypes.DEFAULT_TYPE):     
    await update.message.reply_text('سلام به ربات فناوری مهندسی اینگلیسی خوش آمدید .')
#______________________________________________________________________________




#______________________________[ /help ] ______________________________________

# اگه روی /help زد این text که نوشتم رو براش reply کن.
async def help_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
    سلام به بخش کمک بات خوش امدید
    دستورات موجود:

    استارت : /start
    کمک : /help
    """
    await update.message.reply_text(text)
#______________________________________________________________________________




#_____________________________[ error handler ]________________________________

# این خط همیشه همینطوری نوشته میشه
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")
#______________________________________________________________________________




#______________________________________________________________________________
def main():
    
    # این خط برنامه مارو با این توکن که بهش دادیم وصل میکنه به بات که در @Botfather ساختیم    
# این توکن مخصوص باتی هست که در @Botfather گرفتیم    
    TOKEN = '7595970797:AAHneoE0fNQrw1Uhn9_hgaxBYPMsHkr20cI'    
    application = Application.builder().token(TOKEN).build()     


    # اگه کسی روی /start زد وصلش کن به start_func()    
    application.add_handler(CommandHandler('start',start_func))

 
    # اگه کسی روی /help زد وصلش کن به help_func()    
    application.add_handler(CommandHandler('help',help_func))


    # این خط ارورها رو هندل میکنه.    
    application.add_error_handler(error_handler)
     
    
    # اگه run شدی همیشه روی run بمون    
    application.run_polling()
#______________________________________________________________________________




if __name__ == "__main__":
    main()