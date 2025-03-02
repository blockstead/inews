import time
import sys
import random

def typewriter(text, speed):
    delay = []
    for i in text:
        delay.append(random.randint(1,20))
    for char,d in list(zip(text,delay)):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(d/speed)

# Example usage
text_1 ='''
Welcome to our interactive dashboard, where we present 
a comprehensive view of COVID-19 data across 
European Union countries from 2020 to 2022. 
This platform helps you understand the pandemic's 
impact through clear visualizations. 
Dive into a time-series analysis of cases and fatalities, 
exploring trends and comparisons using easy-to-use filters. 
Whether you're curious about a specific country 
or a particular time frame, this dashboard empowers you 
to find the answers you seek. 

'''
text_2 = '''Join us on this journey of insights and exploration 
as we navigate the data together.'''

# Printing them out
typewriter(text_1,100)
typewriter(text_2,60)
