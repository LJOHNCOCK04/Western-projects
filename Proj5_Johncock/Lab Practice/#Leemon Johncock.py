#Leemon Johncock
#LAB EXERCISE 6 pt2 10/08/2025
# reading a txt file then editing the quanity of item then writing to a new txt file

#functions
def get_id(line):
    return line[:6].strip()

def get_quanity(line):
    return line[7:11].strip()

def get_name(line):
    return line[12:].strip()

def print_record(id,quanity,name):
    print(f'{id} ({name}) - {quanity}')



#Main fuctions
def main():
    SENTINEL_CODE = 'END'
    
    newfile = open("Items_new.txt", "w")
    oldfile = open("items_old.txt","r")

    line = oldfile.readline().rstrip()
  
    while line != SENTINEL_CODE:
        id = get_id(line)
        quanity = get_quanity(line)
        name = get_name(line)
        print_record(id,quanity,name)
        line = oldfile.readline().rstrip()

        new_quanity = int(input("Enter new quanity: "))

        while new_quanity <=0:
            print("Quanity must be a positve integer.")
            new_quanity = int(input("Enter new quanity: "))


        newfile.write(f"{id} {new_quanity:>4} - {name}\n")
        
    newfile.write(SENTINEL_CODE)

    newfile.close()
    oldfile.close()
        

if __name__ == "__main__":
    main()


