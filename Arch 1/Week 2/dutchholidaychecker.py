Holiday_List = {"Month: 1, Day: 1" : "Nieuwjaarsdag", 
                "Month: 4, Day: 7" : "Goede Vrijdag",
                "Month: 4, Day: 9" : "Pasen",
                "Month: 4, Day: 10" : "Pasen",
                "Month: 4, Day: 27" : "Koningsdag",
                "Month: 5, Day: 5" : "Bevrijdingsdag",
                "Month: 5, Day: 18" : "Hemelvaartsdag",
                "Month: 5, Day: 28" : "Pinksteren",
                "Month: 5, Day: 29" : "Pinksteren",
                "Month: 12, Day: 25" : "Kerst",
                "Month: 12, Day: 26" : "Kerst"}


Date = input("Please provide a Month and Day: ")

if Date in Holiday_List: 
    Holiday = Holiday_List[Date]
    print(f"{Holiday}")
elif Date not in Holiday_List: print("No holiday found on given input")
else: print("Please enter a valid date")