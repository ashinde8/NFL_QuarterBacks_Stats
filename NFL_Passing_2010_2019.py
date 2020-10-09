# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:21:08 2020

@author: Lenovo
"""

import pandas as pd
import os

def nfl_passing(year1,year2):

    folder_path = 'C:\\Users\\Lenovo\\Desktop\\NFL'
    url = 'https://www.pro-football-reference.com/years/'
    
    for i in range(year1,year2):
    
        yr = str(i)
        
        url_link = url + yr + '/passing.htm'
        df_name = yr + '_NFL_Passing'
    
        new_path = os.path.join(folder_path, df_name)
        new_path = new_path + '.csv'
    
        df = pd.read_html(url_link)
        df_full = df[0]
        
        final_df = df_full[['Player', 'Tm', 'Pos', 'Cmp', 'Att','Yds', 'TD','Int', 'Lng','Sk', 'Yds.1','4QC', 'GWD']]
        
        final_df.to_csv(new_path, index = False, header = True)

nfl_passing(2010,2020)