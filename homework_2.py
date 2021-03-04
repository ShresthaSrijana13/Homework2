# Srijana Shrestha
# 1918305
import datetime  # to import current date

# making month dictionary
month_dict = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6", "july": "7",
              "august": "8", "september": "9", "october": "10", "november": "11", "december": "12"}

input_file = ['march 9, 2020']

for line in input_file:
    first_space = line.find(" ")  # using find function to get the index of the first space
    second_space = line.find(" ", first_space + 1, -1)  # using find function to get the index of the second space

    if first_space != -1:  # to get rid of date without any space
        month_name = line[:first_space]  # get month name
        year = line[second_space + 1:]   # get year
        day = line[first_space + 1:second_space - 1]  # get day

        if month_name.lower() in month_dict:  # covert the month name in lower case and check if it is in dictionary
            month_number = (month_dict[month_name.lower()])  # get month number with its corresponding month name
            ans = month_number + "/" + day + "/" + year  # get the final result

            # Get the result in year month day format
            ans_date = datetime.datetime(int(year), int(month_number), int(day))
            current_date = datetime.datetime.now()  # get the current date in year month day format
            if current_date >= ans_date:  # compare current date with the result date
                print(ans)  # print the final result
