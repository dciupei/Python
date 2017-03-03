def fib (n, depth):
    print 1 * depth * "-" + "computing fibonacci(", n, ") + fibonacci(", n, ")"
    if n == 0:
        return 0
    #if fibonacci is 0 result will equal 0
    if n <= 2:
        return 1
    #if n is less then or equal to 2 it will return it to 1 because fib of 2 is 1 and fib of 1 is 1
    else:
        return fib(n - 1, depth + 1) + fib(n - 2, depth + 1)
# did not know how to test the function fibonacci    
def test():
    assert fib(1,1) == 1, "fib(1) should be 1"
    assert fib(2,1) == 1, "fib(2) should be 1"
    assert fib(12,1) == 144, "fib(12) should be 144"
    print "congrats"
test()    
    

            
            

        
         
    