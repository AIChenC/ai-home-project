import machine
import urequests 

KL1 = machine.Pin(25, machine.Pin.OUT)
KL1.off()
KL2 = machine.Pin(26, machine.Pin.OUT)
KL2.off()
LL1 = machine.Pin(27, machine.Pin.OUT)
LL1.off()
LL2 = machine.Pin(33, machine.Pin.OUT)
LL2.off()
door = machine.Pin(32, machine.Pin.OUT)
door.off()
#------------------------
import network
ssid = 'aiot'
password = 'xyz@1234'
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
        
    if LL2.value() == 1:
        LL2_state = 'ON'
    elif LL2.value() == 0:
        LL2_state = 'OFF'
        
    ''' if door.value() == 1:
        door_state = 'ON'
    elif door.value() == 0:
        door_state = 'OFF' '''  
   
    html_page = """ <!DOCTYPE HTML>
                <html>
                <head>
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    
                </head>
                <body>
                    <center><h2>ESP32 Web Server in MicroPython </h2></center>
                    <center>
                        <form>
                            <button type='submit' name="KL1" value='1'> Kitchen light 1 ON </button>
                            <button type='submit' name="KL1" value='0'> Kitchen light 1 OFF </button><br>
                            <button type='submit' name="KL2" value='1'> Kitchen light 2 ON </button>
                            <button type='submit' name="KL2" value='0'> Kitchen light 2 OFF </button><br>
                            <button type='submit' name="LL1" value='1'> Living light 1 ON </button>
                            <button type='submit' name="LL1" value='0'> Living light 1 OFF </button><br>
                            <button type='submit' name="LL2" value='1'> Living light 2 ON </button>
                            <button type='submit' name="LL2" value='0'> Living light 2 OFF </button><br>
                            <button type='submit' name="door" value='1'> Door will Open for 10 secs! </button>

                        </form>
                    </center>
                    <center><p>Kitchen light 1<strong>"""+ KL1_state + """</strong>.</p></center>
                    <center><p>Kitchen light 2<strong>"""+ KL2_state + """</strong>.</p></center>
                    <center><p>Living light 1<strong>"""+ LL1_state + """</strong>.</p></center>
                    <center><p>Living light 2 is<strong>"""+ LL2_state + """</strong>.</p></center>
                    <center><p>Door is<strong>"""+ door_state + """</strong>.</p></center>

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
    KL1_on = request.find('/?KL1=1')
    KL1_off = request.find('/?KL1=0')
    KL2_on = request.find('/?KL2=1')
    KL2_off = request.find('/?KL2=0')

    
    if KL1_on == 6:
        print('KL1 ON')
        print(str(KL1_on))
        KL1.value(1)
    elif KL2_on == 6:
          print('KL2 ON')
          print(str(KL2_on))
          KL2.value(1)
    '''elif LL1_on == 6:
          print('LL1 ON')
          print(str(LL1_on))
          LL1.value(1)          
    elif LL2_on == 6:
        print('LL2 ON')
        print(str(LL2_ON))
        led.value(1)
    elif door_on == 6:
        print('door ON')
        print(str(door_on))
        door.value(1)'''
    elif KL1_off == 6:
        print('KL1 OFF')
        print(str(KL1_off))
        KL1.value(0)
     elif KL2_off == 6:
          print('KL2 OFF')
          print(str(KL2_off))
          KL2.value(0)
    '''elif LL1_off == 6:
          print('LL1 OFF')
          print(str(LL1_off))
          LL1.value(0)          
    elif LL2_off == 6:
        print('LL2 OFF')
        print(str(LL2_OFF))
        led.value(0)
    elif door_off == 6:
        print('door OFF')
        print(str(door_off))
        door.value(0)'''

        
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    
    conn.close()
    
          
    
                            
                        
        