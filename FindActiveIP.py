import commands
import threading,time

subnet="192.168.122"
host_start=1
host_end=254
ping_command_prefix="ping -c 1 -W 1 "
threadpool = []

def ping_host(i,ping_command):
	(status,output) = commands.getstatusoutput(ping_command)
	if 0 == status:
		print "----Find! %s" % i


for i in range(host_start,host_end):
	host_ip="%s.%d"%(subnet,i)
	ping_command = ping_command_prefix + host_ip
	th=threading.Thread(target=ping_host,args=(i,ping_command))
	threadpool.append(th)

for th in threadpool:
	th.start()

for th in threadpool:
	threading.Thread.join(th)





