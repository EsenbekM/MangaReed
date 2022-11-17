ython manage.py makemigrations
python manage.py migrate
python manage.py scrapy_data
python manage.py collectstatic --no-input  
gunicorn -b 0.0.0.0:8666 core.wsgi --reload
