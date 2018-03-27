import pandas as pd
import csv
import facebook

sources = csv.DictReader(open('included_sources.csv'))
graph = facebook.GraphAPI(access_token='', version='2.12')

final = []

for source in sources:
    try:
        page = graph.get_object(id='{0}'.format(source['fb_id']), fields='fan_count,name,link')

        source['name'] = page['name']
        source['fan_count'] = page['fan_count']
        source['fb_id'] = page['id']
        source['link'] = page['link']

        final.append(source)

    except Exception as e:
        print('{0}: {1}'.format(page['name'], e))

db = pd.DataFrame(final, columns=final[0].keys())
db.set_index('fb_id', inplace=True)
db.to_csv('updated_sources_master.csv')
