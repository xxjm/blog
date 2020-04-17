from django.shortcuts import render,redirect
from .models import Todo


# Create your views here.



def bianji(request,i_id):
	if request.method == "POST":
		if request.POST['已更改内容']=='':
			return render(request, "todolist/edit.html",{"警告":"请输入内容"})
		else:
			a=Todo.objects.get(id=i_id)
			a.thing=request.POST['已更改内容']
			a.save()
			return redirect("todolist:项目")
	else:
		content = {'更改内容': Todo.objects.get(id=i_id).thing}
		return render(request, "todolist/bianji.html", content)


def edit(request):
	if request.method=="POST":
		if request.POST["待办事项"] == '':
			content = {"清单": Todo.objects.all()}
			return render(request,"todolist/edit.html",{"警告": "请输入内容！"})
		else:
			a_row =Todo(thing=request.POST["待办事项"], done=False)
			a_row.save()
			content = {"清单": Todo.objects.all()}
			return render(request, "todolist/edit.html", content)
	else:
		content = {"清单": Todo.objects.all() }
		return render(request, "todolist/edit.html",content)


def delete(request, i_id):
	a=Todo.objects.get(id=i_id)
	a.delete()
	return redirect("todolist:项目")


def cross(request, i_id):
	if request.POST['完成状态']=="已完成":
		a=Todo.objects.get(id=i_id)
		a.done = True
		a.save()
		return redirect("todolist:项目")
	else:
		a=Todo.objects.get(id=i_id)
		a.done = False
		a.save()
	return redirect("todolist:项目")

