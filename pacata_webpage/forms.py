# from django import forms
# from models import Post

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('title', 'author', 'body', 'image', 'post_type', 'event_date')

#         widget = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'author': forms.Select(attrs={'class': 'form-control'}),
#             'body': forms.Textarea(attrs={'class': 'form-control'}),
#             'image': forms.FileInput(attrs={'class': 'form-control'}),
#             'post_type': forms.RadioSelect(choices=Post.POST_TYPES, attrs={'class': 'form-control'}),
#             'event_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
#         }