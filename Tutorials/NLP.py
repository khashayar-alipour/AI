
'''
===============================================================================
===============================================================================
================       Created on Thu Oct  8 22:08:17 2026     ================
================                IDE: Spyder                    ================
================         Author: Khashayar Alipour             ================
================        Natural Language Processing (NLP)      ================
===============================================================================
===============================================================================
'''




#✅ 1-NLP intro

#✅ 2-Tokenization

#✅ 3-Tokenizer

#✅ 4-Vocabulary

#✅ 5-Numerical representation

#✅ 6-Embedding -> Embedding models / genism library

#✅ 7-Word2vec model -> CBOW model / Skip-gram model / genism library

#✅ 8-SpaCy library for NLP

#✅ 9-NLTk(Natural Language Toolkit) library for NLP

#✅ 10-NLP pipeline: from start to end







'''
====================================
=======  ⭐  NLP intro  ⭐  =======
====================================
'''

# تعریف: NLP یکی از شاخه‌های AI است که هدفش اینه که کامپیوتر بتونه زبان انسان را دریافت، پردازش، درک و تولید کند
# کامپیوتر در نهایت باید متن را به عدد تبدیل کند تا Neural Network بتواند با آن کار کند

# کاربردهای NLP
#               NLP
#                │
#     ┌──────────┼──────────┐
#     ↓          ↓          ↓
#  Text       Speech      Chat
#     │          │          │
#     ↓          ↓          ↓
# Translation  Speech      Chatbots
# Sentiment    Recognition
# Summarization
# Classification






'''
===========================================
=======  ⭐  NLP Tokenization  ⭐  =======
===========================================
'''

# این مفهموم یعنی شکستن یک متن به بخش های کوچکتر به نام Token

# I love machine learning
# ["I", "love", "machine", "learning"]
# I       → Token
# love    → Token
# machine → Token
# learning→ Token


# اما Token لزوماً همیشه یک کلمه نیست.
# می‌تواند شامل:
# یک کلمه
# بخشی از یک کلمه
# یک punctuation
# یا حتی یک character باشد

# مثلا "unbelievable" ممکن است به شکل زیر Tokenize شود که این بستگی به tokenizer مورد استفاده داره:
    # ["un", "believ", "able"]
    


# ----------------انواع مدل Tokenization ----------------

"✅ 1-Word-Level Tokenization"

# در این روش، متن معمولاً بر اساس کلمات تقسیم می‌شود
# I love machine learning!
# Tokens -> I   love   machine   learning!

# هر کلمه یک Token محسوب می‌شود. البته اینکه علامت ! جدا شود یا همراه کلمه بماند، به روش Tokenizer بستگی دارد

# مزیت: ساده و قابل فهم است
# مشکل: کلمات جدید یا کلماتی که در Vocabulary وجود ندارند، دردسرساز می‌شوند
# مثلاً اگر مدل کلمه unhappiness را ندیده باشد، ممکن است نتواند آن را به‌درستی نمایش دهد



"✅ 2-Character-Level Tokenization"

# در این روش، هر کاراکتر یک Token است
# cat
# tokens -> c  a  t

# مزیت: تقریباً هر کلمه‌ای را می‌توان با کاراکترهایش ساخت و مشکل کلمات ناشناخته کمتر می‌شود
# مشکل: توالی‌ها طولانی‌تر می‌شوند و مدل باید برای درک معنی، از تعداد بیشتری کاراکتر استفاده کند



"✅ 3-Subword-Level Tokenization"

# این روش یکی از مهم‌ترین روش‌ها در NLP مدرن است و در بسیاری از مدل‌های زبانی استفاده می‌شود
# ایده‌اش چیست؟
# به‌جای اینکه همیشه کل کلمه را یک Token بگیریم یا آن را به تک‌تک حروف بشکنیم
# کلمه را به زیرکلمه‌ها (Subwords) تقسیم می‌کنیم

# unhappiness
# tokens -> un  happi  ness

# مزیتش اینه که مدل میتونه قسمت‌های مشترک کلمات را یاد بگیرد. مثلاً un- در کلماتی مانند unhappy و unknown دیده میشه

# سه الگوریتم مشهور برای Subword Tokenization عبارت‌اند از:
    # BPE (Byte Pair Encoding)
    # WordPiece
    # Unigram Language Model



"✅ 4-BPE — Byte Pair Encoding"

