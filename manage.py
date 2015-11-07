#!/usr/bin/env python
# coding=utf-8

import click


@click.group(context_settings={
    'help_option_names': ['-h', '--help']
})
def cli():
    """The commandline interface for project_sketch"""
    pass


@cli.command()
def ping():
    """Do a ping"""
    print "pong!"


if __name__ == '__main__':
    cli()
