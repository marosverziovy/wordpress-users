#!env/bin/python

import re
import sys
import argparse
import requests
from prettytable import PrettyTable

# Ignore SSL mismatch warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Options
START_ID=1
DEFAULT_COUNT=10

class wordpressUsers:

  def findUsers(self, url, startId, endId, debug):
    x = PrettyTable()
    x.field_names = ["ID", "User", "URL"]

    for userId in range(int(startId), int(endId)):
      r = requests.head(url + '?author={}'.format(userId), allow_redirects=True, verify=False) 
      if debug:
        sys.stdout.write('.')
        sys.stdout.flush()
      for redirect in r.history:
        MatchObj = re.search(r'\/(\w+)\/?$', redirect.headers['Location'])
        if MatchObj:
          user = MatchObj.group().strip('/')
          x.add_row([userId, user, redirect.headers['Location']])
    return(x)

  def debugPrint(self, debug, args):
    d = PrettyTable()
    d.field_names = ["Key", "Value"]
    for key,value in args.__dict__.iteritems():
      d.add_row([key, value]) 
    return(d)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Find Wordpress users")
  parser.add_argument('url', action='store', help="Site url, including protocol (e.g. http://)")
  parser.add_argument('-s', '--start', action='store', default=START_ID, help="Starting ID")
  parser.add_argument('-e', '--end', action='store', default=DEFAULT_COUNT - 1, help="Last ID")
  parser.add_argument('-d', '--debug', action='store_true', default=False, help="Print debug info")
  args = parser.parse_args()
   
  wu = wordpressUsers()

  # Debug info
  if args.debug:
    print(wu.debugPrint(args.debug, args))

  # Run search
  print("\n{}".format(wu.findUsers(args.url, args.start, args.end, args.debug)))
