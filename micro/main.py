import usocket


def http_post(url):
    _, _, host, path = url.split('/', 3)
    addr = usocket.getaddrinfo(host, 5000)[0][-1]
    s = usocket.socket()
    s.connect(addr)
    s.send(bytes('POST /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break

http_post('http://127.0.0.1/click')
