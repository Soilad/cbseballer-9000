from bs4 import BeautifulSoup
from requests import get
from random import randint
import re
import io
import requests
import pytesseract
from PIL import Image
import os

cwd = os.getcwd()
TAG_RE = re.compile(r"<[^>]+>")


links = [
    "https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-1-some-basic-concepts-of-chemistry/",
    "https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-2-structure-of-atom/",
    "https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-3-classification-of-elements-and-periodicity-in-properties/",
    "https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-4-chemical-bonding-and-molecular-structure/",
    "https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-6-thermodynamics/",
    "https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-8-redox-reactions/",
    "https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-7-equilibrium/",
    "https://www.learncbse.in/ncert-solutions-class-11th-chemistry-chapter-13-hydrocarbons/",
    "https://www.learncbse.in/cbse-class-11th-chemistry-organic-chemistry-basic-principles-techniques/",
    "https://www.learncbse.in/ncert-solutions-class-11th-physics-chapter-2-units-measurements/",
    "https://www.learncbse.in/ncert-solutions-class-11th-physics-chapter-3-motion-straight-line/",
    "https://www.learncbse.in/ncert-solutions-class-11th-physics-chapter-4-motion-plane/",
    "https://www.learncbse.in/ncert-class-11-solutions-physics-5-laws-motion/",
    "https://www.learncbse.in/ncert-solutions-class-11-physics-chapter-6-work-energy-power/",
    "https://www.learncbse.in/ncert-solutions-class-11-physics-chapter-7-system-particles-rotational-motion/",
    "https://www.learncbse.in/ncert-class-11-solutions-physics-chapter-8-gravitation/",
    "https://www.learncbse.in/cbse-class-11-physics-ncert-solutions-chapter-9-mechanical-properties-solids/",
    "https://www.learncbse.in/ncert-solutions-class-11-physics-chapter-10-mechanical-properties-fluids/",
    "https://www.learncbse.in/ncert-solutions-class-11-physics-chapter-11-thermal-properties-matter/",
    "https://www.learncbse.in/ncert-solutions-class-11-physics-chapter-12-thermodynamics/",
    "https://www.learncbse.in/ncert-solutions-class-11-physics-chapter-13-kinetic-theory/",
    "https://www.learncbse.in/ncert-solutions-class-11-physics-chapter-14-oscillations/",
    "https://www.learncbse.in/ncert-solutions-class-11-physics-chapter-15-waves/",
]

# links = ['https://www.learncbse.in/ncert-class-11-solutions-physics-chapter-8-gravitation/']

