def cal(self, str)
	n = len(str)
	res = 0
	if n == 1:
		res = Ord(str) - Ord('A') + 1
	i = 0
	while i < n:
		res +=  (Ord(str[i]) - Ord('A') + 1)*26**(n - i - 1)
		i += 1