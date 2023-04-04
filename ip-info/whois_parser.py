import re

def match(text, match_list):
    for string in match_list:
        # pattern = string + ":\s+((?!\n).*)"
        pattern = string + ":\s+(.*)$"
        match = re.search(pattern, text, re.MULTILINE|re.IGNORECASE)

        if match:
            result = match.group(1).replace("\r", " ").replace("\n", " ")
            if result == "REDACTED FOR PRIVACY":
                continue
            else:
                return result
        
    return None