# با قطعات کوچک شروع می‌کند و به‌تدریج قطعاتی را که زیاد کنار هم دیده می‌شوند، با هم ادغام می‌کند
# فرض کن در دیتاست این کلمات را داریم:
    # low
    # lower
    # lowest

# ابتدا ممکن است کلمات به قطعات کوچک تقسیم شوند:
    # l | o | w
    # l | o | w | e | r
    # l | o | w | e | s | t

# سپس الگوریتم جفت‌های پرتکرار را ادغام می‌کند:
    # l + o → lo
    # lo + w → low

# بعد می‌تواند low را به‌عنوان یک Token نگه دارد و از آن برای ساخت کلمات دیگر استفاده کند



"✅ 5-WordPiece"

# این روش هم کلمات را به زیرکلمه‌ها تقسیم می‌کند، اما معیار انتخاب قطعاتش با BPE یکسان نیست؛ 
# انتخاب قطعات بر اساس مناسب بودن آن‌ها برای مدل‌سازی زبان انجام می‌شود

# unwanted
#    ↓
# un | ##want | ##ed
# علامت ## در این مثال نشان می‌دهد که قطعه به ادامه کلمه متصل است؛
# این شیوه نمایش در Tokenizerهای WordPiece مانند BERT دیده می‌شود



"✅ 6-Unigram Language Model"

# در روش Unigram، معمولاً ابتدا مجموعه‌ای از قطعات احتمالی در نظر گرفته می‌شود
# سپس الگوریتم بررسی می‌کند کدام قطعات برای نمایش متن مناسب‌ترند و به‌تدریج قطعات کم‌فایده را حذف می‌کند

# مثلاً برای کلمه playing چند تقسیم‌بندی ممکن است وجود داشته باشد:
    # playing
    # ├── play | ing
    # ├── play | i | n | g
    # └── p | l | a | y | i | n | g
# حالا Tokenizer بر اساس مدل آماری خود، یکی از تقسیم‌بندی‌های مجاز را انتخاب می‌کند

# تفاوت شهودی با BPE:
#  روش BPE: قطعات را با ادغام جفت‌های پرتکرار می‌سازد
# روش Unigram: از مجموعه‌ای از قطعات شروع می‌کند و قطعات نامناسب را حذف می‌کند
# این روش در SentencePiece قابل استفاده است









'''
=====================================
=======  ⭐  Tokenizer  ⭐  ========
=====================================
'''

# به زبان ساده، Tokenizer ابزاریه که متن را به Token تبدیل می‌کند و هر Token را به Token ID مربوط به آن نگاشت می‌کند
# یعنی پروسه Tokenization و اختصاص دادن ID (یا برعکس) توسط Tokenizer انجام میشه
# هر Tokenizer شناسه‌های مخصوص خودش را دارد
# این ابزار یکی از اولین مراحل پردازش متن در مدل‌های NLP و LLM است


# حالا Tokenizer چطوری ساخته میشه؟
# درواقع Tokenizer معمولاً پیش از آموزش مدل اصلی، روی مجموعه‌ای از متن‌ها
# آموزش داده می‌شود. این فرایند را Tokenizer Training می‌نامیم و 4 مرحله دارد.

"------------------------------------"
# مرحلهٔ اول: جمع‌آوری متن‌ها (Corpus)
# تعداد زیادی متن از کتاب‌ها، مقاله‌ها، وب‌سایت‌ها و منابع دیگر جمع‌آوری می‌شوند
# book1.txt
# poem.txt
# book2.txt
# ...

"-------------------------------------"
# مرحلهٔ دوم: انتخاب روش Tokenization
# مشخص می‌کنیم متن با چه روشی به Token تبدیل شود؛ مثلاً Word-Level، Character-Level یا Subword-Level

"-------------------------------------"
# مرحلهٔ سوم: ساخت Vocabulary
# الگوریتم Tokenizer (مثلا BPE) تعیین می‌کند کدام Tokenها در واژگان قرار بگیرند و برای هرکدام یک ID اختصاص داده می‌شود

"-------------------------------------"
# مرحلهٔ چهارم: ذخیرهٔ Tokenizer
# اینجا Vocabulary و قوانین تقسیم متن ذخیره می‌شوند تا بعداً متن‌های جدید با همان قواعد پردازش شوند


# بعد از ساخت Tokenizer حالا Neural Network Training اتفاق میوفته
# دریافت Token IDها  -->  یادگیری Embeddingها  -->  یادگیری وزن‌های شبکهٔ عصبی
# برای یک مدل ازپیش‌آموزش‌دیده، Vocabulary و قواعد Tokenizer معمولاً ثابت می‌مانند
# درحالی‌که وزن‌های شبکه، از جمله Embeddingها، طی آموزش یاد گرفته می‌شوند






