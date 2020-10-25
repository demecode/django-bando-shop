from django.shortcuts import render


def test_vue(request):
    return render(request, 'vue_app/templates/vue_app/test.html')

# Create your views here.
