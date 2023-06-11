choose = input("What do you want to calculate? Present value or future value? ")

if choose == 'Present value':
    Future_value = float(input("How much is the future value? "))
    
    rate = int(input("How much the rate? "))
    rate = rate / 100
    
    years = int(input("For how many years? "))
    
    Present_value= Future_value / ((1 + rate)** years)
    
    if years is None:
        Present_value = Future_value / (1 + rate)
    
    print (Present_value)
else:
    Present_value = float(input("How much is the present value? "))
    
    rate = int(input("how much the rate? "))
    rate = rate / 100
    
    years = int(input("For how many years? "))
    
    Future_value = Present_value * ((1 + rate)** years)
    
    if years is None:
        Future_value = Present_value * (1 + rate)
    
    print(Future_value)
    
        
    
