def number_prompt():

    while True: 
      user_number= int(input("enter a number between between 5 and 12 (inclusive): "))
      if 5 <= user_number <= 12:
        print("You entered the number:", user_number)
        return user_number
      else:
        print("try agian!")
        
     while True: 

      user_number_plus_one = user_number + 1
      user_number_two=int(input(f"enter a number between {user_number_plus_one} and 30: "))
      if user_number_plus_one <= user_number_two <= 30:
        print("You entered the number:", user_number_two)
        return user_number_two
      else:
        print("try agian!")
   


    

def problem_three():
    # put the code for problem 3 here
    print()

def problem_four():
    # put the code for problem 4 here
    print()

def problem_five():
    # put the code for problem 5 here
    print()

def fizz_buzz():
    # put the code for extra problem here
    print()


def main():
    number_prompt()
    problem_three()
    problem_four()
    problem_five()
    fizz_buzz() #extra credit

if __name__ == '__main__':
    main()
