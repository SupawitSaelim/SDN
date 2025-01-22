# Load Balancing with OpenFlow Groups - Practice Lab

## Overview
ในแลปนี้ คุณจะได้เรียนรู้เกี่ยวกับการทำ Load Balancing โดยใช้ OpenFlow Group Tables บนเครือข่ายที่มี switches 4 ตัวและ hosts 2 ตัว

## เริ่มต้น Lab

### ส่วนที่ 1: Network Topology
คุณได้รับโค้ดพื้นฐานสำหรับสร้าง topology ดังนี้:
```python
class SingleSwitchTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1', protocols='OpenFlow13')
        s2 = self.addSwitch('s2', protocols='OpenFlow13')
        s3 = self.addSwitch('s3', protocols='OpenFlow13')
        s4 = self.addSwitch('s4', protocols='OpenFlow13')
        
        h1 = self.addHost('h1', mac="00:00:00:00:00:01", ip="192.168.1.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:00:02", ip="192.168.1.2/24")
        
        self.addLink(s1,h1,1,1)
        self.addLink(s1,s2,2,1)
        self.addLink(s1,s3,3,1)
        self.addLink(s2,s4,4,2)
        self.addLink(s3,s4,4,3)
        self.addLink(s4,h2,1,1)
```

### ส่วนที่ 2: การกำหนดค่า Group Tables
จากข้อมูล Group Tables ที่กำหนดให้:

Switch s1 (dpid: 1):
- Group ID: 51
- Type: SELECT
- Bucket 1: weight 40, output port 2
- Bucket 2: weight 60, output port 3

Switch s4 (dpid: 4):
- Group ID: 50
- Type: SELECT
- Bucket 1: weight 70, output port 2
- Bucket 2: weight 30, output port 3

## คำถามและงานที่ต้องทำ

1. จากโครงสร้าง topology ที่ให้มา:
   - วาดไดอะแกรมแสดงการเชื่อมต่อระหว่าง switches และ hosts
   - ระบุ port number ที่ใช้ในแต่ละการเชื่อมต่อ
   - อธิบายเส้นทางที่เป็นไปได้ระหว่าง h1 ไป h2

2. การกำหนดค่า Group Tables:
   - แปลง Group Table configuration เป็นคำสั่ง ovs-ofctl ที่เหมาะสม
   - อธิบายความหมายของ weight ในแต่ละ bucket

3. การทดสอบ:
   - เขียนขั้นตอนการทดสอบว่า traffic ถูกแบ่งตาม weight ที่กำหนดหรือไม่
   - ระบุคำสั่งที่ใช้ในการ monitor traffic distribution
   - เสนอวิธีการคำนวณ % การกระจาย traffic

4. การวิเคราะห์:
   - จากค่า weight ที่กำหนด สัดส่วนการแบ่ง traffic ที่คาดหวังควรเป็นเท่าไร
   - ในกรณีที่ผลลัพธ์ไม่เป็นไปตามที่คาดหวัง อะไรอาจเป็นสาเหตุที่เป็นไปได้
   - เสนอวิธีการปรับปรุงประสิทธิภาพของ load balancing

## Tips
- ใช้คำสั่ง `ovs-ofctl -O OpenFlow13 dump-groups` เพื่อตรวจสอบการตั้งค่า
- ใช้ iperf ในการสร้าง traffic ระหว่าง hosts
- ใช้คำสั่ง `ovs-ofctl -O OpenFlow13 dump-group-stats` เพื่อดูสถิติของ group

## ส่งงาน
1. ไดอะแกรมแสดง topology พร้อมหมายเลข port
2. คำสั่งที่ใช้ในการกำหนดค่า Group Tables
3. ผลการทดสอบและการวิเคราะห์การกระจาย traffic
4. ข้อเสนอแนะในการปรับปรุงประสิทธิภาพ

Good luck! 🚀