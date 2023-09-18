def oxford_comma(items):
    
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return items[0] + " and " + items[1]
    else:
        return ", ".join(items[0:-1]) + ", and " + items[-1]
