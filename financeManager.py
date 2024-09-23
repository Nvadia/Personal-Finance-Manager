def userInfo():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    email = input("Enter your email: ")
    return name, age, gender, email


def needs(salary, needsdict, percent = 0.5):
    # for general case we will assume 50% of our salary will be used in basic needs
    use = percent * salary
    
    for keys, expense in needsdict.items():
        use = use - float(expense)
        print (f"{keys} will use {expense}, therefore remaining amount = {use}")
    if use >= 1:
        extra = use
        return extra
    else: 
        return("nothing left after expense")
        

def wants(salary, wantsdict, percent = 0.2):
    # for general case we will assume 20% of our salary will be used in wants
    use = percent * salary
    for keys, expense in wantsdict.items():
        use = use - float(expense)
        print (f"{keys} will use {expense}, therefore remaining amount = {use}")
    if use >= 1:
        extra = use
        return extra
    else: 
        return("nothing left after expense")
          


def savings( salary,a , b, percent = 0.2):
    # for general case we will assume 20% of our salary will be saved
    use = percent * salary
    use += (a + b)
    return use
    
  
def Investment(salary, percent = 0.1):
    # for general case we will assume 10% of our salary will be invested
    use = percent * salary
    return use


def main():
    salary  = float(input("Enter your fortnightly/ monthly salary: "))
    # Here we will use zero dollar budget, the leftovers will be returned and sent to savings
    info = userInfo()
    print(info)
    needsdict = {}
    wantsdict = {}

    #Let's ask the user what type of expenses are in his basic needs
    print("Enter exit to stop.")
    while True:
        key = input("Enter the types of basic expenditure: ")
        if key.lower() == 'exit':
            break
        needsdict[key] = None
    for key in needsdict:
        value = input(f"Enter your expense for {key}: ")
        needsdict[key] = value

    nextra = needs(salary, needsdict)
    print("your remaining amount: " , nextra)

    
    #Let's ask the user what type of expenses are in his wanted lists

    print("Enter exit to stop.")
    while True:
        key = input("Enter the types of wanted expenditure: ")
        if key.lower() == 'exit':
            break
        wantsdict[key] = None
    for key in wantsdict:
        value = input(f"Enter your expense for {key}: ")
        wantsdict[key] = value
    wextra = wants(salary, wantsdict)
    print("you remaining amount: " , wextra)

    save = savings(salary, nextra, wextra)
    print("Your savings are", save)
        
    Invest= Investment(salary)
    print("The remaining amout that you will invest is: ", Invest)    
main()
