def is_valid_email(email):
    
    # rule 1
    if "@" not in email:
        return "INVALID"
    elif email.count("@") > 1:
        return "INVALID"
    
    local_part, domain = email.split("@")
    
    # rule 6
    if not local_part or not domain:
        return "INVALID"
    
    # rule 4
    if domain.count(".") < 0:
        return "INVALID"
    
    # rule 5
    if domain.count("..") > 0:
        return "INVALID"
    
    local_allowed = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._')
    domain_allowed = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.')

    # rule 2
    for char in local_part:
        if char not in local_allowed:
            return "INVALID"
    
    # rule 3
    for char in domain:
        if char not in domain_allowed:
            return "INVALID"
    
    return "VALID"

email = input()
print(is_valid_email(email))