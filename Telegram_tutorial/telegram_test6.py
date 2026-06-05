

'''    _____________________________
      /      SECURITY SYSTEM       /
      ============================

Tip 1 -> Never use password, token, api key or ... inside your codes.
Tip 2 -> Create a .env file for your tokens, where your other files are.
Tip 3 -> .env file should not be commited to github -> use .gitignore file for insurance

creating .env file:
    git bash
    cd -> where your file (telegram_test6.py) is located
    touch .env (a hidden file)
    vim .env
    place your Token here  ->  TOKEN = 'gh21y7d1ydbhhd71hbd1uid313ohdu'
    cat .env
    
'''




from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram import Update 
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler
from telegram.ext import filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram.ext import ConversationHandler




#__________________________[ /start ]__________________________________________

async def start_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_text  = """
    سلام به ربات زبان برنامه نویسی همراه با انگلیسی خوش آمدید 
    برای استفاده 
    ابتدا از ....
    """

    await update.message.reply_text(start_text)
#______________________________________________________________________________






# ______________________________[ dashboard ]__________________________________

#------------- dashboard -> 'NAME'

# این همون entrypoint بنام dashboard هست
async def dashboard_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    # وقتی کاربر نوشت dashboard این text رو بهش نشون بده    
    dashboard_text = """
    سلام اسمتون رو بفرمایید :‌
    """
    await update.message.reply_text(dashboard_text)

    # میخوایم وقتی کاربر نام رو وارد کرد، این نام رو بدیم به یک تابع دیگه   
    # یک اسم رمز روش میزاریم ('NAME') و return میکنیم   
    return 'NAME'
#-------------



#------------- 'NAME' -> 'AGE'

async def name_func(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # این متغیر name همون ورودی کاربر از تابع بالاست که با اسم 'NAME' برگشت داده شد    
    name = update.message.text


    await update.message.reply_text(f'سلام {name} خوش آمدید')
    await update.message.reply_text('سنتون چقدره')
    return 'AGE'      # یک اسم رمز میذاریم و برگشت میدیم
#-------------



#------------- 'AGE' -> 'KEY'

async def age_func(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # متغیر age همون 'AGE' هست که از تابع بالا return شده    
    age = update.message.text

    if age.isdigit():
        age = int(age)
        
        if age >= 8:
            await update.message.reply_text('شما میتونید از ربات استفاده کنید')

            keyword = [
                [InlineKeyboardButton("پرمیوم", callback_data="permium")],
                [InlineKeyboardButton("ساده ", callback_data="basic")],
            ]
            reply_markup = InlineKeyboardMarkup(keyword)

            await update.message.reply_text('لطفا یک گزینه انتخاب کن',reply_markup =reply_markup )
            return 'KEY'

        else:
            await update.message.reply_text('شما نمیتونید از ربات استفاده کنید')
            return ConversationHandler.END
        
    else:
        await update.message.reply_text('سنتون رو به عدد وارد کنید')
        return 'AGE'     # یک اسم رمز میذاریم و برگشت میدیم
#-------------




#-------------
# این تابع میاد بر اساس گزینه هایی که کاربر در تابع بالا انتخاب کرده(permium or basic) یه کاری انجام میده

async def key_func(update: Update, context: ContextTypes.DEFAULT_TYPE):


    query = update.callback_query
    query.answer()

    if query.data=='permium':
        await query.edit_message_text(text='شما پرمیوم انتخاب کردید')
        return ConversationHandler.END
    elif query.data=='basic':
        await query.edit_message_text(text='شما ساده انتخاب کردید')
        return ConversationHandler.END
#______________________________________________________________________________





# __________________________[ error_handler ]__________________________________

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")
#______________________________________________________________________________






#______________________________________________________________________________
def main():


# استفاده از توکن داخل فایل .env اینجوریه:    
    
    #pip install python-dotenv
    from dotenv import load_dotenv
    import os
    load_dotenv()
    TOKEN = os.getenv('TOKEN')


# دیگه اینجوری نمینویسیم، توکن رو با روش امن این بالا گرفتیم و استفاده میکنیم:    
    #TOKEN = '7595970797:AAHneoE0fNQrw1Uhn9_hgaxBYPMsHkr20cI'
    application = Application.builder().token(TOKEN).build()




    # /start
    application.add_handler(CommandHandler('start',start_func))


    # dashboard
    application.add_handler(ConversationHandler(entry_points=[CommandHandler('dashboard',dashboard_func)],
                                                            states={
                                                                'NAME':[MessageHandler(filters.TEXT,name_func)],
                                                                'AGE':[MessageHandler(filters.TEXT,age_func)],
                                                                'KEY':[CallbackQueryHandler(key_func)]
                                                            },
                                                            fallbacks=[])  ) 




    application.add_error_handler(error_handler)
    application.run_polling()
#______________________________________________________________________________






if __name__ == "__main__":
    main()