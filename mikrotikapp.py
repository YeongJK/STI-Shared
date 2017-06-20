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

#ERROR HANDLER 401/403
@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error': 'Unauthorized access'}), 403)

#ERROR HANDLER 400
@mikrotik.errorhandler(400)
def not_found(error):
	return make_response(jsonify({'error': 'Bad request'}), 400)

#ERROR HANDLER 404
@mikrotik.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

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
	
	return jsonify({'address': address, 'list': l})

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
	
	return jsonify({'chain': chain, 'action': action, 'reject-with': rejectw, 'protocol': protocol, 'source address list': src, 'destination address list': dst, 'log': log})

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
	
	return jsonify({'outinterface': outinterface})

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
	
	return jsonify({'srcaddr': srcaddr, 'dstaddr': dstaddr})

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

if __name__ == '__main__':
	mikrotik.run(debug=True)



