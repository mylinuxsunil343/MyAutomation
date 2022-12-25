<h3>Ansible inventory</h3>
3 methods   
<ol>
<li>default</li>
<li>custom location</li>
<li>alias</li>
</ol>

<p style="text decoration:underline;">default</p>: /etc/ansible/hosts 

ex: 
Local host settings 

[local]

localhost ansible_connection=local  


<p style="text decoration:underline;">custom location:</p> use -i with playbook commands  

ex: ansible -i /home/sunil/ansible/hosts playbooks.yml  


<p style="text decoration:underline;">alias:</p>  

server1 ansible_alias_host=1.2.3.4  
<hr>
<h3>use become=yes to run as root</h3>

ansible-playbook playbooks.yml -K

use -K or --ask-become-pass