'''
=====================================
=======  ⭐  Vocabulary  ⭐  =======
=====================================
'''
# تعریف: Vocabulary یعنی مجموعه تمام Tokenهایی که یک Tokenizer می‌تواند به‌عنوان واحدهای شناخته‌شده در نظر بگیرد
# به زبان ساده، تصور کن می‌خواهیم به کامپیوتر یاد بدهیم متن را بخواند
# ابتدا باید مشخص کنیم چه کلمات یا قطعاتی را می‌تواند بشناسد. مجموعه این قطعات، Vocabulary نام دارد

# مثلا یک vocab فرضی:
    # Vocabulary
    # -----------
    # 0  → [PAD]
    # 1  → [UNK]
    # 2  → I
    # 3  → love
    # 4  → machine
    # 5  → learning
    # 6  → AI
    # 7  → !
# هر Token یک Token ID دارد. این شناسه صرفاً برای شناسایی Token است و به‌خودی‌خود معنای آن را نشان نمی‌دهد.


# -------------مراحل ساخته شدن یک vocabulary-----------

# فرض کنیم دیتاست ما این جملات رو داره:
    # I love AI
    # I love machine learning
    # I love machine learning!

    
"[1]-Gathering the texts"
# ابتدا مجموعه‌ای از متن‌ها را برای ساخت Tokenizer در اختیار داریم
# به این مجموعه، در این مثال، Training Corpus می‌گوییم


"[2]-Primary tokenization"
# فرض کنیم از Word-Level Tokenization استفاده می‌کنیم:
#     I love AI
#         ↓
# ["I", "love", "AI"]

# I love machine learning
#           ↓
# ["I", "love", "machine", "learning"]

# با کنار هم گذاشتن Tokenها، کلمات منحصربه‌فرد را پیدا می‌کنیم.


"[3]-Deleting repeated tokens"
# کلمه I سه بار ظاهر شده است، اما در Vocabulary فقط یک بار ثبت می‌شود

# کلمه های ثبت شده از متن tokenها:
    # I   love   AI   I   love   machine   learning   I    love    machine    learning!

# پس از حذف موارد تکراری:
    # I  love   AI   machine   learning   learning!


"[4]-Assigning token ID"
# حالا به هر Token یک شناسه اختصاص می‌دهیم
# مثلا به یکی 0 میدیم به یکی 1 میدیم به یکی 2 میدیم و ...

# Token      Token ID
# [PAD]        0
# [UNK]        1
# I	         2
# love         3
# AI           4
# machine      5
# learning     6

# اینجا [PAD] برای پرکردن دنباله‌های کوتاه‌تر تا طول یکسان استفاده می‌شود
# همچنین [UNK] هم در بعضی Tokenizerها برای Token ناشناخته به کار می‌رود
# همه Tokenizerها الزاماً از این دو مورد استفاده نمی‌کنند

# در نتیجه این جمله (I love AI) تبدیل میشه به [2, 3, 4]








'''
===================================================
=======  ⭐  Numerical representation  ⭐  =======
===================================================
'''
# مشکل اینه که token ها هنوز حروف هستند
# ولی Neural Network با اعداد کار میکنه نه حروف

# پس Numerical Representation به شکل ساده فقط یک ID است
# به هر توکن فقط یه عدد اختصاص میده تا برای شبکه عصبی خوانا بشه

# "I love AI"
# "I"   → 1
# "love"→ 2
# "AI"  → 3


# ویژگی مهم numerical represent اینه که این اعدادی که به هر توکن اختصاص داده میشن فقط نقش ID دارن
# و هیچ رابطه معنایی خاصی رو نشون نمیدن
# مثلا اینجا چون AI بهش عدد 3 داده شده به این معنی نیست از I که عدد 1 بهش داده شده، بزرگتره
# AI > I    3 > 1






'''
====================================
=======  ⭐  Embedding  ⭐  =======
====================================
'''
# درواقع Embedding یعنی تبدیل یک Token به یک Vector از اعداد
# که بتواند اطلاعات معنایی و روابط بین کلمات را بهتر نمایش دهد

