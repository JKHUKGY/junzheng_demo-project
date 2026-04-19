# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from junzheng_demo.tests import run_cov_test

    run_cov_test(
        __file__,
        "junzheng_demo",
        is_folder=True,
        preview=False,
    )
