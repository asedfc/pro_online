function start(){
    python manage.py runserver 0:80
}

function stop(){
    ps -ef | grep runserver
}

start