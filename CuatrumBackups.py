import getpass
import sys
import telnetlib
import time

hostRouters = ["172.4.31.254", "172.4.41.254", "172.4.21.254"]
hostSwitches = ["172.4.38.1","172.4.48.1","172.4.28.1"]

hostNamesRt = ["Guadalajara","Monterrey","Colima"]
hostNamesSw = ["Sw_Guadalajara","Sw_Monterrey","Sw_Colima"]

username = "cisco1"
password = "cisco"

commandsRouters = ["show version", "show running-config", "show access-lists", "show arp", "show cdp neighbors",
                    "show interfaces", "show ip interface brief", "show ip eigrp interfaces", "show ip eigrp neighbors",
                    "show ip nat translations", "show ip route", "show mac-address-table", "show ntp status", "show ip dhcp binding" ]

commandsSwitches = ["show arp", "show cdp neighbors", "show hosts", "show interfaces", "show mac-address-table",
                        "show ntp status", "show port-security", "show running-config", "show sessions",
                        "show spanning-tree", "show version", "show vlan"]

count = 0;

for r in hostRouters:
    print("Accediendo a router ", hostNamesRt[count])
    hostname = hostNamesRt[count] + "#"
    hostnameByte = bytes(hostname, encoding='utf-8')
    tn = telnetlib.Telnet(host=r, port=23, timeout=10)
    tn.read_until(b"Username: ")
    time.sleep(1)
    tn.write(username.encode('ascii') + b"\r\n")
    tn.read_until(b"Password: ")
    time.sleep(1)
    tn.write(password.encode('ascii') + b"\r\n")
    tn.read_until(hostnameByte)
    time.sleep(1)
    tn.write("terminal length 0".encode('ascii') + b"\r\n")
    tn.read_until(hostnameByte)
    time.sleep(1)
    file = open("configRouter"+r+".txt","w+")

    for cr in commandsRouters:
        print("Guardando: ", cr)
        tn.write(cr.encode('ascii') + b"\r\n")
        time.sleep(1)
        x = tn.read_until(hostnameByte)
        time.sleep(5)
        x = str(x.decode('ascii'))
        file.write(x)
        file.write("\n---------------------------------------------------------------------------------------------\n")
        time.sleep(5)

    file.close()
    print("Configuración guardada de router: " + hostNamesRt[count])
    count += 1


count = 0

for s in hostSwitches:
    print("Accediendo a Switch ", hostNamesRt[count])
    hostname = hostNamesSw[count] + "#"
    hostnameByte = bytes(hostname, encoding='utf-8')
    tn = telnetlib.Telnet(host=s, port=23, timeout=10)
    tn.read_until(b"Username: ")
    time.sleep(1)
    tn.write(username.encode('ascii') + b"\r\n")
    tn.read_until(b"Password: ")
    time.sleep(1)
    tn.write(password.encode('ascii') + b"\r\n")
    tn.read_until(hostnameByte)
    time.sleep(1)
    tn.write("terminal length 0".encode('ascii') + b"\r\n")
    tn.read_until(hostnameByte)
    time.sleep(1)
    file = open("configSwitch"+s+".txt","w+")

    for cs in commandsSwitches:
        print("Guardando: ", cs)
        tn.write(cs.encode('ascii') + b"\r\n")
        time.sleep(1)
        x = tn.read_until(hostnameByte)
        time.sleep(5)
        x = str(x.decode('ascii'))
        file.write(x)
        file.write("\n---------------------------------------------------------------------------------------------\n")
        time.sleep(5)

    file.close()
    print("Configuración guardada de switch: " + hostNamesSw[count])
    count += 1

print("Fin")