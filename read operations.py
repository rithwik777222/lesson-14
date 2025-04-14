x = open('ttt.txt','r')
print(x.read())
x.close()

x = open('ttt.txt','r')
print('\n read in parts \n')
print(x.read(12))
x.close()

y = open('ttt.txt','a')
y.write("confusing lines")
y.close()