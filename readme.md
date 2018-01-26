# Wordpress-users

This utility searches Wordpress users.

## Requirements
* python 2.7
* virtualenv

##Install
```bash
$ git clone git@github.com:marosverziovy/wordpress-users.git
$ cd wordpress-users
$ virtualenv env
$ pip install -r src/requirements.txt
```

##Usage
```bash
$ source env/bin/activate
$ ./src/wordpress-users.py https://revalid.sk
```

###Debug
To print debug info, use `-d` (or `--debug`) parameter.
