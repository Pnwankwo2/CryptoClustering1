# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
# Initialize the order list
order_list = []

order1 = {
    "menu_item_name": "Burger",
    "item_price": 5.99,
    "quantity_ordered": 2
}

order2 = {
    "menu_item_name": "Fries",
    "item_price": 2.99,
    "quantity_ordered": 1
}

order3 = {
    "menu_item_name": "Soda",
    "item_price": 1.50,
    "quantity_ordered": 3
}

# Add orders to the order list
order_list.append(order1)
order_list.append(order2)
order_list.append(order3)

# Print the order list
for order in order_list:
    print(order)


# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = # Create a dictionary to store the menu for later retrieval
menu_items = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Print the menu to verify
for category, items in menu_items.items():
    print(f"{category}:")
    for item, price in items.items():
        if isinstance(price, dict):
            print(f"  {item}:")
            for sub_item, sub_price in price.items():
                print(f"    {sub_item}: ${sub_price:.2f}")
        else:
            print(f"  {item}: ${price:.2f}")

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    
        # Define the menu with item numbers
menu_items = {
    1: {"category": "Snacks", "item": "Cookie", "price": 0.99},
    2: {"category": "Snacks", "item": "Banana", "price": 0.69},
    3: {"category": "Meals", "item": "Burrito", "price": 4.49},
    4: {"category": "Meals", "item": "Teriyaki Chicken", "price": 9.99},
    5: {"category": "Drinks", "item": "Soda", "price": 1.99},
    6: {"category": "Dessert", "item": "Chocolate lava cake", "price": 10.99}
}

# Print the menu with item numbers
print("Menu:")
for number, details in menu_items.items():
    print(f"{number}. {details['category']} - {details['item']}: ${details['price']:.2f}")

# Ask the customer to input a menu item number
item_number = int(input("Please enter the menu item number: "))

# Retrieve and print the selected item
if item_number in menu_items:
    selected_item = menu_items[item_number]
    print(f"You selected: {selected_item['category']} - {selected_item['item']} for ${selected_item['price']:.2f}")
