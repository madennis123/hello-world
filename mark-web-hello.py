from wsgiref.simple_server import make_server

def hello_world(environ, start_response):
    status = '200 ok'
    headers = [('Content-type', 'teext/plain')]
    start_response(status, headers)
    return ['Hello World this is Mark Speaking - you know we come in peace!']
	
httpd = make_server('', 8080, hello_world)

print 'Serving on port 80'

httpd.serve_forever()	