import argparse
import sys

def main():
	parser = argparse.ArgumentParser()
	parse.add_argument('--x', type = float, default = 1.0, help = 'What is the first num?')
	parse.add_argument('--y', type = float, default = 1.0, help = 'What is the second num?')
	parse.add_argument('--op', type = str, default = '+', help = 'What is the first num?')
	args = parser.parse_args()
	sys.stdout.write(str(calc(args)))
def calc(args):
	if args.op == 'add':
		return args.x + args.y
	elif args.op == 'sub':
		return args.x - args.y
	elif args.op == 'mul':
		return args.x*args.y
	elif args.op == 'div':
		return args.x/args.y
if __name__ == '__main__':
	main()
