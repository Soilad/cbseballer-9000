from bs4 import BeautifulSoup
from requests import get
from random import choice
import re
import io
import requests
import pytesseract
from PIL import Image

TAG_RE = re.compile(r'<[^>]+>')
# links = ['https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-1-some-basic-concepts-of-chemistry/',
#          'https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-2-structure-of-atom/',
#          'https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-3-classification-of-elements-and-periodicity-in-properties/',
#          'https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-4-chemical-bonding-and-molecular-structure/',
#          'https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-6-thermodynamics/',
#          'https://www.learncbse.in/ncert-solutions-class-11th-physics-chapter-2-units-measurements/',
#          'https://www.learncbse.in/ncert-solutions-class-11th-physics-chapter-3-motion-straight-line/',
#          'https://www.learncbse.in/ncert-solutions-class-11th-physics-chapter-4-motion-plane/',
#          'https://www.learncbse.in/ncert-class-11-solutions-physics-5-laws-motion/',
#          'https://www.learncbse.in/ncert-solutions-class-11-physics-chapter-6-work-energy-power/',
#          'https://www.learncbse.in/ncert-solutions-class-11-physics-chapter-7-system-particles-rotational-motion/',
#          'https://www.learncbse.in/ncert-class-11-solutions-physics-chapter-8-gravitation/',
#          'https://www.learncbse.in/cbse-class-11-physics-ncert-solutions-chapter-9-mechanical-properties-solids/',
#          'https://www.learncbse.in/cbse-maths-solutions-class-11th-chapter-1-sets/',
#          'https://www.learncbse.in/ncert-class-11-solutions-maths-chapter-2-relations-functions/',
#          'https://www.learncbse.in/cbse-free-ncert-solutions-for-class-11th-maths-chapter-3-trigonometric-functions/',
#          'https://www.learncbse.in/ncert-solutions-for-class-11th-maths-chapter-5-complex-numbers-and-quadratic-equations/',
#          'https://www.learncbse.in/free-ncert-solutions-for-class-11th-maths-chapter-6-linear-inequalities/',
#          'https://www.learncbse.in/ncert-solutions-for-class-11th-maths-chapter-7-permutation-and-combinations/',
#          'https://www.learncbse.in/ncert-solutions-for-class-11th-maths-chapter-8-binomial-theorem/',
#          'https://www.learncbse.in/ncert-solutions-for-class-11th-maths-chapter-9-sequences-and-series/',
#          'https://www.learncbse.in/free-ncert-solutions-class-11th-maths-chapter-10-straight-lines/']
#
# links = ['https://www.learncbse.in/ncert-class-11-solutions-physics-chapter-8-gravitation/']

links = ['https://www.learninsta.com/class-11-physics-important-questions-chapter-2/',
         'https://www.learninsta.com/class-11-physics-important-questions-chapter-3/',
         'https://www.learninsta.com/class-11-physics-important-questions-chapter-4/',
         'https://www.learninsta.com/class-11-physics-important-questions-chapter-5/',
         'https://www.learninsta.com/class-11-physics-important-questions-chapter-6/',
         'https://www.learninsta.com/class-11-physics-important-questions-chapter-7/',
         'https://www.learninsta.com/class-11-physics-important-questions-chapter-8/',
         'https://www.learninsta.com/class-11-physics-important-questions-chapter-9/',
         'https://www.learninsta.com/class-11-physics-important-questions-chapter-10/'
         'https://www.learninsta.com/class-11-chemistry-important-questions-chapter-1/',
         'https://www.learninsta.com/class-11-chemistry-important-questions-chapter-2/',
         'https://www.learninsta.com/class-11-chemistry-important-questions-chapter-3/',
         'https://www.learninsta.com/class-11-chemistry-important-questions-chapter-4/',
         'https://www.learninsta.com/class-11-chemistry-important-questions-chapter-6/',
         'https://www.learninsta.com/class-11-chemistry-important-questions-chapter-7/']

def aeg(text):
    return TAG_RE.sub('', text).replace('&gt;','>').replace('&lt;','<')

def aeglist(element):
    uhh = []
    for i in element:
        return uhh.append(aeg(i))

def fuckimages(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # print( type(img) ) # <class 'PIL.JpegImagePlugin.JpegImageFile'>
    return f'{pytesseract.image_to_string(Image.open(io.BytesIO(get(url, headers=headers).content)))}\n{url}'

def main():
    qna = {}
    idkq = []
    idka = []
    for link in links:
        # r = BeautifulSoup(get('https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-4-chemical-bonding-and-molecular-structure/').content, 'html.parser').find_all('p')
        web = BeautifulSoup(get(link).content, 'html.parser')
        r = web.find_all('p')
        pain = web.find_all('ol')
        pain2 =web.find_all('ul')
        # print(r)
        for i in r:
            # print(aeg(str(i)))
            # input()
            if aeg(str(i)).strip().split('Maths ')[-1].startswith('Question'):
                splitit = str(i).replace('Ans.','Answer:').split('Answer:')
                q,a = aeg(splitit[0]),aeg(splitit[-1])
                if len(splitit[-1].split('src="')) > 1:
                    a = a + '\n' + fuckimages(splitit[-1].split('src="')[1].split('"')[0])
                    # print(a)
                if len(splitit[0].split('src="')) > 1:
                    q = q + '\n' + fuckimages(splitit[0].split('src="')[1].split('"')[0])
                    # print(q)
                qna[q] = a
            elif aeg(str(i)).strip().startswith('Answer:'):
                idka.append(aeg(str(i)))
            else:
                idkq.append(aeg(str(i)))
    print(f'mismatched questions:{len(idkq)} mismatched answers:{len(idka)}')
    with open(r'/home/soi/Documents/bigbrain9000/pyqdict.txt','w') as d:
        d.write(str(qna))
    return qna,idkq,idka

if __name__ == '__main__':
    # qna,idkq,idka = main()
    with open(r'/home/soi/Documents/bigbrain9000/dict.txt') as s:
        qna = eval(s.read())
    with open(r'/home/soi/Documents/bigbrain9000/pyqdict.txt') as s:
        qna = qna | eval(s.read())
    print(f'{len(qna.keys())}')
    while 1:
        x = choice(list(qna.keys()))
        print(f'\n{x}')
        input('>>>')
        print(qna[x])

