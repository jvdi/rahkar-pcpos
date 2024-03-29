# آموزش راه اندازی رابط نرم افزاری PCPOS برای حسابداری راهکار
<p>
<img src="https://user-images.githubusercontent.com/40993115/190509697-c185e51a-cf4e-4bef-b22b-1f8a552cd138.PNG" alt="PaX-q80" width="200" height="250" />
<img src="https://user-images.githubusercontent.com/40993115/190509710-d35b8629-b257-4159-aab5-7ccf32709b11.gif" alt="PaX-S800" width="200" height="250" />
</p>

- نحوه کارکرد : اگر تراکنش در حسابداری راهکار به عنوان پرداخت با کارتخوان ثبت شود و کارتخوان مربوطه به برنامه شناسانده شده باشد مبلغ تراکنش بر روی کارتخوان ظاهر می شود - و منتظر کشیدن کارت میشود و در صورت هر اتفاقی به جز موفقیت آمیز بودن عملیات پیغام آن بر روی کامپیوتر مربوطه ظاهر می شود
- **لطفا کل مطلب را با دقت بخوانید تا در نصب به مشکل نخورید یه دونه هم بکاپ از نرم افزار حسابداریتون بگیرید برای محکم کاری(هر چند که اتصال نرم افزار به حسابداری صرفا خواندن را شامل می شود - و دستکاری در دیتا صورت نمیگیرد) - سوال و انتقاد و پیشنهاد و ... را به این ایمیل بفرستید m.javidii@yahoo.com با تشکر**

