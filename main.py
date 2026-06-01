from Expense_Tracker import user_input
from Expense_Tracker import add_expense
from Expense_Tracker import get_expenses
from Expense_Tracker import print_expenses 
from Expense_Tracker import delete_expense
from Expense_Tracker import display_expenses

    
# Running the program    
def main(): 
    
    print('Welcome to the Expense Tracker')
    
    while True: 
        
        try: 
            print('\n1. Add Expense\n2. View Expenses\n3. Delete expense\n4. Quit\n')
            user_choice = int(input("What operation you would like to do? "))
            
            if user_choice == 4: 
                break
            
            elif user_choice == 1: 
                expense_name,expense_amount,category_number = user_input()
                add_expense(expense_name,expense_amount,category_number)
                
            elif user_choice == 2: 
                print_expenses()
                total_expenses, total_count,categories = get_expenses()
                display_expenses(total_expenses,total_count,categories)
                
            elif user_choice == 3: 
                try: 
                    expense_id = int(input('what is the id of the expense you want to remove? '))
                    delete_expense(expense_id)
                    total_expenses, total_count, categories = get_expenses()
                    
                except ValueError: 
                    print("Invalid expense id")
                
            else: 
                print('Invalid choice, please enter (1-4)')
                
        except ValueError: 
            print('Please enter the choice as a number (1-4)')
            
            
        
if __name__ == "__main__": 
    main()
