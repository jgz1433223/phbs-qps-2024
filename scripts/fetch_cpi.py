import os
import sys

# Ensure the script can access modules in the src directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir, "src"))

from cpi_utils import fetch_cpi_data, calculate_quarterly_inflation
import matplotlib.pyplot as plt


def main():
    # Fetch CPI data
    print("Fetching CPI data...")
    cpi_data = fetch_cpi_data()

    # Calculate quarterly inflation rates
    print("Calculating quarterly inflation rates...")
    last_4_quarters = calculate_quarterly_inflation(cpi_data)

    # Display the results
    print("The quarterly inflation rates for the last 4 quarters:")
    print(last_4_quarters)

    # Plot the CPI data
    print("Plotting the CPI data...")
    plt.figure(figsize=(10, 6))
    cpi_data['CPIAUCSL'].plot(title='Consumer Price Index (CPI)')
    plt.ylabel('CPI Level')
    plt.xlabel('Date')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