## توضیحات در مورد حسابداری راهکار و این برنامه
- این برنامه به صورت غیر رسمی است (یعنی توسط خود راهکارسافت -> سازنده حسابداری راهکار ارائه نشده است)
- برنامه به دیتابیس راهکار هیچ تغییری وارد نمی کند - (یوزری هم که می سازید و به برنامه می دهید صرفا وظیفه و اجازه ی خواندن یک تراکنش را دارد یعنی می توانید فقط به آن اجازه ی خواندن بدهید و مشکلی پیش نمی آید
- برنامه بر بنای دیتابیس ورژن رایگان حسابداری راهکار (1.0.0.0) ساخته شده (توسط کاربران بر روی ورژن 6.0.0.0 هم امتحان شده و جواب داده) یعنی تا وقتی که آن ساختار دیتابیس مربوطه عوض نشود برنامه به طور صحیح کار میکند و کلا ما بر بنای ورژن رایگان حسابداری راهکار توسعه را انجام میدهیم و به نسخه های بعدی دسترسی نداریم
- فرض بر آن است که حسابداری و دیتابیس و این برنامه رابط همه بر روی یک کامپیوتر اند (البته که غیر از این هم باشد قابل کاربرد است اما پیچیدگی های خودش را دارد و باید در فایل .env مشخص شود)
- فرض بر آن است که کامپیوتر مربوطه به یک مودم یا روتر متصل است البته باید کارتخوان ها هم به این مودم متصل باشند (بحث این است که از یگ جا و یک رنج آی پی گرفته باشد)

## اول میرسیم به چیزایی که لازم داریم یعنی کارتخوان های اینترنتی 
- در اول اینکه برنامه بر روی شبکه کار میکند یعنی لازم است که کارتخوان ها و کامپیوتری که حسابداری روی آن است به یک شبکه متصل باشند (اتصال با یک مودم یا روتر از طریق کابل شبکه)
- برنامه با کارتخوان های : تجارت الکترونیک پارسیان و شرکت سداد و آسان پرداخت سازگار می باشد
- کارتخوان ها باید از نوع اینترنتی باشند با ارتباط LAN - یا حداقل بتوانند آی پی بگیرند و با آی پی کار کنند (چون ارسال تراکنش از طریق شبکه tcp صورت میگیرد)
- مربوط به تنظیم کارتخوان : پی سی پوز یا به اصطلاح ارتباط با رایانه باید روی کارتخوان ها فعال باشند با نوع ارتباط شبکه (وظیفه نماینده یا مدیر کارتخوان)
- مربوط به تنظیم کارتخوان : آی پی استاتیک باید روی کارتخوان ها ست شده باشد (آی پی را یادداشت چون در فایل کانفیگ باید به رابط بدهیم -> .env)
- مربوط به تنظیم کارتخوان : ترجیحا پورت 8888 برای کارتخوان سداد استفاده کنید و پورت 1362 برای کارتخوان تجارت الکترونیک پارسیان و در آسان پرداخت هم که 17000 (پورت را هم یادداشت چون در فایل کانفیگ باید به رابط بدهیم -> .env)

## نصب برنامه های مورد نیاز برای کار با کارتخوان ها
### برنامه کارتخوان یا کارتخوان های مورد نظر که میخواهید در برنامه استفاده کنید را دانلود و نصب کنید:
- اول برنامه سداد را نصب کنید (حتما dot NET Framework 3.5 در ویندوز نصب باشد - یا آنرا از کنترل پنل درقسمت turn windows features on or off فعال کنید تا API کار کند) -> [Sadad Rest](https://drive.google.com/file/d/1jxvKtlQ1WPAsSeMGyPDHTnTAW6Kfu9RH/view?usp=sharing) در اینجا چون نرم افزار بوسیله RestAPI با کارتخوان سداد ارتباط برقرار می کند، در نتیجه فقط آنرا نصب میکنیم
- خب حالا سرویس API مربوط به کارتخوان تجارت الکترونیک پارسیان را نصب می کنیم(پیش نیاز خاصی ندارد) -> [PEC Service Installer](https://drive.google.com/file/d/1MdbCYuq2LXHdqVzlAE6NOkQhGMLcd9fB/view?usp=sharing) برنامه مربوطه به صورت سرویس ویندوزی نصب می شود و فایلهای unzip شده را حذف نکنید (پس به محل extract فایل ها دقت کنید) - و داخل پوشه یه فایل bat هست به اسم install.bat که بوسیله آن سرویس نصب می شود

## نصب رابط نرم افزاری
**اگر موارد بالا را با دقت انجام داده باشید الان فقط نیاز است که آخرین ورژن برنامه را دانلود و نصب کنید و آنرا تا کانفیگ ها را انجام ندادید باز نکنید**
- لینک دانلود آخرین نسخه برنامه [PCPosAPI](https://github.com/jvdi/rahkar-pcpos/releases)
- دانلود کنید و به سادگی نصب کنید

## پیکربندی (کانفیگ)
- خب حالا بر روی آیکون برنامه در منوی استارت کلیک راست کرده و Open file location را میزنیم تا وارد محل نصب برنامه شویم (توجه داشته باشید که روی دسکتاپ شما آیکونی ظاهر نخواهد شد پس در منوی استارت دنبال آیکون برنامه بگردید)
- فایل env. را باز میکنیم (اگر فایل منیجر شما نوع فایل را نمایش نمی دهد احتمالا یک فایل بی نام در آن می بینید آنرا با برنامه notepad باز کنید)
- با یک سری خطوط مواجه می شوید که باید به این شرح باشند (به هیچ وجه فاصله یا اصطلاحا space درون فایل اضافه نکنید - فقط مقدار بدهید):
- اگر مبلغ هایی که در حسابداری شما استفاده شده به واحد پولی تومان است پس باید PRICE_FACTOR را 10 بگذارید واگر مبالغ حسابداری شما به ریال است نیاز به تغییر آن ندارید همان 1 درست است (دقت داشته باشید این قسمت وظیفه تبدیل تومان به ریال را دارد چون کارتخوان با ریال کار میکند و اگر عددی در آن دستکاری شود باعث اشتباه در مبالغ می شود)
- در قسمت بعد که با یک مربع بالای آن مشخص شده MsSql مشخصات ارتباط با دیتا بیس راهکار را از شما می گیرد (ولی به طور کلی نیاز به برنامه مدیریت دیتابیس دارید که از این لینک [Microsoft SQL Server 2008 SQLManagementStudio](https://www.microsoft.com/en-us/download/details.aspx?id=30438) دانلود کنید حالا یا 32 بیت یا 64 بیت دیگه بسته به سیستم خودتون دانلود کنید و در اول به کانفیگ کننده دیتابیس بروید و ارتباط از tcp را فعال کنید و سپس بر روی پورت 1433 آنرا به اجرا در بیاورید و سپس از داخل برنامه مدیریت دیتابیس یک یوزر بسازید با نام کاربری: PCPos_API و رمز عبور دلخواه و آنرا در فایل .env ست کنید و سطح دسترسی یوزر را خواندن بگذارید)
- کلید اول MSSQL_HOST است که بنا بر پیش فرض ها نیازی به تغییر نیست همان localhost باشد (یا آی پی دیتابیس راهکار بر روی شبکه شما)
- کلید MSSQL_USER را یوزرنیم که با دسترسی خواندن ساخته اید را میگذارید
- کلید MSSQL_PASSWORD رمز عبور همان یوزرنیم را میگذارید
- کلید MSSQL_db را نیازی به تغییر نیست

### در قسمت بعد هم مشخصات پوز های مربوطه را از شما می گیرد اول **سداد** که در بالای آن با یک مربع مشخص شده Sadad POS :
- برای غیرفعال سازی استفاده از پوز سداد - مقدار SADAD_RUN را NO بگذارید (یا اگر از این نوع پوز استفاده نمی کنید)
- برای کلید SADAD_ACC_ID که مقدارش 1 است -> چون مثلا اولین حساب بانکی که من در حسابداری راهکار معرفی کردم حساب کارتخوان سداد است پس این 2 است (به طور کلی : اگر مثلا برای شما پنجمین حساب بانکی که معرفی کردید متصل یه کارتخوان سداد است پنج را به علاوه 1 میکنید میشود 6 یعنی باید این را 6 بگذارید یعنی شماره پوز به علاوه 1)
- کلید SADAD_REST_API_IP را هم همان که هست بگذارید
- کلید SADAD_DEVICE_IP را آی پی دستگاه سداد که آن آی پی استاتیک گذاشتید (همان که گفتم نگهدارید لازممون میشه) را اینجا وارد کنید (قاعدتا باید آنرا از مسئول کارتخوان بگیرید)
- کلید SADAD_DEVICE_PORT را هم قاعدتا از مسئول کارتخوان میگیرید (اکثر مواقع پیشفرض هست همان 8888)
- کلید بعدی را هم همان بگذارید بماند
- کلید SADAD_DEVICE_TYPE نیز مشکلی نداره با همون کار میکنه 3 بگذارید باشه (بسته به نوع کارتخوان بر اساس مستندات شرکت سداد باید تعیین شود)

### در قسمت بعد تنظیم دستگاه پوز تجارت الکترونیک پارسیان که در بالای آن با یک مربع مشخص شده PEC POS :
- برای غیرفعال سازی استفاده از پوز تجارت الکترونیک پارسیان - مقدار PEC_RUN را NO بگذارید (یا اگر از این نوع پوز استفاده نمی کنید)
- کلید PEC_ACC_ID را همانند SADAD_ACC_ID کانفیگ میکنیم (حساب های بانکی که در حسابداری معرفی کردیم را می شماریم و مثلا حساب سوم مربوط به دستگاه پوز تجارت الکترونیک پارسیان است و سه را به علاوه 1 میکنیم و مقدار را 4 قرار می دهیم)
- کلید PEC_DEVICE_IP را که باید آی پی دستگاه که از مسئول پوز گرفتیم بگذاریم (آی پی ثابت باشد) و PEC_DEVICE_PORT را که این را نیز همان پورت مربوطه تعیین شده از سمت دستگاه بگذاریم 

### در قسمت بعد تنظیم دستگاه پوز آسان پرداخت که در بالای آن با یک مربع مشخص شده ASAN-P POS :
-  برای غیرفعال سازی استفاده از پوز آسان پرداخت - مقدار SADAD_RUN را NO بگذارید (یا اگر از این نوع پوز استفاده نمی کنید)
- کلید ASAN-P_ACC_ID را همانند قبلی ها کانفیگ میکنیم (حساب های بانکی که در حسابداری معرفی کردیم را می شماریم و مثلا حساب چهارم مربوط به دستگاه پوز آسان پرداخت است و چهار را به علاوه 1 میکنیم و مقدار را 5 قرار می دهیم)
- کلید ASAN-P_DEVICE_IP را که باید آی پی دستگاه که از مسئول پوز گرفتیم بگذاریم (آی پی ثابت باشد) و ASAN-P_DEVICE_PORT را که این را نیز همان پورت مربوطه تعیین شده از سمت دستگاه بگذاریم 17000 هست اکثرا در دستگاههای آسان پرداخت
