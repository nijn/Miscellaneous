########################################
# CheckURLs.py
# 2013-01-09
# janek@nijn.nu
#
# Checks URLs from a batch list against a
# live website, as if an end-user were
# to open them from following links.
########################################

from urllib2 import quote
from httplib import HTTPConnection, HTTPException


######## USER-DEFINED VARIABLES ########

working_dir = r'C:\agreement_documents'
urls_file = 'urls.txt'
results_file = 'urls-errors.txt'


######## MAIN ##########################

# open files
urls = open(working_dir+urls_file, 'r')
results = open(working_dir+results_file, 'w')

# helper variables
counter = 0
counter_bad = 0

# create connection to host
conn = HTTPConnection('www.testsite.com')

print 'Reading ' + urls_file + '...'
urls.readline()
for url in urls:

    # skip empty lines
    url = url.strip()
    if len(url) > 0 and url != 'NULL':
        counter += 1
        print url

        try:
            # open conn with formatted URL string
            conn.request('HEAD', '/testpath/'+quote(url, safe="%/:=&?~#+!$,;'@()*[]"))

            try:
                # handle server output
                res = conn.getresponse()
                res.read()
                s = str(res.status) + ': ' + url + '\n'

                # report on erroneous URLs
                if res.status != 200:
                    results.write(s)
                    counter_bad += 1
                #endif

            except HTTPException as e:
                print 'Script error: ' + e.message
            #endtry

        except HTTPException as e:
            print 'Script error: ' + e.message
        #endtry

    #endif
#endfor

if counter_bad == 0:
    results.write('All URLs are good.')

# close all resources
conn.close()
urls.close()
results.close()

print '\n============='
print str(counter) + '\tTotal'

if counter_bad > 0:
    print str(counter_bad) + '\t:(    -->  check ' + results_file
else:
    print '\t:D'
#endif

