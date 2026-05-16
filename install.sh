#!/bin/bash

# اسم الأداة
TOOL_NAME="arsalan"
# مسار الأداة الحالي
CURRENT_DIR="$(pwd)"
# مسار التثبيت
INSTALL_DIR="/opt/$TOOL_NAME"
# مسار الملف التنفيذي
EXEC_PATH="$INSTALL_DIR/arsalan.py"

# التأكد من الصلاحيات
if [ "$EUID" -ne 0 ]; then 
    echo "الرجاء تشغيل السكربت بصلاحيات root"
    echo "استخدم: sudo ./install.sh"
    exit 1
fi

echo "بدء تثبيت أداة $TOOL_NAME..."

# إنشاء مجلد في opt
echo "إنشاء مجلد التثبيت..."
mkdir -p "$INSTALL_DIR"

# نسخ الملفات
echo "نسخ ملفات الأداة..."
cp "$CURRENT_DIR/arsalan.py" "$INSTALL_DIR/"

# إعطاء صلاحيات التنفيذ
chmod +x "$EXEC_PATH"

# إنشاء اختصار في /usr/local/bin
echo "إنشاء اختصار في terminal..."
cat > "/usr/local/bin/$TOOL_NAME" << EOF
#!/bin/bash
cd $INSTALL_DIR
python3 $EXEC_PATH
EOF

# إعطاء صلاحيات للاختصار
chmod +x "/usr/local/bin/$TOOL_NAME"

# إنشاء ملف .desktop للتطبيقات
echo "إنشاء اختصار في قائمة التطبيقات..."
cat > "/usr/share/applications/$TOOL_NAME.desktop" << EOF
[Desktop Entry]
Version=1.0
Name=Arsalan Tool
Comment=أداة اختبار اختراق الشبكات
Exec=python3 $EXEC_PATH
Icon=utilities-terminal
Terminal=true
Type=Application
Categories=Utility;Security;
Path=$INSTALL_DIR
EOF

# تحديث قاعدة بيانات التطبيقات
update-desktop-database

echo "تم التثبيت بنجاح!"
echo "يمكنك الآن تشغيل الأداة بكتابة: $TOOL_NAME"
echo "أو من قائمة التطبيقات باسم: Arsalan Tool"
