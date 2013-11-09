from os import listdir, symlink
from os.path import isfile, dirname, join, expanduser

if __name__ == '__main__':
  dotdir = dirname(__file__)
  for dfname in listdir(dotdir):
    dfpath = join(dotdir, dfname)
    lnpath = expanduser(join('~', dfname))
    if isfile(dfpath) and dfname.startswith('.') and dfname.count('.') == 1:
      print dfpath, '>', lnpath
      symlink(dfpath, lnpath)
      
    

