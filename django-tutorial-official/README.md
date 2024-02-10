# Official Tutorial - Poll Application
I am learning django by following the official [tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/) from version 5 of the Django documentation to create a Poll Application.
- Part 1 - [Creating an app, and the Request and Response Flow](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
- Part 2 - [Working with databases](https://docs.djangoproject.com/en/5.0/intro/tutorial02/)

## What I learned
- **Creating Projects** - If you do not specify the `.` at the end of the command, you will have a nested folder structure. I prefer the non-nested version, since there is less redundancy. I created the project in root due to personal preference here as well. 
    >Personally, I am not a fan of the commands to create projects and applications, sounds a little weird. I would have preferred if they were `createproject` `createapp` instead of `startproject` `startapp`, however I am sure there must be some valid reason why it is this way.
- **URL Configuration** - These are also called *URLconf* and are defined in the `urls.py` file. URL patterns are defined in this file, using django's `path()` function. The `name` parameter passed to this function is convenient for naming that specific route, for reference in templates and other places.
- **Database Configuration** - You can configure which database to use in the `settings.py` file of your project. This file acts as a global configuration module. By default, django uses *SQLite*, however its use is not recommended in production.
- **Timezone Configuration** - You can configure the timezone django uses to display, interpret and store datetime values.