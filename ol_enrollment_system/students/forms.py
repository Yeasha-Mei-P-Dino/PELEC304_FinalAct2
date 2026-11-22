from django import forms
from .models import Student


class OneTimeProfilePicForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['profile_pic']
        widgets = {
            'profile_pic': forms.FileInput(attrs={
                'accept': 'image/*',
                'id': 'id_profile_pic',
            })
        }

    def clean_profile_pic(self):
        if self.instance and self.instance.profile_pic:
            raise forms.ValidationError(
                "This profile picture has already been uploaded and cannot be changed."
            )
        pic = self.cleaned_data.get('profile_pic')
        if not pic:
            raise forms.ValidationError("Please select an image file first.")
        return pic


class StudentEnrollmentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['profile_pic', 'profile_pic_uploaded_at', 'date_enrolled']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 2}),
        }