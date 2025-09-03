"""
String Comparison & Using Boolean in Ternary
"""
password = input("Enter Password: ")

success = "Access Granted" if password == "OpenSesame"  else "Access Denied"

has_permission = True if success == "Access Granted" else False
print(has_permission)

status = "Allowed" if has_permission == True else "Denied"
print(status)

"""
Function Returns Function
"""

def make_adder(num):
    return lambda n: num + n


add_5 = make_adder(5)

print(add_5(3))