from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
from django.http import Http404

# Create your views here.
def home(request):
    # return HttpResponse("hellp world")
    boards = Board.objects.all()
    # print(boards)
    return render(request,'home.html',{'boards': boards})

    # board_name = list()
    #
    # for board in boards:
    #     board_name.append(board.name)
    #
    # response_html = '<br>'.join(board_name)
    # return HttpResponse(response_html)

def board_topics(request,pk):
    try:
        board = Board.objects.get(pk = pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request,'topics.html',{'board':board})