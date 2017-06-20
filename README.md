# STI

This is a STI Project based on the Mikrotik RouterOS, aimed at making a RESTFUL API for it which includes CRUD for several functions. The project utilizes components / applications such as JSON , the Mikrotik API as well as Flask.

Sample Commands for using flask to curl command requests:

# Firewall Address List

Create Address List:

curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"address":"20.20.20.0/24", "list":"20network"}' http://localhost:5000/todo/api/mikrotik/addrlist/create

Print All Address Lists:

curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/addrlist/print

Update Selected Address List:

curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"numbers":"1", "address":"30.30.30.0/24", "list":"30network"}' http://localhost:5000/todo/api/mikrotik/addrlist/update

Delete Selected Address List:

curl -u admin:python -H "Content-Type: application/json" -X DELETE -d '{"numbers":"1"}' -i http://localhost:5000/todo/api/mikrotik/addrlist/delete

# Firewall Filter Rules

Create Filter Rule:

curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"chain":"input", "action":"reject", "rejectw":"icmp-network-unreachable", "protocol":"icmp", "src-address-list":"10network", "dst-address-list":"10network", "log":"no"}' http://localhost:5000/todo/api/mikrotik/filterrule/create

Print All Filter Rules:

curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/filterrule/print

Update Selected Filter Rule:

curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"numbers":"1", "chain":"input", "action":"accept", "rejectw":"icmp-network-unreachable", "protocol":"icmp", "src-address-list":"10network", "dst-address-list":"10network", "log":"no"}' http://localhost:5000/todo/api/mikrotik/filterrule/update

Delete Selected Filter Rule:

curl -u admin:python -H "Content-Type: application/json" -X DELETE -d '{"numbers":"1"}' -i http://localhost:5000/todo/api/mikrotik/filterrule/delete

# Firewall NAT Print & Delete

Print all Firewall NAT Rules:

curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/nat/print

Delete Selected Firewall NAT Rule:

curl -u admin:python -H "Content-Type: application/json" -X DELETE -d '{"numbers":"1"}' -i http://localhost:5000/todo/api/mikrotik/nat/delete

# Firewall Masquerade NAT

Create Masquerade NAT:

curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"outinterface":"ether1"}' http://localhost:5000/todo/api/mikrotik/masqnat/create


Update Selected Masquerade NAT:

curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"numbers":"1", "outinterface":"ether2"}' http://localhost:5000/todo/api/mikrotik/nat/updatemasqnat


# Firewall NAT Bypass

Create NAT Bypass:

curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"srcaddr":"10.10.10.0/24", "dstaddr":"20.20.20.0/24"}' http://localhost:5000/todo/api/mikrotik/natbypass/create

Update Selected NAT Bypass:

curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"numbers":"1", "srcaddr":"30.30.30.0/24", "dstaddr":"40.40.40.0/24"}' http://localhost:5000/todo/api/mikrotik/nat/updatenatbypass
