from dateutil import parser
import datetime
import time
import sys
import csv

stock = sys.argv[1]

f_stocks_name = "%s-all.csv" % (stock,)
f_tweets_name = "tweets/%s.csv" % (stock,)
f_out_name = "tweets/%s-labels.csv" % (stock,)

# Get labels

labels = {}

with open(f_stocks_name) as f:
  f_csv = csv.reader(f)
  headers = next(f_csv)

  for row in f_csv:
    tm = parser.parse(row[0]).strftime("%y%m%d%H%M")
    labels[tm] = row[-1]

# Label tweets

with open(f_tweets_name) as f_in, open(f_out_name, 'w') as f_out:
  f_out_csv = csv.writer(f_out)

  for line in f_in:
    row = line.split("\t")

    # tm = datetime.datetime.strptime(row[0], "%y%m%d%H%M")
    # tm = tm - datetime.timedelta(seconds=tm.second) + datetime.timedelta(minutes=1)
    f_out_csv.writerow((row[0], labels.get(row[0]), row[1].strip()))
