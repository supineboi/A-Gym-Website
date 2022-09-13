from django import forms
from myApp.models import Employee

class EmployeeForm(forms.ModelForm):
 class Meta:
  model = Employee

# If don't want to include that column
  # exclude = ['empId']