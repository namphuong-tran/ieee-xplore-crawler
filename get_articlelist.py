import requests
import json
import urllib3

def single_page(headers, searchword, url, page):
    # refinements = 'ContentType:Journals'
    # ranges = '2020_2023_Year'
    data = {
        "newsearch": 'true',
        "queryText": searchword,
        "pageNumber": str(page),
        # "refinements": refinements,
        # "ranges": ranges,
        "rowsPerPage": str(500),
    }
    res = requests.post(url=url, data=json.dumps(data), headers=headers, verify=False)
    print(res)
    dic_obj = res.json()
    return dic_obj

#queryText=federated%20learning&highlight=true&returnType=SEARCH&matchPubs=true&pageNumber=1&refinements=ContentType:Journals&ranges=2020_2023_Year&returnFacets=ALL&rowsPerPage=100

def airtcle_list(searchword):
    headers = {
        'Accept': 'application/json,text/plain,*/*',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '147',
        'Content-Type': 'application/json',
        'Referer': 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }
    url = 'https://ieeexplore.ieee.org/rest/search'
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    dic_obj = single_page(headers, searchword, url, 1)
    # print(dic_obj)
    totalpage = int(dic_obj["totalPages"])
    print(totalpage)
    totalrecords = int(dic_obj["totalRecords"])
    print('Search keywords: ' + searchword)
    print('Total retrieved '  + str(totalrecords) + ' articles')
    result_list = []    # Store the serial number of the article
    for i in range(1, totalpage + 1):
        dic_obj = single_page(headers, searchword, url, i)
        
        for dic_obj in dic_obj["records"]:
            if(dic_obj["contentType"] == 'IEEE Journals'):
                if(int(dic_obj["publicationYear"]) > 2019 & int(dic_obj["publicationYear"]) < 2024):
                    result_list.append(dic_obj["articleNumber"])
    
    return result_list
