This describes setting up REDIS server on the ATA dsp-control server

Setting up REDIS on the new dsp-control 

According to: https://redis.io/docs/getting-started/installation/install-redis-on-linux/

```
$ curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

$ echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

$ sudo apt-get update
$ sudo apt-get install redis
```

Disable the builtin redis systemctl service

```
$ sudo systemctl stop redis-server.service
$ sudo systemctl disable redis-server.service
```

Create redis working directory:

`$ sudo mkdir -p /var/redis/6379`

(6379 is the default TCP port number we are using)

Change ownership of working directory:

`sudo chown redis:redis /var/redis/6379/`

`6379.conf` and `redis_6379` should be in:
`/etc/redis/`

`redis.service` should be in:
`/etc/systemd/system/`


Once all the above configuration files and executables are in their corresponding directories:
```
$ sudo systemctl daemon-reload
$ sudo systemctl enable redis.service
$ sudo systemctl start redis.service
```


The REDIS log file (as specified in the `6379.conf` configuration file) should be:

```
/var/log/redis/redis_6379.log
```

One can also view the systemctl log file with:

```
$ sudo journalctl -u redis.service
```
