#Declaring variables for ten types of books
"The Hound of the Baskervilles"
"a tigger skinner"
"carlson"
"spiral"
"Me, grandmother and Hilarion"
"READER,I MURDERED HIM"
"thirteen dorways wolves behind them all"
"one of us is lying"
"the heart is a lonely hunter"
"how the dead speak"

#Declare variables for ten types of book prices
price_The_Hound_of_the_Baskervilles = 150
price_a_tigger_skinner = 150
price_carlson = 150
price_spiral = 150
price_me_grandmother_and_hilarion = 150
price_READER_I_MURDERED_HIM = 150
price_thirteen_dorways_wolves_behind_them_all = 150
price_one_of_us_is_lying = 150
price_the_heart_is_a_lo0nely_hunter = 150
price_how_the_dead_speak = 150

#discounte of 10%
discount01 = 10
discount02 = 10
discount03 = 10
discount04 = 10
discount05 = 10

#adding discounts01 -10%
price_after_discount01 = price_The_Hound_of_the_Baskervilles - price_a_tigger_skinner * discount01 / 150
print(price_after_discount01)
price_after_discount02 = price_carlson - price_spiral * discount02 / 150
print(price_after_discount02)
price_after_discount03 = price_me_grandmother_and_hilarion - price_a_tigger_skinner * discount03 / 150
print(price_after_discount03)

#discounte of 20%
discount06 = 20
discount07 = 20
discount08 = 20
discount09 = 20
discount10 = 20

#adding discount02 -20%
price_after_discount1 = price_READER_I_MURDERED_HIM - price_thirteen_dorways_wolves_behind_them_all * discount06 / 150
print(price_after_discount1)
price_after_discount2 = price_one_of_us_is_lying - price_the_heart_is_a_lo0nely_hunter * discount07 / 150
print(price_after_discount2)
price_after_discount3 = price_one_of_us_is_lying - price_how_the_dead_speak * discount08 / 150
print(price_after_discount3)






