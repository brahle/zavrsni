import fileinput 
import re

temp_str = "Temp = (?P<temp>\d+(.\d+)?)"
neigh_str = "Neigh = -(?P<neigh>\d+(.\d+)?)"
best_str = "Best = -(?P<best>\d+(.\d+)?)"
curr_str = "Curr = -(?P<curr>\d+(.\d+)?)"
my_regex = re.compile(".+{0}.+{1}.+{2}.+{3}".format(best_str, curr_str, neigh_str, temp_str))

def main():
	i = 0
	print("['x', 'temperatura', 'najbolji susjed', 'najbolji', 'trenutni'],")
	for line in fileinput.input():
		m = my_regex.match(line)
		if m is None:
			continue
		t = float(m.group('temp'))*30
		n = m.group('neigh')
		b = m.group('best')
		c = m.group('curr')
		i += 1
		print("[{}, {}, {}, {}, {}],".format(i, t, n, b, c), sep=';')

if __name__ == '__main__':
	main()