
/wait-for-it.sh db:3306 --timeout=30 --strict -- echo "Database is up"

python manage.py migrate

python manage.py collectstatic --noinput

python manage.py runserver 0.0.0.0:8000
