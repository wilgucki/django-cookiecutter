import os


if '{{ cookiecutter.celery_broker }}'.lower() == 'none':
    os.remove(os.path.join('{{ cookiecutter.project_slug }}', 'celery.py'))
    with open(os.path.join('{{ cookiecutter.project_slug }}', '__init__.py'), 'w'):
        pass
