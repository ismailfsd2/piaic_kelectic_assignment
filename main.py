def get_unit():
    return int(input("Enter your unit: "))

def get_unit_price(unit):
    price = 0
    if unit <= 100:
        price = 13.48
    elif unit <= 200:
        price = 18.95
    elif unit <= 300:
        price = 22.14
    elif unit <= 400:
        price = 25.53
    elif unit <= 500:
        price = 27.74
    elif unit <= 600:
        price = 29.16
    elif unit <= 700:
        price = 30.30
    else:
        price = 35.22
    return price

def cal_net_amount(uniform,unit,price):
    return unit*(price+uniform)

get_unit_value = get_unit()
get_price = get_unit_price(get_unit_value)
net_amount = cal_net_amount(10,get_unit_value,get_price)
print('Total Net Amount: '+str(net_amount))

