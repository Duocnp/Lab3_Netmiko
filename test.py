# import netmiko : Import cả thư viện
from netmiko import ConnectHandler # import thư viện nhỏ
#dictionary , object
Router = {
"device_type": "cisco_ios" ,
"ip": "10.18.8.150",    #nhập IP
"username": "vnpro",
"password": "vnpro#123", 
"secret" : "vnpro#321" #password enable
}

#user, privileges, config
connect=ConnectHandler(**Router) #unpack
print("OK")
#hàm Send_command
a=ConnectHandler(**Router).send_command("show ip interface brief")


for i in range(1,4) :
    print(connect.send_config_set(["int e0/"+ str(i),"ip add 1.2."+str(i) +".1 255.255.255.0", "no shut"])) 
print(a)

interface = {
    "e0/1":"192.168.1.1",
    "e0/2":"192.168.2.2",
    "e0/3":"192.168.3.3"
}
for i in interface:
    print(connect.send_config_set(["int "+ i,"ip addr " + interface[i]+ " 255.255.255.0", "no shut" ]))

#send_command 
print(connect.send_command("show ip int br")) #lenh day du hoac viet tat

#disconnect
connect.disconnect()