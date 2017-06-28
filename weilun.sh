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
argument9=${10}
argument10=${11}

#IP ROUTE
if [ "$choice" == "printRoute" ]
then
	python api.py printRoute > route.txt

elif [ "$choice" == "createRoute" ]
then
	python api.py createRoute $argument1 > route.txt

elif [ "$choice" == "updateRoute" ]
then 
        python api.py updateRoute $argument1 $argument2 > route.txt
elif [ "$choice" == "deleteRoute" ]
then 
        python api.py deleteRoute $argument1 > route.txt
#IPSEC POLICY
elif [ "$choice" == "printPolicy" ]
then
	python api.py printPolicy > ipsecpolicy.txt

elif [ "$choice" == "createPolicy" ]
then
	python api.py createPolicy $argument1 $argument2 $argument3 $argument4 $argument5 $argument6 $argument7 $argument8 $argument9 > ipsecpolicy.txt

elif [ "$choice" == "updatePolicy" ]
then 
        python api.py updatePolicy $argument1 $argument2 $argument3 $argument4 $argument5 $argument6 $argument7 $argument8 $argument9 $argument10 > ipsecpolicy.txt

elif [ "$choice" == "deletePolicy" ]
then 
        python api.py deletePolicy $argument1 > ipsecpolicy.txt
#IPSEC PEER
elif [ "$choice" == "printPeer" ]
then
	python api.py printPeer > ipsecpeer.txt

elif [ "$choice" == "createPeer" ]
then
	python api.py createPeer $argument1 $argument2 $argument3 > ipsecpeer.txt

elif [ "$choice" == "updatePeer" ]
then 
        python api.py updatePeer $argument1 $argument2 $argument3 $argument4 > ipsecpeer.txt

elif [ "$choice" == "deletePeer" ]
then 
        python api.py deletePeer $argument1 > ipsecpeer.txt
fi
