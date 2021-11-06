import os, sys, time

runid = os.environ['INPUT_ID']
for x in range(20):
  print("Run number: {}, repeated {}".format(runid, x))
  time.sleep(20)