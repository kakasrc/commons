'''
Created on 2011-11-21

@author: shk
'''
import sys, threading, httplib, time, urllib2

SERVER_NAME = 'www.google.com'
RESOURCE = '/test'
TEST_COUNT = 1

threads = []
thread_count = 1

all_status = [0 for i in range(thread_count)]
ok_status = [0 for i in range(thread_count)]
notFound_status = [0 for i in range(thread_count)]

class RequestThread(threading.Thread):
    def __init__(self, thread_name, number):
        threading.Thread.__init__(self)
        self.test_count = 0
        self.number = number
        print self.getName() + ' initialized successfully'

    def run(self):
        i = 0
        while i < TEST_COUNT:
            self.test_performace()
            i += 1

    def test_performace(self):
        conn = httplib.HTTPConnection(SERVER_NAME)
        url = RESOURCE;
        request = urllib2.Request('http://' + SERVER_NAME + RESOURCE)
        try:
            rsps = urllib2.urlopen(request)
            if rsps.getcode() == 200:
                ok_status[self.number] += 1
                
        except urllib2.HTTPError, e:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            conn.close()
            return
        except urllib2.URLError, e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
            conn.close()
            return
        else:
  # everything is fine
            print 'exception!!!'
            print sys.exc_info()[0],sys.exc_info()[1]
            conn.close()
            return  
        all_status[self.number] += 1  
        conn.close()

time_start = time.time();
for i in range(thread_count):        
    t = RequestThread("thread" + str(i), i)
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
print time.time() - time_start

all = 0
ok = 0
notFound = 0
for i in range(thread_count):
    all += all_status[i]
    ok += ok_status[i]
    notFound += notFound_status[i]
 
print '-------------------Result-------------------'   
print 'allStatus:' + str(all)
print 'okStatus:' + str(ok)
print 'notFoundStatus:' + str(notFound)
