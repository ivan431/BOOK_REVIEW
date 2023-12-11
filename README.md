
Выполнить по порядку
1.git clone https://github.com/ivan431/PANEL_CATALOG_DJ.git из гитхаба
2. Перейдите в папку склонированного репозитория с помощью команды
`cd имя_папки_репозитория`.
3.python -m venv virt_env_for_base - создаем вирт. окружение
4.Активируйте виртуальное окружение ->
    venv\Scripts\activate
5.Установите зависимости проекта из файла requirements.txt
    pip install -r requirements.txt
6.Запустите проект - python manage.py runserver (если порты все заняты как у меня,
 то напишите свободный порт -> cmd -> netstat -ano - посмотреть какие порты свободны)

7. Чтобы сразу же приступить к проверке задания нужно перейти по адресу: http://localhost:ваш_порт_или_порт_по_умолчанию/catalog/add_review/
 и вбить требуемые значения, Вас должно перекинуть на форму /catalog/feedback_success/ - где будет написано: Спасибо за отзыв
8. Чтобы убедиться, что данные поступили, нужно перейти в админ-панель Django, обратиться к модели Book review и там Вы должны обнаружить вбитые Вами данные
