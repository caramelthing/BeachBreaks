#Surfing wales advise
#def a functin which when called and passed an argument from input will open then read the text file then loo through digging ""==" out:

def surf_spots(my_location):
    with open("beach_break.txt") as f:
        f = f.splitlines()

county = input("enter gower: ")
with open("surf_wales.txt") as f: #get it and open it
    show_arp = f.read()         #read it and assign it

print()
for line in show_arp.splitlines(): #makes the string into a list of lines,
    fields = line.split() #makes the line element into a list of words
    print(fields)
    '''
    county = fields[0] #assigns the index 0 element of each line into variable county
    area = fields[1] #assigns the index 1 element of each line into variable area
    wave = fields[2] #assigns the index 2 element of each line into wave
    level = fields[3] #assigns the index 3 element of each line into level
    #gotta take the input and use it 
    if county == "gower":
        print("Default gateway IP/Mac is: {}/{}".format(county, area)) # string format to print the above 2 variables
print()'''

my_location = input("Where are you currently? ")
print((surf_spots(my_location)))