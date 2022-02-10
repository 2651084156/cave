from pyquery import PyQuery as pyq


def css_find(html: str, rule: str):
    html1 = pyq(html)
    a = html1(rule)
    return str(a)


def css_get_item(html: str, rule: str):
    html1 = pyq(html)
    a = html1(rule).items()
    list1 = []
    for i in a:
        list1.append(str(i))

    return list1


def css_get_attr(html: str, attr: str):  # 获取属性
    """获取属性，attr是要获取的属性"""
    html1 = pyq(html)
    a = html1.attr(attr)
    return str(a)


def css_get_text(html: str):  # 获取属性
    """获取属性，attr是要获取的属性"""
    html1 = pyq(html)
    a = html1.text()
    return str(a)


def css_get_html(html: str):  # 获取属性
    """获取属性，attr是要获取的属性"""
    html1 = pyq(html)
    a = html1.html()
    return str(a)
