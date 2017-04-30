
import os

def sed(str1,str2,file1,file2):
    try:
        fin = open(file1,"r")
        fout = open(file2,"w")
    except:
        print("open exception")
    list_fin = []
    try:
        for line in fin:
            for word in line.split():
                list_fin.append(word)
        print(list_fin)    
        for i in range(len(list_fin)):
            if list_fin[i] == str1:
                list_fin[i] = str2
        delimiter = " "
        output = delimiter.join(list_fin) 
    except:
        print("replace exception")
    try:
        fout.write(output)
        fout.close()
        fin.close()
    except:
        print("Writein exception")
    
    
def main():
    sed("is", "was","file1.txt","file2.txt")
    
if __name__=="__main__":
    main()
