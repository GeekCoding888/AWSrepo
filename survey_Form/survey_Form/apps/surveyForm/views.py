from django.shortcuts import render

# Create your views here.
def index(request):
    print '*'*50
    request.session
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        user ={
            'name' : request.session['name'],
            'location': request.session['location'],
            'language' : request.session['language'],
            'comment'  : request.session['comment']
        }
        return render(request, 'surveyForm/user.html', user)
    else:
        return render(request, 'surveyForm/index.html')
