#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.httpauth import HTTPBasicAuth
import os, api, csv, json, subprocess, re, natcrud

mikrotik = Flask(__name__)
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username =='admin':
		return 'python'
	return None


@auth.error_handler
def unauthorized():
	return make_response(jsonify({'Error':'Unauthorized Access'}), 401)

#ERROR HANDLER 400
@mikrotik.errorhandler(400)
def not_found(error):
	return make_response(jsonify({'error': 'Bad request'}), 400)

#ERROR HANDLER 404
@mikrotik.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

#CRUD FOR IP ADDRESSING (JINGKANG)


@mikrotik.route('/todo/api/mikrotik/createip', methods=['POST'])
@auth.login_required
def createip():
    ip = request.json['ip']
    interface = request.json['interface']
    subprocess.call(['./test.sh', 'createip', ip, interface])
    with open('file.txt') as f:
	output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'ip address': ip, 'interface': interface})


@mikrotik.route('/todo/api/mikrotik/printip', methods=['GET'])
@auth.login_required
def getip():
    subprocess.call(['./test.sh', 'printip'])
    with open('file.txt') as f:
	output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'ip': output2})


@mikrotik.route('/todo/api/mikrotik/updateip', methods=['PUT'])
@auth.login_required
def updateip():
    number = request.json['number']
    ip = request.json['ip']
    interface = request.json['interface']
    subprocess.call(['./test.sh', 'updateip', number, ip, interface])
    with open('file.txt') as f:
	output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'ip': output2})


@mikrotik.route('/todo/api/mikrotik/deleteip', methods=['DELETE'])
@auth.login_required
def deleteip():
    number = request.json['number']
    subprocess.call(['./test.sh', 'deleteip', number])
    with open('file.txt') as f:
	output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'ip': output2, 'delete': True})


#CRUD FOR WHOLE VLAN (JING KANG)


@mikrotik.route('/todo/api/mikrotik/createvlanall', methods=['POST'])
@auth.login_required
def createvlanall():
    vlaninterface = request.json['vlaninterface']
    vlanname = request.json['vlanname']
    vlanid = request.json['vlanid']
    vlanbridgename = request.json['vlanbridgename']
    vlantrafficinterface = request.json['vlantrafficinterface']
    subprocess.call(['./test.sh', 'createvlanall', vlaninterface, vlanname, vlanid, vlanbridgename, vlantrafficinterface])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2})


@mikrotik.route('/todo/api/mikrotik/readvlanall', methods=['GET'])
@auth.login_required
def readvlanall():
    subprocess.call(['./test.sh', 'readvlanall'])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2})


@mikrotik.route('/todo/api/mikrotik/updatevlanall', methods=['PUT'])
@auth.login_required
def updatevlanall():
    vlannumber = request.json['vlannumber']
    vlanname = request.json['vlanname']
    vlanid = request.json['vlanid']
    vlaninterface = request.json['vlaninterface']
    subprocess.call(['./test.sh', 'updatevlanall', vlannumber, vlanname, vlanid, vlaninterface])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2})


@mikrotik.route('/todo/api/mikrotik/deletevlanall', methods=['DELETE'])
@auth.login_required
def deletevlanall():
    vlannumber = request.json['vlannumber']
    vlanbridgenumber = request.json['vlanbridgenumber']
    subprocess.call(['./test.sh', 'deletevlanall', vlannumber, vlanbridgenumber])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2})


#CRUD FOR VLAN ONLY (JINGKANG)

@mikrotik.route('/todo/api/mikrotik/createvlan', methods=['POST'])
@auth.login_required
def createvlan():
    vlaninterface = request.json['vlaninterface']
    vlanname = request.json['vlanname']
    vlanid = request.json['vlanid']
    subprocess.call(['./test.sh', 'createvlan', vlaninterface, vlanname, vlanid])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2})


@mikrotik.route('/todo/api/mikrotik/readvlan', methods=['GET'])
@auth.login_required
def readvlan():
    subprocess.call(['./test.sh', 'readvlan'])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2})


@mikrotik.route('/todo/api/mikrotik/updatevlan', methods=['PUT'])
@auth.login_required
def updatevlan():
    vlannumber = request.json['vlannumber']
    vlanname = request.json['vlanname']
    vlanid = request.json['vlanid']
    vlaninterface = request.json['vlaninterface']
    subprocess.call(['./test.sh', 'updatevlan', vlannumber, vlanname, vlanid, vlaninterface])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2})


@mikrotik.route('/todo/api/mikrotik/deletevlan', methods=['DELETE'])
@auth.login_required
def deletevlan():
    vlannumber = request.json['vlannumber']
    subprocess.call(['./test.sh', 'deletevlan', vlannumber])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'vlan': output2, 'delete': True})


#CRUD FOR BRIDGES (JINGKANG)


