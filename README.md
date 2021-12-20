[![pytest with Github Actions](https://github.com/khan2a/python-repo/actions/workflows/pytest-main.yml/badge.svg)](https://github.com/khan2a/python-repo/actions/workflows/pytest-main.yml)
# python-repo
First let's create a virtual environment

option 1) which virtualenv
virtualenv --help
virtualenv ~/Python/venvs/python-repo-venv

option 2) python3 -m venv env

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

# python-repo integration with AWS
Generate a new SSH key:
ssh-keygen -t rsa -C "engineer.atique@gmail.com"
Copy the contents of the file ~/.ssh/id_rsa.pub to your SSH keys in your GitHub account settings (https://github.com/settings/keys).
Test SSH key:
$ ssh -T git@github.com
Hi! You've successfully authenticated, but GitHub does not provide shell access.
Change directory into the local clone of your repository (if you're not already there) and run:
git remote set-url origin git@github.com:khan2a/python-repo.git
Now try editing a file (try the README) and then do:
$ git commit -am "Update README.md"
$ git push
You should not be asked for a username or password. If it works, your SSH key is correctly configured.


In AWS create cloudshell and clone (SSH) url from github
cloudshell: git clone git@github.com:khan2a/python-repo.git
Same for cloud9

CodeBuild in AWS is equivalent to Github Actions
uses buildspec.yml for Github Actions for install lint test and format