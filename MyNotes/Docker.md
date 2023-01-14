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

- Docker container shell script: <code>docker run -it centos /bin/bash</code><br>
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

MySQL Server: <code>docker container run -d -p 3306:3306 --name db -e MYSQL_RANDOM_ROOT_PASSWORD-yes mysql</code><br>
<ul>
<li>-e : environment varable</li>
<li>-p : port</li>
</ul>