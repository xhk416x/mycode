import csv

## retrieve data set from excel
def get_csv(fileloc):

    d= [] # start with an empty list we will fill up

    with open(fileloc, "r") as host_list:
        for row in csv.DictReader(host_list):
            # first value of row == {'user': 'bender', 'ip': '10.10.2.3'}
            keypair= {row['user']: row['ip']}
            # first value of keypair == {'sw-1': 'arista_eos'}
            d.append(keypair)

    return d # return the completed dictionary -> {'sw-1': 'arista_eos', 'sw-2': 'arista_eos'}

x = get_csv("creds.csv")
print(x)