@mikrotik.route('/todo/api/mikrotik/createbridge', methods=['POST'])
@auth.login_required
def createbridge():
    bridgename = request.json['bridgename']
    subprocess.call(['./test.sh', 'createbridge', bridgename])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridge': output2})


@mikrotik.route('/todo/api/mikrotik/readbridge', methods=['GET'])
@auth.login_required
def readbridge():
    subprocess.call(['./test.sh', 'readbridge'])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridge': output2})


@mikrotik.route('/todo/api/mikrotik/updatebridge', methods=['PUT'])
@auth.login_required
def updatebridge():
    bridgenumber = request.json['bridgenumber']
    bridgename = request.json['bridgename']
    subprocess.call(['./test.sh', 'updatebridge', bridgenumber, bridgename])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridge': output2})


@mikrotik.route('/todo/api/mikrotik/deletebridge', methods=['DELETE'])
@auth.login_required
def deletebridge():
    bridgenumber = request.json['bridgenumber']
    subprocess.call(['./test.sh', 'deletebridge', bridgenumber])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridge': output2, 'delete': True})


#CRUD FOR BRIDGE PORTS (JINGKANG)


@mikrotik.route('/todo/api/mikrotik/createbridgeport', methods=['POST'])
@auth.login_required
def createbridgeport():
    bridgeportname = request.json['bridgeportname']
    bridgevlaninterface = request.json['bridgevlaninterface']
    bridgeportinterface = request.json['bridgeportinterface']
    subprocess.call(['./test.sh', 'createbridgeport', bridgeportname, bridgevlaninterface, bridgeportinterface])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridgeport': output2})


@mikrotik.route('/todo/api/mikrotik/readbridgeport', methods=['GET'])
@auth.login_required
def readbridgeport():
    subprocess.call(['./test.sh', 'readbridgeport'])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridgeport': output2})


@mikrotik.route('/todo/api/mikrotik/updatebridgeport', methods=['PUT'])
@auth.login_required
def updatebridgeport():
    bridgeportnumber = request.json['bridgeportnumber']
    bridgeportname = request.json['bridgeportname']
    bridgeportinterface = request.json['bridgeportinterface']
    subprocess.call(['./test.sh', 'updatebridgeport', bridgeportnumber, bridgeportname, bridgeportinterface])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridgeport': output2})


@mikrotik.route('/todo/api/mikrotik/deletebridgeport', methods=['DELETE'])
@auth.login_required
def deletebridgeport():
    bridgeportnumber = request.json['bridgeportnumber']
    subprocess.call(['./test.sh', 'deletebridgeport', bridgeportnumber])
    with open('file.txt') as f:
        output = f.read()
        output2 = re.split('\n', output)
    return jsonify({'bridgeport': output2, 'delete': True})


#CRUD FOR FIREWALL RULES NAT (KOH JIE)


#CREATE LIST
#curl -u admin:python -i -H "Content-Type: application/json" -X POST -d '{"address":"20.20.20.0/24", "list":"20network"}' http://localhost:5000/todo/api/mikrotik/addrlist/create
@mikrotik.route('/todo/api/mikrotik/addrlist/create', methods=['POST'])
@auth.login_required
def create_list():
	address = request.json['address']
	l = request.json['list']

	subprocess.call(['./nat.sh', 'createlist', address, l])

	with open('file.txt') as f:
		output = f.read()
	
	return jsonify({'address': address, 'list': l})

#PRINT ALL LISTS
#curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/addrlist/print
@mikrotik.route('/todo/api/mikrotik/addrlist/print', methods=['GET'])
@auth.login_required
def get_list():
	subprocess.call(['./nat.sh', 'printlist'])

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

    	subprocess.call(['./nat.sh', 'updatelist', numbers, address, l])

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
	subprocess.call(['./nat.sh', 'deletelist', numbers])

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

	subprocess.call(['./nat.sh', 'createrule', chain, action, rejectw, protocol, src, dst, log])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'Filter Rule': output2})

#PRINT ALL RULES
#curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/filterrule/print
@mikrotik.route('/todo/api/mikrotik/filterrule/print', methods=['GET'])
@auth.login_required
def get_rule():
	subprocess.call(['./nat.sh', 'printrule'])

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

    	subprocess.call(['./nat.sh', 'updaterule', numbers, chain, action, rejectw, protocol, src, dst, log])

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
	subprocess.call(['./nat.sh', 'deleterule', numbers])

	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'Rule': output2, 'delete': True})

