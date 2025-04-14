fr = open('ttt2.txt','r')
print("file i read mode")
print(fr.read())
fr.close()

fw = open('ttt2.txt','w')

fw.write('file in write mode')
fw.write("i am a penguin(help)")
fw.close()

fa = open('ttt2.txt','a')
fa.write("\n filein append mode")
fa.write('idek what to type T_T')
fa.close()