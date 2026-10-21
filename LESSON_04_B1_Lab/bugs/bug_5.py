# Μετατρέπει λεπτά σε ώρες και λεπτά.
# Αναμενόμενο:  2 ώρες και 15 λεπτά
minutes = 135
hours = minutes / 60
rest = minutes % 60
print(hours, "ώρες και", rest, "λεπτά")