# کلماتی که از نظر معنایی به هم نزدیکن، Embedding آنها نیز معمولاً در فضای برداری به هم نزدیک خواهد بود
# مثلا cat و dog به هم نزدیکن چون هردو حیوان هستند ولی car باهاشون فاصله داره
# cat
#  ↓
# [0.21, 0.72, -0.13, 0.45, ...]

# dog
#  ↓
# [0.19, 0.68, -0.10, 0.42, ...]

# car
#  ↓
# [-0.73, 0.11, 0.91, -0.25, ...]


# در واقع Embeddingها معمولاً ده‌ها، صدها یا حتی هزاران بُعد دارند، نه فقط دو بعد
# هر کلمه در یک فضای چندبعدی قرار گرفته ولی اینجا برای ساده شدن، فقط دو بُعد را تصور کنیم
# ویژگی مهم embedding ها اینه که فاصله و موقعیت Vectorها می‌تواند روابط معنایی را نشان دهد

#           ↑
#     dog ● │
#        ● cat
#           │
#           │                 ● car
#           │
#           └────────────────────────→


# اعدادی که در embedding به هر توکن اختصاص داده میشه ممکن است در ابتدا تصادفی باشند
# ولی مدل در طول Training آنها را تغییر می‌دهد تا برای انجام Task بهتر شوند
# مثلاً در طول آموزش، ممکن است یاد بگیرد که این 3 کلمه در فضای Embedding نسبتاً نزدیک باشند:
    # cat  dog  horse
    


"--------------------"
"✅ Embedding models"
"-------------------"

# همانطور که گفتیم Embedding روشی برای تبدیل یک Token یا آیتم به یک بردار عددی (Vector) است
# که در آن، اطلاعاتی دربارهٔ ویژگی‌ها یا معنای آن آیتم قابل یادگیری است

# با embedding به‌جای یک عدد ساده، می‌توانیم برای هر کلمه یک بردار داشته باشیم
# مثلا به cat عدد 1 داده بودیم الان تبدیل میکنیم به [0.8, 0.7, 0.1, ...]
# این بردار می‌تواند صدها یا هزاران عدد داشته باشد؛ تعداد دقیق آن به Embedding model بستگی دارد

# هر بردار مجموعه‌ای از اعداد است. این اعداد به‌صورت مستقیم برچسب‌هایی مثل «حیوان بودن» یا «وسیلهٔ نقلیه بودن» نیستند
# بلکه مدل طی آموزش، الگوهایی را یاد می‌گیرد که می‌توانند ویژگی‌های معنایی و ارتباطی را منعکس کنند

# پس Token ID: شناسهٔ Token است
# و Embedding Vector: نمایش عددیِ قابل‌آموزش آن Token است


"-------------------------"
# حالا Embedding model چیه؟
# یک مدل یادگیری ماشین است که متن را دریافت می‌کند و آن را به یک بردار عددی تبدیل می‌کند
# پس عملیات embedding توسط embedding model انجام میشه

# این مدل‌ها در دل خودشون به ترتیب مراحل زیر رو انجام میدن:
    # اول میان ورودی رو دریافت میکنن، سپس با استفاده از یک tokenization algorith عملیات tokenization رو انجام میدن
# سپس وقتی متن ورودی تبدیل به token شد، میان این توکن هارو تبدیل به Token ID میکنن
# در مرحله سوم Token ID تبدیل به embedding میشه و embedding matrix ساخته میشه
# در مرحله چهارم پردازش توسط Neural Network انجام میشه
# در این مرحله شبکه با توجه به کلمات اطراف، ترتیب کلمات و الگوهایی که در زمان آموزش یاد گرفته است، بردارهای جدیدی تولید
# مرحله پنجم ساخت نهایی embedding هست.
# اینجا اگر هدف، تبدیل کل جمله به یک بردار باشد، مدل باید نمایش Tokenهای جمله را به یک نمایش واحد تبدیل کند
# این کار بسته به معماری مدل می‌تواند با روش‌هایی مانند Mean Pooling یا یک لایهٔ مخصوص انجام شود


"----------------------"
# Embedding matrix
# مدل یک جدول قابل‌آموزش به نام Embedding Matrix دارد
# فرض کن Vocabulary مدل ۱۰٬۰۰۰ توکن داشته باشد و هر بردار ۳۰۰ بُعد داشته باشد. در این صورت، جدول Embedding به‌طور ساده چنین شکلی دارد:
# E∈R10000×300      یعنی ۱۰٬۰۰۰ ردیف داریم و هر ردیف شامل ۳۰۰ عدد است.