else:
    print("Invalid item number. Please try             1
            # 2. Ask customer to input 
menu item number
            


            # 3. Check if the customer typed a number

                # Convert the menu selection to an integer


                # 4. Check if the menu selection is in the menu items

                    # Store the item name as a variable


                    # Ask the customer for the quantity of the menu item


                    # Check if the quantity is a number, default to 1 if not


                    # Add the item name, price, and quantity to the order list


                    # Tell the customer that their input isn't valid


                # Tell the customer they didn't select a menu option

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input

                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("----------------
# Store the dictionary items as a variable
menu_items = {
    1: {"category": "Snacks", "item": "Cookie", "price": 0.99},
    2: {"category": "Snacks", "item": "Banana", "price": 0.69},
    3: {"category": "Meals", "item": "Burrito", "price": 4.49},
    4: {"category": "Meals", "item": "Teriyaki Chicken", "price": 9.99},
    5: {"category": "Drinks", "item": "Soda", "price": 1.99},
    6: {"category": "Dessert", "item": "Chocolate lava cake", "price": 1}


# Example order list with item numbers and quantities
order_list = [
    {"item_number": 1, "quantity": 2},
    {"item_number": 3, "quantity": 1},
    {"item_number": 5, "quantity": 3}
]

Loop through the items in the customer's order
for order in order_list:
    item_number = order["item_number"]
    quantity = order["quantity"]
    item = menu_items[item_number]["item"]
    price = menu_items[item_number]["price"]
    total_price = price * quantity
    
    # Print the item details
    print(f"Item: {item}")
    print(f"Price: ${price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total_price:.2f}")
    print("-" * 20)
----------|--------|----------")

# 6. Loop throug
 Store the dictionary items as a variable
menu_items = {
    1: {"category": "Snacks", "item": "Cookie", "price": 0.99},
    2: {"category": "Snacks", "item": "Banana", "price": 0.69},
    3: {"category": "Meals", "item": "Burrito", "price": 4.49},
    4: {"category": "Meals", "item": "Teriyaki Chicken", "price": 9.99},
    5: {"category": "Drinks", "item": "Soda", "price": 1.99},
    6: {"category": "Dessert", "item": "Chocolate lava cakm numbers and quantities
order_list = [
    {"item_number": 1, "quantity": 2},
    {"item_number": 3, "quantity": 1},
    {"item_number": 5, "quantity": 3}
]

# Calculate the total cost using list comprehension
total_cost = sum(menu_items[order["item_number"]]["price"] * order["quantity"] for order in order_list)

# Print the total cost
print(f"Total cost of the order: ${total_cost:.2f}")h the items in the customer's order

    # 7. Store the dictionar
items = [
    {"name": "Cookie", "price": 0.99},
    {"name": "Banana", "price": 0.69},
    {"name": "Burrito", "price": 4.49},
    {"name": "Teriyaki Chicken", "price": 9.99},
    {"name": "Soda", "price": 1.99},
    {"name": "Chocolate lava cake", "price": 10.99}
]

# Define the width for formatting
width = 30

# Print the items with formatted spacing
for item in items:
    name = item["name"]
    price = item["price"]
    spaces = ' ' * (width - len(name) - len(f"{price:.2f}"))
    print(f"{name}{spaces}${price:.2f}")y items as variables


    # 8. 
space_string = '   ' * 15

#Print the space string these will bve blanks.
print(f"'{space_string}'")
lculate the number of spaces for formatted printing
# Define the menu with item numbers
menu_items = {
    1: {"category": "Snacks", "item": "Cookie", "price": 0.99},
    2: {"category": "Snacks", "item": "Banana", "price": 0.69},
    3: {"category": "Meals", "item": "Burrito", "price": 4.49},
    4: {"category": "Meals", "item": "Teriyaki Chicken", "price": 9.99},
    5: {"category": "Drinks", "item": "Soda", "price": 1.99},
    6: {"category": "Dessert", "item": "Chocolate lava cake", "price": 10.99}
}

# Print the menu with item numbers
print("Menu:")
for number, details in menu_items.items():
    print(f"{number}. {details['category']} - {details['item']}: ${details['price']:.2f}")

# Ask the customer to input a menu item number
item_number = int(input("Please enter the menu item number: "))

# Check if the item number is valid
if item_number in menu_items:
    # Ask the customer to input the quantity
    quantity = int(input("Please enter the quantity: "))
    
    # Retrieve the selected item
    selected_item = menu_items[item_number]
    
    # Print the item name, price, and quantity
    print(f"You selected: {selected_item['item']}")
    print(f"Price: ${selected_item['price']:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${selected_item['price'] * quantity:.2f}")
else:
    print("Invalid item numr. Please try again.")


    # 9. Create space strings


    # 10. Print t Che item name, price, and quantity


# 11. Calculate the cost of the order using lismenu_items = {
    1: {"category": "Snacks", "item": "Cookie", "price": 0.99},
    2: {"category": "Snacks", "item": "Banana", "price": 0.69},
    3: {"category": "Meals", "item": "Burrito", "price": 4.49},
    4: {"category": "Meals", "item": "Teriyaki Chicken", "price": 9.99},
    5: {"category": "Drinks", "item": "Soda", "price": 1.99},
    6: {"category": "Dessert", "item": "Chocolate lava cake", "price": 10.99}
}

# Example order list with item numbers and quantities
order_list = [
    {"item_number": 1, "quantity": 2},
    {"item_number": 3, "quantity": 1},
    {"item_number": 5, "quantity": 3}
]

# Calculate the total cost using list comprehension
total_cost = sum(menu_items[order["item_number"]]["price"] * order["quantity"] for order in order_list)

# Print the total cost
print(f"Total cost of the order: ${total_cost:.2f}")t comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
