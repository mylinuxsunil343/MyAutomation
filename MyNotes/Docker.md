# Docker Hub
Store all your images

# Docker Images
Hello world - <code>docker run hello-world</code>
CentOs - <code>docker run -it centos /bin/bash</code>

Usually you need to use sudo / run docker as a root. If you run as a normal user, you will get an error "docker.socket issue". <br>

execute below commands to run as a user.<br>
<code>sudo chown sunil:docker /var/run/docker.sock</code><br>
<code>docker context use default</code><br>