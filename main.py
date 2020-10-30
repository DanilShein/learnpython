#!/bin/python3

import datetime as dt
import string


def groner_repr(val: int, base: int = 10, use_standard_format: bool = True) -> str:
    """ Return string nuber representation with base from 2 to 36 
    using standard base prefix for binary, oct, decimal or hex or custom base prefix [base value]
    
    Keyword arguments: 
    val                 -- int, to be converted 
    base                -- int, conversion base 
    use_standard_format -- bool, include or not conversion base prefix 
    """
    
    rng = string.digits[::] + string.ascii_uppercase[::]
    
    res = ''
    is_negative = False
    
    if type(val) != int or type(base) != int or type(use_standard_format) != bool:
        raise TypeError("Argument type error")
    
    if base < 2 or base > 36:
        raise ValueError("Base should be in range from 2 to 36")
    
    if use_standard_format:
        if base == 2:
            return bin(val)
        elif base == 8:
            return oct(val)
        elif base == 10:
            return str(val)
        elif base == 16:
            return hex(val)
    
    if val < 0:
        val = -val
        is_negative = True
    
    while val > base:
        res += str(rng[val % base])
        val //= base
    else:
        res += str(rng[val%base])
    
    res = f'0[{str(base)}]' + res[::-1]
    
    if is_negative:
        res = '-' + res
    
    return res


def main():
    print("Hello World!")
    print("It's alive!")
    print("Current time and date is: ", dt.datetime.now())

if __name__ == '__main__':
    main()
