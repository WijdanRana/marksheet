from django import forms

class courses(forms.Form):
    course1=forms.IntegerField(label="Course 1")
    course2=forms.IntegerField(label="Course 2")
    course3=forms.IntegerField(label="Course 3")
    course4=forms.IntegerField(label="Course 4")
    course5=forms.IntegerField(label="Course 5")
