#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.httpauth import HTTPBasicAuth
import os, api5, csv, json, subprocess, re

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

@mikrotik.route('/todo/api/mikrotik/createuser', methods=['POST'])
@auth.login_required
def createuser():
    name = request.json['name']
    group = request.json['group']
    password = request.json['password']

    subprocess.call(['./test.sh', 'create', name, group, password])
    with open('file.txt') as f:
	output = f.read()
	output2 = re.split('\n',output)

    return jsonify({'user':output2})


@mikrotik.route('/todo/api/mikrotik/printuser', methods=['GET'])
@auth.login_required
def getuser():
    subprocess.call(['./test.sh', 'print'])
    with open('file.txt') as f:
	output = f.read()
	output2 = re.split('\n',output)
    return jsonify({'user': output2})

@mikrotik.route('/todo/api/mikrotik/updateuser/<numbers>', methods=['PUT'])
@auth.login_required
def updateuser(numbers):
    nuser = request.json['nuser']
    group = request.json['group']
    password = request.json['password']

    subprocess.call(['./test.sh', 'update', numbers, nuser, group, password])
    with open('file.txt') as f:
	output = f.read()
	output2 = re.split('\n',output)
    return jsonify({'user': output2})

@mikrotik.route('/todo/api/mikrotik/deleteuser/<numbers>', methods=['DELETE'])
@auth.login_required
def deleteuser(numbers):
    subprocess.call(['./test.sh', 'delete', numbers])
    with open('file.txt') as f:
	output = f.read()
	output2 = re.split('\n',output)
    return jsonify({'user': output2, 'delete': True})


####

@mikrotik.route('/todo/api/mikrotik/createssh', methods=['POST'])
@auth.login_required
def createssh():
    key = request.json['key']
    name = request.json['name']

    subprocess.call(['./test.sh', 'create2', key, name ])
    with open('file.txt') as f:
        output = f.read()
	output2 = re.split('\n',output)
    return jsonify({'ssh':output2})


@mikrotik.route('/todo/api/mikrotik/printssh', methods=['GET'])
@auth.login_required
def getssh():
    subprocess.call(['./test.sh', 'print2'])
    with open('file.txt') as f:
        output = f.read()
	output2 = re.split('\n',output)
    return jsonify({'user': output2})

@mikrotik.route('/todo/api/mikrotik/deletessh/<numbers>', methods=['DELETE'])
@auth.login_required
def deletessh(numbers):
    subprocess.call(['./test.sh', 'delete2', numbers])
    with open('file.txt') as f:
        output = f.read()
	output2 = re.split('\n',output)
    return jsonify({'user': output2, 'delete2': True})

if __name__ == '__main__':
    mikrotik.run(debug=True)

