
###### Hello, this is a quick guide on how to install this app

Aquarium automation
===================


Set raspberry pi app
--------------------
#### Install system requirements and set config files

#### Set timezone
```
sudo rm /etc/localtime
sudo ln -s /usr/share/zoneinfo/Europe/Bucharest /etc/localtime
```

#### Set Temperature sensor
`sudo vim /boot/config.txt` and write at the bottom **dtoverlay=w1-gpio**
```
sudo modprobe w1-gpio
sudo modprobe w1-therm
ls /sys/bus/w1/devices
cat /sys/bus/w1/devices/28-xxx/w1_slave
```

#### Keep ssh alive
sudo vim ~/.ssh/config
Host *
ServerAliveInterval 240

sudo chmod 600 ~/.ssh/config
sudo service ssh restart


