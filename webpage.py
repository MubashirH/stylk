"""This is a doc string
    This program will create an html page and ask the user for following inputs
    -one main header
    -one sub header
    -at lease 2 paragraphs
"""

def title():
    title=raw_input('Enter the title ')
    return title
def H1():
    h1=raw_input('Enter the main header for your website')
    return h1
def H2():
    h2=raw_input('Enter the sub header for your website')
    return h2
def H3():
    h2=raw_input('Enter the topic header for your website')
    return h2
def P():
    list=[]
    i=1
    n=int(raw_input('Enter the no of para'))
    for i in range(n):
        para=raw_input('Enter the paragraph')
        i+=1
        list.append(para)
    return list
def p_H1(h1):
    print '<h1>',h1.capitalize,'</h1>'
def p_H2(h2):
    print '<h2>',h2.capitalize,'</h2>'
def p_H3(h3):
    print '<h3>',h3.capitalize,'</h3>'
def p_head(t):
    print ' <head>\n  <title>',t.capitalize,'</title>\n </head>'
    
if __name__=='__main__':
    t=title()
    h1=H1()
    h2=H2()
    h3=H3()
    p=P()
    str='webpage.html'
    print '\n\n'
    print str.center(80,' ')
    print '\n\n'
    print '<html>'
    p_head(t)
    print ' <body>'
    print '\t',p_H1(h1)
    print '\t<p>',p[1],'\n\t</p>'
    print '\t',p_H2(h2)
    print '\t<p>',p[0],'\n\t</p>'
    print '\t',p_H3(h3)
    print '\t<p>',p[2],'\n\t</p>'
    print ' </body>'
    print '</html>'
        