links += [
    "https://www.learninsta.com/class-11-physics-important-questions-chapter-2/",
    "https://www.learninsta.com/class-11-physics-important-questions-chapter-3/",
    "https://www.learninsta.com/class-11-physics-important-questions-chapter-4/",
    "https://www.learninsta.com/class-11-physics-important-questions-chapter-5/",
    "https://www.learninsta.com/class-11-physics-important-questions-chapter-6/",
    "https://www.learninsta.com/class-11-physics-important-questions-chapter-7/",
    "https://www.learninsta.com/class-11-physics-important-questions-chapter-8/",
    "https://www.learninsta.com/class-11-physics-important-questions-chapter-9/",
    "https://www.learninsta.com/class-11-physics-important-questions-chapter-10/",
    "https://www.learninsta.com/class-11-physics-important-questions-chapter-11/",
    "https://www.learninsta.com/class-11-physics-important-questions-chapter-12/",
    "https://www.learninsta.com/class-11-physics-important-questions-chapter-13/",
    "https://www.learninsta.com/class-11-physics-important-questions-chapter-14/",
    "https://www.learninsta.com/class-11-physics-important-questions-chapter-15/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-physics-chapter-2/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-physics-chapter-3/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-physics-chapter-4/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-physics-chapter-5/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-physics-chapter-6/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-physics-chapter-7/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-physics-chapter-8/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-physics-chapter-9/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-physics-chapter-10/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-physics-chapter-11/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-physics-chapter-12/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-physics-chapter-13/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-physics-chapter-14/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-physics-chapter-15/",
    "https://www.learninsta.com/class-11-chemistry-important-questions-chapter-1/",
    "https://www.learninsta.com/class-11-chemistry-important-questions-chapter-2/",
    "https://www.learninsta.com/class-11-chemistry-important-questions-chapter-3/",
    "https://www.learninsta.com/class-11-chemistry-important-questions-chapter-4/",
    "https://www.learninsta.com/class-11-chemistry-important-questions-chapter-6/",
    "https://www.learninsta.com/class-11-chemistry-important-questions-chapter-7/",
    "https://www.learninsta.com/class-11-chemistry-important-questions-chapter-8/",
    "https://www.learninsta.com/class-11-chemistry-important-questions-chapter-12/",
    "https://www.learninsta.com/class-11-chemistry-important-questions-chapter-13/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-chemistry-chapter-1/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-chemistry-chapter-2/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-chemistry-chapter-3/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-chemistry-chapter-4/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-chemistry-chapter-6/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-chemistry-chapter-7/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-chemistry-chapter-8/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-chemistry-chapter-12/",
    "https://www.learninsta.com/ncert-solutions-for-class-11-chemistry-chapter-13/",
]


def aeg(text):
    return TAG_RE.sub("", text).replace("&gt;", ">").replace("&lt;", "<")


def aeglist(element):
    uhh = []
    for i in element:
        return uhh.append(aeg(i))


def fuckimages(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    }
    # print( type(img) ) # <class 'PIL.JpegImagePlugin.JpegImageFile'>
    return f"{pytesseract.image_to_string(Image.open(io.BytesIO(get(url, headers=headers).content)))}\n{url}"


def main():
    qna = {}
    idkq = []
    idka = []
    for link in links:
        # r = BeautifulSoup(
        #     get(
        #         "https://www.learncbse.in/ncert-solutions-for-class-11-chemistry-chapter-4-chemical-bonding-and-molecular-structure/"
        #     ).content,
        #     "html.parser",
        # ).find_all("p")
        web = BeautifulSoup(get(link).content, "html.parser")
        r = web.find_all("p")
        pain1 = web.find_all("ol")
        pain2 = web.find_all("ul")
        print(r)
        for i in r:
            print(aeg(str(i)))
            # input()
            if aeg(str(i)).strip().split("Maths ")[-1].startswith("Question"):
                splitit = str(i).replace("Ans", "Answer").split("Answer")
                q, a = aeg(splitit[0]), aeg(splitit[-1])
                if len(splitit[-1].split('src="')) > 1:
                    a = (
                        a
                        + "\n"
                        + fuckimages(splitit[-1].split('src="')[1].split('"')[0])
                    )
                    print(a)
                if len(splitit[0].split('src="')) > 1:
                    q = (
                        q
                        + "\n"
                        + fuckimages(splitit[0].split('src="')[1].split('"')[0])
                    )
                    print(q)
                qna[q] = a
            elif aeg(str(i)).strip().startswith("Answer:"):
                idka.append(aeg(str(i)))
            else:
                idkq.append(aeg(str(i)))
    print(f"mismatched questions:{len(idkq)} mismatched answers:{len(idka)}")
    with open(f"{cwd}/cdict.txt", "w") as d:
        d.write(str(qna))
    return qna, idkq, idka


if __name__ == "__main__":
    # qna, idkq, idka = main()
    print(cwd)
    with open(f"{cwd}/cdict.txt") as s:
        qna = eval(s.read())
    print(f"{len(qna.keys())}")
    q = list(qna.keys())
    while 1:
        x = q.pop(randint(0, len(q) - 1))
        print(f"\n{x}")
        input(">>>")
        print(qna[x])
