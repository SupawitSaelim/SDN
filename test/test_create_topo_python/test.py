#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController

class SingleSwitchTopo(Topo):
    def build(self):
        Central  = self.addSwitch('s1', failMode='standalone')

        Edge1 = self.addSwitch('s2', failMode='standalone')
        Edge2  = self.addSwitch('s3', failMode='standalone')
        Edge3  = self.addSwitch('s4', failMode='standalone')

        h1 = self.addHost('h1', mac="00:00:00:00:02:01", ip="172.16.2.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:02:02", ip="172.16.2.2/24")
        h3 = self.addHost('h3', mac="00:00:00:00:03:01", ip="172.16.3.1/24")
        h4 = self.addHost('h4', mac="00:00:00:00:03:02", ip="172.16.3.2/24")
        h5 = self.addHost('h5', mac="00:00:00:00:04:01", ip="172.16.4.1/24")
        h6 = self.addHost('h6', mac="00:00:00:00:04:02", ip="172.16.4.2/24")


        self.addLink(Edge1, Central)
        self.addLink(Edge2, Central)
        self.addLink(Edge3, Central)

        self.addLink(Edge1, h1)
        self.addLink(Edge1, h2)
        self.addLink(Edge2, h3)
        self.addLink(Edge2, h4)
        self.addLink(Edge3, h5)
        self.addLink(Edge3, h6)
        
if __name__ == '__main__':
    setLogLevel('info')
    topo = SingleSwitchTopo()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    #net.pingAll()
    CLI(net)
    net.stop()
