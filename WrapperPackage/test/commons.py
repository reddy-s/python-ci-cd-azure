import sys


class Common(object):

  @staticmethod
  def raise_exception(result):
      if not result.wasSuccessful():
        sys.exit()
