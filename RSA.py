import random

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
#print(gcd(288,55))

def gcdinv(a, m) :
    a = a % m;
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1* x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

def e_gcd(tpq,e):
    if(gcd(tpq,e)==1):
        print("El número",e,"SI es coprimo con tpq")
    else:
        print("El número",e,"NO es coprimo con tpq")

def generate_keypair(p,q):
    n = p*q
    phi = (p-1)*(q-1)
    e = random.randrange(p, phi)

    coprime = gcd(e, phi)
    while coprime != 1:
        e = random.randrange(p, phi)
        coprime = gcd(e, phi)

    d = multiplicative_inverse(e, phi)
    print("Your public key: ", e,n)
    print("Your private key: ", d,n)
    return ((e , n), (d, n))


def powermod(x, y, p) :
    res = 1     # Initialize result

    # Update x if it is more
    # than or equal to p
    x = x % p

    while (y > 0) :

        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = (res * x) % p

        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p

    return res

def RSAencrypt(message, n, e):
    m = powermod(message, e, n)
    return m

def RSAdecrypt(message, n, d):
    m = powermod(message, d, n)
    return m

def RSAencmsg(message,n,e):
    ciphertext = []
    crypt_text = ''
    block = []
    ciphertext = [ord(i) for i in message]
    if ((len(message)%2) != 0):
        ciphertext.append(32)
    for i in range(len(ciphertext)-1):
        ciph_block = (ciphertext[i]*255)+ciphertext[i+1]
        block.append(ciph_block)
    for i in range(0,len(block),2):
        crypt_text += str(RSAencrypt(block[i],n,e))
        if (i != len(block)-1):
            crypt_text += " "
    print("Your encrypted message is: "+crypt_text)
    return crypt_text

def RSAdecmsg(msg,n,d):
    ms = msg.split(" ")
    for i in range(len(ms)):
        ms[i] = int(ms[i])
    text_int = []
    text = ''
    ciphertext = []
    for i in range(len(ms)):
        text_int.append(RSAdecrypt(ms[i],n,d))
        ciphertext.append(text_int[i]//255)
        ciphertext.append(text_int[i]%255)
    for i in range(len(ciphertext)):
        text += chr(ciphertext[i])
    print("Your decrypted config is: "+text)
    return text

p = 245563 #número primo
q = 249779 #número primo
#n = p*q #
n = 1093886025229
#print(n)
tpq = (p-1)*(q-1) #t(n)
#print("tpq es: ",tpq)
e = 898261513829
#print(e)    #coprimo con tpq gcd(55,288) = 1
#e_gcd(tpq,e) #checar si e es coprimo con tpq
#d = multiplicative_inverse(e,tpq)
d = 566270290349
print("d es: ",d)
#d = 37701935879
#print(gcdinv(299,1032))
#RSAmsg(ciphertext)
#msg = [899,642,95,43,788,527,116,642,218,118,62]
#n = 1007
#RSAdecmsg(msg,n,d)
#RSAencmsg("Que pedo",1007,335)
#print(ord("ÿ"))
#print(RSAencrypt(32,1007,335))
#RSAencmsg("Jj324%6597",75023099,75021101)
#RSAdecmsg([44299380,3158162,70264134,43972784,63348950],75023099,14688725)
R1 = """hostname Manzanillo
no ip domain-lookup

ip domain-name example.com
Crypto key generate rsa

1024

ip ssh version 2

enable secret 5 $1$mERr$hx5rVt7rPNoS4wqbXKX7m0
enable password 7 0822455D0A16

username cisco privilege 5 secret 5 $1$mERr$hx5rVt7rPNoS4wqbXKX7m0
Line console 0
Login local
username cisco1 privilege 15 secret 5 $1$mERr$hx5rVt7rPNoS4wqbXKX7m0
Line console 0
Login local

Logging on
Logging buffered 4096
Logging 172.4.31.1

Ntp server 10.40.72.254

lldp run
cdp run
spanning-tree mode pvst

interface GigabitEthernet0/0
No shutdown
No IP address

interface GigabitEthernet0/0.11
description usuarios1_Manzanillo
encapsulation dot1Q 11
ip address 172.4.11.254 255.255.255.0
ip helper-address 172.4.0.1
ip nat inside
No shutdown

interface GigabitEthernet0/0.12
description usuarios2_Manzanillo
encapsulation dot1Q 12
ip address 172.4.12.254 255.255.255.0
ip helper-address 172.4.0.1
ip nat inside
No shutdown

interface GigabitEthernet0/0.14
description vlan 14 l2l Manzanillo_Colima
encapsulation dot1Q 14
ip address 192.168.0.1 255.255.255.248
No shutdown

interface GigabitEthernet0/0.18
description admin switches_Manzanillo
encapsulation dot1Q 18
ip address 172.4.18.254 255.255.255.0
No shutdown



ip route 0.0.0.0 0.0.0.0 GigabitEthernet0/0.14

Router rip
Network 192.168.0.0
Version 2
Network 172.4.0.0
no auto-summary



access-list 1 remark ACL nat
access-list 1 permit 172.4.11.0 0.0.0.255
access-list 1 permit 172.4.12.0 0.0.0.255



banner motd *

##################################################

 Unauthorized access to this device is prohibited

##################################################

 $$$b  `---.__
  "$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$"              .
     "$b          -'            `-.-'            $$$"              .'|
       ".                                       d$"             _.'  |
         `.   /                              ..."             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `"--'             |    `-.     \
        :##.       ==             .###.       `.      `.    `\
        |##:                      :###:        |        >     >
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
          /`-.                                  `.  /   /
         :    `-  ...........,                   | /  .'
         |         ``:::::::'       .            |<    `.
         |             ```          |           x| \ `.:``.
         |                         .'    /'   xXX|  `:`M`M':.
         |    |                    ;    /:' xXXX'|  -'MMMMM:'
         `.  .'                   :    /:'       |-'MMMM.-'
          |  |                   .'   /'        .'MMM.-'
          `'`'                   :  ,'          |MMM<
            |                     `'            |tbap\
             \                                  :MM.-'
              \                 |              .''
               \.               `.            /
                /     .:::::::.. :           /
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .'
                                   `:.:'

*

line con 0
login local
exec-timeout 5 0

line vty 0 4
exec-timeout 5 0
login local

line vty 5 15
exec-timeout 5 0
login local"""




r = RSAencmsg(R1,n,e)
RSAdecmsg(r,n,d)
#print("your Keys are: ",generate_keypair(249827, 249427))
print(" ")
print("1) Encrypt message")
print("2) Decrypt message")
print("3) Generate keys")
print("4) Main menu")
print("5) Exit")
op = input("What do you want to do: ")
while (op != "5"):
    if (op == "1"):
        m = input("Enter your message: ")
        n = input("Enter n ")
        e = input("Enter e ")
        RSAencmsg(m,int(n),int(e))
        op = "4"
    elif (op == "2"):
        m = input("Enter your message: ")
        n = input("Enter n ")
        d = input("Enter d ")
        RSAdecmsg(m,int(n),int(d))
        op = "4"
    elif (op == "3"):
        p = input("Enter your p ")
        q = input("Enter your q ")
        generate_keypair(int(p),int(q))
        op = "4"
    elif (op == "4"):
        print(" ")
        print("1) Encrypt message")
        print("2) Decrypt message")
        print("3) Main menu")
        print("4) Exit")
        op = input("What do you want to do: ")
    elif (op == "5"):
        break
    else:
        op = "5"
