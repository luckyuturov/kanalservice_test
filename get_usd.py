import urllib.request
from xml.dom import minidom


def valute():
    url = 'https://www.cbr.ru/scripts/XML_daily.asp?'
    webfile = urllib.request.urlopen(url)

    data = webfile.read()
    dom = minidom.parseString(data)
    dom.normalize()

    elements = dom.getElementsByTagName('Valute')

    for node in elements:
        if node.getAttribute('ID') == 'R01235':
            usd_currency = float(node.childNodes[4].firstChild.data.replace(',', '.'))    
    return usd_currency
usd = valute()