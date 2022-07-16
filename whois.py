
from ipwhois import IPWhois

obj = IPWhois('20.189.173.1')
who = obj.lookup_whois()
print(who)
