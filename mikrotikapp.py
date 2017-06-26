#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for
from flask.ext.httpauth import HTTPBasicAuth
import os, addrlistcrud, filtercrud, natcrud, csv, json, subprocess, re

mikrotik = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username == 'admin':
		return 'python'
	return None

#ERROR HANDLER 401
@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error': 'Unauthorized Access'}), 401)

#ERROR HANDLER 400
@mikrotik.errorhandler(400)
def not_found(error):
	return make_response(jsonify({'error': 'Bad request'}), 400)

#ERROR HANDLER 404
@mikrotik.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not Found'}), 404)

#ERROR HANDLER 405
@mikrotik.errorhandler(405)
def not_found(error):
	return make_response(jsonify({'Error':'Invalid Method'}), 405)

#CREATE LIST
#curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"address":"20.20.20.0/24", "list":"20network"}' http://localhost:5000/todo/api/mikrotik/addrlist/create
@mikrotik.route('/todo/api/mikrotik/addrlist/create', methods=['POST'])
@auth.login_required
def create_list():
	address = request.json['address']
	l = request.json['list']

	subprocess.call(['./test.sh', 'createlist', address, l])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	
	return jsonify({'Addresslist Created:': output2})

#PRINT ALL LISTS
#curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/addrlist/print
@mikrotik.route('/todo/api/mikrotik/addrlist/print', methods=['GET'])
@auth.login_required
def get_list():
	subprocess.call(['./test.sh', 'printlist'])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Created Address List(s)': output2})

#UPDATE LIST
#curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"numbers":"1", "address":"30.30.30.0/24", "list":"30network"}' http://localhost:5000/todo/api/mikrotik/addrlist/update
@mikrotik.route('/todo/api/mikrotik/addrlist/update', methods=['PUT'])
@auth.login_required
def update_list():
	numbers = request.json['numbers']
    	address = request.json['address']
	l = request.json['list']

    	subprocess.call(['./test.sh', 'updatelist', numbers, address, l])

    	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Updated Address List': output2})

#DELETE LIST
#curl -u admin:python -H "Content-Type: application/json" -X DELETE -d '{"numbers":"1"}' -i http://localhost:5000/todo/api/mikrotik/addrlist/delete
@mikrotik.route('/todo/api/mikrotik/addrlist/delete', methods=['DELETE'])
@auth.login_required
def delete_list():
	numbers = request.json['numbers']
	subprocess.call(['./test.sh', 'deletelist', numbers])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'Deleted List': output2, 'delete': True})

#CREATE RULE
#curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"chain":"input", "action":"reject", "rejectw":"icmp-network-unreachable", "protocol":"icmp", "src-address-list":"10network", "dst-address-list":"10network", "log":"no"}' http://localhost:5000/todo/api/mikrotik/filterrule/create
@mikrotik.route('/todo/api/mikrotik/filterrule/create', methods=['POST'])
@auth.login_required
def create_rule():
	chain = request.json['chain']
	action = request.json['action']
	rejectw = request.json['rejectw']
	protocol = request.json['protocol']
	src = request.json['src-address-list']
	dst = request.json['dst-address-list']
	log = request.json['log']

	subprocess.call(['./test.sh', 'createrule', chain, action, rejectw, protocol, src, dst, log])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'Filter Rule': output2})

#PRINT ALL RULES
#curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/filterrule/print
@mikrotik.route('/todo/api/mikrotik/filterrule/print', methods=['GET'])
@auth.login_required
def get_rule():
	subprocess.call(['./test.sh', 'printrule'])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Rule': output2})

