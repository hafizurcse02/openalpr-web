# Openalpr Webservice in a docker container

```
docker run -d -p 8888:8888 ankushagarwal11/openalpr-web

curl -X POST -F "image=@license.jpg" http://boot2docker:8888/alpr
```
