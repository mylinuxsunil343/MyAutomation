#!/bin/bash
banner()
{
  echo "+------------------------------------------+"
  printf "| %-40s |\n" "`date`"
  echo "|                                          |"
  printf "|`tput bold` %-40s `tput sgr0`|\n" "$@"
  echo "+------------------------------------------+"
}
banner "Configuring git services"
git config --global user.name "Sunil Marella"
git config --global user.email "mylinux.sunil343@gmail.com"
banner "Ansible SSH will not prompt yes or no"
echo -e "[defaults]
inventory = /home/sunil/Desktop/Sunil/Automation/MyAutomation/Ansible/Web/Demo/Inventory/inventory
host_key_checking = False" >> /etc/ansible/ansible.cfg
banner "Ansible hosts config"
echo -e "[local]
localhost ansible_connection=local" >> /etc/ansible/hosts
echo "current host name : $(hostname)"
hostnamectl set-hostname marellasunil