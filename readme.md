To do list:
* Design UI
* create a new app (if necessary)
* using the html in templates

The base.html must be used throught the project for visual consistency. 

# Useful Django command

```python
	# to start a new app
	python manage.py startapp app_name
	
	# to run server:
	python manage.py runserver
	
	# to clear all expired session:
	python manage.py clearsessions
```

# Useful git command
After installing github desktop, we are ready to follow these steps.
```shell
	git config --global user.name "YOUR NAME"
	git config --global user.email "YOUR EMAIL ADDRESS"
	
	# to clone remote repository to local
	git clone https://github.com/wasit7/djapps.git
	
	# to pull latest update from remote repository
	git pull
	
	# to reset local repository
	git fetch origin
	git reset --hard origin/master
	
	# to add all local update to remote repository
	git commit -a -m "this is all updates"
	git push
```
