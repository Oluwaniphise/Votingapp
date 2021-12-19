from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib import messages
from .forms import SignUpForm, UpdateProfileForm
from .models import Course, Profile, Choice, Question
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# class GeneralCourseListView(ListView):
#     model = Question
#     template_name = 'vote.html'
#     context_object_name = 'questions'
#     paginate_by = 1




# class GeneralCourseDetailView(DetailView):
#     model = Question
#     template_name = 'details.html'
#     context_object_name = 'q'


# def save_vote(request, pk):
    
#     try:
#         question = Question.objects.get(pk=pk)
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'details.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.vote += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('result', 
#         args=(question.id,
#         )))
#         # return HttpResponse("You have successfully voted")
    
    
def result(request, pk: int):
    question = Question.objects.get(pk=pk)
    context = {
        'question':question
    }
    return render(request, 'result.html', context)
    

def vote(request):
    questions = Question.objects.all()
        
    paginator = Paginator(questions, 1) 
    
    try:
        page_number = request.GET.get('page', 1)

        print('current_page: ', page_number)
        
        page_obj = paginator.get_page(page_number)

        question = page_obj.object_list.get() # object list contains the objects in the page

        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # increment selected choice and save
        selected_choice.vote += 1
        selected_choice.save()

        # since there is only one object per page
        # after submitting a current entry on a page, there is no next object in this page,
        # just go to the next page number which will be checked in the above try except block

        url = f"{reverse('vote')}?page={page_obj.next_page_number()}"

        print('next_url: ', url)
            
        return HttpResponseRedirect(url)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'vote.html', {
            'page_obj': page_obj,
            'error_message': "You didn't select a choice.",
        })
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages) 
           
    context = {
        'questions': questions,
        "page_obj": page_obj
    }
    return render(request, 'vote.html', context)
    
    

    # for q in questions:
    #     choices = []
    #     for a in q.choice_set.all():
    #         choices.append(a.choice_field)
    #     question.append({str(q): choices})
    # return JsonResponse({
    #     'data':question
    #     })

    # for q in question:
    #     a_selected = request.POST.get(q.question_post)
    #     print(a_selected)


 
    




def register(request):
    user = request.user
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.mat_no = form.cleaned_data.get('mat_no')
            user.profile.dept = form.cleaned_data.get('dept')
            # user.profile.level = form.
            user.save()
        
            messages.success(request, 'Your account has been successfully created.')
            return redirect('login')
    else:
        form = SignUpForm()

    context = {
        'form':form, 'user':user
    }

    
    return render(request, 'account/register.html', context)


def login(request):
    # form = SignUpForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'username of password incorrect')
            # print('username or password incorrect')
    context = {
        # 'form':form

    }

    return HttpResponse("HEllo")


# def profile(request):
#     user_profile = Profile.objects.get(user=request.user)
#     if request.method == 'POST':
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=user)
#         if profile_form.is_valid():
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='dashboard')
#     else:
#         profile_form = UpdateProfileForm(instance=user_)
#     context = {
#         'profile_form': profile_form
#     }
#     return render(request, 'dashboard.html', context)



def dashboard(request):
    user_profile = Profile.objects.get(user=request.user)
    course = Course.objects.all()
    # profile = Profile.objects.all()
    context = {
        'user_profile':user_profile, 'course':course
        # 'profile':profile 
    }
    return render(request, 'dashboard.html', context)


