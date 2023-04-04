import pycountry
import re
import subprocess
import whois_parser

class IP:
    def __init__(self, addr, user_agent, count):
        self.addr = addr
        self.user_agent = user_agent

        self.occurrences = 1
        self.count_min = count
        self.count_max = count

        self.whois = subprocess.run(["whois", addr], stdout=subprocess.PIPE).stdout.decode("ISO-8859-1")
        country_code = whois_parser.match(self.whois, ["country"])
        try:
            self.whois_country = pycountry.countries.get(alpha_2=country_code).name
        except:
            self.whois_country = country_code
        self.whois_org = whois_parser.match(self.whois, ["org", "orgname", "organization", "registrar", "netname", "responsible"])

    def update(self, count):
        self.occurrences += 1
        self.count_min = min(self.count_min, count)
        self.count_max = max(self.count_max, count)

    def output_header():
        return ["IP", "Max Count", "Min Count", "Occurrences", "User Agent", "Country", "Org"]
    
    def output(self):
        return [self.addr, self.count_max, self.count_min, self.occurrences, self.user_agent, self.whois_country, self.whois_org]
