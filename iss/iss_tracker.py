#!/usr/bin/env python3
"""script to read the ISS location with timestamp"""

import requests
import json
import time
import reverse_geocoder

iss_local = "http://api.open-notify.org/iss-now.json"
iss_gps= (response["iss_position"]["latitude"],response["iss_position"]["longitude"])
response= requests.get(iss_local).json()

def main():
    print("CURRENT LOCATION OF THE ISS:")
    print(time.strftime('%m-%d-%Y %H:%M:%S', time.localtime()))
    print("Long: ", response["iss_position"]["longitude"])
    print("Lat: ", response["iss_position"]["latitude"])
    print("City, State/Province, Country: ", reverse_geocoder.search(iss_gps)[0]["name"], ", ", reverse_geocoder.search(iss_gps)[0]["admin1"], ", ", reverse_geocoder.search(iss_gps)[0]["cc"], sep="")

if __name__ == "__main__":
    main()