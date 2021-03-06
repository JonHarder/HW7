import pycosat as psat
import copy

# You should call this function instead of psat.solve, since the whole point of
# this assignment is to reconstruct the solve method
def satdecide(formula):
	if psat.solve(formula) == 'UNSAT':
		return False

	return True


# TODO: given a formula (list of lists) return a list of all of the var indices
# so findvars([[-1,2],[3,-2]]) should return [1,2,3]
# you might want to use the set datastructure and you might also want to use abs
# for absolute value.
def findvars(formula):
	thevars = set([])
	for l in formula:
		for item in l:
			thevars.add(abs(item))

	return list(thevars)

# TODO: given a formula as list of lists, return a list with a satisfying
# assignment. The output should match what psat.solve returns if there is only
# one satisfying assignment, but might differ if there are multiple different
# ways to satisfy the formula 
def findsatisfying(formula):
	if not satdecide(formula):
		return 'UNSAT'

	ans = []
	variables = findvars(formula)
	form = copy.deepcopy(formula)
	for var in variables:
		f = setvartrue(form, var)
		if f == 'UNSAT':
			f = setvartrue(form, -var)
			if f == 'UNSAT':
				return 'UNSAT'
			else:
				ans.append(-var)
				form = f
		else:
			ans.append(var)
			form = f

	return ans
 
# TODO: given we want x (which could be something like 2 or the negation -2) 
# to be true in formula, modify the formula accordingly  and return the new
# formula that results.  It is useful to note that [[][1]] can never be satisfied
# because we are ANDing an empty clause: no setting of variables can make []
# true.  This property will help a lot in this function, since you might end up 
# removing elements from lists at some point... 
def setvartrue(formula, x):
	f = copy.deepcopy(formula)
	for l in f:
		for item in l:
			if item == -x:
				l.remove(item)

		if len(l) == 0:
			return 'UNSAT'

	return f
