def make_adder(x):
       def adder(y):
           return x+y
       return adder
make_adder(5)     
