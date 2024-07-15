#prg06-02.py
import os

def show_file(dir):
    try:
        if os.path.isfile(dir):
            print(dir)
        else:
            dirs=os.listdir(dir)
            dirs.sort()
            for item in dirs:
                show_file(os.path.join(dir,item))
    except PermissionError as err:
        print(err)
    except FileNotFoundError as Ferr:
        print(Ferr)

def main():
    show_file(os.path.join('C:\\'))

if __name__=="__main__":
    main()