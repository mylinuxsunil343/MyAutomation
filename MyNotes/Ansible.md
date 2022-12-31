<h3>Ansible inventory</h3>
3 methods   
<ol>
<li>default</li>
<li>custom location</li>
<li>alias</li>
</ol>

<u>default</u>: /etc/ansible/hosts <br> 
ex: <br> 
Local host settings <br> 

[local] <br> 
localhost ansible_connection=local <br>  
<u>custom location:</u> use -i with playbook commands   <br> 
ex: ansible -i /home/sunil/ansible/hosts playbooks.yml  <br> 
<u>alias:</u>  
server1 ansible_alias_host=1.2.3.4  <br> 

list inventory: ansible-inventory --list <br>    
Ping all hosts: ansible all -m ping / ansible -a "uptime" all<br> 
<hr>
<h3>use become=yes to run as root</h3>
ansible-playbook playbooks.yml -K <br> 
use -K or --ask-become-pass<br> 
<hr>
<h3>Connection to remote clients</h3>
Generate SSH Keys on the control node and copy over to clients for password less SSH Connection
<ol>
<li>ssh-keygen</li>
<li>Leave everything default and enter</li>
<li>ssh-copy-id server1</li>
<li>ssh-copy-id server2</li>
</ol>
<hr>
<h3>General</h3>
Syntax check: ansible-playbook playbook.yml --syntax-check

<h3>Ansible Ad-hoc commands</h3>
Adhoc commands you can use without need of playbooks <br> 
syntax: ansible [target] -m [module] -a "[module options]" <br>  


Pinging servers<br>
ex: ansible webservers -m ping <br>

Creating file: <br>
ex: ansible webservers file -a "path=/home/sunil/sunil.txt state=touch mode=0755"<br>

Deleting file: <br>
ex: ansible webservers file -a "path=/home/sunil/sunil.txt state=absent"<br>

Copying file <br>
ex: ansible webservers copy -a "src=source dest=destination"<br>

Installing package: <br>
ex: ansible all -m yum -a "name=telnet state=present"<br>

Deleting package: <br>
ex: ansible all -m yum -a "name=telnet state=absent"<br>

Starting and enabling service<br>
ex: ansible all -m service -a "name=telnet state=started enabled=yes"<br>

Checking status (Using shell module): <br>
ex: ansible all -m shell -a "systemctl status telnet"<br>

Creating user: <br>
ex: ansible all -m user -a "name=splunk home=/home/splunk shell=/bin/bash state=present"<br>

Deleting user: <br>
ex: ansible all -m user -a "name=splunk home=/home/splunk shell=/bin/bash state=absent" <br>
or<br>
ec: ansible all -m shell -a "userdel splunk" <br>

clients information: <br>
ex: ansible all -m setup <br>

rebooting client: <br>
ex: ansible client1 -a "/sbin/reboot"<br>

<hr>
<h3>Roles</h3>
Roles are helpful when managing different environment by same service.<br>
Roles are like templet that are most of the time static and can be called by the playbooks. <br>

Roles allow the entire configuration to ve grouped in: 
<ol>
<li>Tasks</li>
<li>Modules</li>
<li>Variables</li>
<li>Handlers</li>
</ol>

<hr>
<h3>Tags</h3>
Reference or alias of a task <br>
Instead of runnign entire playbook, add tags to a task you need to run <br>
<br>
List tags:<br>
ansible-playbook 16-ansible-tags.yml  --list-tags <br>
<br>
Running tags:<br>
ansible-playbook 16-ansible-tags.yml -t i-httpd <br>
<br>
To skip task
ansible-playbook 16-ansible-tags.yml --skip-tags i-httpd

<hr>
<h3>Tasks</h3>
Tasks are different to tag. This will ask ansible to start the task from perticular point. <br>
ex: ansible-playbook 16-ansible-tags.yml --start-at-task "Start httpd"<br>

<hr>
<h3>Variables</h3>
Variables should always start with letter <br>
Name can include letters, no's underscores <br>
canot have . or - <br>
can define inside inventory files as well<br>

<hr>
<h3>Handlers</h3>
Handlers are executed at the end of the play once all tasks are finished.<br>
Typically used to start, reload, restart or stopping service<br>
<br>
Sometime, you want to restart the service if config changes, but no when config not chnaged. <br>
Handlers are tasks that only run when notified<br>
Each handlers should have globally uniqe name<br>

<hr>
<h3>Conditions</h3>
Conditions allow ansible to take action based on certain condition.<br>
ex: Install yum package if OS is centos/fedora<br>

Use when statement to make ansible more smarter<br>

To know host details: <br>
ansible localhost -m setup<br>
You can find lot of information about os/host name through ansible built in functions. <br>
ex:<br>
"ansible_nodename": "marellasunil",<br>
"ansible_os_family": "RedHat",<br>
"ansible_pkg_mgr": "dnf",<br>
<hr>
<h3>Loops</h3>
Enables you to execute set of commands repeatdly until condition met
<hr>
<h3>Ansible Vault</h3>
Ansible vault feature which will password protect your code. <br>

Creating password protected ansinle file: <b>
ansible-vault create 23-vault.yml <br>
Password used: changeme <br>

To run playbook which is password protected: <br>
ansible-playbookk 23-vault.yml --ask-vault-pass <br>

To view the vault protected yaml file:<br>
ansible-vault view 23-vault.yml<br>

To edit the vault protected yaml file:<br>
ansible-vault edit 23-vault.yml <br>

To convert existing yaml file to vault protected: <br>
ansible-vault encrypt 21-loops.yml

To convert existing vault protected yaml file to normal file: <br>
ansible-vault decrypt 21-loops.yml<br>
<hr>
<h3>encrypt string </h3>
ansible-valut encrypt_string <<Name of string>> <br>
enter the password and copy encrypted value, paste in the code. <br>

You can decrypt the string (Ex code: 24-encrypt-string.yml) <br>

ansible-playbook 24-encrypt-string.yml --ask-vault-pass<br>