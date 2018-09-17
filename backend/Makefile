bootstrap:

	virtualenv venv
	echo "Installing packages from requirements.txt"
	venv/bin/pip install -r requirements.txt

dev:

	. venv/bin/activate; python create_app.py

prod:

	. venv/bin/activate; gunicorn --bind "0.0.0.0:8090" -w 4 create_app:app

docker-prod:

	gunicorn --bind "0.0.0.0:8090" -w 4 create_app:app

