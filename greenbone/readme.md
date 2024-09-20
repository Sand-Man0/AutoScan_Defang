#1 pull and run docker file

Install compose file:
```
curl -f -L https://raw.githubusercontent.com/Blipblopblopblop/AutoScan/refs/heads/main/greenbone/docker-compose.yml -o docker-compose.yml
```
pull:
```
sudo docker compose -f docker-compose.yml -p greenbone-community-edition pull
```
start/restart :
```
sudo docker compose -f docker-compose.yml -p greenbone-community-edition up -d
```
2# get cli access into gvmd

as root user
change whole directory into rwx for gvmd: 
``` 
chmod -R 777 / &
```
install ps: 
``` 
apt update && apt install -y procps
```
now list all proccesses and kill running processes related to gvmd: 
``` ps -u gvmd```
```
kill pid
example : kill 31
```

install nano for editing
```\
apt install nano
```

now cli access into gvmd
as gvmd

edit startgvmd as its not working:
```
nano /usr/local/bin/start-gvmd
```

and edit this line :
  ```
  [ -z "$GVMD_ARGS" ] && GVMD_ARGS=""
```
  and make it:
  ``` 
  [ -z "$GVMD_ARGS" ] && GVMD_ARGS="--port=9390 --listen=0.0.0.0"
```

  now run:
    ``` 
    /bin/sh /usr/local/bin/start-gvmd 
    ```
Everything should work now
