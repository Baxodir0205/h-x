from django.shortcuts import render
from .models import Correct, Incorrect


def index_view(request):
    correct = None
    incorrects = None
    message = None

    query = request.GET.get('q', None)
    if query:
        query = query.lower()

        corrects = Correct.objects.filter(word__icontains=query)
        if corrects.exists():
            correct = corrects.first()
            incorrects = correct.incorrect_set.all()
        else:
            incorrects_qs = Incorrect.objects.filter(word__icontains=query)
            if incorrects_qs.exists():
                incorrect = incorrects_qs.first()
                correct = incorrect.correct
                incorrects = correct.incorrect_set.all()
            else:
                if 'x' not in query and 'h' not in query:
                    message = "So'z tarkibida 'x' yoki 'h' mavjud emas!"
                else:
                    message = "Bu so'z lug'atda mavjud emas!"

    context = {
        'correct': correct,
        'incorrects': incorrects,
        'message': message,
        'query': query,
    }
    return render(request, 'index.html', context)