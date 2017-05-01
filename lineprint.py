#!/usr/bin/env python

import os
import sys
import time

__ntrp_units_config = {
                       'D9800-SS-NFE-NCI-NTC-BASIC-NDM-ANALOG': { # basicUnit
                        'fpgaList': ['NFE-FPGA',
                                     'NDM-FPGA'],
                        'units': []},
                       'D9800-SS-NFE-NTC-BASIC-NDM-ANALOG': { # noNciUnit
                        'fpgaList': ['NFE-FPGA',
                                    'NCI-FPGA'],
                        'units': []},
                       'D9800-MS-NFE-NCI-2NTM-2NTB': { # ms2Ntm2Ntb
                        'fpgaList': ['NFE-FPGA',
                                     'NCI-FPGA',],
                        'units': []}
                      }
    
def main():
    
    
    for configName, value in __ntrp_units_config.iteritems():
        print configName , value
    print ""
    
    unt = ['NFE-FPGA', 'NCI-FPGA', 'NTC-ANALOG-ENCRYPTED-FPGA', 'NDM-ANALOG-FPGA']
    print unt
    #unt = str(['NFE-FPGA', 'NCI-FPGA', 'NTC-ANALOG-ENCRYPTED-FPGA', 'NDM-ANALOG-FPGA']).replace('[', '').replace(']', '')
    #unt.replace("","",1)
    unt = 'FPGA'
    
    __ntrp_units_config['D9800-ABC'] = { # basicUnit
                        'fpgaList': [unt],
                        'units': ['10.85.163.72']}
    
    unt = 'NDM'
    __ntrp_units_config['D9800-ABC'] = { # basicUnit
                    'fpgaList': [].append(unt),
                    'units': ['10.85.163.72']}
    
    for configName, value in __ntrp_units_config.iteritems():
        print configName , value['units'] , value['fpgaList']
    print ""
    
            
    
if __name__ == "__main__":
    sys.exit(main())
