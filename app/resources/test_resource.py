from flask_restful import Resource

class TestResource(Resource):
    def get(self):
        return {'message': 'This is a GET request'}
    
    def post(self):
        return {'message': 'This is a POST request'}
    
    def put(self):
        return {'message': 'This is a PUT request'}
    
    def delete(self):
        return {'message': 'This is a DELETE request'}
