from lxml.etree import HTML as lxml_html1
from lxml import etree


def xpath_get(html:str,ru):
    html1 = str(html)
    rule = str(ru)
    a= lxml_html1(html1)
    b = a.xpath(rule)
    return b

def xpath_out_html(xpathL):

    c = etree.tostring(xpathL, encoding='utf-8')
    a =c.decode('utf-8')
    return a

def xpath_out_test(html:str):
    a = lxml_html1(html)
    b = a.xpath('//text()')
    return b