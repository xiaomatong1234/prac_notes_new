from chap9_8 import Admin
eric = Admin('eric', 'matthes', 90)

eric_privileges = [
 'can reset passwords',
 'can moderate discussions',
 'can suspend accounts',
 ]
eric.privileges.privileges = eric_privileges
print(f"\nThe admin has these privileges: ")
eric.privileges.show_privileges()