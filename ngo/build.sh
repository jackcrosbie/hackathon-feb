set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input --settings=ngo.settings
python manage.py makemigrations --settings=ngo.settings
python manage.py migrate --settings=ngo.settings
 