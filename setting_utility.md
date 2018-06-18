# setting for utility

if not exist 'utility' directory   
```
$ mkdir utility
```

## install geckodriver 
```
$ cd ./utility
$ wget https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-linux64.tar.gz
$ tar -xvzf geckodriver-v0.21.0-linux64.tar.gz 
$ chmod +x geckodriver
$ export PATH=$PATH:~/seo/nosql4uspto/utility/geckodriver ??
$ sudo mv geckodriver /usr/local/bin
```

