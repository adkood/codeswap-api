import json


class JsonResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path.startswith('/admin'):
            # Skip processing for admin URLs
            return self.get_response(request)
        if response.status_code < 400:
            # Success response
            data = json.loads(response.content.decode('utf-8'))
            response_data = {
                'status': 'success',
                'data': data,
            }
        else:
            # Error response
            response_data = {
                'status': 'error',
                'code': response.status_code,
                'data': {},
            }

        response.content = json.dumps(response_data).encode('utf-8')
        response['Content-Type'] = 'application/json'
        return response
