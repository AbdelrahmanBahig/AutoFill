huge_list = []
with open("data.txt", encoding="utf8") as temp:
    for line in temp:
        line = line.lower()
        line = line.replace(',', ' ')
        line = line.replace('/', ' ')
        line = line.replace('(', ' ')
        line = line.replace(')', ' ')
        line = line.replace('.', ' ')
        line = line.replace(';', ' ')
        line = line.replace(';', ' ')
        line = line.replace('"', ' ')
        line = line.replace('[', ' ')
        line = line.replace(']', ' ')
        line = line.replace('-', ' ')
        line = line.replace('#', ' ')
        line = line.replace('``', ' ')
        line = line.replace(':', ' ')
        line = line.replace('،', ' ')
        line = line.replace('$', ' ')
        line = line.replace('%', ' ')
        line = line.replace('!', ' ')
        line = line.replace('?', ' ')
        huge_list.extend(line.split())

## unigram
unigram = {}

for w in huge_list:
    if w not in unigram:
        unigram[w] = 1
    else:
        unigram[w] += 1


##bigram


bigram = {}
for n in range(len(huge_list) - 1):
    if huge_list[n] + ' ' + huge_list[n + 1] not in bigram:
        bigram[huge_list[n] + ' ' + huge_list[n + 1]] = 1
    else:
        bigram[huge_list[n] + ' ' + huge_list[n + 1]] += 1

##trigram


trigram = {}
for n in range(len(huge_list) - 2):
    if huge_list[n] + ' ' + huge_list[n + 1] + ' ' + huge_list[n + 2] not in bigram:
        trigram[huge_list[n] + ' ' + huge_list[n + 1] + ' ' + huge_list[n + 2]] = 1
    else:
        trigram[huge_list[n] + ' ' + huge_list[n + 1] + ' ' + huge_list[n + 2]] += 1


### Predict Bigram
def predict_big(word):
    predicted = {}
    found = unigram[word]
    for n in bigram:
        arr = n.split()
        if arr[0] == word:
            if arr[1] not in predicted:
                predicted.update({arr[1]: bigram[n] / found})
    predictedSorted = dict(sorted(predicted.items(), key=lambda item: item[1]))
    out = ('\n'.join(list(reversed(list(predictedSorted)))[0:5]))
    return out


### Predict Trigram
def predict_tri(word):
    predicted = {}
    found = bigram[word]
    for n in trigram:
        arr = n.split(" ")
        if arr[0] + ' ' + arr[1] == word:
            if arr[2] not in predicted:
                predicted.update({arr[2]: trigram[n] / found})
    predictedSorted = dict(sorted(predicted.items(), key=lambda item: item[1]))
    out = ('\n'.join(list(reversed(list(predictedSorted)))[0:5]))
    return out

### predict for any word
def predict(word):
    if word == '':
        return ""
    if len(word.split(' ')) == 1:
        return predict_big(word)
    elif len(word.split(' ')) > 1:
        return predict_tri(word.split()[len(word.split(" ")) - 2] + " " + word.split()[len(word.split(" ")) - 1])



from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('500x500')

lbl = Label(window, text="")
lbl.grid(column=2, row=2)

def clicked():
    input = txt.get()
    result =predict(input)
    lbl.configure(text=result)

btn = Button(window, text="Predict", command=clicked ,font=("Arial Bold",15))
btn.grid(column=5, row=0)

txt = Entry(window, width=20)
txt.grid(column=2, row=0)

lbl1 = Label(window, text="Autofil:" ,font=("Arial Bold", 15))
lbl1.grid(column=1, row=0)

window.mainloop()
