# VSCode Tutorial
I am learning django by creating this sample application. I am following [this](https://code.visualstudio.com/docs/python/tutorial-django) tutorial from the official VSCode documentation.

## What I learned
This tutorial was very new and extensive, so I will split the content under multiple sub headings.

### VSCode
- **User Snippets** - You can create custom snippets in vscode, which appear as intellisense suggestion when typing. This lets you write boilerplate code with only a few keypresses. An example of a built-in snippet is `!`, which generates html boilerplate when you press `tab` afterwards.
- **requirements.txt** - This file helps to easily create the virtual environment quickly with all the dependencies. You can do so by running the following:
    ```sh
    pip freeze > requirements.txt
    ```
    >Please note that the `pip freeze` command will include all the installed libraries in the currently selected virtual environment.

### Django
- **CLI utility** - `manage.py` is django's CLI utility used for administrative commands such as 
    - `migrate` to apply db migrations. 
    - `runserver` to start django's development server.
- **Projects** - A django project can contain multiple applications that work together to deliver a complete package. I like to think of django project as a Visual Studio solution, and applications as Visual Studio projects. You can create a project using the command:
    ```sh
    django-admin startproject <PROJECT-NAME> .
    ```
- **Applications** - A django application contains multiple folders and python files that contain definitions for your views, models, migrations, routing and tests. You can create a django application using the command:
    ```sh
    python manage.py startapp <APPLICATION-NAME>
    ```
- **Routing** - django has 2 kinds of routing:
    - *Project level* - includes routes for all the applications inside the project.
    - *Application level* - contains routes for all the views and actions of a particular application.
- **Templates** - You can create html templates in your application, which contain placeholders for values that can be passed using python/django code in the `views.py` file. Placeholders are generally encapsulated by `{{` and `}}`. The `render` method can take a template and pass in some variables, then return the result to the client. Benefit of templates is the security against [XSS](https://en.wikipedia.org/wiki/Cross-site_scripting).
- **Static Files** - django can serve static files as well, such as CSS. You must have the `{% load static %}` declaration in your html before you try to access any static files. 
- **Layouts** - You can create a base template that can be extended by other templates to remove writing the whole page from scratch. Think of the layout being the navigation bar, footer, side bar, essential buttons, basically things you need on every page. Then another template can extend that and add additional content in place of placeholders.
- **Data and Models** - Django uses a code first approach. You can define models in `models.py` in your application. Each class in that file, that is derived from `models.Model` represents a table, and the fields in that class initialized as model Fields (`CharField`, `DateTimeField` etc) represent columns. These classes can have functions as well. 
- **Migrations** - Whenever you update a model, you need to update the database to reflect those changes as well. To do so, you first create the migrations, and then apply them to your database:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
- **Forms** - I created a file `forms.py` and created a form class that used a model I created earlier. I defined which fields I wanted in my form and used it in `views.py`.
- **Template Conditions and Loops** - You can have conditional rendering in your template, and also loops to render lists.
- **Admin Panel** - you can create a superuser and admin panel in django, and I plan on experimenting on it, in order to try and create a shopping site where the admin can upload items in the admin panel, and users can login and make purchases through the normal view. 