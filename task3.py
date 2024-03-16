def not_intersections(lines):
	lines.sort(key=lambda x: x[0])
	intersections = set()
	num = len(lines)

	for _ in range(num):
		line = lines.pop(0)
		if line not in intersections:
			for sub_line in lines:
				start_dif = line[0] - sub_line[0]
				end_dif = line[1] - sub_line[1]

				if end_dif > 0 or start_dif == 0 or end_dif == 0:
					intersections.add(line)
					intersections.add(sub_line)

	print(num - len(intersections))


n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

not_intersections(lines)
