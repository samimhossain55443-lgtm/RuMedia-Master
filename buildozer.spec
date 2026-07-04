# ১. অ্যাপের নাম পরিবর্তন
title = RuMedia Master

# ২. লোগো ফাইলের নাম যুক্ত করা 
icon.filename = %(source.dir)s/logo.png

# ৩. রিকোয়ারমেন্টে plyer যুক্ত করা (গ্যালারি বা ফাইল ম্যানেজার ওপেন করার জন্য)
requirements = python3,kivy==2.3.0,plyer,android

# ৪. ফোন মেমোরি ব্যবহারের সব পারমিশন অন করা
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# ৫. অ্যান্ড্রয়েডএক্স সাপোর্ট অন করা (নতুন ফোনে পারমিশন পপআপ আসার জন্য)
android.enable_androidx = True
