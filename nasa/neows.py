#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/mycode/nasa/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## start date
    while True:
        try:    
            usr_start = input("Please write a date to start from (YYYY-MM-DD)")
            break
        except:
            print("That wasn't the right format")
            continue
    startdate = str("start_date=" + usr_start)

    ##end date
    while True:
        try:    
            usr_end = input("Please write a date to end on (YYYY-MM-DD)")
            break
        except:
            print("That wasn't the right format")
            continue
    enddate = str("end_date=" + usr_end)

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds + "&" + enddate)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()
