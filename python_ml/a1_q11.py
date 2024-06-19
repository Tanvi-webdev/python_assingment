#Write a python program that generates the first n numbers in the Fibonacci sequence.

def fibonacci(n):
  fibonacci_series=[0,1]
  for i in range(2,n) :
    next = fibonacci_series[-1] + fibonacci_series[-2]
    fibonacci_series.append(next)
  return fibonacci_series


n = int(input("Enter the number of fibonnaci numbers to generated "))
fibonacci_number = fibonacci(n)
print(fibonacci_number )