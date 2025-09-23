# Tweet App - Django Project

A simple Django-based web application for creating, viewing, editing, and deleting tweets. Users can post text-based tweets with optional photo uploads, and manage their content through a user-friendly interface.

## Features

- **User Authentication**: Secure login and registration system.
- **Tweet Management**: Create, read, update, and delete tweets.
- **Photo Uploads**: Attach images to tweets (stored in media/tweets/photos/).
- **Admin Panel**: Manage users and content via Django's built-in admin interface.
- **Responsive UI**: Clean and simple templates for easy navigation.
- **Database Integration**: Uses Django's ORM for data handling.

## Folder Structure

Here's an easy-to-understand overview of the project structure:

```
center/                          # Main Django project directory
├── center/                      # Project configuration
│   ├── __init__.py
│   ├── asgi.py                  # ASGI configuration
│   ├── settings.py              # Project settings (apps, database, etc.)
│   ├── urls.py                  # Main URL routing
│   └── wsgi.py                  # WSGI configuration
├── tweet/                       # Tweet app directory
│   ├── __init__.py
│   ├── admin.py                 # Admin configuration
│   ├── apps.py                  # App configuration
│   ├── forms.py                 # Forms for tweet creation/editing
│   ├── models.py                # Tweet model definition
│   ├── tests.py                 # Unit tests
│   ├── urls.py                  # App-specific URL routing
│   ├── views.py                 # View functions
│   ├── migrations/              # Database migrations
│   │   ├── __init__.py
│   │   └── 0001_initial.py      # Initial migration
│   └── templates/               # HTML templates
│       ├── index.html           # Home page
│       ├── tweet_confirm_delete.html  # Delete confirmation
│       ├── tweet_form.html      # Create/edit form
│       └── tweet_list.html      # List of tweets
├── media/                       # User-uploaded files
│   └── tweets/
│       └── photos/              # Tweet photos
├── static/                      # Static files (CSS, JS, images)
├── templates/                   # Shared templates
│   ├── layout.html              # Base layout
│   └── registration/            # Auth templates
│       ├── logged_out.html
│       ├── login.html
│       └── register.html
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
└── Documentaion/                # Documentation files
    ├── 01setup.md               # Setup guide
    ├── 02model.md               # Models documentation
    ├── 03views.md               # Views documentation
    └── templates.md             # Templates documentation
```

## Installation

Follow these step-by-step instructions to set up the project. This guide is based on the detailed setup in `Documentaion/01setup.md`.

### Prerequisites
- Python installed on your system (download from [python.org](https://www.python.org/downloads/)).
- Command Prompt or Terminal access.

### Step 1: Create a Virtual Environment
1. Open Command Prompt.
2. Navigate to your desired project directory (e.g., `cd C:\Users\YourName\Desktop`).
3. Create a virtual environment:
   ```
   python -m venv .venv
   ```
4. Activate the virtual environment:
   - On Windows: `.venv\Scripts\activate`
   - On macOS/Linux: `source .venv/bin/activate`

### Step 2: Install Dependencies
1. Install Django and other required packages:
   ```
   pip install -r requirements.txt
   ```

### Step 3: Set Up the Project
1. Start a new Django project (if not already done):
   ```
   django-admin startproject center
   cd center
   ```
2. Create the tweet app:
   ```
   python manage.py startapp tweet
   ```

### Step 4: Configure Settings
1. Open `center/settings.py` and add `'tweet'` to `INSTALLED_APPS`:
   ```python
   INSTALLED_APPS = [
       # ... existing apps
       'tweet',
   ]
   ```
2. Add media and static file settings:
   ```python
   import os
   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   STATIC_URL = 'static/'
   STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
   ```
3. In `center/urls.py`, add media serving for development:
   ```python
   from django.conf import settings
   from django.conf.urls.static import static
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

### Step 5: Set Up Database
1. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
   - Enter username, email, and password when prompted.

### Step 6: Configure Templates
1. In `settings.py`, add to `TEMPLATES`:
   ```python
   'DIRS': [os.path.join(BASE_DIR, 'templates')],
   ```

## Usage

### Running the Server
1. Start the development server:
   ```
   python manage.py runserver
   ```
2. Open your browser and go to `http://127.0.0.1:8000/`.

### Using the App
- **Home Page**: Visit the root URL to see the welcome page.
- **Tweet List**: View all tweets at `/tweet/`.
- **Create Tweet**: Log in and create a new tweet with text and optional photo.
- **Edit/Delete Tweets**: Users can edit or delete their own tweets.
- **Admin Panel**: Access at `/admin/` to manage users and content.

### Key Components

#### Models
Based on `Documentaion/02model.md`, the core model is `Tweet`:
- **Fields**:
  - `user`: Foreign key to the user who created the tweet.
  - `text`: Text content (max 280 characters).
  - `photo`: Optional image upload.
  - `created_at`: Automatic timestamp for creation.
  - `updated_at`: Automatic timestamp for updates.
- **Usage**: Models are defined in `tweet/models.py` and interact with the database via Django's ORM.

#### Views
From `Documentaion/03views.md`, the main views are:
- `index()`: Renders the home page.
- `tweet_list()`: Displays all tweets.
- `tweet_create()`: Handles new tweet creation.
- `tweet_edit()`: Allows editing existing tweets.
- `tweet_delete()`: Manages tweet deletion with confirmation.
- **Security**: Views ensure users can only edit/delete their own tweets.

#### Templates
As described in `Documentaion/templates.md`:
- **Base Layout**: `layout.html` provides consistent structure.
- **Tweet Templates**:
  - `index.html`: Simple welcome page.
  - `tweet_list.html`: Lists tweets with edit/delete options.
  - `tweet_form.html`: Form for creating/editing tweets.
  - `tweet_confirm_delete.html`: Confirmation for deletion.
- **Features**: Templates use Bootstrap for styling and include CSRF protection.

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Make your changes and commit: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## Documentation

For more detailed guides, refer to the `Documentaion/` folder:
- `01setup.md`: Complete setup instructions.
- `02model.md`: In-depth model explanations.
- `03views.md`: View function details.
- `templates.md`: Template structure and usage.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter issues, check the documentation files or open an issue on GitHub.
