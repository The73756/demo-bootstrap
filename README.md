# Django startapp

1. Создать проект в pycharm без "-" и с приложением
2. py manage.py migrate
3. Настроить язык в настройках
    - LANGUAGE_CODE = 'RU-ru'
    - STATIC_URL = 'static/'
    - LOGIN_REDIRECT_URL = '/'
    - LOGOUT_REDIRECT_URL = '/'
    - LOGIN_URL = '/login'
    - STATICFILES_DIRS = ['static/', 'www/var/static']
4. Создать urls.py в **приложении**
5. Подключить urls в проекте
    ```python
     from django.contrib import admin
     from django.urls import path, include
    
     urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include('demo2app.urls'))
    ```
6. Скачать либы (бутстрап, тв)
7. {% load static %} {% static 'bootstrap.min.js' %}
8. admin.py admin.site.register(Profile)
9. Делать демку