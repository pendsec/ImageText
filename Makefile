.DEFAULT_GOAL := all

coverage:
	coverage run manage.py test
	coverage report

test:
	python manage.py test

clean:
	find . -name '*.pyc' -delete
	coverage erase
	rm -r **/__pycache__

format:
	isort . -rc
	autopep8 . -r --aggressive --in-place

validate:
	isort . -rc -c
	flake8 . --count

check:
	python manage.py check

runserver:
	python manage.py runserver

all: validate check coverage