#UPDATE RULE
#curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"numbers":"1", "chain":"input", "action":"accept", "rejectw":"icmp-network-unreachable", "protocol":"icmp", "src-address-list":"10network", "dst-address-list":"10network", "log":"no"}' http://localhost:5000/todo/api/mikrotik/filterrule/update
@mikrotik.route('/todo/api/mikrotik/filterrule/update', methods=['PUT'])
@auth.login_required
def update_rule():
	numbers = request.json['numbers']
    	chain = request.json['chain']
	action = request.json['action']
	rejectw = request.json['rejectw']
	protocol = request.json['protocol']
	src = request.json['src-address-list']
	dst = request.json['dst-address-list']
	log = request.json['log']

    	subprocess.call(['./test.sh', 'updaterule', numbers, chain, action, rejectw, protocol, src, dst, log])

    	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Rule': output2})

#DELETE RULE
#curl -u admin:python -H "Content-Type: application/json" -X DELETE -d '{"numbers":"1"}' -i http://localhost:5000/todo/api/mikrotik/filterrule/delete
@mikrotik.route('/todo/api/mikrotik/filterrule/delete', methods=['DELETE'])
@auth.login_required
def delete_rule():
	numbers = request.json['numbers']
	subprocess.call(['./test.sh', 'deleterule', numbers])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'Rule': output2, 'delete': True})

#PRINT ALL NAT
#curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/nat/print
@mikrotik.route('/todo/api/mikrotik/nat/print', methods=['GET'])
@auth.login_required
def get_masqnat():
	subprocess.call(['./test.sh', 'printnat'])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'NAT Rule(s)': output2})

#DELETE NAT
#curl -u admin:python -H "Content-Type: application/json" -X DELETE -d '{"numbers":"1"}' -i http://localhost:5000/todo/api/mikrotik/nat/delete
@mikrotik.route('/todo/api/mikrotik/nat/delete', methods=['DELETE'])
@auth.login_required
def delete_masqnat():
	numbers = request.json['numbers']
	subprocess.call(['./test.sh', 'deletenat', numbers])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Deleted NAT Rule': output2, 'delete': True})

#CREATE MASQ NAT
#curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"outinterface":"ether1"}' http://localhost:5000/todo/api/mikrotik/nat/createmasqnat
@mikrotik.route('/todo/api/mikrotik/nat/createmasqnat', methods=['POST'])
@auth.login_required
def create_masqnat():
	outinterface = request.json['outinterface']

	subprocess.call(['./test.sh', 'createmasqnat', outinterface])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	
	return jsonify({'outinterface': output2})

#UPDATE MASQ NAT
#curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"numbers":"1", "outinterface":"ether2"}' http://localhost:5000/todo/api/mikrotik/nat/updatemasqnat
@mikrotik.route('/todo/api/mikrotik/nat/updatemasqnat', methods=['PUT'])
@auth.login_required
def update_masqnat():
	numbers = request.json['numbers']
	outinterface = request.json['outinterface']

    	subprocess.call(['./test.sh', 'updatemasqnat', numbers, outinterface])

    	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Updated NAT Rule': output2})

#CREATE NAT BY PASS
#curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"srcaddr":"10.10.10.0/24", "dstaddr":"20.20.20.0/24"}' http://localhost:5000/todo/api/mikrotik/nat/createnatbypass
@mikrotik.route('/todo/api/mikrotik/nat/createnatbypass', methods=['POST'])
@auth.login_required
def create_natbypass():
	srcaddr = request.json['srcaddr']
	dstaddr = request.json['dstaddr']

	subprocess.call(['./test.sh', 'createnatbypass', srcaddr, dstaddr])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	
	return jsonify({'Create NAT BYPASS': output2})

#UPDATE NAT BY PASS
#curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"numbers":"1", "srcaddr":"30.30.30.0/24", "dstaddr":"40.40.40.0/24"}' http://localhost:5000/todo/api/mikrotik/nat/updatenatbypass
@mikrotik.route('/todo/api/mikrotik/nat/updatenatbypass', methods=['PUT'])
@auth.login_required
def update_natbypass():
	numbers = request.json['numbers']
	srcaddr = request.json['srcaddr']
	dstaddr = request.json['dstaddr']

    	subprocess.call(['./test.sh', 'updatenatbypass', numbers, srcaddr, dstaddr])

    	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Updated NAT Rule': output2})

