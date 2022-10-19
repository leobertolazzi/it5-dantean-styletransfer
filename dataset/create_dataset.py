import pandas as pd

def create_ita2dante(path):
    """
    create a csv file with original text and paraphrases from Dante's 'Divine Comedy'
    scraped from the website "https://divinacommedia.weebly.com and aligned manually"
    """

    cantiche = ['inf','purg','par']
    dante = []
    italian = []

    for cantica in cantiche:

        if cantica == 'inf':
            for canto in range(1,35):

                canto_para_file = path + cantica + "_" + str(canto) + "_para.txt"
                with open(canto_para_file, 'r', encoding="UTF-8-sig") as a:
                    for para in a.read().split("\n"):
                        italian.append(para)

                canto_og_file = path + cantica + "_" + str(canto) + "_og.txt"
                with open(canto_og_file, 'r', encoding="UTF-8-sig") as b:
                    for sent in b.read().split("\n"):
                        dante.append(sent)

        else:
            for canto in range(1,34):

                canto_para_file = path + cantica + "_" + str(canto) + "_para.txt"
                with open(canto_para_file, 'r', encoding="UTF-8-sig") as a:
                    for para in a.read().split("\n"):
                        italian.append(para)

                canto_og_file = path + cantica + "_" + str(canto) + "_og.txt"
                with open(canto_og_file, 'r', encoding="UTF-8-sig") as b:
                    for sent in b.read().split("\n"):
                        dante.append(sent)

    ita2dante_df = pd.DataFrame({"italian" : italian , "dante" : dante})
    ita2dante_df.to_csv(path+"ita2dante.csv", index=False)

    return

path = '...'
create_ita2dante(path)