from pythongrid import *


class Test:

  sideEffect="not set"

  def doSomething(self, a):
    print "executing test"
    self.sideEffect="sideeffect set"

    return a+a


def makeMethodJobs():

  myobj=Test()

  jobs=[]
  jobs.append(MethodJob(myobj.doSomething, ["aaaaaXXXXXXXXXXX"]))
  jobs.append(MethodJob(myobj.doSomething, ["bbbbbbbbbXXXXXXXXXYa"]))
  jobs.append(MethodJob(myobj.doSomething, ["ccccccccccXXXXXXXXX"]))

  return jobs


def makeJobs():

  jobs=[]
  jobs.append(Job(test, ["aaaaaXXXXXXXXXXX"]))
  jobs.append(Job(test, ["bbbbbbbbbXXXXXXXXXYa"]))
  jobs.append(Job(test, ["ccccccccccXXXXXXXXX"]))

  return jobs



def test(string):

  print string
  return string+string;




def runExample():

  print "generating fuction jobs"

  functionJobs = makeJobs()

  print functionJobs[0].ret

  processedFunctionJobs = processJobs(functionJobs)

  print processedFunctionJobs[0].ret


  print "generating method jobs"

  methodJobs = makeMethodJobs()

  print methodJobs[0].obj.sideEffect
  print methodJobs[0].ret

  processedMethodJobs = processJobs(methodJobs)
 
  print processedMethodJobs[0].obj.sideEffect
  print processedMethodJobs[0].ret
 


def main(argv=None):


  if argv is None:
    argv = sys.argv

  try:
    try:

      opts, args = getopt.getopt(argv[1:], "h", ["help"])

      runExample() 

    except getopt.error, msg:
      raise Usage(msg)


  except Usage, err:

    print >>sys.stderr, err.msg
    print >>sys.stderr, "for help use --help"

    return 2

  

if __name__ == "__main__":

  main()
  #sys.exit(main())

