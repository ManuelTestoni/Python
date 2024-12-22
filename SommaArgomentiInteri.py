import argparse
parser = argparse.ArgumentParser(description='Somma dei primi interi.')
parser.add_argument(dest='integers', metavar='N', type=int,nargs='*', help='Interi per la somma')
args = parser.parse_args()

print("1: Per sapere la somma degli input\n")
print("2: Per sapere il minimo degli input\n")
print("3: Per sapere il massimo degli input\n")
print("4: Per sapere la media degli input\n")
scelta = int(input())

if scelta == 1:
    print(sum(args.integers))
elif scelta == 2:
    print(min(args.integers))
elif scelta == 3:
    print(max(args.integers))
elif scelta == 4:
    avg = sum(args.integers)/len(args.integers)
    print(avg)