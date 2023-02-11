#instantiates class named Shoe that takes in the arguments country, code, product, cost and quantity for a shoe
#defines the methods: __str__, get_cost to extract the cost argument of the object, and get_quantity to extract the quantity argument of the object
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country 
        self.code = code 
        self.product = product 
        self.cost = cost 
        self.quantity = quantity 
        
        
    def __str__(self):
        return f"Country: {self.country} \nCode: {self.code} \nProduct: {self.product} \nCost: {self.cost} \nQuanity: {self.quantity}"
        
    def get_cost(self):
        return f"Cost: {self.cost}"
        
    def get_quantity(self):
        return f"Quantity: {self.quantity}"
        
#creates an empty list to store all shoe objects        
shoe_list = []
        
#defines read_shoes_data which opens up the inventory text file and reads through all lines. each line is split up into the different details about the shoe object and creates an object for each line in the text file. It also prints out the date for all objects in the shoe_list
def read_shoes_data():
    f = open('inventory.txt', 'r')
    fl = f.readlines()    
    counter = 0
    
    for line in fl:
        counter+=1
        parts = line.split(",")
        
        country = parts[0]
        code = parts[1]
        product = parts[2]
        cost = parts[3]
        quantity = parts[4].strip("\n")
        
        shoe_object = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe_object)
        print(f"***********Product number {counter} : ****************")
        print(shoe_object)
     
#defines capture_shoes which adds a new shoe to the shoe_list and to the text file but getting a user input of all necessary arguments to create a shoe object
def capture_shoes():
    print("Enter the following details of the shoe you would like to add. \n")
    country = input("Country: \n")   
    code = input("Code\n")
    product = input("Product name: \n")
    cost = input("Cost: \n")
    quantity = input("Quantity: \n")
    
    shoe_object = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe_object)
    print("Shoe added successfully!")
    f = open('inventory.txt', 'a')
    l = f"\n{country},{code},{product},{cost},{quantity}"
    f.write(l)   
    
#defines view_all which reads through inventory text file and prints the details of each object in the list    
def view_all():
    f = open('inventory.txt', 'r')
    fl = f.readlines()
    counter = 0
    
    for line in fl:
        counter+=1
        parts = line.split(",")
        
        country = parts[0]
        code = parts[1]
        product = parts[2]
        cost = parts[3]
        quantity = parts[4].strip("\n")
        
        shoe_object = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe_object)
    for obj in shoe_list:
        print(obj)
        print("*******************************")
    
#defines re_stock which reads the inventory text file and finds the object with the lowest quantity which is need of a restock. the user input takes inn the new desired quantity and rewrites this on the text file.    
def re_stock():
    with open('inventory.txt', 'r') as f:
        data = f.readlines()
        quantity_list = []
        shoes = []
            
        for line in data:
            parts = line.split(",")
            quantity = int(parts[4].strip("\n"))
            quantity_list.append(quantity)
        
        lowest_q_index = quantity_list.index(min(quantity_list))
        lowest_parts = data[lowest_q_index].split(",")
        print(f"{lowest_parts[2]} Quantity: {min(quantity_list)}. \n{lowest_parts[2]} must be restocked.")
        restock_num = int(input(f"How many units of {lowest_parts[2]} would you like to add to the existing quantity?"))
        restock_total = int(restock_num + min(quantity_list))
        print(f"Updated! The new quantity of {lowest_parts[2]} is {restock_total}")
        
        for line in data:
            parts = line.split(",")
            if parts[4].strip("\n") == str(min(quantity_list)):
                parts[4] = f"{restock_total}\n"
            shoes.append(",".join(parts))
            
    with open('inventory.txt', 'w') as f:
        f.writelines('')
        new = ("".join(shoes))
        f.write(new)

#defines search_shoe which takes in the code from a user input and prints out the details of the shoe which has that code. if no shoe has that code, error handling prevents an error message    
def search_shoe():
    while True:
        shoe_code = input("To search for shoe, enter shoe code here: \n")
        found = False 
        
        for obj in shoe_list:
            if shoe_code == obj.code:
                found = True
                print("Product found! Product details: \n")
                print(obj)
                
            else:
                continue 
        if found == False:
            print("Product not found. Please try again" )
        else:
            break
        
#defines value_per_item which reads through the inventory text file and extracts the name and code of each item, as well as its value by dividing the total cost by the quanity of each item
def value_per_item():
    f = open('inventory.txt', 'r+')
    fl = f.readlines()

    cost_list = []
    quantity_list = []
    counter = 0
    
    for line in fl:
        parts = line.split(",")
        counter +=1
        
        cost = int(parts[3])
        cost_list.append(cost)    
        quantity = int(parts[4].strip("\n"))
        quantity_list.append(quantity)
        
        value = cost / quantity
        print(f"***********Product number {counter} : ****************")
        print(f"{parts[2]} - Code: {parts[1]} \nValue per item: £{value}")
        

#defines highest_qty which reads the inventory text file, finds the line with the highest quantity and prints out the details of the object, as well as listing it for sale        
def highest_qty():        
    f = open('inventory.txt', 'r+')
    fl = f.readlines()
    
    quantity_list = []
    counter = 0
    
    for line in fl:
        parts = line.split(",")
        counter +=1
        
        
        quantity = int(parts[4].strip("\n"))
        quantity_list.append(quantity)
        
        
    highest_q_index = quantity_list.index(max(quantity_list))
    highest_parts = fl[highest_q_index].split(",")
    print(f"{highest_parts[2]} Quantity: {max(quantity_list)}. \n{highest_parts[2]} is FOR SALE.")
    f.close()
        
        
        
        

            
            
            
            
            
            
#displays user menu, which triggers constituent functions            
user_choice = ""

while user_choice != "quit":
    user_choice = input("""USER MENU:
    
    r = read shoes data from inventory
    a = add a shoe to inventory
    va = view all shoes data
    rs = restock the shoe of lowest quantity
    s = search for a shoe via shoe code
    ve = show value of each shoe
    sa = check which shoe is for sale
    q = quit
    
    
    """).lower()
    
    if user_choice == "r":
        read_shoes_data()
        
    if user_choice == "a":
        capture_shoes()
        
    if user_choice == "va":
        view_all()
        
    if user_choice == "rs":
        re_stock()
        
    if user_choice == "s":
        search_shoe()
        
    if user_choice == "ve":
        value_per_item()
        
    if user_choice == "sa":
        highest_qty()
        
    if user_choice == "q":
        print("Goodbye!")
        break
        
