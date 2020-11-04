from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.

def todoView(request):
    all_items_todo =TodoItem.objects.all()
    return render(request,'todo.html', {'items': all_items_todo})

def addTodo(request):  # httprequest sent by form to dis page.
    #create a newtodo items.
   # save
  # redirect browser to full list.

    #c=request.POST['content'] #name=content given in form corresponds to database attribute.
    #new_item= TodoItem.objects.create(content=c) #content is attribute of model.
  # the above two lines can be written as :

    new_item= TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


def deleteTodo(request,todo_id):
    delete_item=TodoItem.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect('/todo/')

 #the deletetodo() get todo_id from urls.py and retrieves the record with that id with get()
 # den it deletes n redirects the user to first page.