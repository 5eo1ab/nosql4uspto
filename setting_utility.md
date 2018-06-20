# setting for utility

## install python-pip
```
$ cd ~
$ sudo apt update
$ sudo apt install python3 python3-dev
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py
$ pip3 --version
pip 10.0.1 from /usr/local/lib/python3.5/dist-packages/pip (python 3.5)
```

## install selenium & chrome-driver
```
# install selenium
$ sudo pip3 install selenium
$ sudo apt-get install chromium-chromedriver
```

## install mongodb
reference url: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
## install pymongo
```
$ python -m pip install --upgrade pymongo
Installing collected packages: pymongo
Successfully installed pymongo-3.6.1
```

## install spluck connector
```
$ pip install splunk-sdk
Installing collected packages: splunk-sdk
Successfully installed splunk-sdk-1.6.4

$ export PYTHONPATH=~/splunk-sdk-python
```

