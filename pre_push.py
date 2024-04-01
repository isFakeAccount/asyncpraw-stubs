"""Run static analysis on the project."""

from __future__ import annotations

import argparse
import sys
from subprocess import CalledProcessError, check_call


def do_process(args: list[str], shell: bool = False, cwd: str = ".") -> bool:
    """Run program provided by args.

    Return ``True`` on success.

    Output failed message on non-zero exit and return False.

    Exit if command is not found.

    """
    print(f"Running: {' '.join(args)}")
    try:
        check_call(args, shell=shell, cwd=cwd)
    except CalledProcessError:
        print(f"\nFailed: {' '.join(args)}")
        return False
    except Exception as exc:
        sys.stderr.write(f"{exc!s}\n")
        sys.exit(1)
    return True


def run_static() -> bool:
    """Run static analysis on the source code.

    :returns: True if static analysis processes were successful, False otherwise.
    :rtype: bool

    """
    success = True
    success &= do_process(["mypy", "src"])
    success &= do_process(["pyright"])

    return success


def run_linting() -> bool:
    """Run linting checks on the source code.

    :returns: True if all linting processes were successful, False otherwise.
    :rtype: bool

    """
    success = True
    success &= do_process(["black", "src"])
    success &= do_process(["ruff", "check", "src", "--fix"])
    success &= do_process(["docstrfmt", "."])

    return success


def main() -> int:
    """Run the main function.

    Run static and lint on code

    """

    parser = argparse.ArgumentParser(description="Run static and/or unit-tests")
    parser.add_argument(
        "-s",
        "--static",
        action="store_true",
        help="Do not run static tests (black/flake8/pydocstyle/sphinx-build)",
        default=False,
    )

    parser.add_argument(
        "-l",
        "--linting",
        action="store_true",
        default=True,
        help="Run the linting",
    )

    args = parser.parse_args()
    success = True
    try:
        if args.static:
            success &= run_static()

        if args.linting:
            success &= run_linting()

    except KeyboardInterrupt:
        return int(not False)
    return int(not success)


if __name__ == "__main__":
    exit_code = main()
    print("\npre_push.py: Success!" if not exit_code else "\npre_push.py: Fail")
    sys.exit(exit_code)
