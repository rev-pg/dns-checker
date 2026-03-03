 ````markdown
# DNS Resolver & SlipStream Tester
Valid DNS Scanner for SlipStream/DNStt  
By: [REV](https://github.com/rev-pg)

----------------------------------------------------------------------------------------

## 🌐 English

### Description
This script tests a list of DNS resolvers using the SlipStream client.  
It checks if the resolvers can successfully connect to a target domain via DNStt/SlipStream protocol and measures the ping latency.

Features:
- Multi-threaded testing of resolvers.
- Optional timeout and threads with default values.
- Ping measurement for successful resolvers.
- Works with Linux systems (SlipStream binary required).

### Requirements
- Python 3.10+  
- SlipStream client binary (`slipstream-client-linux-amd64`)  
- `resolvers.txt` file containing a list of DNS resolver IPs.

----------------------------------------------------------------------------------------

### Installation
1. Clone this repository:

git clone https://github.com/rev-pg/dns-checker.git
cd dns-checker

2. Place your SlipStream binary in the project folder.
3. Prepare a `resolvers.txt` file with one resolver IP per line.

----------------------------------------------------------------------------------------

### Usage

Run the script:

chmod +x slipstream-client-linux-amd64
python3 scan.py

The script will ask for:

1. TARGET_DOMAIN (required) – The domain you want to test.
2. SLIPSTREAM_TIMEOUT (optional) – Timeout in seconds (default: 5).
3. MAX_THREADS (optional) – Number of threads (default: 10).

After running, valid resolvers will be listed with ping times if available.

----------------------------------------------------------------------------------------


## 🌐 فارسی

### توضیحات

این اسکریپت یک لیست از DNS Resolver ها را با استفاده از کلاینت SlipStream تست می‌کند.
هدف بررسی اتصال موفق Resolver ها به یک دامنه مشخص از طریق پروتکل DNStt/SlipStream و اندازه‌گیری زمان پاسخ (ping) است.


----------------------------------------------------------------------------------------

ویژگی‌ها:

* تست همزمان (multi-thread) Resolver ها
* تنظیمات اختیاری Timeout و تعداد Threads با مقادیر پیش‌فرض
* اندازه‌گیری زمان پاسخ برای Resolver های موفق
* قابل اجرا روی سیستم‌های لینوکس (نیاز به فایل باینری SlipStream)


----------------------------------------------------------------------------------------
### پیش‌نیازها

* Python 3.10+
* فایل باینری SlipStream (`slipstream-client-linux-amd64`)
* فایل `resolvers.txt` شامل لیست IP های DNS Resolver


----------------------------------------------------------------------------------------

### نصب

1. کلون کردن مخزن:


git clone https://github.com/rev-pg/dns-checker.git
cd dns-checker


2. قرار دادن فایل باینری SlipStream در پوشه پروژه
3. آماده کردن فایل `resolvers.txt` با یک IP در هر خط

### نحوه استفاده

اسکریپت را اجرا کنید:


chmod +x slipstream-client-linux-amd64
python3 scan.py


اسکریپت از شما می‌خواهد:

1. TARGET_DOMAIN (الزامی) – دامنه‌ای که می‌خواهید تست کنید.
2. SLIPSTREAM_TIMEOUT (اختیاری) – زمان تایم‌اوت به ثانیه (پیش‌فرض: 5)
3. MAX_THREADS (اختیاری) – تعداد Thread ها (پیش‌فرض: 10)

پس از اجرا، Resolver های معتبر به همراه زمان پاسخ (ping) نمایش داده می‌شوند.

```
