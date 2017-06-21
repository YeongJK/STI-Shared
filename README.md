# STI-Shared

This is a STI Project based on the Mikrotik RouterOS, aimed at making a RESTFUL API for it which includes CRUD for several functions.
The project utilizes components / applications such as JSON , the Mikrotik API as well as Flask.

List of CRUDs:

- ip route
- DHCP
- Users
- IP Addressing
- VLAN
- Bridge
- Bridge Port
- Firewall Rules
- NAT

Please note:
IP addresses of the following files (s.socket...) must be changed to fit the router IP
As well as the username and passwords in the Login method.
Flask files (E.g mikrotik.py) also have usernames and passwords for authentication purposes that can be changed accordingly.

- addrlistcrud.py
- api.py
- api5.py
- crud.py
- dhcp.py
- filtercrud.py
- natcrud.py

Sample Commands for using flask to curl command requests:

Can be found on https://app.swaggerhub.com/apis/YeongJK/Mikrotik/1.0.0
