Prerequsites:  
Docker  

Start app:  
1 git clone https://github.com/boyboyjoy/Shop.git  
2 cd Shop  
3 docker-compose up -d --build  
4 docker-compose restart django  
5 docker-compose run django python manage.py migrate  
6 open 127.0.0.1:8000 in any browser  
