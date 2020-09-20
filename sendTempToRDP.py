#!/usr/bin/python
from max6675 import MAX6675, MAX6675Error
import time
import socket#for sockets
import sys#for exit
import struct

# Make sure to use the pi's GPIO numbers of pins rather than the generic pin numbers 1-40 as they do not match.
cs_pin = 24 #(CS)
clock_pin = 23 #(SCLK/SCK)
data_pin = 22 #(SO/MOSI)
units = "c" # Leave as Celsius as Roastmaster can convert if desired.
thermocouple = MAX6675(cs_pin, clock_pin, data_pin, units)

def udp_socket():
    # This is the IP and port we will be multicasting to via UDP protocol.
    # This way we do not have to worry about handshakes or the IP of the iOS device.
    localIP     = "224.0.0.1"
    localPort   = 5050
    multicastGroup = (localIP, localPort)

    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # UDPServerSocket.settimeout(0.3)

    ttl = struct.pack('b', 1)
    UDPServerSocket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    print("UDP server up")

    running = True
    while(running):
        try:            
            try:
                # This is the actual temperature from the thermocouple.
                temp = thermocouple.get()        
                # print("tc: {}".format(temp))
                payload = '{"RPChannel":1,"RPEventType":3,"RPValue":%s,"RPMetaType":3000}' % (temp)
                datagram = '{"RPVersion":"RDP_1.0","RPSerial":"kaldidrum","RPEpoch":%s,"RPPayload":[%s]}' % (time.time(), payload)
                bytesToSend = str.encode(datagram)
                try:
                    # Sending data to Roastmaster
                    UDPServerSocket.sendto(bytesToSend, multicastGroup)
                    # Display this via cli for feedback/fallback.
                    print(bytesToSend)
                except socket:
                    print >>sys.stderr, 'could not send'
            except MAX6675Error as e:
                temp = "Thermocouple Error: "+ e.value
                running = False
                print("tc: {}".format(temp))

            # How long in seconds to wait before sending again. Roastmaster recommends max of 1 (5 seconds is considered a broken connection).
            time.sleep(0.3)
        except KeyboardInterrupt:
            running = False
            # Cleanup when interrupted.
            UDPServerSocket.close()

# Run main function.
udp_socket()
# Cleanup when done.
thermocouple.cleanup()
