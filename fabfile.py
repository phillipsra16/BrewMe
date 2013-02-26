from fabric.api import local, lcd, local

def prepare_deployment(branch_name):
    local('python manage.py test BrewMe')
    local('git add -p && git commit')

def deploy():
    with lcd('/home/deployer/BrewMe'):
        local('git pull github master -ff')
        local('python setup.py develop')
        local('python manage.py runserver 0.0.0.0:8000')
