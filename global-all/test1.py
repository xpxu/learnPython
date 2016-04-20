SOLR_URL='http://solr.org'
def tt():
    global SOLR_URL
    SOLR_URL=SOLR_URL+'#aa'

if __name__=='__main__':
    tt()
    print SOLR_URL
