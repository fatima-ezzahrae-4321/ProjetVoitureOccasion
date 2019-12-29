from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.autopark.ma/annonces/chercher?marque=hyundai'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "item-list"})
# print(len(containers))
filename= "hyundai.csv"
f = open(filename,"w")
headers="nom;serie;prix;liquide;ville;heure_annonce;url"
f.write(headers)
for contain in containers:
    title = contain.findAll("h5", {"class": "add-title"})
    title_contain = title[0].text.strip()

    heure = contain.findAll("span", {"class": "date"})
    heure_contain = heure[0].text

    ville = contain.findAll("span", {"class": "item-location"})
    ville_contain = ville[0].text.strip()

    liquide = contain.findAll("div", {"class": "col-sm-2 text-center"})
    liquide_contain = liquide[0].text.strip()

    annee = contain.findAll("div", {"class": "col-sm-1 text-center"})
    annee_contain = annee[0].text.strip()

    prix = contain.findAll("h2", {"class": "item-price"})
    prix_contain = prix[0].text.strip()

    print(title_contain, ";" + annee_contain, ";" + prix_contain, ";" + liquide_contain, ";" + ville_contain,";" + heure_contain,";"+my_url)
   # f.write(title_contain, ";" + annee_contain, ";" + prix_contain, ";" + liquide_contain, ";" + ville_contain,";" + heure_contain)

baseurl = 'https://www.autopark.ma/annonces/chercher/'
valid_pages = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for n in range(len(valid_pages)):
    my_urll = f'{baseurl}{valid_pages[n]}?marque=hyundai'
    # print(my_urll)
    uClient = uReq(my_urll)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    containers = page_soup.findAll("div", {"class": "item-list"})

    for contain in containers:
        title = contain.findAll("h5", {"class": "add-title"})
        title_contain = title[0].text.strip()

        heure = contain.findAll("span", {"class": "date"})
        heure_contain = heure[0].text

        ville = contain.findAll("span", {"class": "item-location"})
        ville_contain = ville[0].text.strip()

        liquide = contain.findAll("div", {"class": "col-sm-2 text-center"})
        liquide_contain = liquide[0].text.strip()

        annee = contain.findAll("div", {"class": "col-sm-1 text-center"})
        annee_contain = annee[0].text.strip()

        prix = contain.findAll("h2", {"class": "item-price"})
        prix_contain = prix[0].text.strip()

        print(title_contain, ";" + annee_contain, ";" + prix_contain, ";" + liquide_contain, ";" + ville_contain,";" + heure_contain,";"+my_urll)
       # f.write(title_contain, ";" + annee_contain, ";" + prix_contain, ";" + liquide_contain, ";" + ville_contain, ";" + heure_contain)

f.close()




