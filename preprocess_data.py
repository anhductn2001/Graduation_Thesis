import json

if __name__=='__main__':
    with open("/home/duc/pegasus/Pegasus_with_Longformer_summarization/test.txt", encoding="utf-8") as f:
        articles =[]
        # abstracts=[]
        for id_, row in enumerate(f):
            data = json.loads(row)

            """
            'article_id': str,
            'abstract_text': List[str],
            'article_text': List[str],
            'section_names': List[str],
            'sections': List[List[str]]
            """

            article = [d.strip() for d in data["article_text"]]
            article = " ".join(article)
            articles.append(article)
            # abstract = [ab.replace("<S>", "").replace("</S>", "").strip() for ab in data["abstract_text"]]
            # abstract = " \n ".join(abstract)
            # abstracts.append(abstract)
    idx = 0
    dic = {}
    for i in articles:
        a = ""
        a = i.replace("@xmath","").replace("@xmath0","").replace("@xmath1","").replace("@xmath2","").replace("@xmath3","").replace("@xmath4","").replace("@xmath5","").replace("@xmath6","").replace("@xmath7","").replace("@xmath8","").replace("@xmath9","").replace("@xmath10","").replace("@xmath11","").replace("@xmath12","").replace("@xmath13","").replace("@xmath14","").replace("@xmath15","").replace("@xmath16","").replace("@xmath17","").replace("@xmath18","").replace("@xmath19","").replace("@xmath20","").replace("@xmath21","").replace("@xmath22","")
        a = a.replace("@xcite","")
        a = a.replace("$","")
        a = a.replace("[ f1 ]","")
        a = a.replace("[ f2 ]","")
        a = a.replace("[ f3 ]","")
        a = a.replace("[ f4 ]","")
        a = a.replace("[ f5 ]","")
        a = a.replace("[ f6 ]","")
        a = a.replace("[ f7 ]","")
        a = a.replace("[ f8 ]","")
        a = a.replace("[ f9 ]","")
        a = a.replace("[ f10 ]","")
        a = a.replace("[ f11 ]","")
        a = a.replace("[ f12 ]","")
        dic[str(idx)] = a
        idx+=1
    with open('clean.json', 'w', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=4)
