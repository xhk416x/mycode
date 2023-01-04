#!/usr/bin/env python3
"""Understanding dictionaries
   {key: value, key:value, ...}
   using the del keyword with a dict
   adding and removing values from the dict"""

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

    # remove a value from our dictionary using del
    del switch["vendor"]   # this just removes key/value pair and returns nothing
    # del switch["pizza"]  # if you try to delete a key that does not exist
                           # it will return an error!!

    # remove a value from our dictionary using a method
    print( "Seventh test - .pop()" )
    print(switch.pop("version")) # removes this key and ALSO return the VALUE "1.2"
    print( switch.keys() )   # notice the value of version is gone
    print( switch.values() ) # notice the value 1.2


    # add a value to the dictionary
    print( "Eighth test - ADD a new value" )
    switch["adminlogin"] = "karl08"
    print( switch.keys() )
    print( switch.values() )

    # add another value to the dictionary
    print( "Ninth test - ADD a new value" )
    switch["password"] = "qwerty"
    print( switch.keys() )
    print( switch.values() )


    # select a value from the results
    # we must first convert this "list like" structure into an actual list
    # using the list()
    print(list(switch.values())[2]) # this selects the 2nd position (3rd item) from the list


# call our main function
if __name__ == "__main__":
    main()
