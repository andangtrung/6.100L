## 6.100A PSet 1: Part C
## Name: An Dang Trung
## Time Spent: 0:20
## Collaborators: None

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_dream_home = 800000
portion_down_payment = 0.25
cost_for_down_payment = cost_of_dream_home * portion_down_payment
months = 36
epsilon = 100
low = 0
high = 1
amount_saved = initial_deposit * (1 + high / 12) ** months
r = None
steps = 0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
if amount_saved < cost_for_down_payment:
    pass
else:
    while abs(amount_saved - cost_for_down_payment) > epsilon:
        r = (high + low) / 2
        amount_saved = initial_deposit * (1 + r / 12) ** months

        if amount_saved < cost_for_down_payment:
            low = r
        else:
            high = r

        steps += 1

print(f"Best saving rate: {r}")
print(f"Steps in bisection search: {steps}")
