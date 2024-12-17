# cp = 500
# sp = 800
 
cost_price = int(input("enter the cost price: "))
selling_price = int(input("enter the selling price "))
def calculater_bouns(parcentage_numer,cost_price):
    bouns = parcentage_numer/100*cost_price
    return bouns

if cost_price>selling_price:
    profit= sp-cp
    bouns= calculater_bouns(5,cp)
    total_amount = profit+bouns
elif sp>cp:
    loss 