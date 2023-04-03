import re
import whois
import whois_parser

class IP:
    def __init__(self, addr, user_agent, count):
        self.addr = addr
        self.user_agent = user_agent

        self.occurrences = 1
        self.count_min = count
        self.count_max = count

        self.whois = whois.whois(addr)
        self.whois_text = self.whois.text
        text = self.whois.text
        self.whois_country = "-"
        self.whois_country = whois_parser.match(text, ["country"])
        self.whois_org = whois_parser.match(text, ["org", "orgname", "organization"])
        # match = re.search("^OrgName:\s+(.+)", self.whois.text, re.MULTILINE|re.IGNORECASE)
        # # match = re.match(r"OrgName:\s+((?!\n).*)", "OrgName:        DigitalOcean, LLC")
        # if match:
        #     self.whois_org = match.group(1)
        # else:
        #     self.whois_org = "-"
        # self.whois_org = self.match_org()

    def update(self, count):
        self.occurrences += 1
        self.count_min = min(self.count_min, count)
        self.count_max = max(self.count_max, count)

    def output_header():
        return ["IP", "Occurrences", "Min Count", "Max Count", "User Agent", "Country", "Org"]
    
    def output(self):
        return [self.addr, self.occurrences, self.count_min, self.count_max, self.user_agent, self.whois_country, self.whois_org]
    
    def match_country(self):
        match = re.match(r"country:\s+((?!\n).*)", self.whois_text, re.IGNORECASE)
        if match:
            return match.group(1)
        else:
            return None
        
    def match_org(self):
        match = re.match(r"OrgName:\s+((?!\n).*)", self.whois_text)
        if match:
            return match.group(1)
        else:
            return None
