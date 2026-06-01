import csv 
import os 
import datetime


# Getting user inputs and printing the messages 
def user_input():
    
    expense_name = input('Enter the expense name: ').strip().lower()
    expense_category = ["🍔 Food","🏡 Home","💼 Work","🎉 Fun","✨ Misc"]
    
    while True:
        try:    
            expense_amount = float(input('Enter the expense amount ($): ').strip())
              
            print('(Expense Category) ')
            for idx, i in enumerate(expense_category):
                print(f'{idx+1}. {i}')
                
            category_number = int(input('Enter a category number (1-5): ')) 
            
            if not category_number in range(1,len(expense_category)+ 1) :
                raise(ValueError) 
            
            return expense_name,expense_amount,category_number
        
        except ValueError:
            print('Invalid input')
            
    
 
# Adding the expenses based on the category user gives
def add_expense(expense_name,expense_amount,category_number):
    
    # Checking if the csv file exists or has any line stored 
    file_empty = not os.path.exists('Expenses.csv') or os.path.getsize('Expenses.csv') == 0
    
    row_count = 0 
    if os.path.exists('Expenses.csv'): 
        # Read the file and count the number of rows
        with open('Expenses.csv', 'r') as file: 
           row_count = len(list(csv.DictReader(file)))
        
    with open('Expenses.csv', 'a',newline='') as file: 
        
        field_names = ['Id','Expense_Amount','Expense_Name','Category','Date'] 
        csv_writer = csv.DictWriter(file,fieldnames=field_names,delimiter=',',restval='')
        
        if file_empty:
            csv_writer.writeheader()
        
        # Getting the current date 
        current_time = datetime.datetime.now()
        time = current_time.strftime('%a/%b/%d %H:%M') 
        
        # Using dictionary instead of 5 if/else conditions
        d = {1:'Food',2:'Home',3:'Work',4:'Fun',5:'Misc'}
    
        for key in d.keys():
            if category_number == key:
                csv_writer.writerow({'Id': row_count + 1 ,'Expense_Amount': expense_amount,'Expense_Name':expense_name,'Category':d[key] ,'Date':time})
    
        print(f'You have added {expense_name} (${expense_amount}) to your expenses')
   
    

# Reading the csv file and returning total amount of expenses and total number of expenses 
def get_expenses():
    
    # A dictionary containing count and total of each category 
    categories = {
        'Food' : {'count' : 0, 'total' : 0},
        'Home' : {'count': 0 , 'total' : 0},
        'Work' : {'count': 0 , 'total' : 0},
        'Fun' : {'count': 0 , 'total' : 0},
        'Misc' : {'count': 0 , 'total' : 0}
    }

    # Exit and return defult values if the file doesnt exist  
    if not os.path.exists('Expenses.csv'): 
        return 0,0,categories
    
    with open('Expenses.csv','r',newline='') as file : 
        
        reader = csv.DictReader(file,delimiter=',')
        
        for line in reader : 
            for c in categories: 
                if c == line['Category'] : 
                    categories[c]['count'] += 1
                    categories[c]['total'] += float(line['Expense_Amount'])
                    
                    
    # Calculating the total expenses of all items 
    total_expenses = sum([categories[i]['total'] for i in categories])
    total_count = sum([categories[j]['count']for j in categories])
    
    return total_expenses, total_count, categories


# Removing an expense 
def delete_expense(expense_id): 
    
    with open('Expenses.csv','r') as file: 
        reader = csv.DictReader(file,delimiter=',')
        
        # Reading the csv file into list of dictionaries
        rows = list(reader)
        
        # validating if the specific expense exists 
        deleted = False 
        for i in range(0,len(rows)):
                if str(expense_id) == rows[i]['Id']: 
                    rows.pop(expense_id - 1)
                    deleted = True
                    print(f'Expense with the id {expense_id} has been removed') 
                    break

        # decreasing the id of expenseses after the one that has been removed by one 
        if deleted:
            for i in range(expense_id -1 , len(rows)):
                rows[i]['Id'] = int(rows[i]['Id']) -  1
            
            with open('Expenses.csv' , 'w') as file:
                writer = csv.DictWriter(file,fieldnames=['Id','Expense_Amount','Expense_Name','Category','Date'] ,delimiter=',',restval='')
                writer.writeheader()
                writer.writerows(rows) 
        else: 
             print(f'The expense with id {expense_id} does not exist')
            
                


# Printing all the lines in csv file to user 
def print_expenses():
    
   
    if not os.path.exists('Expenses.csv'): 
        return None
    
    with open('Expenses.csv', 'r') as file: 
        reader = csv.DictReader(file,delimiter=',')
        
        for line in reader:
                print(f'\n{line['Id']}. {line['Expense_Name']} - {line['Expense_Amount']} | {line['Category']} | {line['Date']}', end="\n")
            


# Displaying messages 
def display_expenses(total_expenses , total_count, categories):
    
    print(f'\nyou have {total_count} expenses totalling {round(total_expenses,2)}')
    print('\n📈 Expenses by category: ')
    
    print(f'''\
🍔 Food: ${round(categories['Food']['total'],1)}
🏡 Home: ${round(categories['Home']['total'],1)}
💼 Work: ${round(categories['Work']['total'],1)}
🎉 Fun: ${round(categories['Fun']['total'],1)}
✨ Misc: ${categories['Misc']['total']}''')
    
            
 

         
