"""5.Write a program to print the Fibonacci series till n terms (Accept n from user) using while loop. (Bonus
1.ask user to input the number where they want to stop to print the fibonacci series.
and assign it to the varaible un.
2.declare the variable no1 no2 qnd no3 and assign it the value 0, 1 and 0 respectively
3.run while loop until no3 is less than user input
4 print no3 till the loop stops .
where
no1=no2(this is how the fibonacci series run.)
no2=no3
no3=no2+no1
"""

un=input("enter number to stop series")
un=int(un)
no1=0#(first number)
no2=1#(second number)
no3=0#(third number)
while no3<un:
    print(no3)
    no1=no2
    no2=no3
    no3=no1+no2
   
   