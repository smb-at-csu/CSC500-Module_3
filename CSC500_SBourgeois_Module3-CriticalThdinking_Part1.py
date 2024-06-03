def main():
    # Customer inputs original total.
    initial_total = float(input("Enter initial total without tip and tax: $"))

    # Calculate tip and tax 
    tip = initial_total * 0.18
    tax = initial_total * 0.07
    
    #Calculate final total
    final_total = initial_total + tip + tax
    
    # Display the results
    print("\nBill Breakdown:")
    print(f"Initial total:   ${initial_total:.2f}")  
    print(f"Tip amount:      ${tip:.2f}")
    print(f"Tax amount:      ${tax:.2f}")
    print(f"Final total:     ${final_total:.2f}")

# Ensure main function is executed when the program is run.
if __name__ == "__main__":
    main()
