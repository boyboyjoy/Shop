Prerequsites:
Docker

Start app:
git clone https://github.com/boyboyjoy/Shop.git
cd Shop
docker-compose up -d --build
docker-compose restart django
docker-compose run django python manage.py migrate
open 127.0.0.1:8000 in any browser
