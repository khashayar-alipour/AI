
'''       _______________________________
         \        creating a server      \
          ================================
'''


# حالت TEST
# تازمانیکه لپتاپ روشنه و فایل تلگرام run هست بات کار میکنه


# حالت PRODUCTION
# باید سرور بخریم و روی سرور run کنیم

# فارس پک  -  یا لینود  -> 1 یا 2 گیگ رم - لینوکس (ubuntu - debian)
# دو راه برای run شدن روی سرور -> terminal کامپیوتر  -  برنامه terminus


# بعد از خرید سرور یک IP و Password داریم

'''
Terminus:
    1- NEW HOST (top left)
    2- Address (top right) -> enter server IP
    3- General > Label = optional name 
    4- SSH on 22 port
    5- root = username  |  password = was written by me while buying the server
    6- connect
    7- add and continue
'''



# داخل TERMINUS بعد از اتصال یک ترمینال بالا میاد:

root@localhost:~# pwd
/root
root@localhost:~# cd /    ->  go to the first directory possible
root@localhost:/# pwd
/
root@localhost:/# ls
bin   dev  home  lib32  libx32      media  opt   root  sbin  srv  tmp  var
boot  etc  lib   lib64  lost+found  mnt    proc  run   snap  sys  usr
root@localhost:/# cd root
root@localhost:~# ls      -> root is empty


# اول باید آپدیت کنیم
sudo apt update


# ساخت یک دایرکتوری برای بات تلگرام خودمون
mkdir telegram_bot
cd telegram_bot


# ساخت یک محیط مجازی بنام TEL برای پروژه تلگرام خودمون
apt install python3.10-venv
python3 -m venv TEL




root@localhost:~/telegram_bot   #ls
TEL
root@localhost:~/telegram_bot   #source TEL/bin/activate   فعال کردن محیط مجازی که ساختیم
(TEL) root@localhost:~/telegram_bot

# ________ از الان به بعد دیگه توی محیط TEL هستیم ________

(TEL) root@localhost:~/telegram_bot   # touch bot.py
(TEL) root@localhost:~/telegram_bot   # vim bot.py  ->  copy telegram_test6 final codes
(TEL) root@localhost:~/telegram_bot   # ls
bot.py  TEL
(TEL) root@localhost:~/telegram_bot   # vim .env  ->  copy TOKEN here
(TEL) root@localhost:~/telegram_bot   # ls
bot.py  TEL
(TEL) root@localhost:~/telegram_bot   # cat .env
TOKEN = '7595970797:AAHneoE0fNQrw1Uhn9_hgaxBYPMsHkr20cI'

(TEL) root@localhost:~/telegram_bot   # python bot.py  -> run the codes

# error
Traceback (most recent call last):
  File "/root/telegram_bot/bot.py", line 1, in <module>
    from telegram.ext import Application
ModuleNotFoundError: No module named 'telegram'
(TEL) root@localhost:~/telegram_bot# pip install python-telegram-bot
(TEL) root@localhost:~/telegram_bot# pip install python-dotenv

(TEL) root@localhost:~/telegram_bot   # python bot.py  -> run the codes
#-----

# الان دیگه روی سرور کدهای تلگرام رو run کردیم و تا زمانیکه توی لپتاپ برنامه terminus باز باشه بات هم فعاله
# برای اینکه همیشه run بمونه از یک ابزار بنام tmux استفاده میکنیم
# از طریق این ابزار میشه یه چیزی رو run کنیم و تا ابد run بمونه


# _________ tmux __________

sudo apt install tmux   # install
tmux -v   # check if tmux is already installed
tmux new -s mytelegram   # creating a session
python bot.py   # توی این سشن فایل کدها برای همیشه اجرا میشه
ctrl + d + b   # to exit from session
tmux ls   # mytelegram: 1 windows (created Tue Feb 10 18:10:22 2026)
tmux attach -t mytelegram   # to open mytelegram session







