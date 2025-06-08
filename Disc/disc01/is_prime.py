def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return False
    else:
        count = 1
        while count < n:
            if n % count == 0 and count != 1:
                return False
            count += 1
        return True
