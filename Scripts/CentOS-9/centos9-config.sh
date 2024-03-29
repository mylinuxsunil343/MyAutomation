#!/bin/bash
banner()
{
  echo "+------------------------------------------+"
  printf "| %-40s |\n" "`date`"
  echo "|                                          |"
  printf "|`tput bold` %-40s `tput sgr0`|\n" "$@"
  echo "+------------------------------------------+"
}
banner "Hi, Sunil Marella/n checking system details"
echo "Linux kernal : $(uname -or)"
echo "Using $(getconf LONG_BIT) bit Linux distro."

echo "Changing to download directory"
echo "updating system"
dnf -y update; dnf -y upgrade
Banner "Mandatory software installation"
cd /home/sunil/Downloads/
echo "Installing yum-utils, epel repos"
dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
yum -y install yum-utils
echo "Installing necessary sw for virtualbox guest additions"
dnf -y install gcc kernel-devel kernel-headers make bzip2 perl
banner "Creating / updating repos"
echo "Adding docker repo"
if [[ ! -e /etc/yum.repos.d/docker-ce.repo ]]; then
      echo "Docker repo File does not exist, creating docker repo"
      yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
fi
echo "Updating  google repos"
if [[ ! -e /etc/yum.repos.d/google-chrome.repo ]]; then
      echo "Google repo does not exist, creating google chrome repo"
      touch /etc/yum.repos.d/google-chrome.repo
fi
echo "Updating VSCode repo"
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
echo "Updating Jenkins repo"
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
banner "Installing all softwares detaiils"
echo "Installing google chrome"
dnf -y install google-chrome-stable
echo "Installing ansible"
dnf -y install ansible
echo "Installing python3"
dnf -y install python3
echo "Installing docker"
dnf -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin
echo "Installing git"
dnf -y install git
echo "Installing VS Code"
dnf -y install code
echo "Installing Open java 11"
dnf -y install java-11-openjdk
echo "Installing jenkins"
dnf -y install jenkins
banner "All version detaiils"
echo "Ansible version $(ansible --version)"
echo "git version $(git --version)"
echo "Docker version $(docker --version)"
echo "Python3 version $(python3 --version)"
echo "Google Chrome version $(google-chrome --version)"
echo "Java version $(java --version)"
banner "Updating system, reboot after script"
echo "updating system"
dnf -y update; dnf -y upgrade
banner "Starting services"
echo "Starting docker service"
systemctl start docker
echo "Enabling docker service"
systemctl enable docker
echo "Starting jenkins service"
systemctl start jenkins
echo "Enabling jenkins service"
systemctl enable jenkins
echo "Reloading services"
systemctl daemon-reload
banner "Enabling firewall"
YOURPORT=8080
PERM="--permanent"
SERV="$PERM --service=jenkins"

firewall-cmd $PERM --new-service=jenkins
firewall-cmd $SERV --set-short="Jenkins ports"
firewall-cmd $SERV --set-description="Jenkins port exceptions"
firewall-cmd $SERV --add-port=$YOURPORT/tcp
firewall-cmd $PERM --add-service=jenkins
firewall-cmd --zone=public --add-service=http --permanent
firewall-cmd --reload
banner "Status checks"
echo "Docker service status $(systemctl show -p SubState --value docker)"
echo "Jenkins service status $(systemctl show -p SubState --value jenkins)"
echo "Firewalld service status $(systemctl show -p SubState --value firewalld)"
banner "final configurations"
echo "resolving docker.socket issue"
sudo chown sunil:docker /var/run/docker.sock
docker context use default
banner "Testing softwares"
echo "Docker hello world"
docker run hello-world
echo "Python hello world"
echo "Ansible ping test"
ansible localhost -a "/bin/echo hello world"
banner "default browser settings"
echo "Removing firefox"
dnf -y remove firefox
echo "default browser $(xdg-settings get default-web-browser)"
if [[ $(xdg-settings get default-web-browser) != "google-chrome.desktop" ]]
    then
    echo "Setting google-chrome as a defualt broswer"
    xdg-settings set default-web-browser google-chrome.desktop
    else
    echo "Google chrome is already your default broswer"
fi
banner "Cleaning"
dnf -y autoremove
banner "The End"