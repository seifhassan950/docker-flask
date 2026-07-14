To bulid the image:
 run : docker build -t hello:v1

hello:v1 : image name and version 

To build the container :

run : docker run -d --name app -p 80:5000 hello:v1

-d : to run in deattached mode

--name app : to name the container to app

-p 80:5000 : to map port 80 on the host to port 5000 on the container

hello:v1 : image name
