def card_hide(card_number):
    if len(card_number) > 4:
        card_number = '*' * (len(card_number) - 4) + card_number[len(card_number) - 4:]
    return card_number
