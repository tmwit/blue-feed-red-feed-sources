import csv

left_sources = csv.DictReader(open('sampled_sources_left.csv'))
right_sources = csv.DictReader(open('sampled_sources_right.csv'))

left_file = open('sampled_sources_left_links.txt', 'w')
right_file = open('sampled_sources_right_links.txt', 'w')

for source in left_sources:
    print(source['link'], file=left_file)

for source in right_sources:
    print(source['link'], file=right_file)
