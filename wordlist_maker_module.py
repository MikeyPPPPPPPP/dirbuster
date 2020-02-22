from bs4 import BeautifulSoup
import requests
import time



class request:
    def __init__(self, word_list, url):
        self.word_list = open('word_list.txt','w')
        self.url = url
        self.unsort = []
        self.words = []
        self.wordss = []
        self.new = []

        self.up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.upperwords = []
        self.upperword = []
        
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'}
        self.r = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.r.text, 'lxml')

    def remv_dub(self, x):
        return list(set(x))


    def get_paraghraph_text(self):
        for x in self.soup.findAll('p'):
            t = x.text.encode('utf-8')
            try:
                self.new.append(t.decode('utf-8'))
            except:
                pass


    def hass_upper(self, x):
        self.upperword
        s = []
        word = []
        s[:0] = x
        if s[0] in self.up:
            for a in s:
                if a in self.alph:
                    word.append(a)        
            self.upperword.append(''.join(word))#write(''.join(word),'\n')

            
    def split_upper_lower(self):
        for x in self.new:
            for line in x.split():
                self.hass_upper(line)
                a = []
                a[:1] = line
                word = []
                for x in a:
                    if x in self.alph:
                        word.append(x)
            
                    self.wordss.append(''.join(word))

        for x in self.new:
            for line in x.split():
                self.hass_upper(line)
                a = []
                a[:1] = line
                word = []
                for x in a:
                    if x in self.alph:
                        word.append(x)
            
                self.wordss.append(''.join(word))
        
        for x in self.remv_dub(self.upperword):
            self.upperwords.append(x)


    def replace_with(self):
        counter = 0

        comw = []
        for x in self.upperwords:
            for line in x.split():
              if counter <= 20:
                comw.append(line)
                counter += 1
              else:
                a = '*'.join(comw)
                self.word_list.write(a)
                self.word_list.write('\n')
                counter = 0
                comw = []

        counter = 0

        comw = []
        for x in self.wordss:
          
          for line in x.split():
            if counter <= 22:
              comw.append(line)
              counter += 1
            else:
              a = '*'.join(comw)
              self.word_list.write(a)
              self.word_list.write('\n')
              counter = 0
              comw = []

#ussage
'''
a = request('word_list.txt','https://en.wikipedia.org/wiki/Lead')
a.get_paraghraph_text()
a.split_upper_lower()
a.replace_with()
a.word_list.close()
'''

def setup_file(fn, ul):
    a = request(fn, ul)
    a.get_paraghraph_text()
    a.split_upper_lower()
    a.replace_with()
    a.word_list.close()

 


