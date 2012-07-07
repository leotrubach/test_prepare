from os.path import abspath, dirname, join


def absolute(subdir=''):
    return join(dirname(abspath(__file__)), subdir)
