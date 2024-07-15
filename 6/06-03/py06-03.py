#py06-03.py
import os

file_path=R"C:\Users\K24G2040\Desktop\data"
text_path=R"C:\Users\K24G2040\Desktop\myfile.txt"
with open(text_path, 'a') as file:
    file.truncate(0)
def show_file(dir):
    try:
        if os.path.isfile(dir):
            #print(dir)
            with open(text_path, 'a') as file:
                txt=str(dir+"\n")
                file.write(txt)
        else:
            dirs=os.listdir(dir)
            dirs.sort()
            for item in dirs:
                show_file(os.path.join(dir,item))
    except PermissionError as err:
        print(err)
    except FileNotFoundError as Ferr:
        print(Ferr)

def search(words,array):
    ans=[i for i in array if words in i]
    print(ans)



def main():
    lists=[]
    show_file(os.path.join(file_path))
    with open(text_path, 'r') as file:
        content=file.read()
        lists=content.splitlines()

    words=input("検索")
    search(words,lists)

if __name__=="__main__":
    main()