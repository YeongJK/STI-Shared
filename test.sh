#!/bin/bash

choice=$1
arguement1=$2
arguement2=$3
arguement3=$4
arguement4=$5
arguement5=$6
arguement6=$7
arguement7=$8
arguement8=$9

#firewall rules
if [ "$choice" == "printrule" ]
then
	python filtercrud.py printrule > file.txt

elif [ "$choice" == "createrule" ]
then
	python filtercrud.py createrule $arguement1 $arguement2 $arguement3 $arguement4 $arguement5 $arguement6 $arguement7 > file.txt

elif [ "$choice" == "updaterule" ]
then
 	python filtercrud.py updaterule $arguement1 $arguement2 $arguement3 $arguement4 $arguement5 $arguement6 $arguement7 $arguement8 > file.txt

elif [ "$choice" == "deleterule" ]
then
	python filtercrud.py deleterule $arguement1 > file.txt

#firewall address lists
elif [ "$choice" == "printlist" ]
then
	python addrlistcrud.py printlist > file.txt

elif [ "$choice" == "createlist" ]
then
	python addrlistcrud.py createlist $arguement1 $arguement2 > file.txt

elif [ "$choice" == "updatelist" ]
then
	python addrlistcrud.py updatelist $arguement1 $arguement2 $arguement3 > file.txt

elif [ "$choice" == "deletelist" ]
then
	python addrlistcrud.py deletelist $arguement1 > file.txt

#nat print & delete
elif [ "$choice" == "printnat" ]
then
	python natcrud.py printnat > file.txt
elif [ "$choice" == "deletenat" ]
then
	python natcrud.py deletenat $arguement1 > file.txt
#firewall masq nat 
elif [ "$choice" == "createmasqnat" ]
then
	python natcrud.py createmasqnat $arguement1 > file.txt

elif [ "$choice" == "updatemasqnat" ]
then
	python natcrud.py updatemasqnat $arguement1 $arguement2 > file.txt

#firewall bypass nat
elif [ "$choice" == "createnatbypass" ]
then
	python natcrud.py createnatbypass $arguement1 $arguement2 > file.txt

elif [ "$choice" == "updatenatbypass" ]
then
	python natcrud.py updatenatbypass $arguement1 $arguement2 $arguement3 > file.txt
fi
