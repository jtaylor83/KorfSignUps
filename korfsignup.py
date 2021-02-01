#https://github.com/jtaylor83/KorfSignUps/blob/main/korfsignup.py
#for use with https://forms.gle/didNimPz4PpafATD9
#author - James Taylor
import csv
wed = "Wednesday 1-3pm"
thu = "Thursday 3:30-5pm"
fri = "Friday 5-6:30pm"
MAXSIZE_outdoor = 20
MAXSIZE_indoor = 20
wedIndoor = []
wedOutdoor = []
thuIndoor = []
friMorn = []
friEveIndoor = []
friEveOutdoor = []
seen = []
emails = []
names = []

with open("Korfball training sign up.csv") as file:
    reader = csv.reader(file, delimiter=",")
    """
    for row in reader:
        print(row[1],"\n") #prints all data
    """
    
    for row in reader:
        outSession = row[1]
        inSession = row[2]
        firstTeam = row[3]
        name = row[4]
        email = row[5]
        
        #check uniqueness
        if email in seen:
            continue
        else:
            seen.append(email)
            emails.append(email)
            names.append(name)
        
        #allocate friday morning
        if firstTeam == "Yes":
            friMorn.append(name)

        #allocate outdoor sessions
        #allocate wed afternoon
        if outSession == wed and (len(wedOutdoor) < MAXSIZE_outdoor):
            wedOutdoor.append(name)
            
        #allocate fri eve
        elif outSession == fri and (len(friEveOutdoor) < MAXSIZE_outdoor):
            friEveOutdoor.append(name)
            
        #allocate if both
        elif outSession == (wed +";"+ fri): 
            if len(wedOutdoor) < MAXSIZE_outdoor and len(wedOutdoor) < len(friEveOutdoor):
                wedOutdoor.append(name)
            elif len(friEveOutdoor) < MAXSIZE_outdoor:
                friEveOutdoor.append(name)

                
        #allocate indoor sessions
        #allocate wed afternoon
        if inSession == wed and (len(wedIndoor) < MAXSIZE_indoor) and not (name in wedOutdoor):
            wedIndoor.append(row[4])
            
        #allocate fri eve
        elif inSession == fri and (len(wedIndoor) < MAXSIZE_indoor) and not (name in friEveOutdoor):
            friEveIndoor.append(name)
            
        #allocate thu eve
        elif inSession == thu and (len(thuIndoor) < MAXSIZE_indoor):
            thuIndoor.append(name)
            
        #if wed and fri
        elif inSession == (wed+";"+fri): 
            if len(wedIndoor) < MAXSIZE_indoor and len(wedIndoor) <= len(friEveIndoor):
                if not (name in wedOutdoor):
                    wedIndoor.append(name)
                elif len(friEveIndoor) < MAXSIZE_indoor:
                    friEveIndoor.append(name)
                    
            elif len(friEveIndoor) < MAXSIZE_indoor:
                if not (name in friEveOutdoor):
                    friEveIndoor.append(name)
                elif len(wedIndoor) < MAXSIZE_indoor:
                    wedIndoor.append(name)
                    
        #if wed and thu
        elif inSession == (wed+";"+thu): 
            if len(wedIndoor) < MAXSIZE_indoor and len(wedIndoor) <= len(thuIndoor):
                if not (name in wedOutdoor):
                    wedIndoor.append(name)
                elif len(thuIndoor) < MAXSIZE_indoor:
                    thuIndoor.append(name)
            elif len(thuIndoor) < MAXSIZE_indoor:
                thuIndoor.append(name)
                
        #if thu and fri
        elif inSession == (thu+";"+fri):
            if len(thuIndoor) < MAXSIZE_indoor and len(thuIndoor) <= len(friEveIndoor):
                thuIndoor.append(name)
            elif len(friEveIndoor) < MAXSIZE_indoor:
                if not (name in friEveOutdoor):
                    friEveIndoor.append(name)
                elif len(thuIndoor) < MAXSIZE_indoor:
                    thuIndoor.append(name)
                    
        #if all three
        elif inSession == (wed+";"+thu+";"+fri):
            if len(wedIndoor) < MAXSIZE_indoor and len(wedIndoor) <= len(thuIndoor) and len(wedIndoor) <= len(friEveIndoor):
                if not (name in wedOutdoor):
                    wedIndoor.append(name)
                elif len(thuIndoor) < MAXSIZE_indoor:
                    thuIndoor.append(name)
            elif len(thuIndoor) < MAXSIZE_indoor and len(thuIndoor) <= len(wedIndoor) and len(thuIndoor) <= len(friEveIndoor):
                thuIndoor.append(name)
            elif len(friEveIndoor) < MAXSIZE_indoor and len(friEveIndoor) <= len(thuIndoor) and len(friEveIndoor) <= len(wedIndoor):
                if not (name in friEveOutdoor):
                    friEveIndoor.append(name)
                elif len(thuIndoor) < MAXSIZE_indoor:
                    thuIndoor.append(name)
            


print("\nWednesday outdoor\n",wedOutdoor)
print("\nFriday outdoor\n",friEveOutdoor)
num = len(wedOutdoor)+ len(friEveOutdoor)
print(num)

print("\nWednesday Indoor\n",wedIndoor)
print("\nThursday Indoor\n",thuIndoor)
print("\nFriday Indoor\n",friEveIndoor)
num = len(wedIndoor) + len(thuIndoor) + len(friEveIndoor)
print(num)

print("\n\n\n")
for name in names:
    if name in list(set().union(wedOutdoor,friEveOutdoor)):
        if name not in list(set().union(wedIndoor,thuIndoor,friEveIndoor)):
            print(name,"got no indoor sessions")
    if name in list(set().union(wedIndoor,thuIndoor,friEveIndoor)):
        if name not in list(set().union(wedOutdoor,friEveOutdoor)):
            print(name,"got no outdoor sessions")
    if name not in list(set().union(wedOutdoor,friEveOutdoor,wedIndoor,thuIndoor,friEveIndoor)):
        print(name,"got nothing :(((")    
        

            
with open("WednesdayOutdoor.csv","w") as file:
        writer = csv.writer(file)
        for row in wedOutdoor:
            file.write(row)
            file.write("\n")
file.close()
            
with open("FridayOutdoor.csv","w") as file:
        writer = csv.writer(file)
        for row in friEveOutdoor:
            file.write(row)
            file.write("\n")
file.close()           
with open("WednesdayIndoor.csv","w") as file:
        writer = csv.writer(file)
        for row in wedIndoor:
            file.write(row)
            file.write("\n")
file.close()
with open("ThursdayIndoor.csv","w") as file:
        writer = csv.writer(file)
        for row in thuIndoor:
            file.write(row)
            file.write("\n")
file.close()
            
with open("FridayIndoor.csv","w") as file:
        writer = csv.writer(file)
        for row in friEveIndoor:
            file.write(row)
            file.write("\n")
file.close()

with open("Emails.csv","w") as file:
    writer = csv.writer(file)
    for i in range(len(emails)):
        file.write(emails[i])
        file.write("\n")
file.close()      

with open("Names.csv","w") as file:
    writer = csv.writer(file)
    for name in names:
          file.write(name)
          file.write("\n")
file.close()

with open("FridayMorning.csv","w") as file:
    writer = csv.writer(file)
    for name in friMorn:
        file.write(name)
        file.write("\n")

        
            
                    
        
