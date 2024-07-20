#Functions with Outputs

def format_name(fname, lname):
    formated_f_name = fname.title() #.title() method returns an output by default, so we capture the output with a variable.
    formated_l_name = lname.title()
    return f"{formated_f_name} {formated_l_name}"

formated_name = format_name("HAMza", "ahmed")
print(formated_name)