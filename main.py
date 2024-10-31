from bs4 import BeautifulSoup
from requests import get
from random import choice
import re
TAG_RE = re.compile(r'<[^>]+>')
links = ['https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-1-some-basic-concepts-of-chemistry/',
         'https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-2-structure-of-atom/',
         'https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-3-classification-of-elements-and-periodicity-in-properties/',
         'https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-4-chemical-bonding-and-molecular-structure/',
         'https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-6-thermodynamics/']

def aeg(text):
    return TAG_RE.sub('', text).replace('&gt;','>').replace('&lt;','<')

def aeglist(element):
    uhh = []
    for i in element:
        return uhh.append(aeg(i))

if __name__ == '__main__':
    qna = {}
    idkq = []
    idka = []
    for link in links:
        # r = BeautifulSoup(get('https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-4-chemical-bonding-and-molecular-structure/').content, 'html.parser').find_all('p')
        web = BeautifulSoup(get(link).content, 'html.parser')
        r = web.find_all('p')
        pain = web.find_all('ol')
        pain2 =web.find_all('ul')
        print(aeglist(str(pain)))
        # print(r)
        for i in r:
            # print(aeg(str(i)))
            # input()
            if aeg(str(i)).strip().startswith('Question'):
                splitit = str(i).replace('Ans.','Answer:').split('Answer:')
                try:
                    try:
                        qna[aeg(splitit[0].split('src="')[1].split('"')[0])] = splitit[1].split('src="')[1].split('"')[0]
                    except:
                        try:
                            qna[aeg(splitit[0])] = splitit[1].split('src="')[1].split('"')[0]
                        except:
                            qna[aeg(splitit[0].split('src="')[1].split('"')[0])] = splitit[1]
                except:
                    try:
                        qna[aeg(splitit[0])] = aeg(splitit[1])
                    except:
                        idkq.append(aeg(str(i)))
            elif aeg(str(i)).strip().startswith('Answer:'):
                idka.append(aeg(str(i)))
            else:
                continue
        # print(f'mismatched questions:{idkq} mismatched answers:{idka}')
    while 1:
        x = choice(list(qna.keys()))
        print(f'\n{x}')
        input('>>>')
        print(qna[x])

