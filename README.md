## Запуск проекта в Docker окружении

- Запустить проект: 
    ```shell
    docker-compose up --build
     ```
- Запустить проект в автономном режиме: 
    ```shell
    docker-compose up -d --build
     ```
- Применить миграции
    ```shell
    docker-compose exec web alembic upgrade head
     ```
## Запуск проекта локально c БД в Docker
  **В файле core/datebase.py использовать** 
  ```python
SQLALCHEMY_DATABASE_URL = "postgresql://user_pg:pg_password@localhost/"
  ```

- Для запуска базы данных используйте postgres-local.yaml
  ```shell
    docker-compose -f postgres-local.yaml up -d
   ```
- Создать виртуальное окружение

- Установить зависимости
  ```shell
    pip install -r requirements.txt
   ```
- Применить миграции
  ```shell
    alembic upgrade head
   ```
- Запустить проект
  ```shell
    python main.py
   ```
  
**Документация http://127.0.0.1:8000/docs#/**