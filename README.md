[![pytest with Github Actions](https://github.com/khan2a/python-repo/actions/workflows/pytest-main.yml/badge.svg)](https://github.com/khan2a/python-repo/actions/workflows/pytest-main.yml)
# python-repo
First let's create a virtual environment
which virtualenv
virtualenv --help
virtualenv ~/Python/venvs/python-repo-venv
source ~/Python/venvs/python-repo-venv/bin/activate
which python

Then create scaffolding of project
touch Makefile
touch requirements.txt
touch hello.py
touch test_hello.py

Then run Makefile to install pre-requisites
make install

To run pytests
make test

To check linting works:
make lint

TO clean-up and format the code:
make format

Finally to freeze requirements
pip freeze and then update versions in the requirements.txt

To do all at once:
make all

Push the code:
git pull
git status
git add *
git commit -m "adding initial layout of python project"
git push
git pull

Github Actions file:
https://github.com/khan2a/python-repo/blob/main/.github/workflows/pytest-main.yml
Copy/paste the badge from Action > Run workflow to Readme.md
