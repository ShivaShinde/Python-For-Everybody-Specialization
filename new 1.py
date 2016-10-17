import sys
prev_word          = "  "                #initialize previous word  to blank string
months             = ['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Nov','Dec']
dates_to_output    = [] 
day_cnts_to_output = [] 
line_cnt           = 0  #count input lines
for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1     
    curr_word  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item
    if curr_word != prev_word:
        if line_cnt>1:
	    for i in range(len(dates_to_output)):  #loop thru dates, indexes start at 0
	         print('{0} {1} {2} {3}'.format(dates_to_output[i],prev_word,day_cnts_to_output[i],curr_word_total_cnt))
	    dates_to_output   =[]
            day_cnts_to_output=[]
        prev_word         =curr_word  #set up previous word for the next set of input lines
    if (value_in[0:3] in months): 
        date_day =value_in.split() #split the value field into a date and day-cnt
        dates_to_output.append(date_day[0])
        day_cnts_to_output.append(date_day[1])
    else:
        curr_word_total_cnt = value_in  
for i in range(len(dates_to_output)):  #loop thru dates, indexes start at 0
         print('{0} {1} {2} {3}'.format(dates_to_output[i],prev_word,day_cnts_to_output[i],curr_word_total_cnt))