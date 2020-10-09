# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:33:16 2020

@author: Lenovo
"""

# NFL QB stats

from bs4 import BeautifulSoup
import os
import time
import requests
import csv
import pandas as pd



def run(year1,year2):
    
    url = 'https://www.pro-football-reference.com/years/'
    folder_path = 'C:\\Users\\Lenovo\\Desktop\\NFL11'

    
    for yr in range(year1,year2):

        file_yr = str(yr)
        file_name = 'nfl_passing_table_' + file_yr +'.txt'
        
        fw=open(file_name,'w',encoding='utf8') # output file
        
        writer=csv.writer(fw,lineterminator='\n')   
            #create a csv writer for this file
        nfl_passing_link = url + str(yr) + '/passing.htm'

        for i in range(5): # try 5 times

            response=requests.get(nfl_passing_link)
                                  #headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
        
            if response: # explanation on response codes: https://realpython.com/python-requests/#status-codes
                break # we got the file, break the loop
            else:time.sleep(2) # wait 2 secs
             
        #html=response.text# read in the text from the file
        soup = BeautifulSoup(response.text, 'html.parser') # parse the html 
       
        #box = soup.find('div',{'class':'overthrow table_container'})
        table = soup.findAll('table')[0]
        table_rows = table.find_all('tr')[2:]
        
        for tr in table_rows:
            
            Player, Team, Position, Passes_Completed, Passes_Attempted, Pass_Cmp_Prcnt, Passing_Yards, Passing_Touchdowns, Interceptions_Thrown, Lngst_Cmp_Pass_Thrown, Times_Sacked, Sacked_Yds_Lost, Comebacks, Game_Winning_Drives   = 'NA', 'NA', 'NA', 'NA', 'NA', 'NA','NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'

            player_name =tr.find('td', {'data=stat':'player'})
            Player = player_name.a.text
            
            print("Player name",Player)
            
            team_chunk=tr.find('td', {'data-stat':'team'})
            team_name = team_chunk.find('a')
            Team = team_name.text
            
            print("Team name", Team)
                    
            position_chunk=tr.find('td',{'data-stat':'pos'})
            Position = position_chunk.text
            
            passes_completed_chunk=tr.find('td',{'data-stat':'pass_cmp'})
            Passes_Completed = passes_completed_chunk.text
            
            passes_attempted_chunk=tr.find('td',{'data-stat':'pass_att'})
            Passes_Attempted = passes_attempted_chunk.text
            
            pass_cmp_prcnt_chunk=tr.find('td',{'data-stat':'pass_cmp_perc'})
            Pass_Cmp_Prcnt = pass_cmp_prcnt_chunk.text
            
            passing_yards_chunk=tr.find('td',{'data-stat':'pass_yds'})
            Passing_Yards = passing_yards_chunk.text
            
            passing_touchdowns_chunk=tr.find('td',{'data-stat':'pass_td'})
            Passing_Touchdowns = passing_touchdowns_chunk.text
            
            Interceptions_Thrown_chunk=tr.find('td',{'data-stat':'pass_int'})
            Interceptions_Thrown = Interceptions_Thrown_chunk.text
            
            Lngst_Cmp_Pass_Thrown_chunk=tr.find('td',{'data-stat':'pass_long'})
            Lngst_Cmp_Pass_Thrown = Lngst_Cmp_Pass_Thrown_chunk.text
            
            Times_Sacked_chunk=tr.find('td',{'data-stat':'pass_sacked'})
            Times_Sacked = Times_Sacked_chunk.text
            
            Sacked_Yds_Lost_chunk=tr.find('td',{'data-stat':'pass_sacked_yds'})
            Sacked_Yds_Lost = Sacked_Yds_Lost_chunk.text
            
            Comebacks_chunk=tr.find('td',{'data-stat':'comebacks'})
            Comebacks = Comebacks_chunk.text
               
            Game_Winning_Drives_chunk=tr.find('td',{'data-stat':'gwd'})
            Game_Winning_Drives = Game_Winning_Drives_chunk.text

           
            writer.writerow([Player, Team, Position, Passes_Completed, Passes_Attempted, Pass_Cmp_Prcnt, Passing_Yards, Passing_Touchdowns, Interceptions_Thrown, Lngst_Cmp_Pass_Thrown,Times_Sacked, Sacked_Yds_Lost, Comebacks, Game_Winning_Drives]) # write to file 
        
        fw.close()
        
        var = str(yr) + 'NFL_Passing_Stats'  
        var = str(var)
        
        new_path = os.path.join(folder_path, var)
        new_path = new_path + '.csv'
                
        nfl_table = pd.read_csv(file_name, names = ['Player', 'Team', 'Position', 'Passes_Completed', 'Passes_Attempted', 'Pass_Cmp_Prcnt', 'Passing_Yards', 'Passing_Touchdowns', 'Interceptions_Thrown', 'Lngst_Cmp_Pass_Thrown','Times_Sacked', 'Sacked_Yds_Lost', 'Comebacks', 'Game_Winning_Drives'], sep = ',')
        nfl_table.to_csv(new_path, index = False, header=True)

run(2019,2020)    
