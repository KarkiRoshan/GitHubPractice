#word counter
def counter(word):
    count={}
    for i in word:
        number= word.count(i)
        count[i]=number
    return count
print(counter('Aakansha'))