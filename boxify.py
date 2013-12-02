'''
Created on Dec 2, 2013

@author: george
'''

import sys

def boxify(astr, border="#", margin=1):
    ''' Prints the string in a pretty box
    e.g. >> print(boxify("hello"))
         #########
         #       #
         # hello #
         #       #
         ######### '''
    
    if len(border) > 1:
        raise ValueError("border must be one character long")
    
    lstr = astr.split("\n")
    width = max([len(x) for x in lstr])
    lstr_padded = ['{:<{width}}'.format(x, width=width) for x in lstr]
    lstr_content = [border + " "*margin + x + " "*margin + border for x in lstr_padded]
    # add on top and bottom bits
    borderbar_len = width + 2*margin + 2*len(border)
    borderbar = border*borderbar_len
    margin_bar = border + " "*margin + " "*width + " "*margin + border
    top = [borderbar,] + [margin_bar,]*margin
    bottom = [margin_bar,]*margin + [borderbar,]
    all_together_now = top+lstr_content+bottom
    return "\n".join(all_together_now)
    

if __name__ == "__main__":
    print("Boxifying %s:" % sys.argv[1])
    print(boxify(sys.argv[1]))
    
    print(boxify("Banana\nsplit", margin=2))