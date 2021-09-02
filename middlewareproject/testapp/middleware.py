class ExecutionMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print('This line added at pre processing of request')
        respone = self.get_response(request)
        print('This line added at post processing of request')
        return respone


from django.http import HttpResponse
class ApplicationMaintanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        return HttpResponse('<h1>The application currently under maintance please visit back after 2 days</h1>')