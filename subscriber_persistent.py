import zmq
import sys

#########################################################################
#Copyright:      8thSensus Inc. @2019
#Maintainer:     Kevin McNamara (kevin@8thsensus.com)
#Description:    0mq persistent subscriber 
#########################################################################

## Persistent Subscriber
## declare variables
server = "localhost"
port = "5556"
topic = "0"
filterby = ""
conn = ""

if len(sys.argv) > 1:
    server =  sys.argv[1]
    port =  sys.argv[2]
    topic = sys.argv[3]
    filterby = sys.argv[4]
    int(port)
else:
    print "usage: subscriber_persistent.py server-target port topic filterby"
    exit(0)
    
## Socket to talk to server
try:
   context = zmq.Context()
   socket = context.socket(zmq.SUB)
except:
    e = sys.exc_info()[0]
    print "ERROR creating socket.  Error Code : "+ e
    exit(0)

print "Starting Peristent Subscriber on Topic "+topic+" ..."
try:
   conn = "tcp://"+server+":%s"
   socket.connect (conn % port)
except:
    e = sys.exc_info()[0]
    print "ERROR creating socket.  Error Code : "+ e
    exit(0)

## Subscribe to Topic
socket.setsockopt(zmq.SUBSCRIBE, topic)

## Persistent subsciber
while True:
    message = socket.recv()
    print "Echo: " + message

      
