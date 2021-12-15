'''
Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses
balanced_parens(0) => [""]
balanced_parens(1) => ["()"]
balanced_parens(2) => ["()()","(())"]
balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
'''
def balanced_parens(n):
    alist = []
    if n == 0:
        return [""]
    if n == 1:
        return ["()"]
    for s in balanced_parens(n - 1):
        alist += [s[:i] + "()" + s[i:] for i in range(0,len(s))]
    return list(set(alist))
print(balanced_parens(4))