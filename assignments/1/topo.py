from mininet.net import Containernet
from mininet.node import RemoteController, Docker, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Link

def topology():

    "Create a network with some docker containers acting as hosts."

    net = Containernet(controller=RemoteController)

    info('*** Adding switch\n')
    r1 = net.addDocker('r1', ip='172.30.1.1/24', dimage="knet/urouter:1.4")
    r2 = net.addDocker('r2', ip='172.30.2.1/24', dimage="knet/urouter:1.4")
    r3 = net.addDocker('r3', ip='172.30.3.1/24', dimage="knet/urouter:1.4")
    h1 = net.addDocker('h1', ip='172.30.1.2/24', defaultRoute='via 172.30.1.1' , dimage="knet/host-ubuntu:1-2")
    h2 = net.addDocker('h2', ip='172.30.2.2/24', defaultRoute='via 172.30.2.1' ,dimage="knet/host-ubuntu:1-2")
    h3 = net.addDocker('h3', ip='172.30.3.2/24', defaultRoute='via 172.30.3.1' ,dimage="knet/host-ubuntu:1-2")
    

    s3 = net.addSwitch('s3', failMode='standalone')
    s4 = net.addSwitch('s4', failMode='standalone')

    info('*** Creating links\n')

    net.addLink(h1, r1)
    net.addLink(h2, r2)
    net.addLink(h3, r3)

    net.addLink(r1, s3, params1={"ip": "10.10.10.1/24"})
    net.addLink(r2, s3, params1={"ip": "10.10.10.2/24"})
    net.addLink(r3, s4, params1={"ip": "10.20.20.2/24"})
    net.addLink(r2, s4, params1={"ip": "10.20.20.1/24"})

    info('*** Starting network\n')
    net.start()

    #copy the bird config files
    s3.cmd("sudo docker cp r1.conf mn.r1:/etc/bird.conf")
    s3.cmd("sudo docker cp r2.conf mn.r2:/etc/bird.conf")
    s3.cmd("sudo docker cp r3.conf mn.r3:/etc/bird.conf")
    s4.cmd("sudo docker cp r1.conf mn.r1:/etc/bird.conf")
    s4.cmd("sudo docker cp r2.conf mn.r2:/etc/bird.conf")
    s4.cmd("sudo docker cp r3.conf mn.r3:/etc/bird.conf")
    r1.cmd("bird -c /etc/bird.conf")
    r2.cmd("bird -c /etc/bird.conf")
    r3.cmd("bird -c /etc/bird.conf")

    info('*** Running CLI\n')
    CLI(net)
    info('*** Stopping network')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
