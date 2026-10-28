def sanitize_phone_numbers(numbers):
    return [
        f"({numbers.strip()[:3]}) {numbers.strip()[3:6]}-{numbers.strip()[6:]}"
        for numbers in numbers
        if numbers.strip().isdigit() and len(numbers.strip()) == 10
    ]