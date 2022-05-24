1. git clone https://github.com/luckyuturov/kanalservice_test

2. Загрузите json файл с google cloud platform в корневую папку проекта для подключения к google sheets по api и переименуйте его credentials.json

3. Создайте виртуальное окружение командой "python -m venv venv" (Если у вас линукс "python3 -m venv venv")

4. Активируйте виртуальное окружение командой ".\venv\Scripts\activate" (Если у вас линукс ". venv/bin/activate")

5. Установите зависимости командой "pip install -r req.txt"

6. Создайте БД в PostgreSQL

7. В файле config.py в db_name напишите имя созданной БД

8. запустите скрипт командой "python main.py"