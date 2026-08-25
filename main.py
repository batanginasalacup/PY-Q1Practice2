from pyscript import display

x = "Year" #string
y = 2025 #integer
z = 3.14
a = True #boolean
b = ['mama', 'mo', 'blue'] #list
c = (6,7,11) #tuple
d = {6,7,11} #set
e = {'sapphire', 'sapphire', 'sapphire'} #set with string
f = {
    "name" : "Mateo",
    "age" : 15,
    "description" : "fat"
}

display('The data type of x is', type(x), target="div1") #display output in div
display(type(y), target="div1") 
display(type(z), target="div1")
display(type(a), target="div1")
display(type(b), target="div1")
display(type(c), target="div1")
display(type(d), target="div1")
display(type(e), target="div1")
display(type(f), target="div1")
display(f["name"], f["description"])
 
