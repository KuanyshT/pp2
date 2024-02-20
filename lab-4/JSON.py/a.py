import json

with open("jsfile.json") as file:
    pydata = json.load(file)
    
print("="*142)

pd = pydata["imdata"]
print("DN","                                                  ", "Speed", "              ", "MTU")
print('-'*142)
for i in range(len(pd)):
    print(pd[i]["l1PhysIf"]["attributes"]["dn"],"          " , pd[i]["l1PhysIf"]["attributes"]["speed"], "            ", pd[i]["l1PhysIf"]["attributes"]["mtu"])
        
