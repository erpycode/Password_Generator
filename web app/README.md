# 🔐 Password Generator | پسورد جنریتور

یک ابزار وب فوری برای تولید پسورد‌های امن و تصادفی!

## ✨ ویژگی‌ها

✅ **تولید فوری** - پسورد‌های ۸-۲۰ کاراکتری  
✅ **کپی آسان** - یک کلیک و کپی شود  
✅ **ذخیره محلی** - فقط روی دستگاه شما  
✅ **بدون اینترنت** - آفلاین هم کار می‌کند  
✅ **Responsive** - موبایل و دسکتاپ  
✅ **ایمن** - بدون ارسال اطلاعات به سرور  

---

## 🚀 نحوه اجرا

### **قدم ۱: نصب Dependency ها**
```bash
pip install -r requirements.txt
```

### **قدم ۲: اجرای اپ**
```bash
python app.py
```

### **قدم ۳: باز کردن در مرورگر**
```
http://localhost:5000
```

---

## 📁 ساختار فایل‌ها

```
password-generator/
├── app.py                 # Flask Backend
├── templates/
│   └── index.html        # Frontend HTML/CSS/JS
├── requirements.txt      # Dependencies
├── saved_passwords/
│   └── Password.txt      # ذخیره‌شده‌ها (خودکار)
└── README.md
```

---

## 🌍 Deploy به اینترنت

### **گزینه ۱: PythonAnywhere (رایگان)**
1. ثبت‌نام: https://www.pythonanywhere.com
2. Upload کردن کد
3. Add Web App و انتخاب Flask
4. شماره دادن به کد

### **گزینه ۲: Heroku (رایگان)**
```bash
pip install heroku-cli
heroku login
heroku create your-app-name
git push heroku main
```

### **گزینه ۳: Render (رایگان)**
1. ثبت‌نام: https://render.com
2. Connect GitHub
3. Deploy خودکار

---

## 🔒 امنیت

- ✅ هیچ داده‌ای به سرور ارسال نمی‌شود
- ✅ `secrets` module استفاده می‌کند
- ✅ پسورد‌ها هم‌راستا (≥۸ کاراکتر)
- ✅ شامل حروف، اعداد، علائم خاص

---

## 📱 برای اینستاگرام/تلگرام

**Screenshot ideas:**
```
1. "۱۵ پسورد مختلف در ۱۵ ثانیه"
2. "کپی کنید و رو بروید"
3. "بدون اینترنت هم کار می‌کنه"
```

---

## 🛠 Custom کردن

### تغییر رنگ‌ها:
```css
/* در index.html */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
/* به هر رنگی که دوست دارید */
```

### تغییر طول پیش‌فرض:
```html
<input type="range" id="lengthSlider" min="8" max="20" value="16">
```

---

## ❓ FAQ

**س:** چرا Python گزینه‌ی بهتری است؟  
**ج:** `secrets` module خیلی محفوظ‌تره از `random`

**س:** می‌تونم این‌را روی موبایل استفاده کنم؟  
**ج:** آره! Responsive است و تمام موبایل‌ها پشتیبانی می‌کند

**س:** پسورد‌های من کجا ذخیره می‌شوند؟  
**ج:** فایل `Password.txt` در پوشه‌ی `saved_passwords`

---

## 📞 پشتیبانی

اگر مشکل داری:
1. Python ۳.۸+ دارید؟
2. Flask install است؟
3. Port ۵۰۰۰ خالی است؟

---

**توسعه‌دهنده:** ErPyCode  
**آخرین بروزرسانی:** ۲۰۲۶
