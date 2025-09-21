# Django Project Setup Guide
---

# Step 1: Create a Virtual Environment

A virtual environment helps keep your project’s Python packages separate from other projects.

- Open your command prompt or terminal.
- Run this command to create a virtual environment named `.venv`:
 ```
- python -m venv .venv 
```
- run venv
```
 .venv\Scripts\Activate
```
# Easy Django Project Setup Guide (For Beginners!)

---




## 1️⃣ Install Python

1. Go to [python.org](https://www.python.org/downloads/)
2. Click **Download Python** and install it on your computer.
3. Open the **Command Prompt** (search for "cmd" on Windows).

---

## 2️⃣ Install Django

1. In the Command Prompt, type:
    ```bash
    pip install django
    ```
2. Press **Enter** and wait for it to finish.

---

## 3️⃣ Start Your Django Project

1. In the Command Prompt, go to the folder where you want your project. Example:
    ```bash
    cd C:\Users\YourName\Desktop
    ```
2. Type:
    ```bash
    django-admin startproject center
    ```
3. Go into your new project folder:
    ```bash
    cd center
    ```

---

## 4️⃣ Run the Server (See Your Website!)

1. Type:
    ```bash
    python manage.py runserver
    ```
2. Open your web browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000)
3. You should see the Django welcome page!

---

## 5️⃣ Make a Django App

1. In the Command Prompt, type:
    ```bash
    python manage.py startapp tweet
    ```
2. This makes a new folder called `tweet` for your app.

---

## 6️⃣ Add Your App to Settings

1. Open `center/settings.py` in a text editor.
2. Find the list called `INSTALLED_APPS`.
3. Add `'tweet',` to the list. Example:
    ```python
    INSTALLED_APPS = [
         ... # existing apps
         'tweet',
    ]
    ```

---

## 7️⃣ Make Migrations (Prepare the Database)

1. In the Command Prompt, type:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

---

## 8️⃣ Create an Admin User (Superuser)

1. In the Command Prompt, type:
    ```bash
    python manage.py createsuperuser
    ```
2. Enter a username, email, and password when asked. **Remember your password!**

---

## 9️⃣ Register Your Models in Admin

1. Open `tweet/admin.py`.
2. Add your models so you can see them in the admin panel. Example:
    ```python
    from .models import YourModel
    admin.site.register(YourModel)
    ```

---

## 🔟 Make Templates and Static Folders

1. Inside your app folder (`tweet`), make a folder called `templates`.
2. Inside your main project folder, make a folder called `static` for images, CSS, and JavaScript.

---

## 1️⃣1️⃣ Use the Admin Panel

1. Start the server again if it’s not running:
    ```bash
    python manage.py runserver
    ```
2. Go to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
3. Log in with the superuser username and password you made.
4. Now you can add, edit, and delete things in your website!

---

## 🎉 You Did It!

Your Django website and admin panel are ready. You can now build cool things and show your friends!

---

## 📝 Extra Tips

- If you change models, always run:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
- To stop the server, press `Ctrl + C` in the Command Prompt.
- If you get stuck, search for help online or ask a friend/teacher.

---

**Have fun coding! 🦄**
```
python manage.py createsuperuser
```

- You will be asked to enter a username (e.g., `rishi`) and a password (e.g., `Rishi123`).

---

## Step 9: Configure Media Files (for Image Uploads)

- Open the `settings.py` file inside the `center` folder.
- Add these lines to the file:

```python
import os

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

## Step 10: Configure Static Files (for CSS, JavaScript, Images)

- In the same `settings.py` file, add these lines at the end:

```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

- Next, open the `urls.py` file inside the `center` folder (main project folder).
- Add these imports at the top of the file:

```python
from django.conf import settings
from django.conf.urls.static import static
```

- Then, update the `urlpatterns` list to include the admin path and serve media files during development:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- Note: The `path('admin/', admin.site.urls),` line appears twice in the current `urls.py` file. You should remove the duplicate to avoid conflicts.

---

## Step 11: Set NPM Path (If Node.js and npm are Installed but Not Detected)

- In your `settings.py` file, add this line to specify the npm path:

```python
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
```

---

## Step 12: Create a New Django App

- Run this command to create a new app called `tweet` (you can choose a different name):

```
python manage.py startapp tweet
```

---

## Step 13: Set Up URLs for the New App

- Inside the `tweet` folder, create a new file named `urls.py`.
- Copy all the URL patterns from the main `urls.py` file into this new file.
- In the `tweet/urls.py` file, add this example view:

```python
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

---

## Step 14: Create a View for Your App

- In the `tweet/views.py` file, add this code:

```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

---

## Step 15: Register the App in Project Settings

- Open `settings.py` and find the `INSTALLED_APPS` list.
- Add your app name `'tweet'` to the list, like this:

```python
INSTALLED_APPS = [
    # other apps
    'tweet',
]
```

---

## Step 16: Configure Templates Directory

- In `settings.py`, find the `TEMPLATES` setting.
- Inside the `'DIRS'` list, add this line to allow templates to be accessed from anywhere:

```python
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

---

Now you have a complete step-by-step guide to set up and run your Django project! Follow these steps carefully, and you will have your project running smoothly.

