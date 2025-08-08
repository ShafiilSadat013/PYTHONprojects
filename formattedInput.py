#answer = my_function()
#print(answer)
def format_name(f_name,l_name):
    formated_fname = f_name.title()
    formated_lname = l_name.title()
   # print(f"{formated_fname} {formated_lname}")
    return f"{formated_fname} {formated_lname}"


first = input("1st name? : ")
second = input("last name ? : ")
formated_string = format_name(first,second)
#formated_string = format_name(f_name="wAynE",l_name="wAYNe")
print(formated_string)

def function_1(text):
    return text + text
def function_2(text):
    return text.title()

#output =  function_1("hello")
output  = function_2(function_1("hello")) #using f1s output in f2s input
print(output)
