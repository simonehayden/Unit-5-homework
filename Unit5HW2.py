def number_prompt():

      while True: 
          
          user_number= int(input("enter a number between between 5 and 12 (inclusive): "))
          if user_number < 5 or user_number > 12:
              print("try agian!")
              continue
          else:
              print("You entered the number:", user_number)
          break

      while True: 

          user_number_plus_one = user_number + 1
          user_number_two=int(input(f"enter a number between {user_number_plus_one} and 30: "))
          if user_number_plus_one <= user_number_two <= 30:
              print("You entered the number:", user_number_two)
              return user_number_two
          else:
              print("try agian!")
    

def problem_three():
    for i in range(4):
        print("****")

def problem_four():
    for i in range(7):
        print("*****")
        
    
def problem_five():
   for i in range(5):
       print("*******")

def fizz_buzz():
    number=int(input("enter a number: "))
    for i in range(1,number + 1):
        if i % 3 == 0:
            print ("Fizz")
        elif i % 5== 0:
            print("Buzz")
        elif i % 15==0:
            print("FizzBuzz")
        else:
        print(i)
                
        
    
def main():
    number_prompt()
    problem_three()
    problem_four()
    problem_five()
    fizz_buzz() #extra credit

if __name__ == '__main__':
    main()
