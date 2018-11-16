from .constants import PackageConstants


class PythonIntegrator(object):

  def __init__(self):
    self.context = PackageConstants.PACKAGE

  def integrator_repo(self):
    return PackageConstants.MESSAGE.format(self.context)


if __name__ == "__main__":
  print(PackageConstants.EXECUTING_MAIN_PROGRAM)
