import time
import csv
import sys

window = 10

f_name = sys.argv[1]
name, ext = f_name.split('.')
f_all_name = "%s-all.%s" % (name, ext)
f_train_name = "%s-train.%s" % (name, ext)
f_test_name = "%s-test.%s" % (name, ext)

with open(f_name) as f_in:

  f_csv_in = csv.reader(f_in)
  headers = next(f_csv_in)[:7]
  data = [row[:7] for row in f_csv_in]

  for i, row in enumerate(data[:-window]):

    # Compute labels for train data and save it to a file
    label = None
    close = float(row[1])

    for j, next_row in enumerate(data[i+1:i+window+1]):
      next_close = float(next_row[1])
      spread = next_close - close

      if abs(spread) >= 0.1:
        label = spread
        break

    if label:
      if label > 0:
        label = 0.1
      else:
        label = -0.1
    else:
      label = spread

    row.append("%.2f" % (label,))

  # Split data to train and test data
  headers.append('label')

  size = int(len(data) * 0.8)
  data = data[:-window]
  train_data, test_data = data[:size], data[size:]

  with open(f_all_name, 'w') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(headers)
    writer.writerows(data)

  with open(f_train_name, 'w') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(headers)
    writer.writerows(train_data)

  with open(f_test_name, 'w') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(headers)
    writer.writerows(test_data)
