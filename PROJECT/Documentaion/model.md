# Django Models Documentation

This document explains how to create models in Django using the example from the Project's `tweet` app. It provides a simple step-by-step guide to help anyone understand how to create and add models in Django.

---

## What is a Django Model?

A Django model is a Python class that represents a database table. Each attribute of the class corresponds to a database field. Models allow you to interact with your database using Python code instead of SQL.

---

## Step-by-Step Guide to Creating a Model

### 1. Define the Model Class

In your Django app folder (e.g., `tweet`), open or create the `models.py` file. Define a class that inherits from `models.Model`.

Example from the Project:

```python
from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=280)
    photo = models.ImageField(upload_to='tweets/photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}: {self.text[:50]}"
```

### 2. Add Fields to the Model

- `user`: Links the tweet to a user using a foreign key relationship.
- `text`: Stores the tweet content with a maximum length of 280 characters.
- `photo`: Optional image field to upload photos related to the tweet.
- `created_at`: Automatically stores the date and time when the tweet was created.
- `updated_at`: Automatically updates the date and time when the tweet is modified.

### 3. Add a String Representation

The `__str__` method defines how the model instance is displayed, useful for admin interfaces and debugging.

---

## How to Add Your Model to the Project

1. After defining your model in `models.py`, save the file.
2. Run the following commands in your terminal to create and apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

This will create the necessary database tables for your model.

3. (Optional) Register your model in the app's `admin.py` to manage it via Django admin.

Example:

```python
from django.contrib import admin
from .models import Tweet

admin.site.register(Tweet)
```

---

## Summary

- Models are Python classes that define your database structure.
- Define fields using Django's field types like `CharField`, `TextField`, `ForeignKey`, etc.
- Use migrations to create/update database tables.
- Register models in `admin.py` for admin interface management.

Using the example `Tweet` model, you can create your own models by following these simple steps.

---

This documentation should help you understand how to create and add models in Django using the Project's structure.
