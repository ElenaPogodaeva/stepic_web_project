def app(environ, start_response):
 
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)

    a=environ['QUERY_STRING'].split('&');
    str = '\n'.join(a);
    data = str.encode();
    return [data]