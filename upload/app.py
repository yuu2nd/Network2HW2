from flask import Flask , request
from flask_restful import Resource , Api,reqparse
import json ,time

app = Flask (__name__)
api = Api(app) 

parser = reqparse.RequestParser()


class Upload(Resource):
	def post(self):
		if 'file' not in request.files:
			return {"code":404,"desc":"upload fail"}
		file = request.files['file']
		file.save("test.jpg")
		return {"code":200,"desc":"upload success"}

api.add_resource(Upload,'/upload')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5500)
