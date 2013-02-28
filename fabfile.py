from fabric.api import local, lcd, local
from datetime import datetime

def prepare_deployment(branch_name):
    #local('python manage.py test BrewMe')
    local('git add -p && git commit')

def deploy_local():
    timestamp = datetime.today().strftime('%Y-%m-%dT%H-%M-%S')
    pathname = '/home/deployer/BrewMe/%s' % timestamp
    local('mkdir %s' % pathname)
    local('cp -r * %s' % pathname)
    with lcd(pathname):
        local('python setup.py develop')
        local('python manage.py runserver 0.0.0.0:8000')
