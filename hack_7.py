"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(ls):
    total_len = len(ls)
    i = 0     
    new_ls = []     
    
    if total_len > 0:    
       while(total_len > i):
            if i % 2 == 0:
               new_ls.append(i)

            new_ls.append(str(i))
            i += 1  

       return new_ls 
  