# Personal Finance Manager

## Description
The **Personal Finance Manager** is a Python-based tool that helps users manage their salary by categorizing their expenses into needs, wants, savings, and investments. The program allows users to allocate portions of their salary into basic needs, wants, and savings, while automatically calculating leftover amounts that can be saved or invested.

This project is ideal for anyone who wants to keep track of their income and manage their finances more effectively.

## Features
- Collects basic user information (name, age, gender, email).
- Categorizes expenses into:
  - **Needs**: Basic expenditures like rent, groceries, utilities, etc.
  - **Wants**: Non-essential expenditures such as entertainment or shopping.
  - **Savings**: Automatically calculates savings based on the leftover amounts.
  - **Investments**: Allocates a fixed percentage of salary into investments.
- Provides a detailed breakdown of how much money is spent and how much is saved or invested.

## Project Structure
The project includes several functions to handle different aspects of personal finance:

- **`userInfo()`**: Collects user information such as name, age, gender, and email.
- **`needs(salary, needsdict, percent=0.5)`**: Allocates 50% of the salary to basic needs, calculates expenses, and returns any remaining amount.
- **`wants(salary, wantsdict, percent=0.2)`**: Allocates 20% of the salary to wants, calculates expenses, and returns any remaining amount.
- **`savings(salary, a, b, percent=0.2)`**: Allocates 20% of the salary to savings and adds any remaining amount from the `needs` and `wants` categories.
- **`Investment(salary, percent=0.1)`**: Allocates 10% of the salary to investments.
- **`main()`**: Handles user inputs, including salary and expenses, and calls the above functions to provide a complete personal finance summary.

## Usage
1. Run the program.
2. Enter your salary when prompted.
3. Enter your basic details: name, age, gender, and email.
4. Add your basic expenditure items (e.g., rent, groceries) and their corresponding costs.
5. Add your wanted expenditure items (e.g., entertainment, shopping) and their corresponding costs.
6. The program will calculate and display:
   - Your remaining amount after covering basic needs.
   - Your remaining amount after covering wants.
   - Total savings.
   - Total investment.

### Example:
```
Enter your fortnightly/monthly salary: 5000
Enter your name: John
Enter your age: 30
Enter your gender: Male
Enter your email: john@example.com
Enter exit to stop.
Enter the types of basic expenditure: Rent
Enter your expense for Rent: 1500
Enter the types of basic expenditure: Groceries
Enter your expense for Groceries: 500
Enter the types of basic expenditure: exit
Rent will use 1500, therefore remaining amount = 1000
Groceries will use 500, therefore remaining amount = 500
your remaining amount:  500
Enter exit to stop.
Enter the types of wanted expenditure: Entertainment
Enter your expense for Entertainment: 300
Enter the types of wanted expenditure: exit
Entertainment will use 300, therefore remaining amount = 700
your remaining amount:  700
Your savings are 1700.0
The remaining amount that you will invest is:  500.0
```

## Requirements
- Python 3.x

## How to Run
1. Clone or download the repository.
2. Open the terminal or command prompt.
3. Run the following command:
   ```bash
   python financeManager.py
   ```

## Future Improvements
- Add a graphical user interface (GUI) for better user interaction.
- Implement a database to store user financial data.
- Add functionality for monthly reporting and analysis.

