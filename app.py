import sys
from googleapiclient.discovery import build
import pprint
from lxml import html
import requests

my_api_key = google_api_key  # Environment Variable
my_cse_id = google_cse_key  # Environment Variable
linkList = []
query = sys.argv
query.remove(query[0])
query = ' '.join(query)


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    query, my_api_key, my_cse_id, num=10)
for result in results:
    linkList.append(result['link'])

for link in linkList:
    page = requests.get(link)
    tree = html.fromstring(page.content)
    title = tree.xpath('//title/text()')
    print(title)
