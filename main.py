#!/bin/python3

import datetime as dt
import string


def groner_repr(val: int, base: int = 10, formatted_printout: bool = True) -> str:
    """ Return string nuber representation with base from 2 to 36 
    with or without base prefix
    
    Keyword arguments: 
    val                -- int, to be converted 
    base               -- int, conversion base 
    formatted_printout -- bool, include or not conversion base prefix 
    """
    
    rng = string.digits[::] + string.ascii_uppercase[::]
    
    res = ''
    is_negative = False
    
    if type(val) != int or type(base) != int or type(formatted_printout) != bool:
        raise TypeError("Argument type error")
    
    if val < 0:
        val = -val
        is_negative = True

    if base < 2 or base > 36:
        raise ValueError("Base should be in range from 2 to 36")
    
    while val > base:
        res += str(rng[val % base])
        val //= base
    else:
        res += str(rng[val%base])
    
    res = res[::-1]
    
    if formatted_printout:
        res = f'0[{str(base)}]' + res
    
    if is_negative:
        res = '-' + res
    
    return res


def main():
    print("Hello World!")
    print("It's alive!")
    print("Current time and date is: ", dt.datetime.now())

if __name__ == '__main__':
    main()
