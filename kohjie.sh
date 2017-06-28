#!/bin/bash

choice=$1
argument1=$2
argument2=$3
argument3=$4
argument4=$5
argument5=$6
argument6=$7
argument7=$8
argument8=$9

#firewall rules
if [ "$choice" == "printrule" ]
then
	python filtercrud.py printrule > file.txt

elif [ "$choice" == "createrule" ]
then
	python filtercrud.py createrule $argument1 $argument2 $argument3 $argument4 $argument5 $argument6 $argument7 > file.txt

elif [ "$choice" == "updaterule" ]
then
 	python filtercrud.py updaterule $argument1 $argument2 $argument3 $argument4 $argument5 $argument6 $argument7 $argument8 > file.txt

elif [ "$choice" == "deleterule" ]
then
	python filtercrud.py deleterule $argument1 > file.txt

#firewall address lists
elif [ "$choice" == "printlist" ]
then
	python addrlistcrud.py printlist > file.txt

elif [ "$choice" == "createlist" ]
then
	python addrlistcrud.py createlist $argument1 $argument2 > file.txt

elif [ "$choice" == "updatelist" ]
then
	python addrlistcrud.py updatelist $argument1 $argument2 $argument3 > file.txt

elif [ "$choice" == "deletelist" ]
then
	python addrlistcrud.py deletelist $argument1 > file.txt

#nat print & delete
elif [ "$choice" == "printnat" ]
then
	python natcrud.py printnat > file.txt
elif [ "$choice" == "deletenat" ]
then
	python natcrud.py deletenat $argument1 > file.txt
#firewall masq nat 
elif [ "$choice" == "createmasqnat" ]
then
	python natcrud.py createmasqnat $argument1 > file.txt

elif [ "$choice" == "updatemasqnat" ]
then
	python natcrud.py updatemasqnat $argument1 $argument2 > file.txt

#firewall bypass nat
elif [ "$choice" == "createnatbypass" ]
then
	python natcrud.py createnatbypass $argument1 $argument2 > file.txt

elif [ "$choice" == "updatenatbypass" ]
then
	python natcrud.py updatenatbypass $arguement1 $arguement2 $arguement3 > file.txt
fi
