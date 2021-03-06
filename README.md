
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

sudo mkdir -p ~/.ssh
sudo echo $'Host *\nServerAliveInterval 240' > ~/.ssh/config
sudo chmod 600 ~/.ssh/config
sudo service ssh restart
sudo rm /etc/localtime
sudo ln -s /usr/share/zoneinfo/Europe/Bucharest /etc/localtime

ssh-keygen -t rsa -b 4096 -C "corneliu.biro@gmail.com"

eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub
#link to github

sudo apt-get -y install vim virtualenv supervisor python-dev
pip install -U flask-cors

virtualenv --no-site-packages aquarium
cd aquarium
git clone git@github.com:birocorneliu/aquarium.git
cd aquarium/raspberry/
sudo pip install -r requirements.txt 
. ../../bin/activate
make configure
sudo cp config_files/supervisor/*.conf /etc/supervisor/conf.d/
echo "" | sudo tee -a /etc/crontab
echo "* *     * * *   root    curl http://127.0.0.1/reload_pins" | sudo tee -a /etc/crontab
echo "*/10 *     * * *   root    curl http://127.0.0.1/set_temperature" | sudo tee -a /etc/crontab
sudo supervisorctl update
tail -f /var/log/supervisor/aquarium_stderr.log 
```

#### Set Temperature sensor
```
echo "dtoverlay=w1-gpio" | sudo tee -a /boot/config.txt
sudo reboot

sudo modprobe w1-gpio
sudo modprobe w1-therm
ls /sys/bus/w1/devices
cat /sys/bus/w1/devices/28-xxx/w1_slave
```
