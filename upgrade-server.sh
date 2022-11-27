# pull latest image
docker pull cepie/ffdb-api

# remove current container
# (if this is a fresh install this will error, but that's fine)
docker rm -f ffdb-api

# run new container
docker run -d \
-p 80:80 \
-v ffdb:/home \
--name ffdb-api \
cepie/ffdb-api