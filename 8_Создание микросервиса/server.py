from flask import Flask, request, jsonify
import pickle
import os
from hashlib import sha256
from datetime import datetime
import re
import random
import string
import json
use=[]
app = Flask(__name__)
DEFAULT_PATH = "./collections.pickle"

def hasher(password, salt = None):
	if salt == None:
		letters_and_digits = string.ascii_letters + string.digits
		salt = ''.join(random.sample(letters_and_digits, 16))
		salt = salt.encode('utf-8')
	password = sha256((password).encode('utf-8')+salt).hexdigest()
	return salt,password

def save_coll(dict_, filename = None):
	filename = DEFAULT_PATH if filename == None else filename
	with open(filename, "wb") as picklefile:
		pickle.dump(dict_, picklefile)

def load_coll(filename = None):
	filename = DEFAULT_PATH if filename == None else filename
	if os.path.exists(filename):
		with open(filename, "rb") as picklefile:
			buffered = pickle.load(picklefile)
		return buffered
	else:
		return {}

def return_(result = True, description = "", exception = None):
	return {
		"result":result,
		"description":description,
		"exception": exception
		}

def email_val(email):
	collection = load_coll()
	return not bool(collection.get(email))

def write_inform(userinfo):
	collection = load_coll()
	password = userinfo["password"]
	if not re.search("^(\w|\d|\_){8,}$", password):
		return False
	login = userinfo["login"]
	date = datetime.now().strftime("%H:%M:%S, %d.%m.%Y")
	password = hasher(password)
	collection[login] = {"password": password, "date": date, }
	save_coll(collection)
	ps= password[1]
	write_json(login,ps)
	return True

def write_json(login,password):

	use.append({login: password})
	with open('users_json.json', 'w') as outfile:
		json.dump(use, outfile)

def auth_chek(info):
	collection = load_coll()
	email = info["login"]
	password = info["password"]
	c_pass = collection.get(email)
	if not c_pass:
		return return_(False, " ", "User doesnt exist")
	cu_pass = c_pass["password"]
	ch = hasher(password, cu_pass[0])
	if cu_pass == ch:
		return return_(True, "Login successful")
	else:
		return return_(False, " ", "Wrong password")



@app.route('/user/auth', methods=['POST'])
def auth():
	userinf = request.get_json()
	return auth_chek(userinf)


@app.route('/user/reg', methods=['POST'])
def reg():
	userinf = request.get_json()
	if email_val(userinf["login"]):
		if write_inform(userinf):
			return return_(True, "Successful registration")
		else:
			return return_(False, "", "The password must be at least 8 characters long")
	else:
		return return_(False, "", "User already exists")


@app.route('/users', methods=['GET'])
def by_login():
	with open('users_json.json') as json_file:
		data = json.load(json_file)
	lis = []
	for i in data:
		lis.append(list(i.keys()))
	s = ''
	for i in range(len(lis)):
		s += str(lis[i][0])
		s += ' '
	return return_(True, s)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)