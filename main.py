from blockchain import Blockchain
from car_sharing import Owner, Customer

# Initialize blockchain
blockchain = Blockchain()

# Owner sets the balance and deploys the contract with initial deposit
owner = Owner(balance=1000)
print(f"Owner is deploying the contract with an initial deposit of 50 ether.")
owner.deploy(ether=50, blockchain=blockchain)  # Owner deposits some ether to start with
print(f"Owner's balance after deployment: {owner.balance} ether.\n")

# Owner input for daily price
daily_price = float(input("Owner: Enter the daily rental price for the car: "))
print(f"Owner has set the daily rental price to {daily_price} ether/day.\n")

# Owner adds car to rent with specified daily price
owner.add_car_to_rent(day_price=daily_price, car_info={"make": "Tesla", "model": "Model S", "year": 2020})
print(f"Car added to rent: Tesla Model S (2020) at {daily_price} ether/day.\n")

# Customer sets their balance
customer = Customer(balance=500)
print(f"Customer has an initial balance of {customer.balance} ether.\n")

# Customer input for number of days
days_to_rent = int(input("Customer: Enter the number of days you want to rent the car: "))
total_cost = daily_price * days_to_rent
print(f"Total cost for renting the car for {days_to_rent} days is {total_cost} ether.\n")

# Ask customer to deposit the exact amount
customer_deposit = float(input(f"Customer: Please deposit {total_cost} ether to proceed with the booking: "))
if customer_deposit >= total_cost:
    customer.request_book(ether=customer_deposit, blockchain=blockchain)
    print(f"Customer deposited {customer_deposit} ether for booking.\n")
    print(f"Customer's balance after deposit: {customer.balance} ether.\n")
else:
    print(f"Insufficient deposit. You need to deposit at least {total_cost} ether.\n")
    exit()

# Customer passes the number of days they want to rent the car
customer.pass_number_of_days(days_no=days_to_rent)
print(f"Car has been booked for {days_to_rent} days.\n")

# Ask the owner to grant permission for car usage
grant_access = input("Owner: Do you want to allow the customer to access the car? (yes/no): ").strip().lower()
if grant_access == 'yes':
    owner.allow_car_usage()
    print("Owner has granted car usage.\n")

    # Customer accesses the car
    customer.access_car()
    print("Customer has accessed the car.\n")
else:
    print("Owner did not grant permission to access the car.\n")
    exit()

# After the rental ends, the customer ends the rental
customer.end_car_rental()
print("Car rental ended. The customer has returned the car.\n")

# Both owner and customer check their balance
owner.withdraw_earnings()
print(f"Owner has withdrawn earnings. Owner's balance is now: {owner.balance} ether.\n")
customer.retrieve_balance()
print(f"Customer's balance after rental: {customer.balance} ether.\n")

# Blockchain transactions and mining
owner.encrypt_and_store_details(blockchain)
print("Blockchain transactions have been mined and recorded.\n")

# Display all blockchain transactions
print("Blockchain transaction log:")
for i, block in enumerate(blockchain.chain):
    print(f"Block {i}:")
    for transaction in block.transactions:
        print(f"  Transaction: {transaction}")
