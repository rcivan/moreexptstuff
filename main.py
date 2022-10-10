from time import perf_counter

def expt(x,n):
  if n < 0:
    raise ValueError("n = {} is less than zero".format(n))
  
  if n == 0:
    return 1
  elif n % 2 == 0:
    result=expt(x,n//2)
    return result*result
  else:
    return x * expt(x, n-1)

def old_expt(x,n):
  if n < 0:
    raise ValueError("n = {} is less than zero".format(n))

  result=1
  for _ in range(n):
    result *= x

  return result

def main():
  n = 17
  x = 10
  f = open("expt_data.csv", "w")
  f.write("exponent,min_runtime_old,min_runtime_new\n")
  for i in range(10000):
    minimum_time = 9999
    min2=9999
    for _ in range(x):
      current_time = perf_counter()
      temp = expt(n,i)
      elapsed_time = perf_counter()-current_time
      if elapsed_time<minimum_time:
        minimum_time=elapsed_time
    for _ in range(x):
      current_time=perf_counter()
      temp=old_expt(n,i)
      elapsed_time=perf_counter()-current_time
      if elapsed_time<min2:
        min2=elapsed_time
    f.write(f"{i}, {min2},{minimum_time}\n")
  f.close

if __name__ == '__main__':
  main()