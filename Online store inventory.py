item_names = ['Laptop', 'Headphones', 'Keyboard', 'Mouse']
item_quantities = [10, 20, 15, 30]
item_prices=[1000,500,200,100]
cart=[]

def display_inventory():
	print("CURRENT INVENTORY")
	for i in range(len(item_names)):
		print(f"{i+1}.We have {item_names[i]}.......Quantity of it.is {item_quantities[i]}...price of each item is.{item_prices[i]}")
		

def add_item():
	new_item=input("Enter new item:              ")
	new_quantity=int(input("Enter the product quantity:     "))
	new_price=int(input("Enter the product price"))
	
	
	item_names.append(new_item)
	item_quantities.append(new_quantity)
	item_prices.append(new_price)
	print("Your item information has been added to the inventory")




def  remove_item():
	display_inventory()
	
	remove_item=input("Enter the name of item:   ")
	
	if remove_item in item_names:
		a=item_names.index(remove_item)
		item_names.pop(a)
		item_quantities.pop(a)
		item_prices.pop(a)
	
		
		print(f"{remove_item} has been removed")
		
	else:
		print(f"{remove_item} is not found in our inventory")
		
		

def update_item():
	 display_inventory()
	 item_to_update=input("Enter the item name you want to update:     ")
	 if item_to_update in item_names:
	 	index=item_names.index(item_to_update)
	 	new_quantity=int(input("Enter your new quantity"))
	 	item_quantities[index]=new_quantity
	 	print(f"{item_to_update} has been updated to{new_quantity}")
	 else:
	 	print(f"{item_to_update} is not found in inventory")
	 	
	 	
	 	
def  add_to_cart():
	 	display_inventory()
	 	add_item_name = input("Enter the name of the item you want to add: ")
	 	
	 	
	 	if add_item_name in item_names:
	 	     index=item_names.index(add_item_name)
	 	     add_quantity=int(input("Enter the quantity"))
	 	     
	 	
	 	 
	 	     if add_quantity<=item_quantities[index]:
	 	     	cart.append((add_item_name,add_quantity))
	 	     	print(f"{add_item_name} and {add_quantity} is added to your cart")
	 	     else:
	 	     	print("Insufficient quantity in inventory")
	 	else:
	 	     	print(f"{add_item_name} is not in inventory")
		      	
	 	     	

def view_cart():
        print("YOUR CART:   ")
        for item,quantity in cart:
        	print(f"{item}:{quantity}")	 	     
        
  
def  checkout():
	 		  sum=0
	 		  for item,quantity in cart:
	 		  	index=item_names.index(item)
	 		  	item_quantities[index]-=quantity
	 		  	
	 		  	sum+=quantity*item_prices[index]
	 		  print(f"The total amount of your item is:        {sum}")
	 		 
	 	

while True:
    print("\nMenu:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Update Item")
    print("5. Add to Cart")
    print("6. View Cart")
    print("7. Checkout")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        display_inventory()
    elif choice == '2':
        add_item()
    elif choice == '3':
        remove_item()
    elif choice == '4':
        update_item()
    elif choice == '5':
        add_to_cart()
    elif choice == '6':
        view_cart()
    elif choice == '7':
        checkout()
    elif choice == '8':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 8.")