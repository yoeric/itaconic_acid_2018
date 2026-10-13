'''
Created on Mar 10, 2014

@author: dbg

Modified by Eric M. Young on 02/04/2015
'''

from openpyxl import *
from openpyxl.cell import *
from openpyxl.utils.cell import *

def main():

    picklist_format = "Source Plate Barcode,Source Well,Destination Plate Barcode,Destination Well,Transfer Volume,Offset"

    #Load source plate
    source_id  = "source_B_L1"  

    dest_id    = "dest_EY_B_P1"

    picklist_id = "B1"

    output = clear('picklist_%(n)s.csv' % {'n' : picklist_id})

    output.write('%(p)s\n' % {'p':picklist_format})
    
    print(picklist_format)

    part2wellD = load_source_description(source_id)

    recipes   = load_dest_description(dest_id, picklist_id)

    volume     = '500'                     

    for recipe in recipes:

        dest_well, design, parts = recipe

        for part in parts:

            part_well = part2wellD[part]

            toks = [source_id,part_well,dest_id,dest_well,volume]

            toks_line = ','.join(toks)
            
            print(toks_line)  #Prints all the text separated by commas

            output.write('%(t)s\n' % {'t':toks_line})

    output.close()

def load_source_description(fname):

    D = {} #The dictionary to be built from the file

    wb = load_workbook('%(f)s.xlsx' % {'f':fname}, data_only=True)

    ws = wb.get_sheet_by_name(fname)
    
    cell_array = ws.rows

    wells = []
    partnames = []

    for row in cell_array :

        for cell in row :
            xy = coordinate_from_string(cell.coordinate)
            col = column_index_from_string(xy[0])
            row = xy[0]

            cell_value = "%(c)s" % {'c':cell.value}
            
            if col is 1 :
                wells.append(cell_value)
                
            if col > 1:
                partnames.append(cell_value)

    for n, x in enumerate(partnames) :
        D[x] = wells[n]

    return D 

def load_dest_description(fname, picklist_id):

    ans = [] #This list will contain all of the recipies, one per line

    wb = load_workbook('%(f)s.xlsx' % {'f':fname}, data_only=True)
    
    ws = wb.get_sheet_by_name(fname)

    cell_array = ws.rows

    for row in cell_array :
        parts = []
        
        for cell in row :
            xy = coordinate_from_string(cell.coordinate)
            col = column_index_from_string(xy[0])
            row = xy[1]

            cell_value = "%(c)s" % {'c':cell.value}


            design = "%(r)s" % {'r':row}
            
            if col is 1 :
                well = cell_value
                
            if col >= 2:
                if cell_value != 'None':
                    parts.append(cell_value)

        ans.append([well, design, parts])

    return ans

def clear(filename) :

    f = open(filename, 'w')
    f.write('')
    f.close()
    f = open(filename, 'a')

    return f

if __name__ == '__main__':main()

