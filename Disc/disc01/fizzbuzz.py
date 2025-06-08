def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    count = 1
    while count <= n:
        if count % 3 == 0 and count % 5 == 0:
            print("fizzbuzz")
        elif count % 3 == 0 and count % 5 != 0:
            print("fizz")
        elif count % 3 != 0 and count % 5 == 0:
            print("buzz")
        else:
            print(count)
        count += 1
    return None