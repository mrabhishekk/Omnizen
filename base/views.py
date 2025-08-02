from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from datetime import timedelta
from django.utils.timezone import now


# views contains the logic & algorithms at the backend, the POST requests get received at the backend inside views


def login_page(request):
    return HttpResponse("Welcome to the Login Page")


def logout_page(request):
    pass


def task_list(request):         # tasks grouping & sorting logic
    tasks = Task.objects.all().order_by('due_datetime')

    today_date = now().date()
    tomorrow_date = today_date + timedelta(days=1)
    seventh_day_date = today_date + timedelta(days=7)

    grouped = {
        "Overdue": [],
        "Today": [],
        "Tomorrow": [],
        "Next 7 Days": [],
        "Upcoming": [],
        "Someday": [],
        "Completed": [],
    }

    priority_order = {"high": 1, "medium": 2, "low": 3}

    for task in tasks:

        if task.completed:
            grouped["Completed"].append(task)
            continue                # Skip further grouping for completed tasks

        due_date = task.due_datetime.date() if task.due_datetime else None

        if due_date is None:
            grouped["Someday"].append(task)
        elif due_date < today_date:
            grouped["Overdue"].append(task)
        elif due_date == today_date:
            grouped["Today"].append(task)
        elif due_date == tomorrow_date:
            grouped["Tomorrow"].append(task)
        elif today_date < due_date <= seventh_day_date:
            grouped["Next 7 Days"].append(task)
        else:
            grouped["Upcoming"].append(task)

    # Sort EACH group by priority (high → low)
    for grp_tasks in grouped.values():
        grp_tasks.sort(key=lambda t: priority_order.get(t.priority or 'low', 4))    # assigning lambda value to key

    return render(request, "create_task.html", {"grouped_tasks": grouped})



def create_task(request):               # form & tasks are variables - not executable
                                        # form = TaskForm()           # creating an empty form instance of the TaskForm
                                        # tasks = Task.objects.all()  # fetches all the user or admin created tasks from Task database model table
    if request.method == "POST":
        form = TaskForm(request.POST)       # creating a form instance, but filled with the user's submitted data

        if form.is_valid():
            form.save()         # saves to database - new task created to render

        return redirect("/")

    context = {"tasks" : Task.objects.all(), "form": TaskForm()}    # dictionary

    return render(request, "create_task.html", context)      # tells django to render the HTML file with the data in context
                                                                            #context connects your model + form logic to the template



def update_task(request, pk):
    some_task = Task.objects.get(id=pk)
    form = TaskForm(instance = some_task)   #Creates a TaskForm and pre-fills it with data from some_task.

    # only executed on submit form
    if request.method == "POST":
        form = TaskForm(request.POST, instance = some_task) #Creates a new form with the submitted data & binds it to the existing task

        if form.is_valid():
            form.save()

        return redirect("/")
    

    context = {"form": form}

    template = "update_task.html"

    # normally the only executable code
    return render(request, template, context)



def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    # alternate - task = get_object_or_404(Task, id=pk)

    #not needed form, as we do not need to render it

    if request.method=="POST":
        task.delete()

        return redirect("/")
    

    
    context = {"task": task}

    template = "delete_task.html"

    return render(request, template, context)



def toggle_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "POST":
        # Set to True if checkbox exists, False otherwise
        task.completed = 'completed' in request.POST
        task.save()

    return redirect('/')  # or your home view name


