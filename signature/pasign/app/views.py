from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserDataForm
from django.http import JsonResponse
from .models import UserData

# LANDING PAGE
class LandingPageView(View):
    landing_page = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.landing_page)

# LOGIN
class LoginPageView(View):
    login_page = 'login-index.html'

    def get(self, request):
        return render(request, self.login_page)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard_page')  # Replace with the actual URL name for your dashboard page
        else:
            # Authentication failed, provide feedback to the user
            error_message = "Invalid username or password. Please try again."
            return render(request, self.login_page, {'error_message': error_message})
        
# FORGOT PASSWORD
class ForgotPassView(View):
    forgotpassword = 'forgotpass.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.forgotpassword)

# DASHBOARD
class DashboardView(View):
    dashboard_page = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.dashboard_page)
    
# UPLOAD
class UploadView(View):
    upload_data = 'upload.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.upload_data)
    
# REGISTER STUDENT
def register_user(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Clear form fields after successful submission
            form = UserDataForm()
            return render(request, 'upload.html', {'form': form})
    else:
        form = UserDataForm()

    return render(request, 'upload.html', {'form': form})

# TEST
class TestView(View):
    test_data = 'test.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.test_data)

def get_student_data(request, student_id):
    try:
        student = UserData.objects.get(student_id=student_id)
        data = {
            'name': f"{student.first_name} {student.last_name}",
            'email': student.email,
            'signature_type': student.signature_type,
            # Assuming you want to return the URL of the uploaded signature file
            'signature_file_url': student.signature_files.url if student.signature_files else '',
        }
        return JsonResponse(data)
    except UserData.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)

    

    

