from Integration.integrator import PythonIntegrator
from .constants import PackageConstants


class Wrapper(object):

  def __init__(self):
    self.context = PackageConstants.PACKAGE
    self.integrator = PythonIntegrator()

  def sample_wrapper_repo(self):
    return PackageConstants.MESSAGE.format(self.context)

  def call_integration_package(self):
    return self.integrator.integrator_repo()


if __name__ == "__main__":
  print(PackageConstants.EXECUTING_MAIN_PROGRAM)
