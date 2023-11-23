import os
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserDataForm
from django.http import JsonResponse
from .models import UserData, get_user_signature_path
from django.contrib import messages
from django.conf import settings

# LANDING PAGE
class LandingPageView(View):
    landing_page = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.landing_page)

# LOGIN
class LoginPageView(View):
    login_page = 'landing/login-index.html'

    def get(self, request):
        return render(request, self.login_page)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  # Check if the checkbox is checked

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if not remember_me:
                # If "Remember Me" is not checked, set session expiry to 0 (browser session)
                request.session.set_expiry(0)

            return redirect('dashboard_page')  # Replace with the actual URL name for your dashboard page
        else:
            # Authentication failed, handle accordingly (e.g., show an error message)
            pass

        return render(request, self.login_page)
        
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
            user_data = form.save()

            # Use the get_user_signature_path function to determine the path
            signature_folder = get_user_signature_path(user_data, '')

            # Create a folder for the specific person using their student_id
            folder_name = f"user_{user_data.student_id}"
            folder_path = os.path.join(settings.MEDIA_ROOT, signature_folder, folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move the uploaded file to the created folder
            original_file_path = os.path.join(settings.MEDIA_ROOT, user_data.signature_files.name)
            signature_file_path = os.path.join(folder_path, os.path.basename(original_file_path))

            os.rename(original_file_path, signature_file_path)
            user_data.signature_files.name = f"{signature_folder}/{folder_name}/{os.path.basename(original_file_path)}"
            user_data.save()

            # Add success message
            messages.success(request, 'Registration successful!')

            return redirect('upload_data')  # Redirect after successful registration

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
            # Assuming you want to return the URL of the uploaded signature file
            'signature_file_url': student.signature_files.url if student.signature_files else '',
        }
        return JsonResponse(data)
    except UserData.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)

    

    

