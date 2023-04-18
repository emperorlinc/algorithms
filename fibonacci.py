def canSum(n, list, memo={}):
	if n in memo: return memo[n]
	if n == 0: return True
	if n < 0: return False

	for i in list:
		target = n - i
		if canSum(target, list, memo) == True:
			memo[n] = True
			return True
	memo[n] = False
	return False


print(canSum(300, [3, 5]))