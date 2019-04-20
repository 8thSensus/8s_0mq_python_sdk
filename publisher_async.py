import zmq
import random
import sys
import time

#########################################################################
#Copyright: 	8thSensus Inc. @2019
#Maintainer:	Kevin McNamara (kevin@8thsensus.com)
#Description:    0mq publisher 
#########################################################################
## Publisher - One Time data push
## declare variables
server = "localhost"
port = "5556"
message = "no data"
topic = "0"

if len(sys.argv) > 1:
    server = sys.argv[1]
    port =  sys.argv[2]
    topic = sys.argv[3]	
    message = sys.argv[4]
    int(port)
else:
    print "usage: pub_server.py server-target port topic message"
    exit(0)

try:
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://"+server+":%s" % port)
except:
    e = sys.exc_info()[0]
    print "ERROR creating socket.  Error Code : "+ e
    exit(0)

## submit data onto bus
def submit_msg(tp, msg):
    time.sleep(1)
    print "%s %s" % (tp, msg)
    socket.send("%s %s" % (tp, msg))
    return;

submit_msg(topic,message)

