# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin?"))
#int( added before input. Single closing quote changed to double quote.
#Deleted one equal

if year <= 1900:
#Added colon 
    print ("Woah, that's the past!")
#open and close Single quotes changed to double.
#works
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
# replaced '&' with 'and'
#works
elif year:
    print ("Far out, that's the future!!")
#added 'year:'
#works

