import paramiko
 
class Switch:
    # Initialize the switch object
    def __init__(self, ip, hostname, model):
        self.ip = ip
        self.hostname = hostname
        self.model = model

    # Describe the switch
    
    def dev_info(self):
        """
        Shows information about the NAD.
        """
        output = (f"Switch mgmt IPv4   : {self.ip}.\n" 
                  f"Sw's hostname      : {self.hostname}.\n"
                  f"Sw's model         : {self.model}.")
        return output

class Router(Switch):
    def dev_info(self):
        output = (f"Router mgmt IPv4:    {self.ip}.\n"
                  f"Router's hostname:   {self.hostname}.\n"
                  f"Router's model:      {self.model}.")
        return output
        
switch_1 = Switch("192.168.1.1", "pesho", "Catalyst")
router_1 = Router("192.1.1.1", "Router1", "ASR")
switch_1.desc = "core switch" # Adding new attr to our object
print("Connect to", switch_1.ip, "with description", switch_1.desc)

print(help(switch_1.dev_info()))
print(router_1.dev_info())
print(switch_1.dev_info())