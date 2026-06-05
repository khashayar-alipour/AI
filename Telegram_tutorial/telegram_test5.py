

'''    ________________________________________________
      /       conversationhandler  -  dashboard       /
      ===============================================
      
'''

# در این فایل تمام قسمتهایی که در فایل های قبلی ساختیم رو میذاریم داخل یک داشبورد.

# تا الان ما میدونستیم که application رو داریم
# حالا application از کاربرها ورودی میگرفت، و باید فانکشن هایی میساختیم که بتونه این ورودی هارو هندل کنه. مثلا:

# command_handler:
    # اومدیم command هایی مثل /start رو به یه تابع وصل کردیم و سپس با await update.message.reply_text بهشون پاسخ میدادیم
    
# message_handler:
    # وقتی از سمت کاربر یک message بیاد با update.message.text پیام کاربر رو میگرفتیم و با update.message.reply_text بهش پاسخ میدادیم

# inlinekeyboardbutton:
    # اینو هرجا بیاریم میتونیم باهاش یک گزینه بسازیم و یک مخفف.

# callbackqueryhandler:
    # اگر کاربر به گزینه هایی که ساختیم پاسخ داد (یعنی callback کرد) میایم گزینه کاربر رو با update.callback_query.data میگیریم
# و با استفاده از query.edit_message_text بهش پاسخ میدیم

# ----------------

# conversationhandler
# حالا میخوایم بخش های مختلف رو از هم جدا کنیم و بزاریم کاربر تو هر قسمت که رفت، فقط همونجا به یه سری چیزها دسترسی داشته باشه
# وظیفه conversationhandler اینه که همه چیز رو local local کنه و از هم جدا کنه
# توی دل خودش commandhandler و messagehandler و callbackquery و ... همرو داره




from telegram.ext import Application
from telegram.ext import CommandHandler
from telegram import Update 
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler
from telegram.ext import filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram.ext import ConversationHandler




#_______________________________[ /start ]_____________________________________

async def start_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_text  = """
    سلام به ربات زبان برنامه نویسی همراه با انگلیسی خوش آمدید 
    برای استفاده 
    ابتدا از ....
    """

    await update.message.reply_text(start_text)
#______________________________________________________________________________





# _______________________________[ dashboard ]_________________________________

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








# _____________________________[ error_handler ]_______________________________

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")
#______________________________________________________________________________








#______________________________________________________________________________
def main():

    TOKEN = '7595970797:AAHneoE0fNQrw1Uhn9_hgaxBYPMsHkr20cI'
    application = Application.builder().token(TOKEN).build()


    application.add_handler(CommandHandler('start',start_func))



# داخل conversationhandler ما entrypoit داریم که یعنی با چی شروع بشه    
# اینجا میگیم entrypoint ما بشه Dashboard و اگه این وارد شده تابع Dashboard_func رو صدا بزن    
# تابع dashboard_func میاد یک نام از کاربر میگیره و در ادامش نمیذاره کاربر ازونجا خارج بشه، بصورت پیوسته وصلش میکنه به یجای دیگه    
# اینجا میگیم که اگه 'NAME' برگشت داده شد، تابع name_func منتظره    
# اگه از دل name_func اینجا 'AGE' برگشت داده شد تابع age_func منتظره    
# اگه از دل age_func اینجا 'KEY' برگشت داده شد فلان کار رو بکن    
    
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