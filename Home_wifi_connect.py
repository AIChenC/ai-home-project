import network

ssid = ''
password = '19831119'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while not station.active():
    pass

print('network isconnected:', station.isconnected())
print('network config:', station.ifconfig())
