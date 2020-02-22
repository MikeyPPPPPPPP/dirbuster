import requests
import time
import wordlist_maker_module

url = ''
file_name = ''
host = ''
dont_want_status_codes = []

def get_list(file):
    words = []
    word = []
    f = open(str(file),'r')
    content = f.read().splitlines()
    for x in content:
        words.append(x.split('*'))
            
    f.close()
    for x in words:
        word.extend(x)
    return word

def add_w():
    print("""
--To add a wordlist--

wordlist format:
    It has to be a list
    
    ['test','test','test']

\n\n\n\n""")
    print("\n\n")
    menu()

def setup():
    global url
    global file_name
    try:
            
        print('url to get words from:')
        url = input('[url]:')
        print('filename to save words to:')
        file_name = input('[words]:')
        word = wordlist_maker_module.setup_file(file_name, url)
    except:
        prin(1)
    print("\n\n")
    menu()
    
def wordlist():
    global file_name
    print('[wordlist of (h)elp]:')
    word_help = str(input('[w,h]:'))
    if word_help != 'h':
        file_name = word_help
    else:
        file_name = word_help
        add_w()
    print("\n\n")
    menu()
    
def status():
    global dont_want_status_codes
    print('status codes')
    stcd = input('[status codes]:')
    dont_want_status_codes = stcd.split(',')
    print("\n\n")
    menu()
    
def urls():
    print('host comes when you start.')
    print('url for the words: ', url, \
     '\nfile name: ',file_name, \
     '\nstatus codes: ', str(dont_want_status_codes))
    print("\n\n")
    menu()

def start():
    global host
    global file_name
    print('host to dirbust:')
    host = input('host:')
    dirs = get_list(file_name)
    for x in dirs:
        r = requests.get(host+x)
        if r.status_code not in dont_want_status_codes:
            print(host+x, '\t\t', r.status_code)
    
        else:
            menu()
    print("\n\n")
    menu()

    
def menu():
    print("dirbuster")
    print("---------")
    print("[0] make a wordlist")
    print("[1] use a wordlist")
    print("[2] set status codes")
    print("[3] variables")
    print("[4] start")
    print("[5] quit")
    while True:
        try:
            select = int(input("\n[0,1,2,3,4]: "))
            if select == 0:
                setup()
                break

            elif select == 1:
                wordlist()
                break
                    
            elif select == 2:
                status()
                break

            elif select == 3:
                urls()
                break
          
            elif select == 4:
                start()
                break
            elif selection == 5:
                exit()
            else:
                menu()

        except ValueError:
            print('error')
    exit()
   
menu()
