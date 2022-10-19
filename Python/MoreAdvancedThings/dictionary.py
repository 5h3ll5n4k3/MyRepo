menu_items={"Burger":5.99, "cheese burger":6.49,"fries":2.49,"drink":1.99}
menu_items["Hot dog"] =2.99
menu_items.update({"Burger":6.59,"cheese burger":6.99,"Drink":2.49, "Hot dog":3.49})

# print(menu_items.keys())

# print(menu_items["cheese burger"])

def get_key(arg, dictionary):
    my_list=[]
    for key, value in dictionary.items():
        if value == arg:
            my_list.append(key)
    return my_list


print(get_key(2.49, menu_items))

my_order=["cheese burger", "fries","drink"]
count={}
total=0
for i in my_order:
    count[i]=count.get(i,0 ) +1
print(count)
for item, quantity in count.items():
    price=menu_items[item]
    total=total+(price*quantity)
print(total)