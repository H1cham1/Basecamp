import re

License_Plate = input("Please enter your license plate: ").upper()



Valid_License_Plates =     [r'^[A-Z]{1,2}-[0-9]{1,2}-[0-9]{1,2}$',
                r'^[0-9]{1,2}-[0-9]{1,2}-[A-Z]{1,2}$',
                r'^[0-9]{1,2}-[A-Z]{1,2}-[0-9]{1,2}$',
                r'^[A-Z]{1,2}-[0-9]{1,2}-[A-Z]{1,2}$',
                r'^[A-Z]{1,2}-[A-Z]{1,2}-[0-9]{1,2}$',
                r'^[0-9]{1,2}-[A-Z]{1,2}-[A-Z]{1,2}$',
                r'^[0-9]{1,2}-[A-Z]{1,3}-[0-9]{1}$',
                r'^[0-9]{1}-[A-Z]{1,3}-[0-9]{1,2}$',
                r'^[A-Z]{1,2}-[0-9]{1,3}-[A-Z]{1}$',
                r'^[A-Z]{1}-[0-9]{1,3}-[A-Z]{1,2}$',
                r'^[A-Z]{1,3}-[0-9]{1,2}-[A-Z]{1}$',
                r'^[0-9]{1}-[A-Z]{1,2}-[0-9]{1,3}$'
                ]

Valid = any(re.match(pattern, License_Plate) for pattern in Valid_License_Plates)

if Valid: print("Valid")
else: print("Invalid")