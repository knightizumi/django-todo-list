# django-todo-list

```shell
# 顯示所有安裝的套件
$ pip list

# 建立虛擬環境
$ python -m venv env

# 進入虛擬環境
$ Windows: .\env\Scripts\activate.bat
$ Mac: source ./env/bin/activate

# 退出虛擬環境
$ deactivate

# 安裝 Django
$ pip install Django

# 安裝 ipython
$ pip install ipython

# 安裝 bootstrap4
$ pip install django-bootstrap4

# 安裝 djangorestframework
$ pip install djangorestframework

# 建立 Django專案 核心目錄
$ django-admin startproject core .

# 建立 app
$ python manage.py startapp todo

# 建立資料表
$ python manage.py makemigrations

# 寫進資料庫
$ python manage.py migrate

# 建立超級專案使用者
$ python manage.py createsuperuser

# 執行 server http://127.0.0.1:8000/admin/
$ python manage.py runserver

# 哪裡有 Python
$ where python

# 建立api app
$ python manage.py startapp api

# 可分享檔案
$ python -m http.server

# 紀錄專案用過的套件及版本
$ pip freeze > ./requirements.txt

# 安裝紀錄的套件及版本
$ pip install -r requirements.txt

#
$ python manage.py shell
$ from django.contrib.auth.models import User
$  u=User.objects.first()
$ u.email_user('title','content')

# 安裝mysqlclient
$ pip install mysqlclient


```
