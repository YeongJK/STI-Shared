# STI

This is a STI Project based on the Mikrotik RouterOS, aimed at making a RESTFUL API for it which includes CRUD for several functions. The project utilizes components / applications such as JSON , the Mikrotik API as well as Flask.

Sample Commands for using flask to curl command requests:

# Firewall Address List

Create Address List:

curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"address":"20.20.20.0/24", "list":"20network"}' http://localhost:5000/todo/api/mikrotik/addrlist/create

Print All Address Lists:

curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/addrlist/print

Update Selected Address List:

curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"address":"30.30.30.0/24", "list":"30network"}' http://localhost:5000/todo/api/mikrotik/addrlist/update/<numbers>

Delete Selected Address List:

curl -u admin:python -H "Content-Type: application/json" -X DELETE -i http://localhost:5000/todo/api/mikrotik/addrlist/delete/<numbers>

# Firewall Filter Rules

Create Filter Rule:

curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"chain":"input", "action":"reject", "rejectw":"icmp-network-unreachable", "protocol":"icmp", "src-address-list":"10network", "dst-address-list":"10network", "log":"no"}' http://localhost:5000/todo/api/mikrotik/filterrule/create

Print All Filter Rules:

curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/filterrule/print

Update Selected Filter Rule:

curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"chain":"input", "action":"accept", "rejectw":"icmp-network-unreachable", "protocol":"icmp", "src-address-list":"10network", "dst-address-list":"10network", "log":"no"}' http://localhost:5000/todo/api/mikrotik/filterrule/update/<numbers>

Delete Selected Filter Rule:

curl -u admin:python -H "Content-Type: application/json" -X DELETE -i http://localhost:5000/todo/api/mikrotik/filterrule/delete/<numbers>

# Firewall Masquerade NAT

Create Masquerade NAT:

curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"outinterface":"ether1"}' http://localhost:5000/todo/api/mikrotik/masqnat/create

Print All Masquerade NATs:

curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/masqnat/print

Update Selected Masquerade NAT:

curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"outinterface":"ether2"}' http://localhost:5000/todo/api/mikrotik/masqnat/update/<numbers>

Delete Selected Masquerade NAT:

curl -u admin:python -H "Content-Type: application/json" -X DELETE -i http://localhost:5000/todo/api/mikrotik/masqnat/delete/<numbers>

# Firewall NAT Bypass

Create NAT Bypass:

curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"srcaddr":"10.10.10.0/24", "dstaddr":"20.20.20.0/24"}' http://localhost:5000/todo/api/mikrotik/natbypass/create

Print All NAT Bypass:

curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/natbypass/print

Update Selected NAT Bypass:

curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"srcaddr":"30.30.30.0/24", "dstaddr":"40.40.40.0/24"}' http://localhost:5000/todo/api/mikrotik/natbypass/update/<numbers>

Delete Selected NAT Bypass:

curl -u admin:python -H "Content-Type: application/json" -X DELETE -i http://localhost:5000/todo/api/mikrotik/natbypass/delete/<numbers>
