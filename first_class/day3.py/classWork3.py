fish = ['sardine','tilapia','salmon']

def linearSearch(arg,target):
    for item in target:
        if arg == item:
            return print('yay!!!!!')
        return print('ouch!!!')
    
linearSearch('cow', fish)