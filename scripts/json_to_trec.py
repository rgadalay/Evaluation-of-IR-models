import json
import urllib.request
import urllib.parse



count = 1
with open('D:/test_queries.txt', encoding="utf-8") as f:
    for line in f:  
        outf = open(str(count)+'.txt', 'a+')
        query = urllib.parse.quote(line)
        corename='LM'
        IRModel = 'LM'
        
        #inurl of solr
        inurl = "http://18.188.90.42:8983/solr/"+corename+"/select?q="+query+"&fl=id%2Cscore&indent=true&rows=20&wt=json&defType=dismax&debugQuery=true&pf=text_en%5E2+text_de5E2+text_ru%5E2&qf=text_en+text_de+text_ru"

        qid = count
        data = urllib.request.urlopen(inurl)
        docs = json.load(data)['response']['docs']
        rank = 0
        for doc in docs:
            if (qid <= 9) :
                outf.write('00'+str(qid) + ' ' + 'Q0' +' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel+ '\n')
            else:
                outf.write('0'+str(qid) + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel+ '\n')
            rank += 1
        outf.close()
        count += 1