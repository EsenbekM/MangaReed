python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py get_data_users
python3 manage.py get_data_genre
python3 manage.py get_data_manga
python3 manage.py create_translators
python3 manage.py collectstatic --no-input
gunicorn -b 0.0.0.0:8666 core.wsgi --reload
