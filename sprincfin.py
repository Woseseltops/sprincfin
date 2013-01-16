import os
import collections

#-------------------------------------
# Ask for the input file
#-------------------------------------

all_files = os.listdir();
txt_files = [];

for i in all_files:
    if i[-3:] == 'txt':
        txt_files.append(i);

print('In this directory, the following .txt files were found:');

for n, i in enumerate(txt_files):
    print('['+str(n)+']',i);

print('')
spr_file = input('The number of the file you want to use: ');
spr_file = open(txt_files[int(spr_file)]).readlines();

#-------------------------------------
# Ask for the cells to investigate
#-------------------------------------

cells = spr_file[0].split('\t');

print('In this file, the following columns were found:');

for n, i in enumerate(cells):
    print('['+str(n)+']',i);

columns = input('Please give a comma-separated list of all columns you want to investigate: ').split(',');

for n, i in enumerate(columns):
    columns[n] = int(i);

#-------------------------------------
# Ask for the base
#-------------------------------------

base = '';

while base not in columns:
    if base != '':
        print('That column is not part of the cells you\'re investigating. Please try again.');
    
    base = int(input('Which one of these columns will be the basic column? '));

#-------------------------------------
# Prepare the output file
#-------------------------------------

outp = input('Name of the outputfile: ') + '.txt';
open(outp,'w');
f = open(outp,'a');

#-------------------------------------
# Start looking for inconsistencies
#-------------------------------------

columns_string = '';

for i in columns:
    columns_string += ' ' + str(cells[i]);

f.write('Comparing colums <' + columns_string[1:] + '> on the basis of ' + cells[base] + '...\n');

result = {};

for i in spr_file:
    #Get the cells and the base
    cells = i.split('\t');
    basevalue = cells[base];

    #Add this basevalue to the results if you weren't tracking it
    try:
        result[basevalue];
    except KeyError:
        result[basevalue] = [];

    #Extract which cells are relevant and save them with the base
    relevant_cells = [];
    for j in columns:
        if j != basevalue:
            relevant_cells.append(cells[j]);

    result[basevalue].append(relevant_cells);

#--------------------------------------
# Show the results
#--------------------------------------

for k,v in result.items():
    if len(v) > 1:

        #Make each group of cells into a string, for easy comparison
        result_strings = [];
        for i in v:
            result_strings.append(str(i));

        #Count what you have and ignore this row if there is only one possibility
        countings = collections.Counter(result_strings)

        if len(countings) == 1:
            continue;

        #When inconsistency is found, change this into something readable        
        f.write('\n');
        f.write(k+'\n');

        countings_str = '';

        for kc,vc in countings.items():
            f.write(str(vc) + 'x ' + kc+'\n');

#Wat doet ie met lege cellen bij een bepaalde categorie?
