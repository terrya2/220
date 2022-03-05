def hourly_wages(in_file_name, out_file_name):
    file = open(in_file_name, "r")
    out_file = open(out_file_name, "a")
    text = file.read()
    x = text.split("\n")
    for person in x:
        data = person.split()
        hourly_wage = eval(data[2])
        number_of_hours_worked = eval(data[3])
        pay = (number_of_hours_worked * hourly_wage) + (1.65 * number_of_hours_worked)
        out = data[0] + " " + data[1] + " " + "{:.2f}" + "\n"
        out_file.write(out.format(pay))
    file.close()
    out_file.close()