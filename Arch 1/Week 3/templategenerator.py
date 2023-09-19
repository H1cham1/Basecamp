import re

while True:
    More_Letters = input("More letters? (Yes or No): ").capitalize()
    if More_Letters == "No":
        break

    elif More_Letters == "Yes":
        Offer_Or_Rejection = input("Job Offer or Rejection?: ").capitalize()
        if Offer_Or_Rejection == "Job Offer" or Offer_Or_Rejection == "Job offer":
            while True:
                First_Name = input("First name?: ").capitalize()
                First_Name_Length = len(First_Name)
                if First_Name_Length < 2 or First_Name_Length > 10:
                    print("Input Error")
                else:
                    break
            while True:
                Last_Name = input("Last name?: ").capitalize()
                Last_Name_Length = len(Last_Name)
                if Last_Name_Length < 2 or Last_Name_Length > 10:
                    print("Input Error")
                else:
                    break
            while True:
                Job_Title = input("Job title?: ").capitalize()
                contains_numbers = False
                for char in Job_Title:
                    if char.isdigit():
                        contains_numbers = True
                        break
                Job_Title_Length = len(Job_Title)
                if Job_Title_Length < 10 or contains_numbers is True:
                    print("Input Error")
                else:
                    break
            while True:
                Annual_Salary_Str = input("Annual Salary?: ")
                Annual_Salary_Str2 = Annual_Salary_Str.replace('.', '').replace(',', '')
                Annual_Salary = int(Annual_Salary_Str2)
                Annual_Salary_Min = 2000000
                Annual_Salary_Max = 8000000
                if Annual_Salary < Annual_Salary_Min or Annual_Salary > Annual_Salary_Max:
                    print("Input Error")
                else:
                    break
            while True:
                Start_Date = input("Start date? (YYYY-MM-DD): ")
                Invalid_Date = not re.match(r'^(2022|2021)-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$', Start_Date)
                if Invalid_Date:
                    print("Input Error")
                else:
                    break
            Offer_Letter = f"""
Here is the final letter to send:
Dear {First_Name} {Last_Name},
After careful evaluation of your application for the position of {Job_Title},
we are glad to offer you the job. Your salary will be {Annual_Salary_Str} euro annually.
Your start date will be on {Start_Date}. Please do not hesitate to contact us with any questions.
Sincerely,
HR Department of XYZ
            """
            print(Offer_Letter)

        elif Offer_Or_Rejection == "Rejection":
            while True:
                First_Name = input("First name?: ").capitalize()
                First_Name_Length = len(First_Name)
                if First_Name_Length < 2 or First_Name_Length > 10:
                    print("Input Error")
                else:
                    break
            while True:
                Last_Name = input("Last name?: ").capitalize()
                Last_Name_Length = len(Last_Name)
                if Last_Name_Length < 2 or Last_Name_Length > 10:
                    print("Input Error")
                else:
                    break
            while True:
                Job_Title = input("Job title?: ").capitalize()
                contains_numbers = False
                for char in Job_Title:
                    if char.isdigit():
                        contains_numbers = True
                        break
                Job_Title_Length = len(Job_Title)
                if Job_Title_Length < 10 or contains_numbers is True:
                    print("Input Error")
                else:
                    break
            Feedback = input("Feedback? (Yes or No): ").capitalize()
            while True:
                if Feedback == "Yes":
                    Text_Feedback = input("Enter your Feedback (One Statement): ").capitalize()
                    RejectionF_Letter = f"""
Here is the final letter to send:
Dear {First_Name} {Last_Name},
After careful evaluation of your application for the position of {Job_Title},
at this moment we have decided to proceed with another candidate.
Here we would like to provide you our feedback about the interview.
{Text_Feedback}
We wish you the best in finding your future desired career.
Please do not hesitate to contact us with any questions.
Sincerely,
HR Department of XYZ"""
                    print(RejectionF_Letter)
                    break
                elif Feedback == "No":
                    Rejection_Letter = f"""
Here is the final letter to send:
Dear {First_Name} {Last_Name},
After careful evaluation of your application for the position of {Job_Title},
at this moment we have decided to proceed with another candidate.
We wish you the best in finding your future desired career.
Please do not hesitate to contact us with any questions.
Sincerely,
HR Department of XYZ"""
                    print(Rejection_Letter)
                    break
    else:
        print("Input Error")