# ___________________________________________________________________________
# |         ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●                                   |
# |  ID 12  ●●●●●●●●●●●                                300 values           |
# |         ●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●                              |
# |                                                                         |
# |         ●●●●●●●●●●●●●●                                                  |
# |  ID 45  ●●●●●●●●●●●                                300 values           |
# |         ●●●●●●●●●●●●●●●●●●●●●●●●                                        |
# |_________________________________________________________________________|
# نمای شماتیک 2 ردیف از جدول
# وقتی Token ID برابر 12 باشد، مدل ردیف شمارهٔ ۱۲ را از جدول انتخاب می‌کند. در نتیجه، هر Token به یک بردار عددی تبدیل می‌شود


"----------------------"
# Embedding model training
# درواقع Embedding Model هم پارامترهای قابل‌آموزش دارد:
    # Weights: تعیین می‌کنند ورودی‌ها چگونه به نمایش‌های جدید تبدیل شوند
    # Biases: در لایه‌هایی که بایاس دارند، به محاسبات مدل کمک می‌کنند
    # Embedding Matrix: خودش شامل وزن‌های قابل‌آموزش است

# در زمان آموزش، مدل با استفاده از Loss Function، Backpropagation و Optimizer پارامترهای خود را به‌روزرسانی می‌کند
# در یک مدل آماده، معمولاً نیازی نیست خودت از صفر این وزن‌ها را آموزش بدهی. می‌توانی از مدل Pretrained استفاده کنی


"---------------------"
# Types of embedding models

#--------World embedding model-----------
# برای هر کلمه یک بردار می‌سازند. روش‌هایی مثل Word2Vec و GloVe از نمونه‌های شناخته‌شده هستند
# محدودیت: در نمایش‌های ثابت، یک کلمه معمولاً در همهٔ جمله‌ها همان بردار را دارد

#--------Contextual Embedding Models---------
# بردار یک کلمه را با توجه به متن اطرافش تولید می‌کنند
# مدل‌های مبتنی بر Transformer مانند BERT می‌توانند چنین نمایش‌هایی بسازند
# مثال: نمایش bank در جملهٔ مربوط به پول با جملهٔ مربوط به رودخانه فرق می‌کند

#--------Sentence / Text Embedding Models---------
# کل جمله یا سند را به یک بردار تبدیل می‌کنند که برای مقایسهٔ معنایی متن‌ها کاربرد دارد
# نمونه: خانوادهٔ مدل‌های Sentence Transformers
# کاربرد: جست‌وجوی معنایی، پیدا کردن اسناد مرتبط و مقایسهٔ جمله‌ها

# این دسته‌ها کاملاً مستقل از هم نیستند: بسیاری از Sentence Embedding Modelها از مدل‌های Contextual به‌عنوان
# بخش اصلی خود استفاده می‌کنند و سپس یک بردار نهایی برای متن تولید می‌کنند



"----------------------------------------------------------"
"✅ Using pretrained embedding model (SentenceTransformer)"
"---------------------------------------------------------"

# ساخت یک embedding model با کدهای پایتون، با استفاده از کتابخوانه sentence-transformers
# در این مثال یک مدل pre-trained استفاده میشه که 3 جمله رو میگیره و به بردار تبدیل میکنه
# درواقع داریم یک مدل آماده که pretrain شده هست رو، با دیتای خودمون fine tune میکنیم
# در نهایت میتونیم از خروجی که بهمون میده تو جای دیگه استفاده کنیم. مثلا این خروجی رو به عنوان ورودی به یک NN بدیم

# نصب کتابخوانه
# pip install sentence-transformers


from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load a pretrained embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# 2. Prepare sentences
sentences = [
    "I love learning artificial intelligence.",
    "I enjoy studying AI and machine learning.",
    "The weather is sunny today."   ]

# 3. Convert sentences into embedding vectors
embeddings = model.encode(sentences)

# 4. Inspect the output
print("Embeddings shape:", embeddings.shape)      # Embeddings shape: (3, 384)
# برای این مدل معمولاً (3, 384) است، یعنی سه جمله و برای هر جمله ۳۸۴ عدد

# 5. Compare semantic similarity
similarities = cosine_similarity(embeddings)

print("similarity matrix: ", similarities)
# ماتریس شباهت نشان می‌دهد بردار هر جمله چقدر با بردار جمله‌های دیگر شباهت دارد
# [[ 1.          0.8097263  -0.08497867]
#  [ 0.8097263   0.9999999  -0.07035123]
#  [-0.08497867 -0.07035123  1.0000002 ]]



