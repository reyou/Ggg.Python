# https://docs.python.org/3/tutorial/stdlib2.html
# Threading is a technique for decoupling tasks which are not sequentially dependent.
"""the preferred approach to task coordination is to concentrate
all access to a resource in a single thread and then use the queue module
to feed that thread with requests from other threads.
Applications using Queue objects for inter-thread communication and
coordination are easier to design, more readable, and more reliable.
"""
import threading, zipfile


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        # Open a ZIP file, where file can be a path to a file (a string),
        # a file-like object or a path-like object.'''
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)


background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()  # Wait for the background task to finish
print('Main program waited until background was done.')
