from fabric.api import local, lcd, local

def prepare_deployment(branch_name):
    local('python manage.py test BrewMe')
    local('git add -p && git commit')

def deploy():
    with lcd('/home/deployer/BrewMe'):
        local('git pull /home/wyattpj/dev/BrewMe')
        local('python manage.py migrate BrewMe')
        local('python manage.py test BrewMe')
        local('python manage.py runserver 0.0.0.0:8000')
