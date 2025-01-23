def calculate_rent(monthly_rent, months, members, additional_charges=0):

    # Calculate the total rent before any additional charges
    total_rent = monthly_rent * months
    
    # Add any additional charges if any
    total_rent += additional_charges
    
    # Calculate how much each member should pay
    if members > 0:
        rent_per_member = total_rent / members
    else:
        rent_per_member = total_rent  # In case there are no members (though unlikely)

    return total_rent, rent_per_member

print("\n----Rent Calculator----\n")

monthly_rent = float(input("Enter the monthly rent: ₹"))
months = int(input("Enter the number of months: "))
members = int(input("Enter the number of members: "))
additional_charges = float(input("Enter any additional charges (if applicable): ₹"))

total_amount, rent_per_member = calculate_rent(monthly_rent, months, members, additional_charges)
print(f"\nThe total rent for {months} months is: ₹{total_amount:.2f}")
print(f"Each member should pay: ₹{rent_per_member:.2f}")
