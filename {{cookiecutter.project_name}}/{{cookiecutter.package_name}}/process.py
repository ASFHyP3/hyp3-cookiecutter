#!/usr/bin/env python3
"""
Processing with {{cookiecutter.package_name|replace('hyp3_', '')}}
"""

import argparse
import logging
import os

log = logging.getLogger(__name__)


def process(hello_world=False):
    """Process hello_world

    Args:
        hello_world (bool): If true, print "Hello world!" (Default: False)
    """
    log.debug(f'Hello world? {hello_world}')
    if hello_world:
        print("Hello world!")


def main():
    """Main entrypoint"""
    parser = argparse.ArgumentParser(
        prog=os.path.basename(__file__),
        description=__doc__,
    )
    parser.add_argument('--hello-world', action='store_true',
                        help='Print "Hello world!"')
    args = parser.parse_args()

    process(**args.__dict__)


if __name__ == "__main__":
    main()
