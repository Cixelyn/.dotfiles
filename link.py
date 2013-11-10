import argparse

from os import listdir, symlink, unlink
from os.path import isfile, dirname, join, expanduser, abspath

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('action', choices=('clean', 'link'))
  parser.add_argument("-d", "--dry", action='store_true')

  args = parser.parse_args()

  dotdir = abspath(dirname(__file__))
  for dfname in listdir(dotdir):
    dfpath = join(dotdir, dfname)
    lnpath = expanduser(join('~', dfname))
    if isfile(dfpath) and dfname.startswith('.') and dfname.count('.') == 1:

      if args.action == 'link':
        if not args.dry:
          symlink(dfpath, lnpath)
        print dfpath, ' >> ', lnpath
      elif args.action == 'clean' and isfile(lnpath):
        if not args.dry:
          unlink(lnpath)
        print '!!', lnpath
