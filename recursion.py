def countdown(i):
    if(i >= -100):
        print(i)
        countdown(i-1)
        
countdown(10)
 #the above is a simple recursive function

def count_down(i):
    print(i)
    if i  <=1:  #base case
        return
    else:
        count_down(i-1) # recursive case

count_down(10)


def fact(x):
    if x == 1:  # base case
        return 1
    else:
        ans = x * fact(x - 1) 
        print(f"{x}! = {ans}")
        return ans

fact(10)



"""
A recursive function without as stop is turns into an infinite loop
A recursive function has two parts:
 -> The base case - when the functions comes to a stop i.e does not call itself again
 -> The recursive case - when the fucntions calls itself

"""