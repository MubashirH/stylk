"""This is a doc string
    This program will create an html page and ask the user for following inputs
    -one main header
    -one sub header
    -at lease 2 paragraphs
"""


def get_input():
    head=str(raw_input('Enter the header for your website'))
    sub=str(raw_input('Enter the sub heading'))
    print 'There must and should be 2 paragraphs for your website'
    n=int(raw_input('no of paragraphs u want to enter'))
    if n>=2:
        final=[]
        i=1
        for i in range(n):
            par=str(raw_input('Enter the paragraph'))
            i+=1
            final.append(par)
        para='\n     </p>\n     <p>'.join(final)
        
    return str(head), str(sub), int(n), str(para)

def webpage(head,sub,n,para):
    str='webpage.html'
    print str.center(80,' ')
    print '<html>'
    print ' <head>'
    print '  <title>'
    print '         ',head.capitalize()
    print '  </title>'
    print ' </head>'
    print ' <body>'
    print '     <h1>',sub.capitalize(),'</h1>'
    print '     <p>',para,'\n     </p>'
    print ' </body>'
    print '</html>'
             
    

#main
head,sub,n,para=get_input()
webpage(head,sub,n,para)
