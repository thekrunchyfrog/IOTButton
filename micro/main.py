import usocket
import esp
from machine import Pin


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


def callback():
    http_post('http://iot.krunchylabs.com/click')


p2 = Pin(2, Pin.IN)
p2.irq(trigger=Pin.IRQ_FALLING, handler=callback)

while true:
    esp.sleep_type(esp.SLEEP_LIGHT)