"----------------------------------------------------------"
"✅ Using pretrained embedding model (genism)"
"---------------------------------------------------------"
# اینجا از یه مدل embedding دیگه بنام gensim که pretrained هست میخوایم برای دیتای خودمون استفاده کنیم

# نصب کتابخوانه
# pip install gensim

import gensim.downloader as api

print(list(api.info()["models"].keys()))

model = api.load("glove-wiki-gigaword-100")

v = model["king"]

print(v)
print(v.shape)


#[0.12, -0.43, 0.81, ... ]
#(100,)
model = api.load("word2vec-google-news-300")
model["computer"]



"--------------------------------------------------"
"✅ Building embedding model with Tensorflow/keras"
"-------------------------------------------------"
# استفاده از این روش بصورت دستی هست یعنی پارامترهارو خودمون تنظیم میکنیم

import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=10000, output_dim=64),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
    ])

# اینجا خروجی 1 نورون هست که یک عدد بین 0 تا 1 میده بهمون









'''
==============================================
=======  ⭐  Embedding: word2vec  ⭐  =======
==============================================
'''
# مدل Word2Vec یک روش یادگیری برای ساخت Word Embedding است
# این روش با استفاده از کلمات اطراف یک کلمه در متن، بردارهای عددی یاد می‌گیرد


# The cat drinks milk
# The dog drinks water
# The cat plays with a ball
# The dog plays in the garden
# چون کلمات cat و dog در موقعیت‌های نسبتاً مشابه ظاهر می‌شوند، Word2Vec می‌تواند
#  با یادگیری از کلمات و بافت اطراف آن‌ها بردارهایی یاد بگیرد که بعضی از ویژگی‌های مشترک آن‌ها را منعکس کنند.


# حالا این مدل چطوری کار میکنه؟
# مدل Word2Vec دو معماری معروف دارد:
    # CBOW (Continuous Bag of Words)
    # Skip-gram
# هر دو از بافت کلمات برای یادگیری Embedding استفاده می‌کنند، اما جهت پیش‌بینی آن‌ها متفاوت است


"✅ Continuous Bag of Words"
# ایده: کلمات اطراف یک کلمه را به مدل بدهیم و از مدل بخواهیم کلمهٔ وسط را حدس بزند
# مثلا میخوایم کلمه Drinks رو حدس بزنیم پس میایم کلمات اطرافش یعنی Cat و milk رو input درنظر میگیریم

# The
# cat      --> 1
# [drinks] --> 0
# milk     --> 1

# چرا به آن Bag of Words می‌گویند؟
# در CBOW، کلمات زمینه معمولاً به‌صورت یک مجموعه در نظر گرفته می‌شوند
# یعنی ترتیب دقیق آن‌ها در محاسبهٔ اصلی مدل اهمیت مستقیم ندارد.
# برای مثال، این دو مجموعهٔ زمینه ممکن است نمایش مشابهی تولید کنند:
    # cat drinks milk
    # milk drinks cat
# مدل CBOW کلاسیک به‌طور معمول ترتیب دقیق کلمات زمینه را مثل یک مدل زبانی ترتیبی یاد نمی‌گیرد.


# کاربرد CBOW چیست؟
# یادگیری سریع‌تر Embedding از متن‌های زیاد
# یافتن کلمات مرتبط از نظر کاربرد و بافت
# ساخت ویژگی‌های عددی برای کارهای NLP
# استفاده از بردار کلمات در طبقه‌بندی متن یا تحلیل احساسات



"✅ Skip-gram"

# جهت پیشبینی این مدل برعکس CBOW هست
# یعنی از روی یه کلمه، کلمات اطراف رو پیشبینی میکنه
# مثلا کلمه drinks رو میگیره و میتونه کلمات Cat یا milk رو پیشبینی کنه
# The
# [cat]  --> 0
# drinks --> 1
# [milk] --> 0



"✅ Running Word2Vec with genism library"
# کتابخوانه رایج برای اینکار genims هست
#pip install gensim

from gensim.models import Word2Vec

# A tiny training corpus
sentences = [
    ["cat", "drinks", "milk"],
    ["dog", "drinks", "water"],
    ["cat", "plays", "outside"],
    ["dog", "plays", "outside"],
    ["cat", "likes", "milk"],
    ["dog", "likes", "water"],  ]

