import os, sys, time

runid = sys.argv[1]
for x in range(20):
  print("Run number: {}, repeated {}".format(runid, x))
  time.sleep(20)