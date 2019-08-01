from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django import forms
from hostels.forms import SignUpForm
from hostels.forms import HostelProfileForm
from hostels.models import HostelProfile, HostelImage
from django.forms import modelformset_factory
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required


def home(request):
	return render(request, 'index.html')



def signup(request):

    registered = False

    user_form = SignUpForm()
    profile_form = HostelProfileForm()
    ImageFormset = modelformset_factory(HostelImage, fields=('image',), extra=6)
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = HostelProfileForm(request.POST)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        

        if user_form.is_valid() and profile_form.is_valid() and formset.is_valid():
            

            user = user_form.save()
            #user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            for f in formset:
            	try:
            		photo = HostelImage(hostel=profile, image=f.cleaned_data['image'])
            		photo.save()
            	except Exception as e:
            		break

            
            registered = True
        else:
        	#messages.error(request, _('Please correct the error below.'))
        	print(user_form.errors, profile_form.errors)
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            # return redirect('home')
    else:
        user_form = SignUpForm()
        profile_form = HostelProfileForm()
        formset = ImageFormset(queryset=HostelImage.objects.none())
  

    return render(request, 'auth/signup.html',  
    	                        {'user_form' : user_form,
    	                         'profile_form': profile_form,
    	                         'registered' : registered,
    	                         'formset':formset})
    	                                                




def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('my_profile'))
        else:
            return HttpResponse("invalid login details")
    else:
        return render(request, 'auth/login.html', {})



@login_required(login_url="/login/")
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


#profile view
class MyProfile(DetailView):
    template_name = 'auth/profile.html'

    def get_object(self):
        return self.request.user.profile











































# def user_login(request):
#     context = RequestContext(request)
#     if request.method == 'POST':
#           username = request.POST['username']
#           password = request.POST['password']
#           user = authenticate(username=username, password=password)
#           if user:
#               if user.is_active:
#                   login(request, user)
#                   # Redirect to index page.
#                   return HttpResponseRedirect('home')
#               else:
#                   # Return a 'disabled account' error message
#                   return HttpResponse("You're account is disabled.")
#           else:
#               # Return an 'invalid login' error message.
#               print("invalid login details")
#               return render_to_response('auth/login.html', {}, context)
#     else:
#         # the login is a  GET request, so just show the user the login form.
#         return render_to_response('auth/login.html', {}, context)