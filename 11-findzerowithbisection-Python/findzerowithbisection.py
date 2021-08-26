# Bisection Algorithm comes into play!
# We know that the square root of x lies between 1 and x, from mathematics
# Rather than exhaustively trying things starting at 1, 
# suppose instead we pick a number in the middle of this range
# Bisection search works when value of function varies monotonically with input
# If g, the users input/guess, is less than/greater than the midpoint of the range, 
# then that number becomes the new high point of said range and is then factored into the new search.

"""
1 2 3 4 5 6 7 8 9 10
"""
def findzerowithbisection(x,epsilon):
    low = 0
    high = max(1.0,x)
    y = (high+low)/2.0
    while abs(y**2-x)>=epsilon:
        if y**2 < x:
            low = y
        else:
            high = y
        y = (high+low)/2.0
    return y
