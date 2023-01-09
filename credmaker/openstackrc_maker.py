#!/usr/bin/env python3
outFile = open("admin.rc", "a")
osAUTH = input("What is the OS_AUTH_URL? ")
print("export OS_AUTH_URL=" + osAUTH, file=outFile)

print("export OS_IDENTITY_API_VERSION=3", file=outFile)

osPROJ = input("What is the OS_PROJECT_NAME? ")
print("export OS_PROJECT_NAME=" + osPROJ, file=outFile)

osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME? ")
print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outFile)

osUSER = input("What is the OS_USERNAME? ")
print("export OS_USERNAME=" + osUSER, file=outFile)

osUSERDOM = input("What is the OS_USER_DOMAIN_NAME? ")
print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outFile)

osPASS = input("What is the OS_PASSWORD? ")
print("export OS_PASSWORD=" + osPASS, file=outFile)
outFile.close()
