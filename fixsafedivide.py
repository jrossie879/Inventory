def safe_divide(a, b):
    if b == 0:
        return("Cannot divide by zero")
    print(a/b)
print(safe_divide(10, 0))


def next_age(age_text):
    # Bug to fix: age_text is text, so convert it before adding.
    age = int(age_text)
    age = age + 1
    return 

            