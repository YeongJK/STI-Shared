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
@mikrotik.route('/todo/api/mikrotik/addrlist/create', methods=['POST'])
@auth.login_required
def create_list():
	address = request.json['address']
	l = request.json['list']

	subprocess.call(['./kohjie.sh', 'createlist', address, l])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	
	return jsonify({'Addresslist Created:': output2})

#PRINT ALL LISTS
@mikrotik.route('/todo/api/mikrotik/addrlist/print', methods=['GET'])
@auth.login_required
def get_list():
	subprocess.call(['./kohjie.sh', 'printlist'])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Created Address List(s)': output2})

#UPDATE LIST
@mikrotik.route('/todo/api/mikrotik/addrlist/update', methods=['PUT'])
@auth.login_required
def update_list():
	numbers = request.json['numbers']
    	address = request.json['address']
	l = request.json['list']

    	subprocess.call(['./kohjie.sh', 'updatelist', numbers, address, l])

    	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Updated Address List': output2})

#DELETE LIST
@mikrotik.route('/todo/api/mikrotik/addrlist/delete', methods=['DELETE'])
@auth.login_required
def delete_list():
	numbers = request.json['numbers']
	subprocess.call(['./kohjie.sh', 'deletelist', numbers])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'Deleted List': output2, 'delete': True})

#CREATE RULE
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

	subprocess.call(['./kohjie.sh', 'createrule', chain, action, rejectw, protocol, src, dst, log])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'Filter Rule': output2})

#PRINT ALL RULES
@mikrotik.route('/todo/api/mikrotik/filterrule/print', methods=['GET'])
@auth.login_required
def get_rule():
	subprocess.call(['./kohjie.sh', 'printrule'])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Rule': output2})

#UPDATE RULE
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

    	subprocess.call(['./kohjie.sh', 'updaterule', numbers, chain, action, rejectw, protocol, src, dst, log])

    	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Rule': output2})

#DELETE RULE
@mikrotik.route('/todo/api/mikrotik/filterrule/delete', methods=['DELETE'])
@auth.login_required
def delete_rule():
	numbers = request.json['numbers']
	subprocess.call(['./kohjie.sh', 'deleterule', numbers])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'Rule': output2, 'delete': True})

#PRINT ALL NAT
@mikrotik.route('/todo/api/mikrotik/nat/print', methods=['GET'])
@auth.login_required
def get_masqnat():
	subprocess.call(['./kohjie.sh', 'printnat'])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'NAT Rule(s)': output2})

#DELETE NAT
@mikrotik.route('/todo/api/mikrotik/nat/delete', methods=['DELETE'])
@auth.login_required
def delete_masqnat():
	numbers = request.json['numbers']
	subprocess.call(['./kohjie.sh', 'deletenat', numbers])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Deleted NAT Rule': output2, 'delete': True})

#CREATE MASQ NAT
@mikrotik.route('/todo/api/mikrotik/nat/createmasqnat', methods=['POST'])
@auth.login_required
def create_masqnat():
	outinterface = request.json['outinterface']

	subprocess.call(['./kohjie.sh', 'createmasqnat', outinterface])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	
	return jsonify({'outinterface': output2})

#UPDATE MASQ NAT
@mikrotik.route('/todo/api/mikrotik/nat/updatemasqnat', methods=['PUT'])
@auth.login_required
def update_masqnat():
	numbers = request.json['numbers']
	outinterface = request.json['outinterface']

    	subprocess.call(['./kohjie.sh', 'updatemasqnat', numbers, outinterface])

    	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Updated NAT Rule': output2})

#CREATE NAT BY PASS
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
@mikrotik.route('/todo/api/mikrotik/nat/updatenatbypass', methods=['PUT'])
@auth.login_required
def update_natbypass():
	numbers = request.json['numbers']
	srcaddr = request.json['srcaddr']
	dstaddr = request.json['dstaddr']

    	subprocess.call(['./kohjie.sh', 'updatenatbypass', numbers, srcaddr, dstaddr])

    	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Updated NAT Rule': output2})

if __name__ == '__main__':
	mikrotik.run(debug=True)



