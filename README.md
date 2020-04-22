### Install braistem
1) Download acroname dev kit: https://acroname.com/software/brainstem-development-kit
1) Install `pip3 install python/brainstem-2.7.12-py2.py3-none-any.whl`

# Docker run
`docker build -t stem . && docker run -dit --restart unless-stopped -p 5000:5000 stem`

# Run as a service
`sudo nano /etc/init/flask.conf`

description "flask" <br />
start on stopped rc RUNLEVEL=[2345] <br />
respawn <br />
exec /usr/bin/python3 /home/pi/stem-api/app.py <br />

`sudo nano /lib/systemd/system/flask.service`

[Unit] <br />
Description=Flask web server <br />
[Install] <br />
WantedBy=multi-user.target <br />
[Service] <br />
User=pi <br />
PermissionsStartOnly=true <br />
ExecStart=/home/pi/stem-api/app.py <br />
TimeoutSec=600 <br />
Restart=on-failure <br />
RuntimeDirectoryMode=755 <br />

`chown pi /home/pi/stem-api/app.py` 
`chmod +x /home/pi/stem-api/app.py`

`sudo service flask start`
`sudo service flask status`