#IP ROUTE CRUD
#READ IP ROUTE
#curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/route/print
@mikrotik.route('/todo/api/mikrotik/route/print', methods=['GET'])
@auth.login_required
def printRoute():
	subprocess.call(['./weilun.sh', 'printRoute'])
	with open('route.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
		
	return jsonify({'PRINT ROUTE': output2})

#CREATE IP ROUTE
#curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"dst":"0.0.0.0", "src":"0.0.0.0", "gateway":"192.168.90.254"}' http://localhost:5000/todo/api/mikrotik/route/create
@mikrotik.route('/todo/api/mikrotik/route/create', methods=['POST'])
@auth.login_required
def createRoute():
	dst = request.json['dst']
	src = request.json['src']
	gateway = request.json['gateway']
	subprocess.call(['./weilun.sh', 'createRoute', dst, src, gateway])
	with open('route.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'IP ROUTE CREATED': output2})
#UPDATE IP ROUTE
#curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"numbers":"1", "dst":"0.0.0.0", "src":"0.0.0.0", "gateway":"192.168.90.1"}' http://localhost:5000/todo/api/mikrotik/route/update
@mikrotik.route('/todo/api/mikrotik/route/update', methods=['PUT'])
@auth.login_required
def updateRoute():
	numbers = request.json['numbers']
	dst = request.json['dst']
	src = request.json['src']
	gateway = request.json['gateway']
	subprocess.call(['./weilun.sh', 'updateRoute', numbers, dst, src, gateway])
	with open('route.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'UPDATED ROUTE': output2})
#DELETE IP ROUTE
#curl -u admin:python -H "Content-Type: application/json" -X DELETE -i -d '{"numbers":"1"}' http://localhost:5000/todo/api/mikrotik/route/delete
@mikrotik.route('/todo/api/mikrotik/route/delete', methods=['DELETE'])
@auth.login_required
def deleteRoute():
	numbers = request.json['numbers']
	subprocess.call(['./weilun.sh', 'deleteRoute', numbers])
	with open('route.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'ROUTE DELETED': output2, 'delete':True})

#IPSEC PEER CRUD

#READ IPSEC PEER
#curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/ipsec/peer/print
@mikrotik.route('/todo/api/mikrotik/ipsec/peer/print', methods=['GET'])
@auth.login_required
def printPeer():
	subprocess.call(['./weilun.sh', 'printPeer'])
	with open('ipsecpeer.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
		
	return jsonify({'PRINT IPSEC PEER': output2})

#CREATE IPSEC PEER
#curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"addr":"192.168.90.2", "port":"500", "secret":"test"}' http://localhost:5000/todo/api/mikrotik/ipsec/peer/create
@mikrotik.route('/todo/api/mikrotik/ipsec/peer/create', methods=['POST'])
@auth.login_required
def createPeer():
	addr = request.json['addr']
	port = request.json['port']
	secret = request.json['secret']
	subprocess.call(['./weilun.sh', 'createPeer', addr, port, secret])
	with open('ipsecpeer.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'IPSEC PEER CREATED':output2})

#UPDATE IPSEC PEER
#curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"numbers":"1", "addr":"192.168.90.2", "port":"500", "secret":"lol"}' http://localhost:5000/todo/api/mikrotik/ipsec/peer/update
@mikrotik.route('/todo/api/mikrotik/ipsec/peer/update', methods=['PUT'])
@auth.login_required
def updatePeer():
	numbers = request.json['numbers']
	addr = request.json['addr']
	port = request.json['port']
	secret = request.json['secret']
	subprocess.call(['./weilun.sh', 'updatePeer', numbers, addr, port, secret])
	with open('ipsecpeer.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'UPDATED IPSEC PEER': output2})

#DELETE IPSEC PEER
#curl -u admin:python -H "Content-Type: application/json" -X DELETE -i -d '{"numbers":"1"}' http://localhost:5000/todo/api/mikrotik/ipsec/peer/delete
@mikrotik.route('/todo/api/mikrotik/ipsec/peer/delete', methods=['DELETE'])
@auth.login_required
def deletePeer():
	numbers = request.json['numbers']
	subprocess.call(['./weilun.sh', 'deletePeer', numbers])
	with open('ipsecpeer.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'IPSEC PEER DELETED': output2, 'Delete':True})

#IPSEC POLICY CRUD

#READ IPSEC POLICY
#curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/ipsec/policy/print
@mikrotik.route('/todo/api/mikrotik/ipsec/policy/print', methods=['GET'])
@auth.login_required
def printPolicy():
	subprocess.call(['./weilun.sh', 'printPolicy'])
	with open('ipsecpolicy.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)	
	return jsonify({'PRINT IPSEC POLICY': output2})

#CREATE IPSEC POLICY
#curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"srcaddr":"10.1.202.0/24", "srcport":"any", "dstaddr":"10.1.101.0/24", "dstport":"any", "sasrcaddr":"192.168.90.1", "sadstaddr":"192.168.90.2", "tunnel":"yes", "action":"encrypt", "proposal":"default"}' http://localhost:5000/todo/api/mikrotik/ipsec/policy/create
@mikrotik.route('/todo/api/mikrotik/ipsec/policy/create', methods=['POST'])
@auth.login_required
def createPolicy():
	srcaddr = request.json['srcaddr']
	srcport = request.json['srcport']
	dstaddr = request.json['dstaddr']
	dstport = request.json['dstport']
	sasrcaddr = request.json['sasrcaddr']
	sadstaddr = request.json['sadstaddr']
	tunnel = request.json['tunnel']
	action = request.json['action']
	proposal = request.json['proposal']
	subprocess.call(['./weilun.sh', 'createPolicy', srcaddr, srcport, dstaddr, dstport, sasrcaddr, sadstaddr, tunnel, action, proposal])
	with open('ipsecpolicy.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'IPSEC POLICY ADDED': output2})

#UPDATE IPSEC POLICY
#curl -u admin:python -i -H "Content-Type: application/json" -X PUT -d '{"numbers":"1", "srcaddr":"10.1.202.0/24", "srcport":"any", "dstaddr":"10.1.101.0/24", "dstport":"any", "sasrcaddr":"192.168.90.1", "sadstaddr":"192.168.90.2", "tunnel":"yes", "action":"encrypt", "proposal":"default"}' http://localhost:5000/todo/api/mikrotik/ipsec/policy/update=?
@mikrotik.route('/todo/api/mikrotik/ipsec/policy/update', methods=['PUT'])
@auth.login_required
def updatePolicy():
	numbers = request.json['numbers']
	srcaddr = request.json['srcaddr']
	srcport = request.json['srcport']
	dstaddr = request.json['dstaddr']
	dstport = request.json['dstport']
	sasrcaddr = request.json['sasrcaddr']
	sadstaddr = request.json['sadstaddr']
	tunnel = request.json['tunnel']
	action = request.json['action']
	proposal = request.json['proposal']
	subprocess.call(['./weilun.sh', 'updatePolicy', numbers, srcaddr, srcport, dstaddr, dstport, sasrcaddr, sadstaddr, tunnel, action, proposal])
	with open('ipsecpolicy.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'UPDATED IPSEC POLICY': output2})

#DELETE IPSEC POLICY
#curl -u admin:python -H "Content-Type: application/json" -X DELETE -i -d '{"numbers":"1"}' http://localhost:5000/todo/api/mikrotik/ipsec/policy/delete
@mikrotik.route('/todo/api/mikrotik/ipsec/policy/delete', methods=['DELETE'])
@auth.login_required
def deletePolicy():
	numbers = request.json['numbers']
	subprocess.call(['./weilun.sh', 'deletePolicy', numbers])
	with open('ipsecpolicy.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'IPSEC POLICY DELETED': output2, 'Delete':True})

if __name__ == '__main__':
	mikrotik.run(debug=True)



