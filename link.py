import argparse

from os import listdir, unlink
from os.path import isfile, dirname, join, expanduser, abspath

def symlink(source, link_name):
    import os
    os_symlink = getattr(os, "symlink", None)
    if callable(os_symlink):
        os_symlink(source, link_name)
    else:
        import ctypes
        csl = ctypes.windll.kernel32.CreateSymbolicLinkW
        csl.argtypes = (ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint32)
        csl.restype = ctypes.c_ubyte
        flags = 1 if os.path.isdir(source) else 0
        if csl(link_name, source, flags) == 0:
            raise ctypes.WinError()

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

      if args.action == 'link' and not isfile(lnpath):
        if not args.dry:
          symlink(dfpath, lnpath)
        print dfpath, ' >> ', lnpath
      elif args.action == 'clean' and isfile(lnpath):
        if not args.dry:
          unlink(lnpath)
        print '!!', lnpath
