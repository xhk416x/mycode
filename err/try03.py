#!/usr/bin/python3
"""try except and else | Alta3 Research"""

# Start with an infinite loop
while True:
    try:
        print("\nLet's divide x by y!")
        x = int(input("What is the integer value of x? "))
        y = int(input("What is the integer value of y? "))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as err:
        print("Handling run-time error:", err)
    except ValueError as err:
        print("That was not a legal value for division:", err)
    # general error handling
    # a practical use might be exceptions we haven't designed solution for yet
    except Exception as err:
        # sys.exc_info returns a 3 tuple with into about the exception handled
        print("We did not anticipate that:", err)
        # raise by itself simply calls the previous exception that was thrown
        raise
    # else ONLY runs if there wasn't any errors
    else:
        print("\nThanks for learning to handle errors!")
        break
