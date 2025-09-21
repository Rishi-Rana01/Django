# Documentation of Django Templates in `center/tweet/templates/`

This document explains step-by-step how each template in the `center/tweet/templates/` directory is formed, describing their purpose, structure, and key elements.

---

## 1. `index.html`

### Purpose
This template serves as a simple welcome page for the Tweet App.

### Structure and Explanation

- **Extends**:  
  The template extends `layout.html`, which is the base layout for the site. This means it inherits the overall page structure and styles defined in `layout.html`.

- **Blocks**:  
  - `title` block: Sets the page title to "Tweet App".  
  - `content` block: Contains the main content of the page:
    - An `<h1>` heading centered with the text "Welcome to the Tweet App".  
    - A paragraph describing the page as a simple template for displaying tweets.

---

## 2. `tweet_confirm_delete.html`

### Purpose
This template is used to confirm the deletion of a tweet by the user.

### Structure and Explanation

- **Extends**:  
  Extends `layout.html` to maintain consistent layout and styling.

- **Blocks**:  
  - `title` block: Sets the page title to "Tweet App".  
  - `content` block: Contains the confirmation UI:
    - A centered heading `<h1>` with "Delete Tweet".  
    - A paragraph with a warning message styled in red, asking the user to confirm deletion.  
    - A form with method `post`:
      - `{% csrf_token %}`: Django template tag to include a CSRF token for security.  
      - A submit button labeled "Confirm Delete" styled as a red danger button.  
      - A cancel link that redirects to the tweet list page using `{% url 'tweet_list' %}`.

---

## 3. `tweet_form.html`

### Purpose
This template is used for creating a new tweet or editing an existing tweet.

### Structure and Explanation

- **Extends**:  
  Extends `layout.html` for consistent layout.

- **Blocks**:  
  - `title` block: Sets the page title to "Tweet App".  
  - `content` block: Contains the form UI:
    - A heading `<h1>` that conditionally displays "Edit Tweet" if the form instance has a primary key (existing tweet), or "Create Tweet" if it is a new tweet. This is done using `{% if form.instance.pk %}`.  
    - A form with method `post` and `enctype="multipart/form-data"` to allow file uploads (photo):
      - `{% csrf_token %}` for security.  
      - A form group for the tweet text:
        - Label linked to the text input field.  
        - The text input rendered with `{{ form.text }}`.  
        - If there are errors on the text field, they are displayed in red below the input.  
      - A form group for the photo upload:
        - Label linked to the photo input field.  
        - The photo input rendered with `{{ form.photo }}`.  
        - If there are errors on the photo field, they are displayed in red below the input.  
      - A submit button that conditionally shows "Update" or "Create" based on whether the tweet is being edited or created.  
      - A link to go back to the tweet list page.

---

## 4. `tweet_list.html`

### Purpose
This template displays a list of tweets with options to create, edit, or delete tweets.

### Structure and Explanation

- **Extends**:  
  Extends `layout.html` for consistent site layout.

- **Blocks**:  
  - `title` block: Sets the page title to "Tweet App".  
  - `content` block: Contains the tweet list UI:
    - A centered heading `<h1>` welcoming users to the Tweet App.  
    - A paragraph describing the page.  
    - A button linking to the tweet creation page using `{% url 'tweet_create' %}`.  
    - A container div that loops over the `tweets` context variable using `{% for tweet in tweets %}`:
      - For each tweet, a Bootstrap card is created:
        - Displays the tweet photo using `<img>` with the source set to `{{ tweet.photo.url }}`.  
        - Card body contains:
          - The tweet author's username in a card title.  
          - The tweet text in a paragraph.  
          - Buttons to edit and delete the tweet, linking to the respective URLs with the tweet's id passed as a parameter.

---

# Summary

All templates extend a common base layout `layout.html` and define `title` and `content` blocks to insert page-specific content. They use Django template tags for dynamic content rendering, form handling, CSRF protection, and URL reversing. The `tweet_form.html` handles form rendering with error display, while `tweet_list.html` dynamically renders a list of tweets with action buttons.

This documentation should help understand how each template is structured and how it contributes to the Tweet App's functionality.
