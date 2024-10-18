from rest_framework.response import Response

class CostumResponJson:
    def __init__(self, statusCode, data):
        self.statusCode = statusCode
        self.data = data
        
    def __str__(self):
        return str(self.data)
    
    
    def generate_success_json(self):
        return Response({
            'status' : 'success',
            'message' : 'Data Retrieved Successfuly',
            'status_code' : self.statusCode,
            'data' : self.data,
        }, status=self.statusCode)
        
    def generate_error_json(self):
        return Response({
            'status' : 'error',
            'message' : 'Data Retrieved failed',
            'status_code' : self.statusCode,
            'errors' : self.data,
        }, status=self.statusCode)