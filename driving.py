def can_drive(age, has_license):
    if age < 0 or > 120:
        return "Invalid age"
    elif age == 16:
        return "Eligible to drive"
    elif age <= 16:
        return "Must get a license first"
    elif age < 16:
        return "Too young to drive"
