from .models import Post
from django.forms import ModelForm


class CreatePost(ModelForm):
    class Meta:
        model = Post
        fields = ['message']
        # widgets = {
        #     'body': Textarea(attrs={'cols': 60, 'rows': 20}),
        # }
    
    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(CreatePost, self).__init__(*args, **kwargs)
    
    
    def save(self, commit=True):
        inst = super(CreatePost, self).save(commit=False)
        inst.author = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst