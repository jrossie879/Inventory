raw_usernames = ["  @alex_99  ", "  BOB  ", "@JESS_DEV", "  ", "  @sam  ", "CATHY_PR0  "]

result = [
    u.strip().lstrip('@').upper() 
    for u in raw_usernames 
    if len(u.strip().lstrip('@')) >= 4
]

print(result)
