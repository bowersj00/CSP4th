# a213_password_analyzer.py
import sys
import time
import pwalgorithms as pwa

# usage 
if len(sys.argv) == 2:
  password = sys.argv[1]
  # store user password
  print("Analyzing a one-word password ...")
  time_start = time.time()
  # attempt to find password
  found, num_guesses = pwa.one_word(password)
  # one-word password analysis
elif len(sys.argv) == 3:
  password = sys.argv[1]+" "+sys.argv[2]
  # store user password
  print("Analyzing a two-word password ...")
  time_start = time.time()
  found, num_guesses = pwa.two_words(password)
  # attempt to find password
elif len(sys.argv) == 4:
  password = sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]
  # store user password
  print("Analyzing a two-word and number password...")
  time_start = time.time()
  found, num_guesses = pwa.two_words_and_num(password)
  # attempt to find password
else:
  print("Please supply a passphrase")
  sys.exit(0)

time_end = time.time()

# report results
if (found):
  print(password, "found in", num_guesses, "guesses")
else: 
  print(password, "NOT found in", num_guesses, "guesses!")
print("Time:", format((time_end-time_start), ".8f"))