from bs4 import BeautifulSoup
import codecs

dir_name = r'D:\_english\html/'
ff = codecs.open(dir_name + "dict_5000_by_theme.txt", "a", "utf-8")

# with open(page.text, encoding='utf-8') as f:
# for i in range(50, 51):
# with open("D:\_english\html\p" + str(i) + ".html", encoding='utf-8') as f:
with open("D:\\_english\\html\\Топ-5000 английских слов - Судьба, удача, несчастье.html", encoding='utf-8') as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')

    data = []
    # table = soup.find('table', attrs={'class':'table-l table-voc'})
    table = soup.find('table', attrs={'id': 'wordtable'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values
        #print(row)
    for r in data:
        print (";".join(r))
        ff.write(";".join(r)+'\n')
    # print (i)
ff.close
