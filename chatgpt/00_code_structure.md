CODE STRUCTURE
---
```
-- Dockerfile
|-- README.md
|-- api
|   |-- __init__.py
|   |-- authenticated
|   |   |-- __init__.py
|   |   |-- apps.py
|   |   |-- profile
|   |   |   |-- __init__.py
|   |   |   |-- serializers.py
|   |   |   |-- tests
|   |   |   |   |-- __init__.py
|   |   |   |   `-- test_views.py
|   |   |   `-- views.py
|   |   |-- urls.py
|   |   `-- user
|   |       |-- __init__.py
|   |       |-- profile
|   |       |   |-- __init__.py
|   |       |   |-- serializers.py
|   |       |   |-- tests
|   |       |   |   |-- __init__.py
|   |       |   |   `-- test_views.py
|   |       |   `-- views.py
|   |       |-- serializers.py
|   |       |-- tests
|   |       |   |-- __init__.py
|   |       |   `-- test_views.py
|   |       `-- views.py
|   |-- authentication
|   |   |-- __init__.py
|   |   |-- apps.py
|   |   |-- tests
|   |   |   |-- __init__.py
|   |   |   `-- tokens
|   |   |       |-- __init__.py
|   |   |       `-- test_tokens.py
|   |   `-- urls.py
|   |-- chatgpt
|   |   |-- 01_prompts.md
|   |   |-- 02_codes.md
|   |   `-- 03_codes.md
|   |-- product_management
|   |   |-- __init__.py
|   |   |-- apps.py
|   |   |-- categories
|   |   |   |-- __init__.py
|   |   |   |-- id
|   |   |   |   |-- __init__.py
|   |   |   |   |-- serializers.py
|   |   |   |   |-- tests
|   |   |   |   |   |-- __init__.py
|   |   |   |   |   `-- test_views.py
|   |   |   |   `-- views.py
|   |   |   |-- serializers.py
|   |   |   |-- tests
|   |   |   |   |-- __init__.py
|   |   |   |   `-- test_views.py
|   |   |   `-- views.py
|   |   |-- products
|   |   |   |-- __init__.py
|   |   |   |-- id
|   |   |   |   |-- __init__.py
|   |   |   |   |-- serializers.py
|   |   |   |   |-- tests
|   |   |   |   |   |-- __init__.py
|   |   |   |   |   `-- test_views.py
|   |   |   |   `-- views.py
|   |   |   |-- serializers.py
|   |   |   |-- tests
|   |   |   |   |-- __init__.py
|   |   |   |   `-- test_views.py
|   |   |   `-- views.py
|   |   `-- urls.py
|   |-- store_management
|   |   |-- __init__.py
|   |   |-- apps.py
|   |   |-- stores
|   |   |   |-- __init__.py
|   |   |   |-- id
|   |   |   |   |-- __init__.py
|   |   |   |   |-- serializers.py
|   |   |   |   |-- tests
|   |   |   |   |   |-- __init__.py
|   |   |   |   |   `-- test_views.py
|   |   |   |   `-- views.py
|   |   |   |-- serializers.py
|   |   |   |-- tests
|   |   |   |   |-- __init__.py
|   |   |   |   `-- test_views.py
|   |   |   `-- views.py
|   |   `-- urls.py
|   `-- user_management
|       |-- __init__.py
|       |-- apps.py
|       |-- urls.py
|       `-- users
|           |-- __init__.py
|           |-- id
|           |   |-- __init__.py
|           |   |-- profile
|           |   |   |-- __init__.py
|           |   |   |-- serializers.py
|           |   |   |-- tests
|           |   |   |   |-- __init__.py
|           |   |   |   `-- test_views.py
|           |   |   `-- views.py
|           |   |-- serializers.py
|           |   |-- stores
|           |   |   |-- __init__.py
|           |   |   |-- serializers.py
|           |   |   |-- tests
|           |   |   |   |-- __init__.py
|           |   |   |   `-- test_views.py
|           |   |   `-- views.py
|           |   |-- tests
|           |   |   |-- __init__.py
|           |   |   `-- test_views.py
|           |   `-- views.py
|           |-- serializers.py
|           |-- tests
|           |   |-- __init__.py
|           |   `-- test_views.py
|           `-- views.py
|-- celerybeat-schedule
|-- docker-compose.yml
|-- domain
|   |-- __init__.py
|   |-- commons
|   |   |-- __init__.py
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- management
|   |   |   |-- __init__.py
|   |   |   `-- commands
|   |   |       |-- __init__.py
|   |   |       `-- celery.py
|   |   `-- models
|   |       |-- Base.py
|   |       `-- __init__.py
|   |-- customers
|   |   `-- __init__.py
|   |-- loggings
|   |   `-- __init__.py
|   |-- orders
|   |   `-- __init__.py
|   |-- products
|   |   |-- __init__.py
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- migrations
|   |   |   |-- 0001_initial.py
|   |   |   |-- 0002_alter_category_id_alter_product_id.py
|   |   |   `-- __init__.py
|   |   |-- models
|   |   |   |-- Category.py
|   |   |   |-- Product.py
|   |   |   `-- __init__.py
|   |   |-- selectors
|   |   |   `-- __init__.py
|   |   |-- services
|   |   |   |-- __init__.py
|   |   |   |-- service_Category.py
|   |   |   `-- service_Product.py
|   |   |-- tasks
|   |   |   `-- __init__.py
|   |   `-- tests
|   |       |-- __init__.py
|   |       |-- models
|   |       |   |-- __init__.py
|   |       |   |-- test_Category.py
|   |       |   `-- test_Product.py
|   |       |-- services
|   |       |   |-- __init__.py
|   |       |   |-- test_service_Category.py
|   |       |   `-- test_service_Product.py
|   |       `-- utils
|   |           |-- __init__.py
|   |           |-- test_utils_Category.py
|   |           `-- test_utils_Product.py
|   |-- stores
|   |   |-- __init__.py
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- migrations
|   |   |   |-- 0001_initial.py
|   |   |   |-- 0002_alter_store_options.py
|   |   |   |-- 0003_alter_store_id.py
|   |   |   `-- __init__.py
|   |   |-- models
|   |   |   |-- Store.py
|   |   |   `-- __init__.py
|   |   |-- selectors
|   |   |   `-- __init__.py
|   |   |-- services
|   |   |   |-- __init__.py
|   |   |   `-- service_Store.py
|   |   |-- tasks
|   |   |   `-- __init__.py
|   |   `-- tests
|   |       |-- __init__.py
|   |       |-- models
|   |       |   |-- __init__.py
|   |       |   `-- test_Store.py
|   |       |-- services
|   |       |   |-- __init__.py
|   |       |   `-- test_service_Store.py
|   |       `-- utils
|   |           |-- __init__.py
|   |           `-- test_utils_Store.py
|   `-- users
|       |-- __init__.py
|       |-- admin.py
|       |-- apps.py
|       |-- migrations
|       |   |-- 0001_initial.py
|       |   |-- 0002_alter_profile_id.py
|       |   `-- __init__.py
|       |-- models
|       |   |-- Profile.py
|       |   |-- Receiver.py
|       |   `-- __init__.py
|       |-- permissions
|       |   `-- permission_group.py
|       |-- selectors
|       |   `-- __init__.py
|       |-- services
|       |   |-- __init__.py
|       |   `-- service_User.py
|       |-- tasks
|       |   |-- __init__.py
|       |   `-- task_mailer.py
|       `-- tests
|           |-- __init__.py
|           |-- models
|           |   |-- __init__.py
|           |   |-- test_Profile.py
|           |   `-- test_Receiver.py
|           |-- permissions
|           |   |-- __init__.py
|           |   `-- test_group.py
|           |-- services
|           |   |-- __init__.py
|           |   `-- test_service_User.py
|           |-- tasks
|           |   |-- __init__.py
|           |   `-- test_task_mailer.py
|           `-- utils
|               `-- utils.py
|-- manage.py
|-- project
|   |-- __init__.py
|   |-- asgi.py
|   |-- celery.py
|   |-- management
|   |   `-- commands
|   |-- serializers.py
|   |-- settings.py
|   |-- tests.py
|   |-- urls.py
|   |-- views.py
|   `-- wsgi.py
`-- requirements.txt
```
