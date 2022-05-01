import machine
import urequests 

led = machine.Pin(25, machine.Pin.OUT)
led.off()
led2 = machine.Pin(26, machine.Pin.OUT)
led2.off()
led3 = machine.Pin(27, machine.Pin.OUT)
led3.off()
#------------------------
import network
ssid = '___'
password = '19831119'
#------------------------
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
station.isconnected()
station.ifconfig()

#while not station.active():
    #pass
for i in range (20):
    print('try to connect wifi in {}s'.format(i))
    
    if station.isconnected():
        break
print('network config:', station.ifconfig())
#------------------------
import socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def web_page():
    
    if KL1.value() == 1:
        KL1_state = 'ON'   
    elif KL1.value() == 0:
        KL1_state = 'OFF'
          
    if KL2.value() == 1:
        KL2_state = 'ON'
    elif KL2.value() == 0:
        KL2_state = 'OFF'
        
    if LL1.value() == 1:
        LL1_state = 'ON'
    elif LL1.value() == 0:
        LL1_state = 'OFF' 
   
    html_page = """ <!DOCTYPE HTML>
                <html>
                <head>
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    
                </head>
                <body>
                    <center><h2>ESP32 Web Server in MicroPython </h2></center>
                    <center>
                        <form>
                            <button type='submit' name="LED" value='1'> LED ON </button>
                            <button type='submit' name="LED" value='0'> LED OFF </button><br>
                            <button type='submit' name="LED2" value='1'> LED2 ON </button>
                            <button type='submit' name="LED2" value='0'> LED2 OFF </button><br>
                            <button type='submit' name="LED3" value='1'> LED3 ON </button>
                            <button type='submit' name="LED3" value='0'> LED3 OFF </button><br>
                        </form>
                    </center>
                    <center><p>LED is now <strong>"""+ led_state + """</strong>.</p></center>
                    <center><p>LED2 is now <strong>"""+ led2_state + """</strong>.</p></center>
                    <center><p>LED2 is now <strong>"""+ led3_state + """</strong>.</p></center>

                </body>
                </html>"""
    return html_page

#                    <center><p>Time is now <strong>"""+ str(time.time()) + """</strong>.</p></center>

while True:
    conn, addr = s.accept()
    print("Got connection from %s" % str(addr))
    
    request=conn.recv(1024)
    print("")
    print("")
    print("Content %s" % str(request))
    
    request = str(request)
    led_on = request.find('/?LED=1')
    led_off = request.find('/?LED=0')
    led2_on = request.find('/?LED2=1')
    led2_off = request.find('/?LED2=0')
    led3_on = request.find('/?LED3=1')
    led3_off = request.find('/?LED3=0')
    
    if led_on == 6:
        print('LED ON')
        print(str(led_on))
        led.value(1)
    elif led2_on == 6:
          print('LED2 ON')
          print(str(led2_on))
          led2.value(1)
    elif led3_on == 6:
          print('LED3 ON')
          print(str(led3_on))
          led3.value(1)          
    elif led_off == 6:
        print('LED OFF')
        print(str(led_off))
        led.value(0)
    elif led2_off == 6:
        print('LED2 OFF')
        print(str(led2_off))
        led2.value(0)
    elif led3_off == 6:
        print('LED3 OFF')
        print(str(led3_off))
        led3.value(0)
        
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    
    conn.close()
    
          
    
                            
                        
        