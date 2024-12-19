import calendar


# Function to show the calendar of a specific month
def show_month_calendar():
    year = int(input("Please, enter year: "))
    month = int(input("Please, enter month (1-12): "))

    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_calendar = cal.formatmonth(year, month)
    print(month_calendar)


# Call the function
show_month_calendar()
