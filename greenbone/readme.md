# 1 Generate certificate for gsa service
Generate Certificates:
```
openssl req -x509 -newkey rsa:4096 -keyout serverkey.pem -out servercert.pem -nodes -days 397
```
move files to readable directory for docker
```
sudo mkdir /home/ali/.ssl && mv serverkey.pem servercert.pem /home/ali/.ssl  
```
edit it so gsa user can read the file
```
cd /home/ali/.ssl
sudo chmod 444 *.pem
sudo chown 1001:1001 *.pem
```



# 2 pull and run docker file
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
change password for admin user:
sudo docker exec -u gvmd greenbone-community-edition-gvmd-1 gvmd --user=admin --new-password='CHANGETHIS'
