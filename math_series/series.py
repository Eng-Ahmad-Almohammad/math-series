def fibonacci(n):
    """ base case """
    if (n == 0):
        return 0
    """ base case """
    if (n == 1):
        return 1
    if(n<0):
        return "Negative values are not allowable"
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    # """ Recursion
    # fibonacci(5) = fibonacci(4)+fibonacci(3)
    #                fibonacci(3)+fibonacci(2)+fibonacci(2)+fibonacci(1)
    #                fibonacci(2)+fibonacci(1)+fibonacci(1)+fibonacci(0)+fibonacci(1)+fibonacci(0)+1
    #                fibonacci(1)+fibonacci(0)+1+1+0+1+0+1
    #                1+0+1+1+0+1+0+1 = 5

    # """


def lucas(n):
    """base case"""
    if (n==0):
        return 2
    """base case"""
    if (n==1):
        return 1
    if (n<0):
        return "Negative values are not allowable"
    
    else:
        return lucas(n-1)+lucas(n-2)
   
# """ Recursion
    # lucas(5) = lucas(4)+lucas(3)
    #                lucas(3)+lucas(2)+lucas(2)+lucas(1)
    #                lucas(2)+lucas(1)+lucas(1)+lucas(0)+lucas(1)+lucas(0)+1
    #                lucas(1)+lucas(0)+1+1+2+1+2+1
    #                1+2+1+1+2+1+2+1 = 11

    # """



def non_fibonacci_lucas(required, first_num, second_num):
    """Base case"""
    if (required==0):
        return first_num
    """Base case"""
    if (required==1):
        return second_num
    if (required<0):
        return "Negative values are not allowable"
    else:
        return non_fibonacci_lucas(required-1, first_num, second_num)+ non_fibonacci_lucas(required-2, first_num, second_num)


# """ Recursion
    # non_fibonacci_lucas(5,1,1) = non_fibonacci_lucas(4,1,1)+non_fibonacci_lucas(3,1,1)
    #                non_fibonacci_lucas(3,1,1)+non_fibonacci_lucas(2,1,1)+non_fibonacci_lucas(2,1,1)+non_fibonacci_lucas(1,1,1)
    #                non_fibonacci_lucas(2,1,1)+non_fibonacci_lucas(1,1,1)+non_fibonacci_lucas(1,1,1)+non_fibonacci_lucas(0,1,1)+non_fibonacci_lucas(1,1,1)+non_fibonacci_lucas(0,1,1)+1
    #                non_fibonacci_lucas(1,1,1)+non_fibonacci_lucas(0,1,1)+1+1+1+1+1+1
    #                1+1+1+1+1+1+1+1 = 8

    # ""

def sum_series(required,first_num=0,second_num=1):
    if(first_num ==0 and second_num==1):
        print(fibonacci(required))
    
    elif (first_num==2 and second_num==1):
        print(lucas(required))

    else:
        print(non_fibonacci_lucas(required,first_num,second_num))



sum_series(-5,2,20)


