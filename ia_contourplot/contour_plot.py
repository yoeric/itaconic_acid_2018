"""
Title: Plotting Fit Equations from OLS Regressions
Created on Wed Sep 28 15:10:29 2016

@author: Eric M. Young
@email: ericyoung7@gmail.com

Version: Python 3.5.2
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as grsp

from pylab import cm, colorbar, xlabel, ylabel, contour, contourf
from matplotlib import rcParams

from models import second_order_model
from models import second_order_nosquare_model
from models import linear_model

# Turn interactive plotting off
# NECESSARY TO PREVENT SQUISHING OF LARGER THAN SCREEN FIGURES!!!
plt.ioff()

#rcParams['mathtext.fontset'] = 'stixsans'
rcParams['font.size'] = 10
rcParams['font.family'] = 'sans-serif'
 
def main() :
    
    lL = ['libA_avg_2', 'libAR_avg_2','libAF_avg_1', 
          'libB_avg_1', 'libC_avg_1', 'all_avg_2','highcad_avg_2']
          

    rL = ['ia','tia', 'mmia', 'sa', 'ma', 'ia2mmia']
    
    #Different strength levels to plot
    sL = ['Low', 'Med', 'High']
    
    # Effect being plotted on y-axis
    eL = ["log_CAD","log_ITE","log_PYC", "log_ACDH", "log_CSC", "log_ACO"]
    
    #Dictionary of X values for each effect being plotted
    xD = {'log_CAD': ["log_ITE","log_PYC", "log_ACDH", "log_CSC", "log_ACO"],
          'log_ITE': ["log_CAD","log_PYC", "log_ACDH", "log_CSC", "log_ACO"],
          'log_PYC': ["log_ITE","log_CAD", "log_ACDH", "log_CSC", "log_ACO"],
          'log_ACDH': ["log_ITE","log_PYC", "log_CAD", "log_CSC", "log_ACO"],
          'log_CSC': ["log_ITE","log_PYC", "log_ACDH", "log_CAD", "log_ACO"],
          'log_ACO': ["log_ITE","log_PYC", "log_ACDH", "log_CSC", "log_CAD"]}
    
               
    for x, l in enumerate(lL):
        for y, r in enumerate(rL):
            for z, e in enumerate(eL):
                
                xL = xD[e]
                
                libL = l.split(sep="_")
                lib = libL[0]
                
                #print(lib, r, e)
                
                make_contour(lib, l, r, sL, xL, e)
    
def load_spreadsheet(file, sheet):
    
    f = "%(f)s" % {'f':file}
    
    df = pd.read_excel(f, sheet)
    
    return df

def make_contour(lib, l, r, sL, xL, e) :
    
    name = '%(l)s_%(r)s' % {'l':l, 'r':r}

    coefs = load_spreadsheet('%(n)s_regression.xlsx' % {'n':name}, 'equation')
    ranges = load_spreadsheet('fixed_values.xlsx', 'range')
    z_ranges = load_spreadsheet('fixed_values.xlsx', 'z_range')
    
    mn = '%(l)s_min' % {'l':lib}
    mx = '%(l)s_max' % {'l':lib}
    zmx = '%(l)s_z_max' % {'l':lib}
    step = '%(l)s_step' % {'l':lib}
    
    fig, axes = plt.subplots(nrows=3, ncols=5, figsize=(15, 8))
    
    gs = grsp.GridSpec(3, 5)

    for m, s in enumerate(sL):
        
        fixed_vals = load_spreadsheet('fixed_values.xlsx', s)
        f_v = fixed_vals['%(l)s_value' % {'l':lib}]
        
        for n, x in enumerate(xL):

            ax = plt.subplot(gs[m,n])
        
            # Create the contour plot to be placed in this subplot
            delta = 0.05
            
            X = np.arange(ranges[mn][x], ranges[mx][x], delta)
            Y = np.arange(ranges[mn][e], ranges[mx][e], delta)
            X, Y = np.meshgrid(X, Y)

            
            if '1' in name:
                
                Z = linear_model(x, e, X, Y, coefs, f_v)
                
            elif '2' in name :
                
                Z = second_order_model(x, e, X, Y, coefs, f_v)
                
            else:
                
                Z = second_order_nosquare_model(x, e, X, Y, coefs, f_v)
                
            levels = np.arange(0, z_ranges[zmx][r], z_ranges[step][r])
            
            norm = cm.colors.Normalize(vmax=z_ranges[zmx][r], vmin=0)
            
            cmap = cm.jet

            cset1 = contourf(X, Y, Z, levels,
                             cmap=cm.get_cmap(cmap, len(levels)),
                             norm=norm,
                             )
            # It is not necessary, but for the colormap, we need only the
            # number of levels minus 1.  To avoid discretization error, use
            # either this number or a large number such as the default (256).

            #If we want lines as well as filled regions, we need to call
            # contour separately; don't try to change the edgecolor or edgewidth
            # of the polygons in the collections returned by contourf.
            # Use levels output from previous call to guarantee they are the same.
            cset2 = contour(X, Y, Z,cset1.levels,
                            colors = 'k',
                            hold='on')
            # We don't really need dashed contour lines to indicate negative
            # regions, so let's turn them off.
            for c in cset2.collections:
                c.set_linestyle('solid')

            xlabel('Expression log('+x+')')
            ylabel('Expression log('+e+')')

            cbar = colorbar(cset1)
            cbar.ax.tick_params(axis='y', direction='out')
            
            ax.set_title(s)
            ax.yaxis.set_ticks(np.arange(ranges[mn][e], ranges[mx][e],0.5))
            ax.xaxis.set_ticks(np.arange(ranges[mn][x], ranges[mx][x],0.5))
            ax.tick_params(axis='x', top='off', direction='out')
            ax.tick_params(axis='y', direction='out', right='off')
        
            # Add the lineplot to the overall figure
            fig.add_subplot(ax)
    
    # Use tight layout to ensure no overlaps, use 'pad' kwarg for spacing title
    plt.tight_layout(pad=1)
    plt.savefig('%(n)s_%(e)s.pdf' % {'n':name, 'e':e})

main()