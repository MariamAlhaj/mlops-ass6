import os, sys 
 
def bad_function( ): 
    x=1 
    y=2 
    z=x+y 
    return z 
 
bad_function() 
print("This will cause linter warnings") 
