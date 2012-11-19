import os

# Select file

all_files = os.listdir();
txt_files = [];

for i in all_files:
    if i[-3:] == 'txt':
        txt_files.append(i);

print('In this directory, the following .txt files were found:');

for n, i in enumerate(txt_files):
    print('['+str(n)+']',i);

print('')
bestand = input('The number of the file you want to use: ');
bestand = open(txt_files[int(bestand)]).readlines();

# Select cells to investigate
cells = bestand[0].split('\t');

print('In this file, the following columns were found:');

for n, i in enumerate(cells):
    print('['+str(n)+']',i);

columns = input('Please give a comma-separated list of all columns you want to investigate: ').split(',');

for n, i in enumerate(columns):
    columns[n] = int(i);

# Select the base
base = '';

while base not in columns:
    if base != '':
        print('That column is not part of the cells you\'re investigating. Please try again.');
    
    base = int(input('Which one of these columns will be the basic column? '));

#Start looking for inconsistencies
columns_string = '';

for i in columns:
    columns_string += ' ' + str(cells[i]);

print('Comparing colums <' + columns_string[1:] + '> on the basis of ' + cells[base] + '...');
