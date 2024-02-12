# Official Tutorial - Poll Application
I am learning django by following the official tutorial from version 5 of the Django documentation to create a Poll Application.
- Part 1 - [Creating an app, and the Request and Response Flow](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
- Part 2 - [Working with databases and the Admin panel](https://docs.djangoproject.com/en/5.0/intro/tutorial02/)
- Part 3 - [Views and templates](https://docs.djangoproject.com/en/5.0/intro/tutorial03/)
- Part 4 - [Forms and generic views](https://docs.djangoproject.com/en/5.0/intro/tutorial04/)
- Part 5 - [Testing](https://docs.djangoproject.com/en/5.0/intro/tutorial05/)

## What I learned
- **Creating Projects** - If you do not specify the `.` at the end of the command, you will have a nested folder structure. I prefer the non-nested version, since there is less redundancy. I created the project in root due to personal preference here as well. 
    >Personally, I am not a fan of the commands to create projects and applications, sounds a little weird. I would have preferred if they were `createproject` `createapp` instead of `startproject` `startapp`, however I am sure there must be some valid reason why it is this way.
- **URL Configuration** - These are also called *URLconf* and are defined in the `urls.py` file. URL patterns are defined in this file, using django's `path()` function. The `name` parameter passed to this function is convenient for naming that specific route, for reference in templates and other places. You can assign namespaces to URLconfs if there are many applications within your project for segregation. 
- **Database Configuration** - You can configure which database to use in the `settings.py` file of your project. This file acts as a global configuration module. By default, django uses *SQLite*, however its use is not recommended in production.
- **Timezone Configuration** - You can configure the timezone django uses to display, interpret and store datetime values.
- **Django Shell** - Interactive shell, when started from `manage.py`, will have the django context enabled. Using this shell you can explore the database API, and test your models and manipulate the db.
- **Admin Panel** - The admin panel is a view included in a django project by default. To access this view, you create a superuser through the `createsuperuser` command. You can also register models and modify them directly in the admin panel.
- **Shortcuts** - Django provides a `django.shortcuts` library that contains many utility methods for common tasks such as rendering templates and safely retrieving objects.
- **Generic Views** - With the help of these classes, you can simplify alot of detail and list views. Instead of retrieving values manually, showing a list of those items or showing details of a particular item, with the help of generic views you can simply provide the primary key of your required model and populate a view automatically.
- **Automated Tests** - You can write tests in django in any file that starts with *test*, by default there is a `tests.py` file. This helps keep your application in check, so you don't break anything while adding a new feature or anything. 