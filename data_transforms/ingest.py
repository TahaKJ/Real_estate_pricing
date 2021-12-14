import pandas as pd

DATA_PATH = "dict.csv"
OUTPUT_CLEAN = "filtered_data.csv"

df = pd.read_csv(DATA_PATH)



#with open(data_path , "r"):
# more feature enginearing


def no_libs(DATA_PATH):

    raw = ''
    with open(DATA_PATH,"r") as f:
        raw = f.read()
    
    # parsing data
    raw  = raw.split('\n')

    # removing garbage lines, line to check for garbage
    # garbage = [line for line in raw if  'Judiciaire' not in line]

    
    # keep just non garbage lines
    raw = [line for line in raw if 'Judiciaire' in line]

    for raw_line in raw:
        #pass
        print(raw_line.split(',')[5])
    
    '''
    data line example :
    J+27 Mar 15/06/21,Judiciaire,Appartement Saint-ouen,Tribunal Judiciaire de BOBIGNY,350 000.00 €,225 000.00 €  -35%,      ,,,

    filtered data example:
    Mar,Appartement,Saint-ouen,BOBIGNY,350 000,225 000
    '''
    # create filtered data file 
    filtered_data = raw
    clean_filtered = []

    # list of lists 
    filtered_data = [line.split(',') for line in filtered_data]

    # applying filtering element vy element as shown in example.

    for li in filtered_data:
        c_li = ['']*7
        # keeping day of the week
        li = [l.replace('\xa0', ' ') for l in li]
        c_li[0]=li[0].split(' ')[1]
        # keeping just type appartement
        c_li[1]=li[2].split(' ')[0]
        # place
        c_li[2]=li[2].split(' ')[1]
        # getting just tribunal place
        if ('Tribunal Judiciaire de' not in li[3]):
            print('/!\ warning did not find Tribunal judiciaire de in li[3]')
        c_li[3]=li[3].split(' ')[-1]
        # Start price 
        c_li[4]=li[4].split('.')[0]
        # End price
        c_li[5]=li[5].split('.')[0]
        # date
        c_li[6]=li[0].split(' ')[2]
        clean_filtered.append(c_li)
    
    for l in clean_filtered:
        print(','.join(l))
    # writing cleaned file
    with open(OUTPUT_CLEAN, 'w') as f:
        f.write('day,type,commune,tribunal,start,end,date')
        f.write('\n')
        for l in clean_filtered:
            # haeader line 

            f.write(','.join(l))
            f.write('\n')

no_libs(DATA_PATH)