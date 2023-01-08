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