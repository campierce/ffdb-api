# credit https://drstearns.github.io/tutorials/deploy2do/

# server's ip address
ip_address=146.190.68.161

# push latest image
docker push cepie/ffdb-api

# run upgrade script on server
# (this depends on the key in ~/.ssh)
ssh -oStrictHostKeyChecking=no root@$ip_address 'bash -s' < upgrade-server.sh