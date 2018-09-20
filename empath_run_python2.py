from poster.encode import multipart_encode, MultipartParam
from poster.streaminghttp import register_openers
import urllib2
import sys

got_line = sys.stdin.readline()
got_line = got_line.strip()

url = "https://api.webempath.net/v2/analyzeWav"
register_openers()
items = []
items.append(MultipartParam('apikey', "jZNehSahdorqYqYUSPg8HYaI9fTHdl1SRvQoglcHQV8"))
items.append(MultipartParam.from_file('wav', "recoding2.wav"))
datagen, headers = multipart_encode(items)
request = urllib2.Request(url, datagen, headers)
response = urllib2.urlopen(request)
if response.getcode() == 200:
    sys.stdout.write(respone.read().encode("utf-8"))
else:
    sys.stdout.write("HTTP status %d" % (response.getcode()))
