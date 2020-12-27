from django.shortcuts import render
from .models import wordItem
from django.http import HttpResponseRedirect
import operator

def task1View(request):
    return render(request, 'Task_1.html')

def task2View(request):
    return render(request, 'Task_2.html')

def wordcountView(request):
    all_word_contents = wordItem.objects.all()
    return render(request, 'count.html',
    {'all_contents':all_word_contents})

def count(request):
    content =request.POST['content']
    wwe = content.split(" ")

    words = {}
    for word in wwe:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
    words = dict(words)
    return render(request, 'results_1.html', {
    'content':content,
    'count':len(wwe),
    'word_dict':words,
    })
