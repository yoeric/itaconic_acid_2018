# -*- coding: utf-8 -*-
"""
Histograms in Python 
MUST BE IN PYTHON 2.7 environment to run
Author: ericyoung7@gmail.com

"""

import FlowCal
import matplotlib.pyplot as plt
import matplotlib.cm as cm

scales = ['log']#,'logicle']
scaleD = {'log'    : (0,1000000)}#, 
          #'logicle': (-100,1000000)}

combos = ['white-cells',
          'Pact1-Tadh1',
          'Pact1-Tcyc1',
          'Pact1-Tdpp1',
          'Peft2-Tklura3',
          'Peno2-Ttal1',
          'Pfba1-Tgpm1',
          'Pfba1-Trpl15a',
          'Phhf2-Tadh1',
          'Phta1-Tvma2',
          'Ppfy1-Taip1',
          'Ppgk1-Ttpi1',
          'Ppre3-Teno1',
          'Ppxr1-Tnat1',
          'Prpl28-Tecm10',
          'Prps3-Tcyc1',
          'Psbtdh3-Tefm1',
          'Psmtef1-Tyhi9',
          'Psptdh3-Tagtef1',
          'Ptdh3-Trpl3',
          'Ptdh3-Ttdh1',
          'Ptef1-Tcyc1',
          'Ptef1-Tpdc1',
          'Ptef1-Ttdh1',
          'Ptef1-Tyol036w',
          'Pvma6-Trps14a',
          'Pykt6-Tprm9',
          'Pzuo1-Tvma16']



colors = [cm.gist_rainbow(i) for i in range(1,256)]

for x, scale in enumerate(scales):
    
    for n, combo in enumerate(combos):

        parts = combo.split('-')
        promoter = parts[0][1:]
        terminator = parts[1][1:]

        combination = ['Promoter:    %(p)s\nTerminator: %(t)s' % {'p':promoter, 't':terminator}]
    
        filenames = ['%(f)s.fcs' % {'f':combo}]

        d = [FlowCal.io.FCSData(f) for f in filenames]
        d = [FlowCal.transform.to_rfi(di) for di in d]
     
        FlowCal.plot.hist1d(d, 
                            channel='B1-A', #B1-A for GFP, Y2-A for RFP, V1-A for BFP
                            xscale=scale,
                            xlim=scaleD[scale],
                            xlabel='Venus Expression (AU)',
                            alpha=0.7, 
                            bins=512,
                            facecolor=colors[n*5])
    
        plt.tick_params(which='both', direction='out', right='off', top='off')
        plt.ylim([0,400])
        plt.legend(combination, loc='upper left')
    
        fig_size = plt.rcParams["figure.figsize"]
        fig_size[1] = 6.0
    
        #print(fig_size)
        plt.show
        plt.savefig('%(f)s_%(s)s.pdf' % {'f':combo, 's':scale})
        plt.close()