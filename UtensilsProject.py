import csv

# Function that read the files

def open_files(csvfile):
    with open(csvfile, 'r',newline='') as file :
        the_list = []
        contents = csv.DictReader(file)
        for item in contents :
            the_list.append(item)
    return the_list


orders = open_files('/Users/Iacopoalessandropedde/Desktop/python/My-mini-project/Week3/orders.csv')
couriers = open_files('/Users/Iacopoalessandropedde/Desktop/python/My-mini-project/Week3/couriers.csv')
utensils = open_files('/Users/Iacopoalessandropedde/Desktop/python/My-mini-project/Week3/products.csv')


order_statuses = ["preparing", "shipped", "delivered", "cancelled"]

# write products list to products.csv
def save_products() :
    
    with open('/Users/Iacopoalessandropedde/Desktop/python/My-mini-project/Week3/products.csv','w',newline='') as products_file :
        fieldnames = ['index','name','price']
        writer = csv.DictWriter(products_file,fieldnames=fieldnames)
        writer.writeheader()
        for item in utensils :
            writer.writerow(item)
        
        print('Lists have been saved.')

# write couriers list to couriers.csv
def save_couriers() :
    
    with open('/Users/Iacopoalessandropedde/Desktop/python/My-mini-project/Week3/couriers.csv','w',newline='') as couriers_file :
        fieldnames = ['name','phone']
        writer = csv.DictWriter(couriers_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in couriers :
            writer.writerow(item)
        
        print('Lists have been saved.')

# write orders list to orders.csv
def save_orders() :
    
    with open('/Users/Iacopoalessandropedde/Desktop/python/My-mini-project/Week3/orders.csv','w',newline='') as orders_file :
        fieldnames = ['customer_name','customer_address',
                     'customer_phone','courier','status','item']
        writer = csv.DictWriter(orders_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in orders :
            writer.writerow(item)
        
        print('Lists have been saved.')
    

def list_print(the_list) :
    
    for product in the_list :
        print(product)

def print_list_index(the_list) :
    for indi, product_new in enumerate(the_list) :
        print(f'Select {indi} for {product_new}')
        
def dict_index(the_dict) :
    for key , value in enumerate(the_dict):
        print(f'Select {key} for {value}')

def index_status(the_list) :
    for indi, status in enumerate(the_list) :
        print(f'Press {indi} to change to {status} status')



# while true keep regardless as no condition 

while True :

    option = int(input('SELECT :\n 0 for Save lists and Exit  \n 1 for Products menu \n 2 for Couriers menu  \n 3 for Orders menu\n'))


    if option == 0 :

        save_couriers()
        save_orders()
        save_products()
        print('EXIT the application')
        exit()

    elif option == 1 :
        while True :
            menu_option = int(input("SELECT :\n 0 - EXIT to Main Menu \n 1 - Products List \n 2 - New Product \n 3 - UPDATE Existing Product \n 4 - Delete Product\n"))
        # if 0 exit to main menu 
            if  menu_option == 0 :

                break

        # if 1 print product list

            elif menu_option == 1 :

                print('Here is our products:')
                list_print(utensils)
                break

        # if 2 create new product

            elif menu_option == 2 :

                new_name = input('Please enter the new product name:\n')
                new_price = float(input('Please enter the new product price:\n'))
                utensils.append({'name': new_name, 'price':new_price})         
                print(utensils)
                save_products()
                break
                
        # if 3 update existing product
        
            elif menu_option == 3 :
            
                print(dict_index(utensils))
                
                operator_index = int(input("Please enter the index to UPDATE:\n"))
                
                if 0 <= operator_index < len(utensils) :
                    utensil_index = utensils[operator_index]
                    for key in ['name','price'] :
                        user_input =  input(f"Enter new value for {key} (enter to skip): \n")
                        if user_input.strip():
                            if key == "price":
                                user_input = float(user_input)
                            utensil_index[key] = user_input
                    print("Product updated successfully.\n")
                else :
                    print('Invalid input\n')            
                save_products()
                break
                    

            #if 4 delete product

            elif menu_option == 4 :
            
                print(dict_index(utensils))

                operator_index = int(input("Please enter the index you want to delete:\n"))
                del utensils[operator_index] 

                list_print(utensils)
                
                #break will take you back to main menu
                break

    # COURIERS menu
    elif option == 2 :
        
        while True :
            courier_option = int(input("SELECT: \n 0 - Exit to Main Menu \n 1 - Couriers list \n 2 - Create courier \n 3 - UPDATE Existing courier \n 4 - DELETE courier \n") )
        # if 0 exit to main menu 
            if  courier_option == 0 :

                break

        # print couriers
            elif courier_option == 1 :
                print(couriers)

                break

        # create new courier
            elif courier_option == 2 :
                new_courier = input('Please enter a new courier name: \n')
                new_phone = input('Please enter a new phone number:\n')
                couriers.append ({'name':new_courier,'phone':new_phone})
                save_couriers()
                break

        # UPDATE existing courier
            elif courier_option == 3 :
                dict_index(couriers)
                op_index = int(input('Please enter the index to UPDATE:\n'))
                if 0 <= op_index < len(couriers) :
                    # if input is valid changing at operator index choise
                    update_index = couriers[op_index]
                    # iterate through the keys
                    for key in ['name', 'phone'] :
                        # ask for changes
                        user_input = input(f'Please enter the value for {key}.(Press enter to skip)\n')
                        # if user input is not an empty string then update at the index
                        if user_input.strip() :

                            update_index[key] = user_input

                    print('Couriers updated succesfully\n')
                    save_couriers()

                else : 
                    print('Invalid index\n')
                    
                    break
                
        # DELETE courier
            elif courier_option == 4 :

                dict_index(couriers)
                op_index = int(input('Please enter the index to DELETE:\n'))
                del couriers[op_index]
                save_couriers()
                break
                
      # ORDERS menu
    elif option == 3 :
        
        while True :
            order_option = int(input("SELECT :\n 0 - Exit to Main Menu \n 1 - View Orders \n 2 - Create order \n 3 - UPDATE Existing order status \n 4 - UPDATE Existing order \n 5 - DELETE order\n") )
        # if 0 exit to main menu 
            if  order_option == 0 :
                break

        # if 1 print product list

            elif order_option == 1 :
                print(orders)
                
                break

        # create new order
            elif order_option == 2:
                
                new_name = input('Enter your name:\n')
                new_address = input('Enter your address:\n')
                new_phone = input('Enter your phone number:\n')
                # open products list with it's index
                print(dict_index(utensils))
                select_product = input('Please select as many products as you like from the list separated by a comma:\n')
                print(dict_index(couriers))
                select_courier = int(input('Please select a courier index:\n'))
                # create a dictionary to store my values
                order = {
                    'customer_name' : new_name ,
                    'customer_address' : new_address , 
                    'customer_phone' : new_phone ,
                    'item' : select_product ,
                    'courier' : select_courier ,
                    'status' : 'preparing'  
                }

                orders.append(order)
                save_orders()
                

          # UPDATE existing order status 
            
            elif order_option == 3 :
                
                print(dict_index(orders)) 
                
                order_index = int(input("Please select the index you want to change:\n"))

                if 0 <= len(orders) :
                    print(index_status(order_statuses))
                    choose_status = int(input('Enter the change you want to apply:\n'))
                    if 0 <= order_index < len(orders) and 0 <= choose_status < len(order_statuses) :
                        orders[order_index]['status'] = order_statuses[choose_status]
                        print('Status updated')
                        print(orders)
                    else :
                        print('Invalid index')
                else :
                    print('Invalid index')
        
        # Update existing orders
            elif order_option == 4:  
                # Print the orders with index values
                print(dict_index(orders))   
                # choose the order from list
                order_index = int(input("Please provide the order index you would like to UPDATE:\n"))
                if 0 <= order_index < len(orders):
                    selected_order = orders[order_index]
                    for key in ['customer_name','customer_address','customer_phone']:
                        user_input = input(f"Enter the new value for {key} (enter to skip): \n")
                        if user_input.strip():
                            selected_order[key] = user_input
                    
                    print(dict_index(utensils))
                        
                    product_input = input('Please select as many products as you like from the list separated by a comma (or enter to skip):\n')
                    if product_input.strip():
                        selected_order['item'] = product_input

                    print(dict_index(couriers))

                    courier_input = input('Please select the index of the courier (or enter to skip):\n')
                    if courier_input.strip():
                        selected_order['courier'] = int(courier_input)
                        
                            

                    print(index_status(order_statuses))

                    choose_status = input('Enter the change you want to apply:\n')
                    if choose_status.strip():
                        index = int(choose_status)

                        if 0 <= order_index < len(orders) and 0 <= index < len(order_statuses) :
                            orders[order_index]['status'] = order_statuses[index]
                            print('Status updated')
                            
                    print("Order updated.\n")
                    save_orders()

                else :
                    print("Invalid index.\n")
                    break

            elif order_option == 5 : # Delete existing order

                print(dict_index(orders)) 
                # Get user input for index I want to delete and place it in a variable
                delete_index = int(input('Please select the index for the order you want to delete:\n'))
                # If condition, to iterate through orders and delete the index choosen
                if 0 <= delete_index < len(orders):
                    del orders[delete_index]
                print('Order deleted\n')
                save_orders()
                break

