# Hint:  use Google to find python function
from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

a_date_format = '%m-%d-%Y'
a_date_start = datetime.strptime(date_start, date_format)
a_date_stop = datetime.strptime(date_stop, date_format)
a_delta = a_date_stop - a_date_start
print(a_delta.days)
# 937 is output

####b)  
date_start = '12312013'  
date_stop = '05282015'  

b_date_format = "%m-%d-%Y"
b_start_date = datetime.fromtimestamp(int(date_start))
b_end_date = datetime.fromtimestamp(int(date_stop))
b_delta = b_end_date - b_start_date
print(b_delta.days)
# output is -82 so 82 days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015' 

c_date_format = '%d-%b-%Y'
c_start_date = datetime.strptime(date_start, date_format)
c_end_date = datetime.strptime(date_stop, date_format)
c_delta = c_end_date - c_start_date
print(c_delta.days)
# output is 7850 days 
