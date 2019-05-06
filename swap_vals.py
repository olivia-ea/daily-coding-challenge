def swap_vals(x, y):
    """
    Swap x and y values without creating a temp val.
    """

    x = x + y
    y = x - y 
    x = x - y 
    
    print('x: ', x, 'y: ', y)
    