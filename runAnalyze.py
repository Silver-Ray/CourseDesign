import sys
import random
import json

def runAnalyze():
  args = sys.argv[1:]

  pScore = random.random()
  nScore = 1 - pScore

  result = {'input': args, 'pScore': pScore, 'nScore': nScore}
  print(json.dumps(result))
  # return result

if __name__ == "__main__":
  runAnalyze()