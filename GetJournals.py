'''
Este programa cria uma lista dos artigos de revistas da science direct e respectivos links do Sci-hub para download
Aceita como input um ficheiro do tipo .txt com as citações dos artigos que se obtem no site da sciencedirect

'''

import sys

def get_content(file_to_load):
    line_list=[]
    ficheiro = open(file_to_load, 'r')
    line=ficheiro.readline()
    while line:
        line_list.append(line.strip('\n'))
        line=ficheiro.readline()
    #print(line_list)
    return line_list

def get_titles_doi(line_list):
    for item in line_list:
        doi_index=item.find('doi.org')
        if(doi_index!=-1):
            title=line_list[line_list.index(item)-6]
            title=title[:len(title)-1]
            doi=item[8+8:len(item)-1]
            print(title)
            print('http://sci-hub.tw/'+doi)
            print('')


get_titles_doi(get_content(sys.argv[1]))