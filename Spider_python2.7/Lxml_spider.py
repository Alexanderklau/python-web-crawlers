import lxml.html
def lxml_scraper(html):
    tree = lxml.html.fromstring(html)
    results = {}
    for field in FIELDS:
        results[field] = tree.csselect('table > tr#places_%s_row'
                                       '> td.')
        return results
