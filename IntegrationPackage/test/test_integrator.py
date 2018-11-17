import unittest

from Integration.integrator import PythonIntegrator


class TestPythonIntegrator(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.stringOutput = "This information is coming form: 'Python Integrator package:1.0.0'"

  def test_integrator_repo(self):
    integrator = PythonIntegrator()
    self.assertEqual(integrator.integrator_repo(), self.stringOutput)


if __name__ == '__main__':
  unittest.main()
