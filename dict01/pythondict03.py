#!/usr/bin/env python3
"""Understanding dictionaries
   {key: value, key:value, ...}
   using dict.keys() and dict.values()"""

def main():
    """runtime function"""

    ## create a dictionary with 4 key:value pairs
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    ## display the entire dictionary
    print(switch)

    ## proove that switch is indeed a dictionary
    print(type(switch))

    ## display parts of the dictionary
    print( switch["hostname"] )    # displays "sw1"
    print( switch["ip"] )          # displays "10.0.1.1"

    ## request a 'fake' key
    # print( switch["lynx"] )   # Be sure to comment out this line,
                                # or your program will CONTINUE to fail!
                                # if a KEY is requested that does not exist,
                                # an ERROR will be thrown!

    ## request a 'fake' key with .get() method
    print( "First test - .get()" )
    print( switch.get("lynx") ) # alternative to switch["lynx"]
    #print(switch.get("lynx", None)) # this is what is actually being run...
                                     # by default dict.get() returns "None"

    # if you want to customize what is returned when the key is not found
    print( "Second test - .get()" )
    print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!") )

    print( "Third test - .get()" )
    print( switch.get("version") ) # alternative to switch['version']
                                   # this key exists, so it will return a value of "1.2"

    # this returns all of the keys in the dictionary
    print( "Fourth test - .keys()" )
    print( switch.keys() )    # dict.keys() returns all the keys in a "list like" structure

    # return all of the values in the dictionary
    print( "Fifth test - .values()" )
    print( switch.values() )  # dict.values() returns all of the values in a "list like" structure



# call our main function
if __name__ == "__main__":
    main()
