#Menu of restaurant
menu = {
    'Masala Chai ':20,
    'Lassi':20,
    'Samosa':30,
    'Pasta':50,
    'Cold Coffee':60,
    'Salad':70,
    'Iced Coffee':80,
    'Pizza':100,
    'Burger':100
}

#Greet
print("\n----Welcome To Python Cafe----\n")
print("Masala Chai: ₹20\nLassi: ₹20\nSamosa: ₹30\nPasta: ₹50\nCold Coffee: ₹60\nSalad: ₹70\nIced Coffee: ₹80\nPizza: ₹100\nBurger: ₹100")
order_total = 0

num_items = int(input("How many items do you want to order? "))

#First Order
for i in range(num_items):
    item = input(f"Enter the name of item {i+1}: ")

    if item in menu:
        order_total += menu[item]
        print("Your order:",item)
    else:
        print(f"Ordered item {item} is not avaialable yet!")
        
#Second Order  
while True:
    another_order = input("Do you want to add another item? (Yes/No) : ")
    if another_order == "Yes":
        item_1 = input("Enter the name of item = ")
        if item_1 in menu:
            order_total += menu[item_1]
            print(f"Item {item_1} has been added to order")
        else:
            print("ordered item {item_1} is not avaialable!")
    else: 
        break        

#Final Result
print(f"The total amount of items to pay is {order_total}")
