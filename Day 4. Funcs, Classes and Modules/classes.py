class Switch:
    # Initialize the switch object
    def __init__(self, ip, hostname, model):
        self.ip = ip
        self.hostname = hostname
        self.model = model
    
    

    # Describe the switch
    def dev_info(self):
        print(f"Device IPv4   : {self.ip}.")
        print(f"Hostname      : {self.hostname}.")
        print(f"Model         : {self.model}.")

switch_1 = Switch("192.168.1.1", "pesho", "Catalyst")
switch_1.desc = "core switch" # Adding new attr to our object
print("Connect to", switch_1.ip, "with description", switch_1.desc)
switch_1.dev_info()