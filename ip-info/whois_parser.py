import re

def match(text, match_list):
    for string in match_list:
        pattern = string + ":\s+((?!\n).*)"
        match = re.search(pattern, text, re.MULTILINE|re.IGNORECASE)

        if match:
            return match.group(1).replace("\r", " ").replace("\n", " ")
        
    return None
