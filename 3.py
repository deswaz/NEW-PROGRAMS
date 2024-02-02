def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        regular_hours = 40
        overtime_hours = hours - 40
        pay = (regular_hours * rate) + (overtime_hours * 1.5 * rate)
    return pay

hours_str = input("Enter hours worked: ")
rate_str = input("Enter hourly rate: ")

hours = float(hours_str)
rate = float(rate_str)

pay = computepay(hours, rate)
print("Gross Pay:", pay)