# Django Project Setup Guide
---

## Step 1: Create a Virtual Environment

A virtual environment helps keep your project’s Python packages separate from other projects.

- Open your command prompt or terminal.
- Run this command to create a virtual environment named `.venv`:

```
python -m venv .venv
```

---

## Step 2: Activate the Virtual Environment

- To start using the virtual environment, activate it by running:

```
.venv\Scripts\Activate
```

You should see your prompt change to show the virtual environment is active.

---

## Step 3: Install Django

- With the virtual environment activated, install Django by running:

```
pip install django
```

---

## Step 4: Create a New Django Project

- Create a new Django project and name it `center` (you can choose a different name if you want):

```
django-admin startproject center
```

---

## Step 5: Enter the Project Folder

- Move into the project folder by running:

```
cd center
```

---

## Step 6: Run the Development Server

- Start the Django development server to see your project in action:

```
python manage.py runserver
```

- Open your web browser and go to `http://127.0.0.1:8000/` to see the default Django welcome page.

---

## Step 7: Apply Database Migrations

- Prepare your database by running these commands one by one:

```
python manage.py makemigrations
python manage.py migrate
```

---

## Step 8: Create a Superuser for Admin Access

- To manage your site through the admin panel, create a superuser account:

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

