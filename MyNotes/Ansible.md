<h3>Ansible inventory</h3>
3 methods   
<ol>
<li>default</li>
<li>custom location</li>
<li>alias</li>
</ol>

<u>default</u>: /etc/ansible/hosts 

ex: 
Local host settings 

[local]
<br>localhost ansible_connection=local  

<u>custom location:</u> use -i with playbook commands  

ex: ansible -i /home/sunil/ansible/hosts playbooks.yml  


<u>alias:</u>  

server1 ansible_alias_host=1.2.3.4  

list inventory: ansible-inventory --list    
Ping all hosts: ansible all -m ping / ansible -a "uptime" all
<hr>
<h3>use become=yes to run as root</h3>

ansible-playbook playbooks.yml -K

use -K or --ask-become-pass
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
Adhoc commands you can use without need of playbooks    
syntax: ansible [target] -m [module] -a "[module options]"  
ex: ansible webservers -m ping
ex: ansible webserrvers file -a "path=/home/sunil/sunil.txt state=touch mode=0755"