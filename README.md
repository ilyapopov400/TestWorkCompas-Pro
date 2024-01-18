Тестовое задание для проверки навыков кандидата на должность стажер с последующим трудоустройством в должности Python разработчик.
Задание необходимо выполнять используя docker- compose

1. Развернуть DRF проект, и создать приложение user_selection
2. подключить Postgresql и Redis
3. создать суперпользователя
4. создать модель User(AbstractBaseUser), добавив к Django users : role_choice (Пользователь, менеджер, CRM- администратор).
Offer (bool).
Avatar (аватар пользователя).
(views.py, serializer.py, admin.py urls.py (GET /api/users/{id})
5. Используя Django command, создать команду create_users, которая создаст 3 типа пользователя (из role_choice), с default avatar (admin.png user.png crm_admin.png)
