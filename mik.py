#!flask/bin/python
from flask import Flask, jsonify, abort, request, url_for, make_response, json
from flask.ext.httpauth import HTTPBasicAuth
import os, api, csv, json, subprocess, re

mikrotik = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username == 'weilun':
		return 'python'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'Error':'Unauthorized Access'}), 401)

#IP ROUTE CRUD
#READ IP ROUTE
#curl -u weilun:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/route/print
@mikrotik.route('/todo/api/mikrotik/route/print', methods=['GET'])
@auth.login_required
def printRoute():
	subprocess.call(['./weilun.sh', 'printRoute'])
	with open('route.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
		
	return jsonify({'PRINT ROUTE': output2})

#CREATE IP ROUTE
#curl -u weilun:python -i -H "Content-Type: application/json" -X POST -d '{"dst":"0.0.0.0", "src":"0.0.0.0", "gateway":"192.168.90.254"}' http://localhost:5000/todo/api/mikrotik/route/create
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
#curl -u weilun:python -i -H "Content-Type: application/json" -X PUT -d '{"dst":"0.0.0.0", "src":"0.0.0.0", "gateway":"192.168.90.1"}' http://localhost:5000/todo/api/mikrotik/route/update=?
@mikrotik.route('/todo/api/mikrotik/route/update=<numbers>', methods=['PUT'])
@auth.login_required
def updateRoute(numbers):
	dst = request.json['dst']
	src = request.json['src']
	gateway = request.json['gateway']
	subprocess.call(['./weilun.sh', 'updateRoute', numbers, dst, src, gateway])
	with open('route.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'UPDATED ROUTE': output2})
#DELETE IP ROUTE
#curl -u weilun:python -H "Content-Type: application/json" -X DELETE -i http://localhost:5000/todo/api/mikrotik/route/delete=?
@mikrotik.route('/todo/api/mikrotik/route/delete=<numbers>', methods=['DELETE'])
@auth.login_required
def deleteRoute(numbers):
	subprocess.call(['./weilun.sh', 'deleteRoute', numbers])
	with open('route.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'ROUTE DELETED': output2, 'delete':True})

#IPSEC PEER CRUD

#READ IPSEC PEER
#curl -u weilun:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/ipsec/peer/print
@mikrotik.route('/todo/api/mikrotik/ipsec/peer/print', methods=['GET'])
@auth.login_required
def printPeer():
	subprocess.call(['./weilun.sh', 'printPeer'])
	with open('ipsecpeer.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
		
	return jsonify({'PRINT IPSEC PEER': output2})

#CREATE IPSEC PEER
#curl -u weilun:python -i -H "Content-Type: application/json" -X POST -d '{"addr":"192.168.90.2", "port":"500", "secret":"test"}' http://localhost:5000/todo/api/mikrotik/ipsec/peer/create
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
#curl -u weilun:python -i -H "Content-Type: application/json" -X PUT -d '{"addr":"192.168.90.2", "port":"500", "secret":"lol"}' http://localhost:5000/todo/api/mikrotik/ipsec/peer/update=?
@mikrotik.route('/todo/api/mikrotik/ipsec/peer/update=<numbers>', methods=['PUT'])
@auth.login_required
def updatePeer(numbers):
	addr = request.json['addr']
	port = request.json['port']
	secret = request.json['secret']
	subprocess.call(['./weilun.sh', 'updatePeer', numbers, addr, port, secret])
	with open('ipsecpeer.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'UPDATED IPSEC PEER': output2})

#DELETE IPSEC PEER
#curl -u weilun:python -H "Content-Type: application/json" -X DELETE -i http://localhost:5000/todo/api/mikrotik/ipsec/peer/delete/<numbers>
@mikrotik.route('/todo/api/mikrotik/ipsec/peer/delete=<numbers>', methods=['DELETE'])
@auth.login_required
def deletePeer(numbers):
	subprocess.call(['./weilun.sh', 'deletePeer', numbers])
	with open('ipsecpeer.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'IPSEC PEER DELETED': output2, 'Delete':True})

#IPSEC POLICY CRUD

#READ IPSEC POLICY
#curl -u weilun:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/ipsec/policy/print
@mikrotik.route('/todo/api/mikrotik/ipsec/policy/print', methods=['GET'])
@auth.login_required
def printPolicy():
	subprocess.call(['./weilun.sh', 'printPolicy'])
	with open('ipsecpolicy.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)	
	return jsonify({'PRINT IPSEC POLICY': output2})

#CREATE IPSEC POLICY
#curl -u weilun:python -i -H "Content-Type: application/json" -X POST -d '{"srcaddr":"10.1.202.0/24", "srcport":"any", "dstaddr":"10.1.101.0/24", "dstport":"any", "sasrcaddr":"192.168.90.1", "sadstaddr":"192.168.90.2", "tunnel":"yes", "action":"encrypt", "proposal":"default"}' http://localhost:5000/todo/api/mikrotik/ipsec/policy/create
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
#curl -u weilun:python -i -H "Content-Type: application/json" -X PUT -d '{"srcaddr":"10.1.202.0/24", "srcport":"any", "dstaddr":"10.1.101.0/24", "dstport":"any", "sasrcaddr":"192.168.90.1", "sadstaddr":"192.168.90.2", "tunnel":"yes", "action":"encrypt", "proposal":"default"}' http://localhost:5000/todo/api/mikrotik/ipsec/policy/update=?
@mikrotik.route('/todo/api/mikrotik/ipsec/policy/update=<numbers>', methods=['PUT'])
@auth.login_required
def updatePolicy(numbers):
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
#curl -u weilun:python -H "Content-Type: application/json" -X DELETE -i http://localhost:5000/todo/api/mikrotik/ipsec/policy/delete=<numbers>
@mikrotik.route('/todo/api/mikrotik/ipsec/policy/delete=<numbers>', methods=['DELETE'])
@auth.login_required
def deletePolicy(numbers):
	subprocess.call(['./weilun.sh', 'deletePolicy', numbers])
	with open('ipsecpolicy.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'IPSEC POLICY DELETED': output2, 'Delete':True})

if __name__ == '__main__':
	mikrotik.run(debug=True)
