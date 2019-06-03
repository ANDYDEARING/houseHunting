total_cost = float(input("What is the cost of your dream home? "))
portion_down_payment = 0.25
current_savings = 0
annual_return = 0.04
annual_salary = float(input("What is your annual salary? "))
portion_saved = float(input("How much do you want to save each month, as a decimal? "))
number_of_months = 0
while current_savings <= (total_cost * portion_down_payment):
    number_of_months = number_of_months + 1
    current_savings = current_savings + ((current_savings * annual_return)/12) + (portion_saved * (annual_salary/12))
    print("Debug savings " + str(current_savings))
    print("Debug month number " + str(number_of_months))
print("It will take " + str(number_of_months) + " months.")