import os.path as os

save_path = '/Users/home/Downloads'

file = "Nombres_variables"

file_name_root = os.join(save_path, file+".txt")

file_final = open(file_name_root, "w+")

lista = []

print('Hola! Vamos a nombrar cosas')

x = input('Que cosa quieres nombrar\n')
# The default value is item
if x == '':
    x = 'Item'
else:
    x = x
y = input('Con que lo quieres separar\n')
# The default value is a plus
if y == '':
    y = '+'
else:
    y = y


n = input('Cantidad de filas\n')
try:
    thenum = int(n)
    if thenum == 0:
        n = 2
    else:
        n = int(n)
except ValueError:
    print("Not a valid number default assigned")
    n = int(30)
else:
   n = int(n)


for i in range(1,n):
    z = (x + str(i).ljust(1) + y)
    file_final.write(z)
file_final.close()

