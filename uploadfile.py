#!/usr/bin/env python

from __future__ import print_function
import os

from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os, sys

date = sys.argv[1]
year = date[5:]
month = date[2:5]
filename = "cm" + date + "bhav.csv.zip"
os.system("wget https://www.nseindia.com/content/historical/EQUITIES/" + year + "/" + month + "/" + filename + " --referer https://www.nseindia.com/products/content/equities/equities/archieve_eq.htm  -U 'Mozilla/5.0'")
del sys.argv[1]
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)
DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

FILES = (
    (filename, None),
#  ('hello.txt', True),
)

for filename, mimeType in FILES:
    metadata = {'name': filename, 'parents': ['0B8uvUsyf4j-EeU1aX09qODJOOU0']}
    if mimeType:
        metadata['mimeType'] = mimeType
    res = DRIVE.files().create(body=metadata, media_body=filename).execute()
    if res:
        print('Uploaded "%s" (%s)' % (filename, res['mimeType']))

#if res:
#    MIMETYPE = 'application/pdf'
#    data = DRIVE.files().export(fileId=res['id'], mimeType=MIMETYPE).execute()
#    if data:
#        fn = '%s.pdf' % os.path.splitext(filename)[0]
#        with open(fn, 'wb') as fh:
#            fh.write(data)
#        print('Downloaded "%s" (%s)' % (fn, MIMETYPE))

#x = DRIVE.about().get().execute()["root"]
#print(x)
#results = DRIVE.files().list(
#    pageSize=10,fields="nextPageToken, files(id, name)").execute()
#items = results.get('files', [])
#if not items:
#    print('No files found.')
#else:
#    print('Files:')
#    for item in items:
#        print('{0} ({1})'.format(item['name'], item['id']))
