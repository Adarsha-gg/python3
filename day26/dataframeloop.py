student = {"hi":[44,33,55],
           "hello":["ez","pz","dg"]}

import pandas

dict = pandas.DataFrame(student)



#looping thru rows of a dataframe

for(index, row) in dict.iterrows():
    if row.hi > 35:
        print(row.hello)