#PRINT ALL NAT
#curl -u admin:python -H "Content-Type: application/json" -i http://localhost:5000/todo/api/mikrotik/nat/print
@mikrotik.route('/todo/api/mikrotik/nat/print', methods=['GET'])
@auth.login_required
def get_masqnat():
	subprocess.call(['./nat.sh', 'printnat'])

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
	subprocess.call(['./nat.sh', 'deletenat', numbers])

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

	subprocess.call(['./nat.sh', 'createmasqnat', outinterface])

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

    	subprocess.call(['./nat.sh', 'updatemasqnat', numbers, outinterface])

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

	subprocess.call(['./nat.sh', 'createnatbypass', srcaddr, dstaddr])

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

    	subprocess.call(['./nat.sh', 'updatenatbypass', numbers, srcaddr, dstaddr])

    	with open('file.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Updated NAT Rule': output2})




#CRUD FOR USERS (IAN)


@mikrotik.route('/todo/api/mikrotik/createuser', methods=['POST'])
def createuser():
    name = request.json['name']
    group = request.json['group']
    password = request.json['password']

    subprocess.call(['./user.sh', 'create', name, group, password])
    with open('file.txt') as f:
	output = f.read()
    return jsonify({'name':name, 'group':group, 'password':password})


@mikrotik.route('/todo/api/mikrotik/printuser', methods=['GET'])
def getuser():
    subprocess.call(['./user.sh', 'print'])
    with open('file.txt') as f:
	output = f.read()
	output2 = re.split('\n', output)
    return jsonify({'user': output2})

@mikrotik.route('/todo/api/mikrotik/updateuser/<numbers>', methods=['PUT'])
def updateuser(numbers):
    nuser = request.json['nuser']
    group = request.json['group']
    password = request.json['password']

    subprocess.call(['./user.sh', 'update', numbers, nuser, group, password])
    with open('file.txt') as f:
	output = f.read()
	output2 = re.split('\n', output)
    return jsonify({'user': output2})

@mikrotik.route('/todo/api/mikrotik/deleteuser/<numbers>', methods=['DELETE'])
def deleteuser(numbers):
    subprocess.call(['./user.sh', 'delete', numbers])
    with open('file.txt') as f:
	output = f.read()
	output2 = re.split('\n', output)
    return jsonify({'user': output2, 'delete': True})

#SSH

@mikrotik.route('/todo/api/mikrotik/createssh', methods=['POST'])
def createssh():
    key = request.json['key']
    name = request.json['name']


    subprocess.call(['./user.sh', 'create2', key, name ])
    with open('file.txt') as f:
        output = f.read()
    return jsonify({'name':name, 'key':key})


@mikrotik.route('/todo/api/mikrotik/printssh', methods=['GET'])
def getssh():
    subprocess.call(['./user.sh', 'print2'])
    with open('file.txt') as f:
        output = f.read()
	output2 = re.split('\n', output)
    return jsonify({'user': output2})

@mikrotik.route('/todo/api/mikrotik/deletessh/<numbers>', methods=['DELETE'])
def deletessh(numbers):
    subprocess.call(['./user.sh', 'delete2', numbers])
    with open('file.txt') as f:
        output = f.read()
	output2 = re.split('\n', output)
	return jsonify({'user': output2, 'delete2': True})


