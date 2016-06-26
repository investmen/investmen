# investmen

1) Goto https://console.developers.google.com/apis/credentials?project=prvdk-1354
2) Download the oauth 2.0 client ID credential JSON and store is as client_secret.json in git clone directory
3) python uploadfile.py DDMMMYYYY
eg.python uploadfile.py 06JUN2015

r@ra:~/vivekd/pratheep/uploadfile$ python uploadfile.py 13MAY2015
--2016-06-26 22:18:15--  https://www.nseindia.com/content/historical/EQUITIES/2015/MAY/cm13MAY2015bhav.csv.zip
Resolving www.nseindia.com (www.nseindia.com)... 23.52.72.93
Connecting to www.nseindia.com (www.nseindia.com)|23.52.72.93|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 55880 (55K) [application/zip]
Saving to: ‘cm13MAY2015bhav.csv.zip’

100%[================================================================================>] 55,880       363KB/s   in 0.2s

2016-06-26 22:18:16 (363 KB/s) - ‘cm13MAY2015bhav.csv.zip’ saved [55880/55880]

Uploaded "cm13MAY2015bhav.csv.zip" (application/zip)

r@ra:~/vivekd/pratheep/uploadfile$ python uploadfile.py 06JUN2015
--2016-06-26 22:18:48--  https://www.nseindia.com/content/historical/EQUITIES/2015/JUN/cm06JUN2015bhav.csv.zip
Resolving www.nseindia.com (www.nseindia.com)... 23.52.72.93
Connecting to www.nseindia.com (www.nseindia.com)|23.52.72.93|:443... connected.
HTTP request sent, awaiting response... 404 Not Found
2016-06-26 22:18:49 ERROR 404: Not Found.

Traceback (most recent call last):
  File "uploadfile.py", line 41, in <module>
    res = DRIVE.files().create(body=metadata, media_body=filename).execute()
  File "/usr/local/lib/python2.7/dist-packages/googleapiclient/discovery.py", line 765, in method
    mimetype=media_mime_type)
  File "/usr/local/lib/python2.7/dist-packages/oauth2client/util.py", line 135, in positional_wrapper
    return wrapped(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/googleapiclient/http.py", line 539, in __init__
    fd = open(self._filename, 'rb')
IOError: [Errno 2] No such file or directory: 'cm06JUN2015bhav.csv.zip'

r@ra:~/vivekd/pratheep/uploadfile$ python uploadfile.py 11JUN2015
--2016-06-26 22:18:55--  https://www.nseindia.com/content/historical/EQUITIES/2015/JUN/cm11JUN2015bhav.csv.zip
Resolving www.nseindia.com (www.nseindia.com)... 23.52.72.93
Connecting to www.nseindia.com (www.nseindia.com)|23.52.72.93|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 55433 (54K) [application/zip]
Saving to: ‘cm11JUN2015bhav.csv.zip’

100%[================================================================================>] 55,433      --.-K/s   in 0.1s

2016-06-26 22:18:56 (463 KB/s) - ‘cm11JUN2015bhav.csv.zip’ saved [55433/55433]

Uploaded "cm11JUN2015bhav.csv.zip" (application/zip)
