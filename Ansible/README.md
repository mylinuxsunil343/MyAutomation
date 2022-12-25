Ansible inventory 
3 methods
default, custom location, alias

default: /etc/ansible/hosts
ex:
Local host settings
[local]
localhost ansible_connection=local

custom location: use -i with playbook commands
ex: ansible -i /home/sunil/ansible/hosts playbooks.yml

alias:
server1 ansible_alias_host=1.2.3.4

use become=yes to run as root
ansible-playbook playbooks.yml -K
use -K or --ask-become-pass