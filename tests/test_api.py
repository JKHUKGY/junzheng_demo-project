# -*- coding: utf-8 -*-

from junzheng_demo import api


def test():
    _ = api


if __name__ == "__main__":
    from junzheng_demo.tests import run_cov_test

    run_cov_test(
        __file__,
        "junzheng_demo.api",
        preview=False,
    )
