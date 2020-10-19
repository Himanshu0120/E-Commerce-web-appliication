from django.shortcuts import redirect
def auth_middleware(get_response):
  
    def middleware(request):
        response=get_response(request)
        print('middleware working')
        print(request.session.get('customer_id'))
        if not request.session.get('customer_id'):
            
            #this stores the path from where middleware is called
            return_url=request.META['PATH_INFO']
            return redirect(f'login?return_url={return_url}')
        return response
    
    return middleware
        