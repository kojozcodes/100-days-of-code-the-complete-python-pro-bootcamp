#Functions with Outputs

def format_name(fname, lname):
    """Take the first name and last name and format it to return the title case version of the name."""

    if fname == "" or lname == "":
        return "You did not provide vaild inputs" #return as an early exit
    formated_f_name = fname.title() #.title() method returns an output by default, so we capture the output with a variable.
    formated_l_name = lname.title()
    return f"{formated_f_name} {formated_l_name}"

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")

formated_name = format_name(first_name, last_name)
print(formated_name)