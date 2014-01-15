import unittest

def main():
    """Runs the testsuite as command line application."""
    try:
        unittest.main()
    except Exception as e:
        print('Error: %s' % e)
