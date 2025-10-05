# Python CLI Book Manager

**מערכת ניהול אוסף ספרים אישי המדגימה פונקציות CRUD מלאות באמצעות Python ו-SQLite3.**

פרויקט זה נועד להציג יכולות בסיסיות של אינטראקציה עם בסיס נתונים מקומי וממשק משתמש פשוט מבוסס קונסולה (CLI).


### תכונות עיקריות (CRUD)

האפליקציה מאפשרת ניהול מלא של אוסף הספרים:
### תכונות עיקריות (CRUD):

* **Create:** הוספת ספר חדש למאגר.
* **Read:** הצגת רשימה מלאה ומעוצבת של כל הספרים.
* **Update:** עדכון סטטוס ספר (סימון כ'נקרא') לפי ID.
* **Delete:** מחיקת רשומת ספר שלמה מהמאגר.

### טכנולוגיות
* **שפה:** Python 3.x
* **בסיס נתונים:** SQLite3 (מובנה, ללא צורך בהתקנה נוספת).
* **ארכיטקטורה:** עיצוב מודולרי מבוסס פונקציות (Modular Design), להפרדת הלוגיקה.
* **אבטחת נתונים:** שימוש ב**פרמטרים מוגנים** (Parameterized Queries) למניעת SQL Injection.

### התקנה והפעלה

כדי להפעיל את הפרויקט במחשב שלך:

1.  **שכפול המאגר (Clone):**
    ```bash
    git clone [https://github.com/yael-shr/python-Book-Manager.git](https://github.com/yael-shr/python-Book-Manager.git)
    cd python-Book-Manager
    ```


2.  **יצירת והפעלת סביבה וירטואלית (Venv):**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows (CMD/PowerShell)
   source venv/bin/activate # Linux/Mac OS
   ```
3.  **הרצת היישום:**


 ```bash
    python app.py
  ```

### הפעלה ראשונית
המערכת תופעל אוטומטית ותיצור את קובץ **books.db** בתיקייה בעת ההרצה הראשונה..
