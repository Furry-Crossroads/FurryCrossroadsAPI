from flask_restful import Resource

class TestResource(Resource):
    def get(self):
        return {'message': 'You made a GET request'}
    
    def post(self):
        return {'message': 'You made a POST request'}
    
    def put(self):
        return {'message': 'You made a PUT request'}
    
    def delete(self):
        return {'message': 'You made a DELETE request'}
