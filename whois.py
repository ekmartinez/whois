
import sys
from ipwhois import IPWhois

def who(ipaddress):

    obj = IPWhois(ipaddress)
    who = obj.lookup_whois()['nets'][0]
    
    data = '\nLookup Information:' + '\n'+'-'*30 + "\n" + ipaddress + "\n" \
            + who["description"] + f'\n{who["city"]} {who["state"]} {who["postal_code"]}' + "\n" + who["country"]  + '\n'+'-'*30
    
    return data

if __name__ == '__main__':
    print(who(sys.argv[1]))

