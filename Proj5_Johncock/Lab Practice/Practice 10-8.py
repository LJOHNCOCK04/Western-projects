 #Leemon Johncock
#LAB EXERCISE 6 10/08/2025
def get_id(line):
    return line[:6].strip()

def get_quanity(line):
    return line[7:11].strip()

def get_name(line):
    return line[12:].strip()

def print_record(id,quanity,name):
    print(f'{id} ({name}) - {quanity}')

def main():
    SENTINEL_CODE = 'END'

    oldfile = open("Items_old.txt", "r")

    line = oldfile.readline().rstrip()
  
    while line != SENTINEL_CODE:
        id = get_id(line)
        quanity = get_quanity(line)
        name = get_name(line)
        print_record(id,quanity,name)
         
        line = oldfile.readline().rstrip()

if __name__ == "__main__":
    main()