# Train a CBOW Word2Vec model
model = Word2Vec(
    sentences=sentences,
    vector_size=20,      # اندازهٔ بردار هر کلمه ۲۰ عدد است
    window=2,   # مدل از کلمات نزدیک در پنجرهٔ زمینه استفاده می‌کند
    min_count=1,   # کلمات حتی اگر فقط یک بار ظاهر شده باشند، نگه داشته می‌شوند
    sg=0,   # if sg=0 -> CBOW model is used   / if sg=1 -> skip-gram model is used
    epochs=200,
    seed=42  )

# Get the embedding vector for "cat"
cat_vector = model.wv["cat"]
print("Vector shape:", cat_vector.shape)
print(cat_vector)

# Find words with similar vectors
print(model.wv.most_similar("cat", topn=3))











'''
===============================================
=======  ⭐  spaCy library for NLP ⭐  =======
===============================================
'''
#  درواقع spaCy یک کتابخانهٔ Python برای NLP است که
# برای ساخت برنامه‌های واقعی و پردازش نسبتاً سریع متن طراحی شده است.

# برخلاف Word2Vec که هدف مشخصش یادگیری بردار کلمات است
# ولی spaCy مجموعه‌ای از ابزارهای آماده برای کار با متن ارائه می‌دهد.

# کاربردهای مهم آن:
# کاربرد اول/Tokenization: تقسیم متن به Token
# کاربرد دوم/POS Tagging: تشخیص نقش دستوری کلمات، مثل اسم و فعل
# کاربرد سوم/Lemmatization: پیدا کردن شکل پایهٔ کلمات
# کاربرد چهارم/Named Entity Recognition (NER): تشخیص نام اشخاص، مکان‌ها، سازمان‌ها و موارد مشابه
# کاربرد پنجم/Dependency Parsing: تحلیل ارتباط دستوری کلمات
# کاربرد ششم/کار با مدل‌های زبانی ازپیش‌آموزش‌دیده


# چه زمانی spaCy مناسب است؟ 
# وقتی می‌خواهی برنامه‌ای بسازی که متن را پردازش کند، اطلاعاتی مثل نام شرکت‌ها
# و مکان‌ها را استخراج کند یا متن را برای مراحل بعدی آماده کند.



"✅ Installing the library" 
# pip install spacy
# !python -m spacy download en_core_web_sm   # نصب نسخه انگلیسی


"-----First use-----"  # Tokenization
import spacy
nlp = spacy.load("en_core_web_sm")  # Load the English NLP pipeline
text = "Apple is opening a new office in Munich."
doc = nlp(text)  # Process the text
for token in doc:  # Print tokens
    print(token.text)

# Apple
# is
# opening
# a
# new
# office
# in
# Munich
# .


"-----Second use------"   # تشخیص نقش دستوری و شکل پایه
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("The cats were running in the gardens.")
for token in doc:
    print(
        token.text,    # نمایش شکل موجود در متن
        token.pos_,    # نمایش نقش دستوری مانند اسم یا فعل
        token.lemma_ ) # نمایش شکل پایه کلمات

# شکل پایه کلمات یعنی: برای مثال، running معمولاً به شکل پایهٔ run تبدیل می‌شود و cats به cat


"-----Third use------"   # تشخیص نام اشخاص و مکان‌ها
# به اینکار Named Entity Recognition (NER) هم میگن
import spacy
nlp = spacy.load("en_core_web_sm")
text = "Apple opened an office in Munich in 2025."
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)

# Apple ORG(سازمان یا شرکت)
# Munich GPE(کشور، شهر یا واحد جغرافیایی سیاسی)
# 2025 DATE(تاریخ یا بازهٔ زمانی)

# خروجی دقیق به مدل و متن بستگی دارد. NER ممکن است بعضی نام‌ها را اشتباه تشخیص دهد











'''
========================================================================
=======  ⭐  NLTK(Natural Language Toolkit) library for NLP ⭐  =======
========================================================================
'''

# این کتابخانه مجموعه‌ای از ابزارهای Python برای یادگیری، آزمایش و اجرای روش‌های مختلف NLP ارائه می‌دهد
# این کتابخوانه به‌خصوص برای آموزش مفاهیم پایهٔ NLP، کار با Corpusها و پیاده‌سازی روش‌های کلاسیک مفید است
# تفاوت کلی آن با spaCy این است که NLTK ابزارهای متنوعی برای یادگیری و آزمایش روش‌های NLP ارائه می‌دهد
# درحالی‌که spaCy برای ساخت Pipelineهای پردازش متن در برنامه‌های کاربردی بسیار مناسب است

