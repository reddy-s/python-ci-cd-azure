# Sample Python CI CD Project using Azure

This repo gives a guideline on how to use Azure Team services to implement a CI/CD pipeline for python based projects

## Packages

This project has two package which are `IntegrationDemo` and `Wrapper`. Here the `Wrapper` package depends on the `IntegrationDemo` package.

* Uses python 3.6

### Integration Package

#### Running Tests

You can run the tests in the integration package by doing the following

```sh
$ cd ./IntegrationPackage
$ python -m unittest discover
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

#### Package the application 

```sh
$ cd ./IntegrationPackage
$ python integration_demo_setup.py sdist bdist_wheel
```

### Wrapper Package

#### Running Tests

You can run the tests in the wrapper package by doing the following

```sh
$ cd ./WrapperPackage
$ python -m unittest discover
...
----------------------------------------------------------------------
Ran 2 test in 0.001s

OK
```

#### Package the application 

```sh
$ cd ./WrapperPackage
$ python wrapper_setup.py sdist bdist_wheel
```
