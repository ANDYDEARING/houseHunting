# default values
total_cost = 1000000
portion_down_payment = 0.25
current_savings = 0
annual_return = 0.04
annual_salary = 120000
portion_saved = 0.1

# get input values, leaving default value if needed
print("For any of the following questions, press ENTER to use the default value.")

total_cost_str = (input("What is the cost of your dream home [" + str(total_cost) +"]? "))
if total_cost_str != "":
    total_cost = float(total_cost_str)
else:
    print("Using " + str(total_cost))

portion_down_payment_str = (input("As a decimal, what percentage do you want for down payment [" + str(portion_down_payment) +"]? "))
if portion_down_payment_str != "":
    portion_down_payment = float(portion_down_payment_str)
else:
    print("Using " + str(portion_down_payment))

current_savings_str = (input("How much have you saved already [" + str(current_savings) +"]? "))
if current_savings_str != "":
    current_savings = float(current_savings_str)
else:
    print("Using " + str(current_savings))

annual_return_str = (input("As a decimal, what is your expected annual rate of return [" + str(annual_return) +"]? "))
if annual_return_str != "":
    annual_return = float(annual_return_str)
else:
    print("Using " + str(annual_return))

annual_salary_str = (input("What is your annual salary [" + str(annual_salary) +"]? "))
if annual_salary_str != "":
    annual_salary = float(annual_salary_str)
else:
    print("Using " + str(annual_salary))

portion_saved_str = (input("How much do you want to save each month, as a decimal [" + str(portion_saved) +"]? "))
if portion_saved_str != "":
    portion_saved = float(portion_saved_str)
else:
    print("Using " + str(portion_saved))

number_of_months = 0

# calculate
while current_savings < (total_cost * portion_down_payment):
    number_of_months = number_of_months + 1
    current_savings = current_savings + ((current_savings * annual_return)/12) + (portion_saved * (annual_salary/12))
    print("Month " + str(number_of_months) + " Savings $" + str(round(current_savings,2)))
print("It will take " + str(number_of_months) + " months.")