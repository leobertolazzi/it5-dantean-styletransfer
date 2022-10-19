import re
import requests
from bs4 import BeautifulSoup as bs

def dante_sent_tokenize(text):
     """
     Tokenize sentences from Dante's "Divine Comedy" original text and paraphrases
     from website "https://divinacommedia.weebly.com" for the scrape_dante function
     """

     sentence = re.sub(r"\xa0", r" ", text)
     sentence = re.sub(r" +[1-9]+", r" ", sentence)
     sentence = re.sub(r"\nTesto\n", r" ", sentence)
     sentence = re.sub(r"\nParafrasi\n", r" ", sentence)
     sentence = re.sub(r"\n\n", r" ", sentence)
     sentence = re.sub(r"\n", r" ", sentence)
     sentence = re.sub(r"[0-9]+", r" ", sentence)
     sentence = re.sub(r"[^a-zA-Z]«", r"\n", sentence)
     sentence = re.sub(r"».", r"\n", sentence)
     sentence = re.sub(r"\.", ".\n", sentence)
     sentence = re.sub(r"\!", "!\n", sentence)
     sentence = re.sub(r"\?", "?\n", sentence)
     sentence = re.sub(r";", ".\n", sentence)
     sentence = re.sub(r"\(.+\)", r" ", sentence)
     sentence = re.sub(r" , ", r", ", sentence)
     sentence = re.sub(r"  +", r" ", sentence)
     

     return [s.strip(" ").capitalize() for s in sentence.split("\n") if s.strip(" ")!=""]

def scrape_dante(path):
     """
     Scrape all texts and paraphrases of Dante's "Divine Comedy" from "https://divinacommedia.weebly.com" 
     and store them as indipendent files (one file for each paraphrase/text for each "canto" for each "cantica")
     in the path chosen as argument
     """
     
     canti = [
          'i','ii','iii','iv','v','vi','vii','viii','ix','x',
          'xi','xii','xiii','xiv','xv','xvi','xvii','xviii','xix','xx',
          'xxi','xxii','xxiii','xxiv','xxv','xxvi','xxvii','xxviii','xxix','xxx',
          'xxxi','xxxii','xxxiii','xxxiv'
     ]        

     canti2id = {
          'i':'1','ii':'2','iii':'3','iv':'4','v':'5','vi':'6','vii':'7','viii':'8','ix':'9','x':'10',
          'xi':'11','xii':'12','xiii':'13','xiv':'14','xv':'15','xvi':'16','xvii':'17','xviii':'18','xix':'19','xx':'20',
          'xxi':'21','xxii':'22','xxiii':'23','xxiv':'24','xxv':'25','xxvi':'26','xxvii':'27','xxviii':'28','xxix':'29','xxx':'30',
          'xxxi':'31','xxxii':'32','xxxiii':'33','xxxiv':'34'
     }

     exc_purg = [
          'ix', 'vii','viii','x','xii','xiii','xiv','xix','xv','xvi','xvii','xviii','xx','xxi','xxii','xxiii','xxiv','xxv','xxvi','xxvii'
     ]
     
     exc_par = [
          'iv','ix','v','vii','viii','xiii','xiv','xvi','xviii','xxix','xxv','xxvi','xxvii','xxviii','xxxi'
     ]

     cantiche = ['inf','purg','par']

     url = "https://divinacommedia.weebly.com/"

     for i in cantiche:
          if i == "inf": # scrape all "canti" in Dante's "Inferno"
               for j in canti:

                    # scrape text from the url
                    url_mod = url + "inferno-canto-" + j + ".html"
                    source = requests.get(url_mod).text
                    soup = bs(source, "lxml")
                    raw_txt = soup.find_all("td", class_ = "wsite-multicol-col")
                    txt = [t.get_text() for t in raw_txt]
                    dante_sents = dante_sent_tokenize(txt[2])
                    dante_para = dante_sent_tokenize(txt[3])

                    # create file with tokenized dante sentences
                    original = path + i + "_" + canti2id[j] + "_og.txt"
                    with open(original, 'w', encoding="UTF-8-sig") as d:
                         for sent in dante_sents:
                              d.write(sent+"\n")

                    # create file with tokenized dante paraphrases
                    para = path + i + "_" + canti2id[j] + "_para.txt"
                    with open(para, 'w', encoding="UTF-8-sig") as d:
                         for sent in dante_para:
                              d.write(sent+"\n")

          elif i == "purg": # scrape all "canti" in Dante's "Purgatorio"
               for j in canti[:-1]:

                    # scrape text from the url
                    url_mod = url + "purgatorio-canto-" + j + ".html"
                    source = requests.get(url_mod).text
                    soup = bs(source, "lxml")
                    raw_txt = soup.find_all("td", class_ = "wsite-multicol-col")
                    txt = [t.get_text() for t in raw_txt]
                    if j in exc_purg:
                         dante_sents = dante_sent_tokenize(txt[0])
                         dante_para = dante_sent_tokenize(txt[1])
                    else:
                         dante_sents = dante_sent_tokenize(txt[2])
                         dante_para = dante_sent_tokenize(txt[3])
                    
                    # create file with tokenized dante sentences
                    original = path + i + "_" + canti2id[j] + "_og.txt"
                    with open(original, 'w', encoding="UTF-8-sig") as d:
                         for sent in dante_sents:
                              d.write(sent+"\n")

                    # create file with tokenized dante paraphrases
                    para = path + i + "_" + canti2id[j] + "_para.txt"
                    with open(para, 'w', encoding="UTF-8-sig") as d:
                         for sent in dante_para:
                              d.write(sent+"\n")
          else:
               for j in canti[:-1]: # scrape all "canti" in Dante's "Paradiso"

                     # scrape text from the url
                    url_mod = url + "paradiso-canto-" + j + ".html"
                    source = requests.get(url_mod).text
                    soup = bs(source, "lxml")
                    raw_txt = soup.find_all("td", class_ = "wsite-multicol-col")
                    txt = [t.get_text() for t in raw_txt]
                    if j in exc_par:
                         dante_sents = dante_sent_tokenize(txt[0])
                         dante_para = dante_sent_tokenize(txt[1])
                    else:
                         dante_sents = dante_sent_tokenize(txt[2])
                         dante_para = dante_sent_tokenize(txt[3])

                    # create file with tokenized dante sentences
                    original = path + i + "_" + canti2id[j] + "_og.txt"
                    with open(original, 'w', encoding="UTF-8-sig") as d:
                         for sent in dante_sents:
                              d.write(sent+"\n")

                    # create file with tokenized dante paraphrases
                    para = path + i + "_" + canti2id[j] + "_para.txt"
                    with open(para, 'w', encoding="UTF-8-sig") as d:
                         for sent in dante_para:
                              d.write(sent+"\n")
     
     return

path = '...'
scrape_dante(path)