import csv


fw = open('newcsv.csv', 'w', newline='')
f1 = open('Bigram_frequencies.csv','r')
#f2 = open('bigram_words2.txt', 'r')

# create the csv writer
writer = csv.writer(fw)

reader = csv.reader(f1)

for line in reader:
    good = True
    for i in line:
        for item in i:
            if(ord(item) > 128):
                good = False
    if good:
        writer.writerow(line)
# close the file
fw.close()
f1.close()
