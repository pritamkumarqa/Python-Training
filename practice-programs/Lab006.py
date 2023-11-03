words = ['apple','banana','mango','cherry','hritvi','pritam','lemon','abcdefghtuiss']
def check_length(word):
    return len(word) >=6

result = list(filter(check_length,words))
print(result)