from telebot import types

def button():
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sum_to_dollar = types.KeyboardButton(text='UZS > USD($)')
    dollar_to_sum = types.KeyboardButton(text='USD($) > UZS')

    btn.add(sum_to_dollar, dollar_to_sum)
    return btn

def back_btn(qwe=1):
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if qwe == 1:
        button_back = types.KeyboardButton(text='Back')
        btn.add(button_back)
    else:
        button_again = types.KeyboardButton(text='Again')
        button_back = types.KeyboardButton(text='Back')
        btn.add(button_back, button_again)

    return btn

def again_btn():
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_again = types.KeyboardButton(text='Again')

    btn.add(button_again)
    return btn
