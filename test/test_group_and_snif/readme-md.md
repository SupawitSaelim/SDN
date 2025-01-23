# LAB: OpenFlow Load Balancing with Static ARP

## Overview
สร้าง Load Balancing โดยใช้ OpenFlow 1.3 แบบ Static ARP ด้วย Ryu Controller

## Network Topology
```
       h1
       |
       s1
     /    \
   s2      s3
  /  \    /
h3    s4
       |
       h2
```

## Network Configuration
- h1: mac="00:00:00:00:00:01", ip="192.168.1.1/24"
- h2: mac="00:00:00:00:00:02", ip="192.168.1.2/24"
- h3: mac="00:00:00:00:00:03", ip="192.168.1.3/24"

## Tasks
1. สร้าง Topology ด้วย Python code โดยใช้ Mininet Python API

2. สร้าง Static ARP entries บน h1, h2 และ h3

3. สร้าง Ryu application ที่มี features:
   - Group table แบบ Select และ All
   - Static Flow entries
   - REST API support (ryu.app.ofctl_rest)

4. ให้ได้ผลลัพธ์ดังนี้:
   - Switch s1: Load balance traffic จาก h1 ด้วย ratio 70:30 
   - Switch s2: Packet sniffer สำหรับ monitoring traffic 
   - Switch s4: Load balance traffic ด้วย ratio 50:50

5. ทดสอบด้วยคำสั่ง:
   - iperf ระหว่าง h1 และ h2  
   - ใช้คำสั่ง ovs-ofctl dump-flows และ dump-group-stats เพื่อดูการกระจาย traffic
