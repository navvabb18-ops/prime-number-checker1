def finding_prime_or_composite_number ():
    while True :

        #asking question---------------
        try:
            customer_number = int(input ("enter your number = "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        #thinking-----------------------
        if customer_number < 2 :
            print ("your number isn't composite or prime!!")
            continue
        
        for i in range(2, customer_number):
            if customer_number % i == 0:
                print("your number is composite !!")
                break
        else:
            print("your number is prime !!")

        #repeat_question-----------------
        while True :
            ask_question = input ("again ? y/n = ")
            if ask_question.lower() == "y":
                break
            elif ask_question.lower() == "n":
                print ("Thank for using this code !!")
                return
            else :
                print ("please enter y or n !!")

finding_prime_or_composite_number()