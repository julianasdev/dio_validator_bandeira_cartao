import re

def validate_card_number(card_number):
    # Remove whitespace and hyphens
    card_number = card_number.replace(" ", "").replace("-", "")
    
    card_patterns = {
        "MasterCard": r"^5[1-5][0-9]{14}$",
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "American Express": r"^3[47][0-9]{13}$",
        "Diners Club": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
        "EnRoute": r"^(2014|2149)[0-9]{11}$",
        "JCB": r"^(?:2131|1800|35\d{3})\d{11}$",
        "Voyager": r"^8699[0-9]{11}$",
        "HiperCard": r"^(606282|3841)[0-9]{10,12}$",
        "Aura": r"^50[0-9]{14,17}$"
    }
    
    for brand, pattern in card_patterns.items():
        if re.match(pattern, card_number):
            return brand
    
    return "Unknown"

# Example usage
card_number = "5069 1366 8742 1908"
print(validate_card_number(card_number))  # Output: Aura"