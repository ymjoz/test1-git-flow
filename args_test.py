

def pos_only_arg(arg1, /):
    print(arg1)
    
def kwd_only_arg(*, arg1):
    print(arg1)
    
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


pos_only_arg(199)
kwd_only_arg(arg1=234)