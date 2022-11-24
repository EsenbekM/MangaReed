ython manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py get_data_users
python manage.py get_data_manga
python manage.py get_data_comments
gunicorn -b 0.0.0.0:8666 core.wsgi --reload
