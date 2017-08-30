#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
	def __init__(self, n=2,**opts):
		Topo.__init__(self,**opts)
		s1=self.addSwitch("s1")
		s2=self.addSwitch("s2")
		s3=self.addSwitch("s3")
		h1=self.addHost("h1")
		h2=self.addHost("h2")
		h3=self.addHost("h3")
		h4=self.addHost("h4")
		h5=self.addHost("h5")		
		self.addLink(h1,s1,bw=10)
		self.addLink(h2,s1,bw=10)
		self.addLink(h3,s2,bw=10)
		self.addLink(h4,s2,bw=10)
		self.addLink(h5,s3,bw=10)
		self.addLink(s1,s2,bw=10)
		self.addLink(s2,s3,bw=10)
		 
def perfTest():
	topo=SingleSwitchTopo(n=4)
	net=Mininet(topo=topo,host=CPULimitedHost,link=TCLink)
	net.start()
	print "dumping"
	dumpNodeConnections(net.hosts)
	print "Testing"
	net.pingAll()
	h1,h4=net.get("h1","h4")
	net.iperf((h1,h4))
	net.stop()

if __name__=="__main__":
	setLogLevel("info")
	perfTest()