#CRUD FOR IP ROUTE / SSH (WEILUN)


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
	gateway = request.json['gateway']
	subprocess.call(['./weilun.sh', 'createRoute', gateway])
	with open('route.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'IP ROUTE CREATED': output2})
#UPDATE IP ROUTE
#curl -u weilun:python -i -H "Content-Type: application/json" -X PUT -d '{"numbers":"1", "dst":"0.0.0.0", "src":"0.0.0.0", "gateway":"192.168.90.1"}' http://localhost:5000/todo/api/mikrotik/route/update
@mikrotik.route('/todo/api/mikrotik/route/update', methods=['PUT'])
@auth.login_required
def updateRoute():
	numbers = request.json['numbers']
	gateway = request.json['gateway']
	subprocess.call(['./weilun.sh', 'updateRoute', numbers, gateway])
	with open('route.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'UPDATED ROUTE': output2})
#DELETE IP ROUTE
#curl -u weilun:python -H "Content-Type: application/json" -X DELETE -i -d '{"numbers":"1"}' http://localhost:5000/todo/api/mikrotik/route/delete
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
#curl -u weilun:python -i -H "Content-Type: application/json" -X PUT -d '{"numbers":"1", "addr":"192.168.90.2", "port":"500", "secret":"lol"}' http://localhost:5000/todo/api/mikrotik/ipsec/peer/update
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
#curl -u weilun:python -H "Content-Type: application/json" -X DELETE -i -d '{"numbers":"1"}' http://localhost:5000/todo/api/mikrotik/ipsec/peer/delete
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
#curl -u weilun:python -i -H "Content-Type: application/json" -X PUT -d '{"numbers":"1", "srcaddr":"10.1.202.0/24", "srcport":"any", "dstaddr":"10.1.101.0/24", "dstport":"any", "sasrcaddr":"192.168.90.1", "sadstaddr":"192.168.90.2", "tunnel":"yes", "action":"encrypt", "proposal":"default"}' http://localhost:5000/todo/api/mikrotik/ipsec/policy/update=?
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
#curl -u weilun:python -H "Content-Type: application/json" -X DELETE -i -d '{"numbers":"1"}' http://localhost:5000/todo/api/mikrotik/ipsec/policy/delete
@mikrotik.route('/todo/api/mikrotik/ipsec/policy/delete', methods=['DELETE'])
@auth.login_required
def deletePolicy():
	numbers = request.json['numbers']
	subprocess.call(['./weilun.sh', 'deletePolicy', numbers])
	with open('ipsecpolicy.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'IPSEC POLICY DELETED': output2, 'Delete':True})


#CRUD FOR DHCP (MINGKANG)


@mikrotik.route('/todo/api/mikrotik/print/pool', methods=['GET'])
@auth.login_required
def printpool():
	subprocess.call(['./dhcp.sh', 'printpool'])
	with open('printpool.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'DHCP pool' : output2})

@mikrotik.route('/todo/api/mikrotik/print/network', methods=['GET'])
@auth.login_required
def printnetwork():
	subprocess.call(['./dhcp.sh', 'printnet'])
	with open('printnet.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'DHCP Network' : output2})

@mikrotik.route('/todo/api/mikrotik/print/server', methods=['GET'])
@auth.login_required
def printserver():
	subprocess.call(['./dhcp.sh', 'printserver'])
	with open('printserver.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'DHCP Server' : output2})

@mikrotik.route('/todo/api/mikrotik/add/pool', methods=['POST'])
@auth.login_required
def addpool():
	name = request.json['name']
	range = request.json['range']
	subprocess.call(['./dhcp.sh', 'addpool', name, range])
	with open('addpool.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)
	return jsonify({'Pool' : output2})

@mikrotik.route('/todo/api/mikrotik/add/network', methods=['POST'])
@auth.login_required
def addnetwork():
	subnet = request.json['subnet']
	gateway = request.json['gateway']
	subprocess.call(['./dhcp.sh', 'addnetwork', subnet, gateway])
	with open('addnetwork.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Network' : output2})

@mikrotik.route('/todo/api/mikrotik/add/server', methods=['POST'])
@auth.login_required
def addserver():
	interface = request.json['interface']
	poolname = request.json['poolname']
        subprocess.call(['./dhcp.sh', 'addserver', interface, poolname])
        with open('addserver.txt') as f:
                output = f.read()
		output2 = re.split('\n', output)

        return jsonify({'Server' : output2})

@mikrotik.route('/todo/api/mikrotik/update/pool', methods=['PUT'])
@auth.login_required
def updatepool():
	number = request.json['number']
	range = request.json['range']
        subprocess.call(['./dhcp.sh', 'updatepool', range, number])
        with open('updatepool.txt') as f:
                output = f.read()
		output2 = re.split('\n', output)

        return jsonify({'Pool' : output2})

@mikrotik.route('/todo/api/mikrotik/update/network', methods=['PUT'])
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

@mikrotik.route('/todo/api/mikrotik/update/server', methods=['PUT'])
@auth.login_required
def updateserver():
	number = request.json['number']
	address = request.json['address']
	poolname = request.json['poolname']
        subprocess.call(['./dhcp.sh', 'updateserver', address, number, poolname])
        with open('updateserver.txt') as f:
                output = f.read()
		output2 = re.split('\n', output)

        return jsonify({'Server' : output2})

@mikrotik.route('/todo/api/mikrotik/delete/pool', methods=['DELETE'])
@auth.login_required
def delpool():
	number = request.json['number']
        subprocess.call(['./dhcp.sh', 'delpool', number])
        with open('delpool.txt') as f:
                output = f.read()
		output2 = re.split('\n', output)

        return jsonify({'Pool' : output2, 'Delete': True})

@mikrotik.route('/todo/api/mikrotik/delete/network', methods=['DELETE'])
@auth.login_required
def delnetwork():
	number = request.json['number']
        subprocess.call(['./dhcp.sh', 'delnetwork', number])
        with open('delnetwork.txt') as f:
                output = f.read()
		output2 = re.split('\n', output)

        return jsonify({'Network' : output2, 'Delete': True})

@mikrotik.route('/todo/api/mikrotik/delete/server', methods=['DELETE'])
@auth.login_required
def delIp():
	number = request.json['number']
	subprocess.call(['./dhcp.sh', 'delserver', number])
	with open('delserver.txt') as f:
		output = f.read()
		output2 = re.split('\n', output)

	return jsonify({'Server': output2, 'Delete': True})

@mikrotik.route('/todo/api/mikrotik/add/dhcp', methods=['POST'])
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
