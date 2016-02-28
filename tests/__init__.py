import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'

from django.test.utils import get_runner
from django.conf import settings

TestRunner = get_runner(settings)


def run_tests():
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['dj_impediments'])
    sys.exit(bool(failures))
