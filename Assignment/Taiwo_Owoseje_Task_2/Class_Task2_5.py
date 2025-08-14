# This is a program to collect the daily market report at a local market.

market = input("Enter Market name: ")
traders = input("Enter Number of traders: ")
revenue = int(input("Enter daily revenue in naira: "))
daily_revenue = f"{revenue:,}"
print(f"The Daily Market report for {market} \n{traders} number of traders were in {market} today \nA total value of ₦{daily_revenue} was exchanged.")