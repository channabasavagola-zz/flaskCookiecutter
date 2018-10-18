rm app.db
rm -rf migrations/

ls

python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py createdb

sqlite3 app.db