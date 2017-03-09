
import urllib.request
import xml.etree.ElementTree

def get_data(zip_code, code_name):
    if code_name == 'isbn':
        API_URL = 'http://iss.ndl.go.jp/api/opensearch?isbn='
    elif code_name == 'title':
        API_URL = 'http://iss.ndl.go.jp/api/opensearch?title='
    # APIに接続
    response = urllib.request.urlopen(API_URL + zip_code)
    xml_result = response.read()
    response.close()
    # 取得したXML文字列を取得
    elem = xml.etree.ElementTree.fromstring(xml_result)
    # 要素の抽出
    title = elem.findtext(".//item/title")
    author = elem.findtext(".//item/author")
    link = elem.findtext(".//item/link")
    book_data = {
                'isbn':str(zip_code),
                'title':str(title),
                'author':str(author),
                'link':str(link),
                }
    # 結果の表示
    print(book_data)
    return book_data

