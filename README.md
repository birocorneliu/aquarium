
###### Hello, this is a quick guide on how to install this app

Aquarium automation
===================




#### Enable / start SSH
```
sudo systemctl enable ssh
sudo systemctl start ssh
```

#### Remote login and run commands:
```
passwd

sudo echo $'Host *\nServerAliveInterval 240' > ~/.ssh/config
sudo chmod 600 ~/.ssh/config
sudo service ssh restart
sudo rm /etc/localtime
sudo ln -s /usr/share/zoneinfo/Europe/Bucharest /etc/localtime

#link to github

sudo aptitude install vim virtualenv supervisor python-dev
pip install -U flask-cors

virtualenv --no-site-packages aquarium
cd aquarium
git clone git@github.com:biropi/aquarium.git
cd aquarium/raspberry/
sudo pip install -r requirements.txt 
. ../../bin/activate
make configure
```

#### Add file(s)
`/etc/supervisorctls/conf.d/aquarium.conf`
```[program:aquarium]
command=/home/pi/aquarium/bin/python /home/pi/aquarium/aquarium/raspberry/server.py
autostart=true
autorestart=true

stdout_logfile=/var/log/supervisor/aquarium_stdout.log
stdout_logfile_maxbytes=10MB
stdout_logfile_backups=3
stdout_capture_maxbytes=10MB
stderr_logfile=/var/log/supervisor/aquarium_stderr.log
stderr_logfile_maxbytes=10MB
stderr_logfile_backups=3
stderr_capture_maxbytes=10MB
```

`/etc/supervisorctls/conf.d/buttons.conf`
```[program:aquarium_buttons]
command=/home/pi/aquarium/bin/python /home/pi/aquarium/aquarium/raspberry/server_buttons.py
autostart=true
autorestart=true

stdout_logfile=/var/log/supervisor/aquarium_buttons_stdout.log
stdout_logfile_maxbytes=10MB
stdout_logfile_backups=3
stdout_capture_maxbytes=10MB
stderr_logfile=/var/log/supervisor/aquarium_buttons_stderr.log
stderr_logfile_maxbytes=10MB
stderr_logfile_backups=3
stderr_capture_maxbytes=10MB
```
#### RUN
`sudo supervisorctl update`

#### Set Temperature sensor
`sudo vim /boot/config.txt` and write at the bottom **dtoverlay=w1-gpio**
```
sudo modprobe w1-gpio
sudo modprobe w1-therm
ls /sys/bus/w1/devices
cat /sys/bus/w1/devices/28-xxx/w1_slave
```
