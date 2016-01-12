# Hint:  use Google to find python function

####a) 
from datetime import datetime

## date strings
date_start = '01-02-2013'  
date_stop = '07-28-2015'

## convert to dates
date1 = datetime.strptime(date_start, '%m-%d-%Y').date()
date2 = datetime.strptime(date_stop, '%m-%d-%Y').date()

## calc diff days
(date2 - date1).days


####b)  
from datetime import datetime

date_start = '12312013'  
date_stop = '05282015'  

## convert to dates
date1 = datetime.strptime(date_start, '%m%d%Y').date()
date2 = datetime.strptime(date_stop, '%m%d%Y').date()

## calc diff days
(date2 - date1).days


####c)
from datetime import datetime

date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

## convert to dates
date1 = datetime.strptime(date_start, '%d-%b-%Y').date()
date2 = datetime.strptime(date_stop, '%d-%b-%Y').date()

## calc diff days
(date2 - date1).days
