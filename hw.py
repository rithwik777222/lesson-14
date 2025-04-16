fr = open('tttt3.txt','r')
print("file i read mode")
print(fr.read())
fr.close()

fw = open('tttt3.txt','w')

fw.write('file in write mode')
fw.write("\n everything on a keyboard")
fw.close()

fa = open('tttt3.txt','a')
fa.write("\n file in append mode")
fa.write('\n idek what to type after this T_T')
fa.close()

fr = open('tttt3.txt','r')
print('\n read in parts \n')
print(fr.read(26))
fr.close()

fa = open('tttt3.txt','a')
fa.write("\n confusing lines")
fa.close()