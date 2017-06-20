#!flask/bin/python
from flask import Flask, jsonify, abort, request, url_for, make_response, json
import dhcp, os, csv, subprocess, json, re
from flask_httpauth import HTTPBasicAuth

mikrotik = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username == 'admin':
		return 'python'
	return none

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'Error':'Unauthorized Access'}), 401)


@mikrotik.route('/print/pool', methods=['GET'])
@auth.login_required
def printpool():
	subprocess.call(['./dhcp.sh', 'printpool'])
	with open('printpool.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'DHCP pool' : output2})

@mikrotik.route('/print/net', methods=['GET'])
@auth.login_required
def printnetwork():
	subprocess.call(['./dhcp.sh', 'printnet'])
	with open('printnet.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'DHCP Network' : output2})

@mikrotik.route('/print/server', methods=['GET'])
@auth.login_required
def printserver():
	subprocess.call(['./dhcp.sh', 'printserver'])
	with open('printserver.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'DHCP Server' : output2})

@mikrotik.route('/add/pool', methods=['POST'])
@auth.login_required
def addpool():
	name = request.json['name']
	range = request.json['range']
	subprocess.call(['./dhcp.sh', 'addpool', name, range])
	with open('addpool.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'Pool' : output2})

@mikrotik.route('/add/network', methods=['POST'])
@auth.login_required
def addnetwork():
	subnet = request.json['subnet']
	gateway = request.json['gateway']
	subprocess.call(['./dhcp.sh', 'addnetwork', subnet, gateway])
	with open('addnetwork.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Network' : output2})

@mikrotik.route('/add/server', methods=['POST'])
@auth.login_required
def addserver():
	interface = request.json['interface']
	poolname = request.json['poolname']
        subprocess.call(['./dhcp.sh', 'addserver', interface, poolname])
        with open('addserver.txt') as f:
                output = f.read()
		output2 = re.split('\n', output)

        return jsonify({'Server' : output2})

@mikrotik.route('/update/pool', methods=['PUT'])
@auth.login_required
def updatepool():
	number = request.json['number']
	range = request.json['range']
        subprocess.call(['./dhcp.sh', 'updatepool', range, number])
        with open('updatepool.txt') as f:
                output = f.read()
		output2 = re.split('\n', output)

        return jsonify({'Pool' : output2})

@mikrotik.route('/update/network', methods=['PUT'])
@auth.login_required
def updatenetwork():
	number = request.json['number']
	address = request.json['address']
	gateway = request.json['gateway']
        subprocess.call(['./dhcp.sh', 'updatenetwork', address, gateway, number])
        with open('updatenetwork.txt') as f:
                output = f.read()
		output2 = re.split('\n', output)

        return jsonify({'Network' : output2})

@mikrotik.route('/update/server', methods=['PUT'])
@auth.login_required
def updateserver():
	number = request.json['number']
	address = request.json['address']
        subprocess.call(['./dhcp.sh', 'updateserver', address, number])
        with open('updateserver.txt') as f:
                output = f.read()
		output2 = re.split('\n', output)

        return jsonify({'Server' : output2})

@mikrotik.route('/delete/pool', methods=['DELETE'])
@auth.login_required
def delpool():
	number = request.json['number']
        subprocess.call(['./dhcp.sh', 'delpool', number])
        with open('delpool.txt') as f:
                output = f.read()
		output2 = re.split('\n', output)

        return jsonify({'Pool' : output2, 'Delete': True})

@mikrotik.route('/delete/network', methods=['DELETE'])
@auth.login_required
def delnetwork():
	number = request/json['number']
        subprocess.call(['./dhcp.sh', 'delnetwork', number])
        with open('delnetwork.txt') as f:
                output = f.read()
		output2 = re.split('\n', output)

        return jsonify({'Network' : output2, 'Delete': True})

@mikrotik.route('/delete/server', methods=['DELETE'])
@auth.login_required
def delIp():
	number = request.json['number']
	subprocess.call(['./dhcp.sh', 'delserver', number])
	with open('delserver.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Server': output2, 'Delete': True})

@mikrotik.route('/add/dhcp', methods=['POST'])
@auth.login_required
def addDHCP():
	name = request.json['name']
	range = request.json['range']
	network = request.json['network']
	gateway = request.json['gateway']
	interface = request.json['interface']
	subprocess.call(['./dhcp.sh', 'adddhcp', name, range, network, gateway, interface])
	with open('adddhcp.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'DHCP': output2})

if __name__ == '__main__':
	mikrotik.run(debug=True)
