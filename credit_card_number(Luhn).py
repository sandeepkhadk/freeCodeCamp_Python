def verify_card_number(card_number):
   
    # Remove dash and space
    card_number = card_number.replace("-", "").replace(" ", "")

    # Convert string to list of integers
    digits = []
    for ch in card_number:
        digits.append(int(ch))

    # Reverse digits
    digits.reverse()

    total = 0

    for i in range(len(digits)):
        if i % 2 == 1:
            d = digits[i] * 2
            if d >= 10:
                d = d // 10 + d % 10
            total += d
        else:
            total += digits[i]

    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


# User input
card = input("Enter card number: ")

# Function call
result = verify_card_number(card)

print(result)