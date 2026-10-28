def can_ride_coaster(height_cm, age, has_heart_condition):
    if height_cm < 50 or height_cm > 250 or age < 0 or age > 120:
        return "Invalid data"
    if has_heart_condition:
        return "Not safe: heart condition"
    if height_cm >= 140 and age >= 10:
        return "Allowed to ride alone"
    if height_cm >= 120 and age >= 8:
        return "Allowed to ride with an adult"
    else:
        return "Not allowed on coaster"