#!/usr/bin/python

"""
Different Mininet Network Topologies
Run: sudo python <filename>.py
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import OVSSwitch, Controller, RemoteController

# Topology 1: Ring Topology (วงแหวน)
class RingTopo(Topo):
    "Ring topology with 4 switches and 4 hosts"
    def build(self):
        # Add switches
        switches = []
        for i in range(4):
            switches.append(self.addSwitch(f's{i+1}', failMode='standalone'))
        
        # Add hosts and connect to switches
        for i in range(4):
            host = self.addHost(f'h{i+1}', 
                              mac=f"00:00:00:00:00:0{i+1}", 
                              ip=f"192.168.1.{i+1}/24")
            self.addLink(host, switches[i])
        
        # Create ring connections between switches
        for i in range(4):
            self.addLink(switches[i], switches[(i+1)%4])

# Topology 2: Hierarchical Tree (ต้นไม้แบบลำดับชั้น)
class HierarchicalTopo(Topo):
    "Hierarchical topology with core, distribution and access layers"
    def build(self):
        # Core layer
        core = self.addSwitch('s1', failMode='standalone')
        
        # Distribution layer
        dist1 = self.addSwitch('s2', failMode='standalone')
        dist2 = self.addSwitch('s3', failMode='standalone')
        
        # Access layer
        access1 = self.addSwitch('s4', failMode='standalone')
        access2 = self.addSwitch('s5', failMode='standalone')
        
        # Connect core to distribution
        self.addLink(core, dist1)
        self.addLink(core, dist2)
        
        # Connect distribution to access
        self.addLink(dist1, access1)
        self.addLink(dist2, access2)
        
        # Add hosts
        h1 = self.addHost('h1', mac="00:00:00:00:00:01", ip="192.168.1.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:00:02", ip="192.168.1.2/24")
        h3 = self.addHost('h3', mac="00:00:00:00:00:03", ip="192.168.1.3/24")
        h4 = self.addHost('h4', mac="00:00:00:00:00:04", ip="192.168.1.4/24")
        
        # Connect hosts to access switches
        self.addLink(h1, access1)
        self.addLink(h2, access1)
        self.addLink(h3, access2)
        self.addLink(h4, access2)

# Topology 3: Mesh Topology (เมช)
class MeshTopo(Topo):
    "Partial mesh topology with 4 switches and 4 hosts"
    def build(self):
        # Add switches
        s1 = self.addSwitch('s1', failMode='standalone')
        s2 = self.addSwitch('s2', failMode='standalone')
        s3 = self.addSwitch('s3', failMode='standalone')
        s4 = self.addSwitch('s4', failMode='standalone')
        
        # Add hosts
        h1 = self.addHost('h1', mac="00:00:00:00:00:01", ip="192.168.1.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:00:02", ip="192.168.1.2/24")
        h3 = self.addHost('h3', mac="00:00:00:00:00:03", ip="192.168.1.3/24")
        h4 = self.addHost('h4', mac="00:00:00:00:00:04", ip="192.168.1.4/24")
        
        # Connect hosts to switches
        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)
        
        # Create mesh connections between switches
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s3, s4)

# Main function to run different topologies
def runTopology(topoClass):
    setLogLevel('info')
    topo = topoClass()
    c1 = RemoteController('c1', ip='127.0.0.1')
    net = Mininet(topo=topo, controller=c1)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    # Uncomment the topology you want to run:
    # runTopology(RingTopo)
    # runTopology(HierarchicalTopo)
    # runTopology(MeshTopo)
    pass
