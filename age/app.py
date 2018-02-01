from flask import Flask , request
from flask_restful import Resource , Api,reqparse
import json ,time 

app = Flask (__name__)
api = Api(app) 

parser = reqparse.RequestParser()
parser.add_argument('birthdate')

class Age(Resource):
	def post(self): 
		args = parser.parse_args()
		birthdate = args['birthdate']
		day,month,year = birthdate.split('-')
		age = int(time.strftime("%Y")) - int(year)
		if int(month)>int(time.strftime("%m")):
			age-=1
		if int(month)==int(time.strftime("%m")):
			if int(time.strftime("%d"))<int(day):
				age-=1
		return {"birthdate":birthdate, "age":age}

api.add_resource(Age,'/age')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5500)
