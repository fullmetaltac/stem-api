# Docker run
`docker build -t stem . && docker run -dit --restart unless-stopped -p 5000:5000 stem`

# Run as a service
`sudo nano /etc/init/flask.conf`

`description "flask"
start on stopped rc RUNLEVEL=[2345]
respawn
exec /usr/bin/python3 /home/pi/stem-api/app.py`

`sudo nano /lib/systemd/system/flask.service`

`[Unit]
Description=Flask web server

[Install]
WantedBy=multi-user.target

[Service]
User=pi
PermissionsStartOnly=true
ExecStart=/home/pi/stem-api/app.py
TimeoutSec=600
Restart=on-failure
RuntimeDirectoryMode=755`

`chown pi /home/pi/stem-api/app.py` 
`chmod +x /home/pi/stem-api/app.py`

`sudo service flask start`
`sudo service flask status`
