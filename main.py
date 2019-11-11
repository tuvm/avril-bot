# -*- coding: utf-8 -*-
import click
import platform


@click.group()
def main(args=None):
    """Console script for avril-bot"""
    pass


@main.command()
def info():
    python_version = platform.python_version()
    system_info = f"{platform.system()}{platform.release()}"
    print("")
    print("ENVIRONMENT")
    print(f"      python version : {python_version}")
    print(f"  system information : {system_info}")


if __name__ == "__main__":
    main()
