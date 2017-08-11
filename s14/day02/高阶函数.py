__author__ = "sun wang"

def add(a,b,f):
    return f(a)+f(b)

res = add(3,-6, abs)
print (res)

git clone https://github.com/gmarik/Vundle.vim.git   ~/.vim/bundle/Vundle.vim