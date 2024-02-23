# Django REST Framework Project

Этот проект представляет собой Django приложение с использованием Django REST Framework, djangorestframework-simplejwt и envparse.

## Установка
1. Сначало создаем и активируем виртуальное окружение:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. Настройка .env
3. Настройка Simple JWT
## Создание приложения profiles
- определяем модели User и Profile
- Создаём сериализаторы в profiles/serializers.py для регистрации пользователя и создания/удаления анкет
- Определяем views в profiles/views.py для сериализаторов
- Добавляем URL-пути в profiles/urls.py
- Затем включаем эти URL-пути в основные URL-пути нашего проекта

## .gitignore
Создаем файл .gitignore и добавляем в него файлы:
```bash
.idea
.my_venv
.vscode
**/__pycashe__
.env
```
## Запуск
```bash
python manage.py runserver