# کاربردهای مهم:
# انجام Tokenization
# حذف Stop Words
# Stemming و Lemmatization
# استخراج و تحلیل فراوانی کلمات
# کار با مجموعه‌داده‌های متنی
# آموزش و آزمایش بعضی مدل‌های کلاسیک NLP


"✅ Installing library"
# pip install nltk

# بعضی قابلیت‌های NLTK به منابع جداگانه نیاز دارند. برای مثال، برای استفاده از Stop Words انگلیسی:
    # import nltk
    # nltk.download("stopwords")


"first use"   # Tokenization
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download("punkt_tab")
text = "I am learning NLP with Python!"
tokens = word_tokenize(text)   # این تابع متن را به توکن تبدیل میکنه
print(tokens)   # ['I', 'am', 'learning', 'NLP', 'with', 'Python', '!']


"Second use"  # deleting Stop Words
# درواقع Stop Words کلمات پرتکراری هستند که در بعضی
# کاربردها برای تحلیل متن، اطلاعات متمایزکنندهٔ کمتری دارند؛ مثل the، is و a
# فرض کن بخواهیم کلمات مهم‌تر یک جمله را استخراج کنیم

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
text = "The cat is sitting on the table."
tokens = word_tokenize(text)
stop_words = set(stopwords.words("english"))
filtered_tokens = [
    word for word in tokens
    if word.lower() not in stop_words  ]
print(filtered_tokens)    # ['cat', 'sitting', 'table', '.']



"Third use"  # Stemming
# درواقع Stemming روشی است که معمولاً با حذف بخشی از حروف کلمه، آن را به یک ریشهٔ تقریبی تبدیل می‌کند
# نکتهٔ مهم این است که Stemming همیشه یک کلمهٔ واقعی یا شکل پایهٔ درست تولید نمی‌کند
# برای مثال، studi کلمهٔ معمول انگلیسی نیست؛ این یکی از محدودیت‌های Stemming است

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = [
    "playing",
    "played",
    "plays",
    "studies",
    "studying"  ]

for word in words:
    print(word, "->", stemmer.stem(word))

# playing -> play
# played -> play
# plays -> play
# studies -> studi
# studying -> studi



"Fourth use"   # تحلیل فراوانی کلمات
# با NLTK می‌توانیم بررسی کنیم کدام کلمات در یک متن بیشتر تکرار شده‌اند
# این قابلیت برای تحلیل Corpus، بررسی فراوانی واژگان و شناخت ویژگی‌های یک مجموعهٔ متن کاربرد دارد

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
text = """
Python is useful.
Python is popular.
NLP with Python is interesting.
"""
tokens = word_tokenize(text.lower())
words = [word for word in tokens if word.isalpha()]  # Keep alphabetic tokens only
frequency = FreqDist(words)
print(frequency.most_common(5))    # [('python', 3), ('is', 3), ('nlp', 1), ...]









'''
==========================================================
=======  ⭐  NLP PIPELINE: FROM START TO END  ⭐  =======
==========================================================
'''
# درواقع Tokenizer Training و NN Training دو فرایند متفاوت هستند
# اولی Vocabulary و الگوریتم تقسیم متن را آماده می‌کند، دومی وزن‌های شبکهٔ عصبی را یاد می‌گیرد

# ========================================================
# ========================================================
#                    Raw Text / Corpus
#                           |
#                           v
#                  ______________________
#                  | Tokenizer Training |
#                  ----------------------
#                           |
#                           v
#                  Tokenization Algorithm (BPE, ...)
#                           |
#                           v
#                      Vocabulary
#              (Tokens + their Token IDs)
#                           |
#                           v
#                     Trained Tokenizer
#                           |
#                           v
#                       Input Text
#                           |
#                           v
#                      Tokenization
#                           |
#                           v
#                         Tokens
#                           |
#                           v
#                       Token ID
#                           |
#                           v
#                 Numerical Representation
#                           |
#                           v
#                       Embedding -> Converting each token ID into a processable vector for NN
#                           |
#                           v
#                    Neural Network
#                           |
#                           v
#                     _______________
#                     | NN Training |
#                     ---------------
#                           |
#                           v
#                Learning Weights and Bias
#                           |
#                           v
#                   Trained NLP Model
#                           |
#                           v
#                   Prediction / Generation
#                           |
#                           v
#                    Final NLP Output

# ============================================================
# ============================================================




















































































































































































