# STI-Shared

This is a STI Project based on the Mikrotik RouterOS, aimed at making a RESTFUL API for it which includes CRUD for several functions.
The project utilizes components / applications such as JSON , the Mikrotik API as well as Flask.

Sample Commands for using flask to curl command requests:

DHCP:

Print Functions


Pool: curl -i http://localhost:5000/todo/api/mikrotik/print/pool

Network: curl -i http://localhost:5000/todo/api/mikrotik/print/network

Server: curl -i http://localhost:5000/todo/api/mikrotik/print/server


Add Functions


Pool: curl -i -H "Content-Type: application/json" -X POST -d '{"name":"<name>", "range":"<range>"}' http://localhost:5000/todo/api/mikrotik/add/pool

Network: curl -i -H "Content-Type: application/json" -X POST -d '{"subnet":"<subnet>", "interface":"<interface>"}' http://localhost:5000/todo/api/mikrotik/add/network

Server: curl -i -H "Content-Type: application/json" -X POST -d '{"interface":"<interface>", "poolname":"<poolname>"}' http://localhost:5000/todo/api/mikrotik/add/server


Update Functions


Pool: curl -i -H "Content-Type: application/json" -X PUT -d '{"number":"<number>", "range":"<range>"}' http://localhost:5000/todo/api/mikrotik/update/pool

Network: curl -i -H "Content-Type: application/json" -X PUT -d '{"number":"<number>", "address":"<address>", "gateway":"<gateway>" }' http://localhost:5000/todo/api/mikrotik/update/network

Server: curl -i -H "Content-Type: application/json" -X PUT -d '{"number":"<number>", "address":"<address>", "poolname":"<poolname>"}' http://localhost:5000/todo/api/mikrotik/update/server


Delete Functions


Pool: curl -i -X DELETE -d '{"number":"<number>"}' http://localhost:5000/todo/api/mikrotik/delete/pool 

Network: curl -i -X DELETE -d '{"number":"<number>"}' http://localhost:5000/todo/api/mikrotik/delete/network

Server: curl -i -X DELETE -d '{"number":"<number>"}' httpL//localhost:5000/todo/api/mikrotik/delete/server


