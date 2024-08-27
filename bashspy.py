
'''
    SIMPLE SOUNDERPY BASH SCRIPT

    -- ARGS 
       -- `site`: BUFKIT site, str, ex: 'KGFK'
       -- `model`: forecast model, str, ex: 'hrrr'
       -- `fhr`: model forecast hour, int, ex: 10
       -- `op`: operation to conduct after loading data, str
                options are: 'to_file' or 'plot'

    (C) Kyle J Gillett, 2024 

'''


print('-------------------------------')
print('[+] SOUNDERPY | starting up script..')


# IMPOPRT SOFTWARE
import sounderpy as spy
import argparse


# RECORD ARGS VIA ARGPARSE 
parser = argparse.ArgumentParser(description='play with SounderPy data')

parser.add_argument("site", type=str,
        help="bufkit site by which to recieve data for")
parser.add_argument("model", type=str,
        help="nwp forecast model by which to recieve data from")
parser.add_argument("fhr", type=int,
        help="forecast hour from run to recieve data for")
parser.add_argument("op", type=str, 
        help="operation to conduct after data is loaded -- plot or save to txt-file")

args = parser.parse_args()


# GET DATA VIA SOUNDERPY 
clean_data = spy.get_bufkit_data(args.model, args.site,  args.fhr)
print("[+] SOUNDERPY | Data loading complete... ")



# PLOT DATA VIA SOUNDERPY
'''
- if operation is to_file, save the data to a sharppy file
- if operation is plot, save the data to a sounderpy sounding plot
'''

if args.op == 'to_file':
    spy.to_file("sharppy", clean_data)
    print("[+] SOUNDERPY | saving data to a file")

elif args.op == 'plot':
    spy.build_sounding(clean_data, color_blind=True, save=True)
    print("[+] SOUNDERPY | saving data as a sounding plot")

else: 
    raise Exception("Invalid Operation")

print("[+] SOUNDERPY | script shutting down, goodbye")
