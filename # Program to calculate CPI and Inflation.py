# Program to calculate CPI and Inflation Rate

# Input costs
base_cost = float(input("Enter cost of basket in Base Year: "))
previous_cost = float(input("Enter cost of basket in Previous Year: "))
current_cost = float(input("Enter cost of basket in Current Year: "))

# Calculate CPI
previous_cpi = (previous_cost / base_cost) * 100
current_cpi = (current_cost / base_cost) * 100

# Calculate Inflation Rate
inflation = ((current_cpi - previous_cpi) / previous_cpi) * 100

# Display results
print("\nPrevious Year CPI =", round(previous_cpi, 2))
print("Current Year CPI =", round(current_cpi, 2))
print("Inflation Rate = {:.2f}%".format(inflation))