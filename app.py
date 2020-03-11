import click
from functools import reduce

# TODO usage to change
# TODO deal with int and floats
# TODO Power of and Square Root of operation
# TODO User can use --help or -h flag to get the sub-commands of command


@click.group()
def cli():
    pass


@cli.command(help='Add numbers')
@click.argument('nums', nargs=-1)
@click.option('-f', is_flag=True)
def add(nums, f):
    if f:
        nums_convert = [float(num) for num in nums]
    else:
        nums_convert = [int(num) for num in nums]
    result = reduce((lambda x, y: x + y), nums_convert)
    click.echo(f"Addition of numbers {nums_convert} is {result}")


@cli.command(help='Subtract numbers')
@click.argument('nums', nargs=-1)
@click.option('-f', is_flag=True)
def subtract(nums, f):
    if f:
        nums_convert = [float(num) for num in nums]
    else:
        nums_convert = [int(num) for num in nums]
    result = reduce((lambda x, y: x - y), nums_convert)
    click.echo(f"Subtraction of numbers {nums_convert} is {result}")


@cli.command(help='Multiply numbers')
@click.argument('nums', nargs=-1)
@click.option('-f', is_flag=True)
def multiply(nums, f):
    if f:
        nums_convert = [float(num) for num in nums]
    else:
        nums_convert = [int(num) for num in nums]
    result = reduce((lambda x, y: x * y), nums_convert)
    click.echo(f"Multiplication of numbers {nums_convert} is {result}")

    
@cli.command(help='Division numbers')
@click.argument('nums', nargs=-1)
@click.option('-f', is_flag=True)
def division(nums, f):
    if f:
        nums_convert = [float(num) for num in nums]
    else:
        nums_convert = [int(num) for num in nums]
    result = reduce((lambda x, y: x // y), nums_convert)
    click.echo(f"Division of numbers {nums_convert} is {result}")

    

if __name__ == '__main__':
    cli()
