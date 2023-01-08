# Docker Hub
Store all your images

# Docker Images
Hello world - <code>docker run hello-world</code><br>
CentOs - <code>docker run -it centos /bin/bash</code><br>

-it is used to mention that we want to run in interactive mode.<br>


<hr>
Usually you need to use sudo / run docker as a root. If you run as a normal user, you will get an error "docker.socket issue". <br>

execute below commands to run as a user.<br>
<code>sudo chown sunil:docker /var/run/docker.sock</code><br>
<code>docker context use default</code><br>
<hr>

Displaying docker images: <code>docker images</code><br>
<ul>
<li><b>TAG</b> − This is used to logically tag images.</li>
<li><b>Image ID</b> − This is used to uniquely identify the image.</li>
<li><b>Created</b> − The number of days since the image was created.</li>
<li><b>Virtual Size</b> − The size of the image.</li>
</ul>

<b>Commands:</b>
Downloading docker images: <code>docker run <<-image name->></code><br>
Ex: <code>docker run centos</code><br>
Removing images: <code>docker rmi <<-Image name or Image ID->></code><br>
To return image ID only <code> docker images -q </code><br>
Details of an image or container <code> docker inspect <<-image name or image ID->></code><br>
Hisotry of docker image: <code>docker history <<-image->></code>. This will show all the commands that were run against the image<br>
<hr>

# Docker Containers

Docker container shell script: <code>docker run -it centos /bin/bash</code><br>
Listing containers (Only running): <code>docker ps</code><br>
Listing all containers (Including dorment): <code>docker ps -a</code><br>
