from django import forms
from .models import Beat, Genre, Review


class BeatForm(forms.ModelForm):
    """ Form for Beat model that uses all fields """
    class Meta:
        model = Beat
        fields = '__all__'

    file = forms.FileField(
        label='File', required=True)

    image = forms.ImageField(
        label='Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in genres]

        self.fields['genre'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-3'


class ReviewForm(forms.ModelForm):
    """ Form for Review model that uses all fields except complete """
    class Meta:
        model = Review
        fields = ['comment']
