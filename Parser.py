from newspaper import Article

def parse(url):
    #언어가 한국어이므로 language='ko'로 설정
    a = Article(url, language='ko')
    a.download()
    a.parse()
    #기사 제목 가져오기
    e1=a.title
    tt=e1.replace("\n","")
    e2=a.text
    sc=e2.replace("\n","")
    return sc,tt