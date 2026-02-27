from django import forms
from .models import Student
from PIL import Image

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'        
        # widgets = {
        #     # Dates
        #     'application_date': forms.DateInput(attrs={
        #         'class': 'form-control air-datepicker',
        #         'placeholder': 'dd/mm/yyyy',
        #         'data-position': 'bottom right',
        #         'autocomplete': 'off'
        #     }),

        #     'dob': forms.DateInput(attrs={
        #         'class': 'form-control air-datepicker',
        #         'placeholder': 'dd/mm/yyyy',
        #         'data-position': 'bottom right',
        #         'autocomplete': 'off'
        #     }),

        #     # Basic Info
        #     'name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter Student Name'
        #     }),
        #     'student_class': forms.Select(attrs={
        #         'class': 'form-control'
        #     }),
        #     'gender': forms.Select(attrs={
        #         'class': 'form-control'
        #     }),
        #     'religion': forms.Select(attrs={
        #         'class': 'form-control'
        #     }),
        #     'caste': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter Caste'
        #     }),

        #     # Parents Info
        #     'mother_name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Mother Name'
        #     }),
        #     'father_name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Father Name'
        #     }),
        #     'mother_occupation': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Mother Occupation'
        #     }),
        #     'father_occupation': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Father Occupation'
        #     }),

        #     # Contact Info
        #     'contact_number': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter Contact Number'
        #     }),
        #     'permanent_address': forms.Textarea(attrs={
        #         'class': 'form-control',
        #         'rows': 2,
        #         'placeholder': 'Permanent Address'
        #     }),
        #     'local_address': forms.Textarea(attrs={
        #         'class': 'form-control',
        #         'rows': 2,
        #         'placeholder': 'Local Address'
        #     }),
        #     'pin_code': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Pin Code'
        #     }),
        #     'district': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'District'
        #     }),
        #     'nationality': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Nationality'
        #     }),

        #     # Extra Info
        #     'adhaar_number': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Adhaar Number'
        #     }),
        #     'residence_length': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Length of Residence in UP'
        #     }),
        #     'last_institution': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Last Institution Name'
        #     }),

        #     # Photo Upload
        #     'photo': forms.FileInput(attrs={
        #         'class': 'form-control-file'
        #     }),
        # }