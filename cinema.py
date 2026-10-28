def get_ticket_price(age, is_student):
    if age < 0 or age > 110:
        return "Invalid age"
    if age <= 12:
        return "$8."
    if age >= 65:
        return "$10."
    if is_student:
        return "$12."
    else:
        return "$15."