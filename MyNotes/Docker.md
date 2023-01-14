# Docker Hub
Store all your images
- Pull imahe from Docker hub <code>docker pull <<-image>>:<<-tag->> </code><br>
    ex: docker pull ubuntu:latest
- Tagging an image <code>docker tag imageID Repositoryname</code>
- Storing custom image in docker hub <code>docker push Repositoryname</code>

# Docker basic commands

- version <code>docker version</code>
- Info <code>docker info</code>

# Docker Images
Hello world - <code>docker run hello-world</code><br>
CentOs - <code>docker run -it centos /bin/bash</code><br>

-it is used to mention that we want to run in interactive mode.<br>

Displaying docker images: <code>docker images</code><br>
<ul>
<li><b>TAG</b> − This is used to logically tag images.</li>
<li><b>Image ID</b> − This is used to uniquely identify the image.</li>
<li><b>Created</b> − The number of days since the image was created.</li>
<li><b>Virtual Size</b> − The size of the image.</li>
</ul>

<b>Commands:</b><br>
- Downloading docker images: <code>docker run <<-image name->></code><br>
Ex: <code>docker run centos</code><br>
- Removing images: <code>docker rmi <<-Image name or Image ID->></code><br>
- To return image ID only <code> docker images -q </code><br>
- Details of an image or container <code> docker inspect <<-image name or image ID->></code><br>
- Hisotry of docker image: <code>docker history <<-image->></code>. This will show all the commands that were run against the image<br>
<hr>

# Docker Containers

- Listing containers (Only running): <code>docker ps</code>
- Listing all containers (Including dorment): <code>docker ps -a</code> or <code>docker container ls -a </code>
- Delete all inactive / dormant containers: <code>docker container prune</code>
- Top process running within container: <code>docker top <<-containerID or name->></code><br>
- Stopping container: <code>docker stop <<-container ID or name->></code>
- Removing container: <code>docker rm <<-container ID/part of container id or name->></code> <br>
ex: <code>docker rm abc</code> will remove the containers starting with abc & if those container stopped<br>
Note: you can not deleted running containers<br>
- statistics of a running container: <code>docker stats <<-container ID or name->></code>
- Attaching container: <code>docker attach <<-container ID or name->></code>, then run top command to see container stats.
- pause the processes in a running container <code>docker pause <<-container ID or name->></code>
- unpause the processes in a running container <code>docker unpause <<-container ID or name->></code>
- kill the processes in a running container <code>docker kill <<-container ID or name->></code>
- starting docker container <code> docker container start <<-container names->> </code>
- Portdetails : <code>docker container port webserver</code>
- Use inspect and format to get additional detials <code>docker container inspect --format "{{ .NetworkSettings.IPAddress }}" container-name </code>

<b>Advanced</b><br>

Publishing Ports:  <code>docker run -it -p 80:80 --detach --name mycontainer nginx</code><br>
<ul>
<li>-it : interactive</li>
<li>-p : publishing ports source:destination</li>
<li>--detach or -d : run in the background</li>
<li>--name : custom name of container</li>
</ul> 

# Docker Architecture vs VM

<image src="docker-arch.jpg">

# Docker container & Shell

- Create container and login to shell <code>docker run -it <<-Image name->> /bin/bash</code>
- Login to shell, already running container <code>docker exec -it <<-Container name->> /bin/bash</code>
<hr>

# Docker file

Sample code: <br>
<code>FROM ubuntu <br>
<br>
RUN apt-get update <br> 
RUN apt-get install –y nginx<br> 
CMD [“echo”,”Image created”] <br>
</code>

# Docker building file
- Command to build, change directory to docker file and execute <code>docker build . </code>
- Build own docker image: <code>docker build -t ImageName:TagName <<-Dockerfile->></code>
<hr>

# Assignment 1 - Managing multiple containers

<b>MySQL Server:</b><br> 
MySql Container: <code>docker container run -d -p 3306:3306 --name db -e MYSQL_RANDOM_ROOT_PASSWORD=yes mysql</code><br>
<ul>
<li>-e : environment varable</li>
<li>-p : port</li>
<li>-d : detached </li>
</ul>
<code>docker container logs db</code> to check mysql password<br>

<b> Web server</b>

- HTTPD Server: <code>docker container run -d --name webserver -p 8081:80 httpd</code>
We are binding containers 80 port to host 8081<br>
- Check http://localhost:8081/ whether httpd container running or not</br>
<code>docker container ls -a</code> to check both container running<br>

<b>Proxy NGINX</b><br>

- Nginx container: <code>docker container run -d --name proxy -p 80:80 nginx</code>
- Check http://localhost whether nginx container running or not</br>
<code>docker container ls -a</code> to check both container running<br>

# Container process monitoring

- List top process <code>docker container top <<-container name->> </code>
- Details of config <code>docker container inspect <<-container name->> </code>
- Performance stats <code>docker container stats <<-container name->> </code>
<hr>

# Getting inside container
- Docker new container accessing shell : <code>docker run -it container-name /bin/bash</code>
- Docker exisitng container accessing shell: <code>docker container exec -it container-name /bin/bash</code>
<hr>

# Create image from Docker container

For ex you created an image using ubuntu and you installed a package. You can create an image using the container, so evrytime you create an instance package automatically installed. <br>

Steps:
- Create container: <code>docker run -d -it --name myubuntu ubuntu</code>
- Login to container shell: <code>docker exec -it myubuntu /bin/bash </code>
- Install necessary packages: <code>apt-get -y update; apt-get install -y curl</code>
- Create image : <code> docker commit -p -a "Author Sunil" container-name myimage:v1 </code>
<hr>

# Docker networking
Each container connected to a provate virtual network "bridge". Each virtual network routes through NAT firewall  on host Ip.<br> 

All containers on a virtual network can talk to each other without -p. Create a new virtual network for wach app (Nginx, httpd & mysql)<br>

<b>Commands</b>

- Show netwroks <code>docker network ls</code>
- Create network <code>docker network create --driver</code>
- Attach network to container <code>docker network connect</code>
- Detach network to container <code>docker network disconnect</code>

Ex: <code>docker network create my_app_network</code><br>
- Attach while creating container <code>docker container run -d --name mycontainer --network my_app_network nginx</code><br>
- Check which containers attached to network <code>docker network inspect my_app_network</code><br>
- Connect exisiting containers <code>docker network connect <<-container/s....>> </code>
- Disconnect network <code>docker network disconnect <<-container/s....>> </code>

<b>Docker networks - DNS</b>

- Docker daemon has a built-in DNS server that containers use by default
- Docker defaults the hostname to the containers name. but you can also set aliases
- Containers attached to the same network can talk to each other irrescptive of their IP Addresses 
Ex: if container1 & container2 attached to mynetwork, both can talk to each other <code>docker container exec -it container1 ping container2</code> vice versa <br>

You can manually link containers using --link (In case if you do not want to use custome network)<br>
<br>

# Assignemtn 2 - DNS Round robin test


