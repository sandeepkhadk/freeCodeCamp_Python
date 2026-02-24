def square_root_bisection(num,tol=0.01,max_iter=50):
    if num<0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if num==0 or num==1:
        print(f"The square root of {num} is {num}")
        return num
    a=0 
    b=max(1,num)
    for i in range(1,max_iter+1):
        m=(a+b) / 2
        if (b - a)/2<= tol:
            print(f"The square root of {num} is approximately {m}")
            return m
        if m*m > num:
            b=m
        else:
            a=m
    print(f"Failed to converge within {max_iter} iterations")
    return None