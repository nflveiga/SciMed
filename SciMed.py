from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
options.set_headless(headless=False)
driver = webdriver.Firefox(firefox_options=options)
is_last=False
nr_art=0
nr_rev=0
pagina='https://www.ncbi.nlm.nih.gov/pubmed/?term=Br+J+Anaesth.+2018+Jul'

#Para max_resultados()
id_maxres="Display"
id_index=2

def obter_pagina(pagina):
    driver.get(pagina)
    print("Headless Firefox Initialized")

def max_resultados(id_maxres,id_index):
    lista=driver.find_elements_by_id(id_maxres)
    lista[id_index].click()
    driver.find_element_by_id("ps200").click()

def sacar():
    lista=driver.find_elements_by_class_name("rslt")
    for item in lista:
        global nr_art
        nr_art+=1
        print("[ "+str(nr_art)+" ] - "+item.find_element_by_class_name("title").text)
        doi = item.find_element_by_class_name("details").text
        #print(doi)
        doi_index = doi.find("doi: ")
        #print(doi_index)
        doi = doi[doi_index+5:]
        doiend_index=doi.find(". ")
        doi=doi[:doiend_index]

        print("http://sci-hub.tw/"+doi)
        print('')

def prox_pagina():
    nxt_btn=driver.find_elements_by_id("EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_Pager.Page")
    for btn in nxt_btn:
        titulo=btn.get_attribute("title")
        if titulo == "Next page of results":
            btn.click()
            break

def check_last():
    try:
        counter=driver.find_element_by_id("pageno" )
        actual=int(counter.get_attribute("value"))
        last = int(counter.get_attribute("last"))
        if actual<last:
            prox_pagina()
        else:
            global is_last
            is_last = True
    except:
        print("Página única")
        is_last =True


def sacar_revistas():
    lista = driver.find_elements_by_class_name("rslt")
    for item in lista:
        global nr_rev
        nr_rev+=1
        titulo = item.find_element_by_class_name("title").text
        abrev = item.find_element_by_class_name('nlmcat_aux').text
        abrev=abrev[24:]
        print('[ '+str(nr_rev)+' ] - '+titulo)
        print(abrev)
        print('')


'''
obter_pagina('https://www.ncbi.nlm.nih.gov/nlmcatalog?term=currentlyindexed%5BAll%5D')
max_resultados("EntrezSystem2.PEntrez.Nlmcatalog.Nlmcatalog_ResultsPanel.Nlmcatalog_DisplayBar.Display",1)
while is_last is False:
    sacar_revistas()
    check_last()
prox_pagina()
'''
obter_pagina(pagina)
max_resultados(id_maxres,id_index)
while is_last is False:
    sacar()
    check_last()
#prox_pagina()
