#Defining the menu of restaurant
menu={
    'Pizza':150,
    'Pasta':100,
    'Burger':40,
    'Salad':20,
    'Coffee':70,
}
#Greet
print("Welcome to Snehal's Restaurant")
print("Pizza: Rs.150\nPasta: Rs.100\nBurger: Rs.40\nSalad: Rs.20\nCoffee: Rs.70")
order_total=0
item_1 = input("Enter the item you want to order:")
if item_1 in menu:
    order_total += menu[item_1]
    print("Your item{item_1}has been added to your order")
else:
    print("Sorry,this Order {item_1}  is not available")
    another_order = input("Do you want to add another item?(Yes/No)")
    if another_order == "Yes":
        item_2 = input("Enter the name of the second item = ")
        if item_2 in menu:
            order_total += menu[item_2]
        print("Item {item_2}has been added to order")
    else:
        print("Ordered item {item_2} is not available!")
        print("The total amount of ordered items to pay is {ordered_total}")