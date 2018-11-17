import unittest

from Wrapper.wrap import Wrapper


class TestPythonIntegrator(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.stringOutput = "This information is coming form: 'Wrapper package'"
    cls.stringOutputChild = "This information is coming form: 'Python Integrator package:1.0.0'"

  @classmethod
  def setUp(self):
        self.wrapper = Wrapper()

  def test_sample_python_repo(self):
    self.assertEqual(self.wrapper.sample_wrapper_repo(), self.stringOutput)

  def test_call_integration_package(self):
    self.assertEqual(self.wrapper.call_integration_package(), self.stringOutputChild)


if __name__ == '__main__':
  unittest.main()
