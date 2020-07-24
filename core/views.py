from django.utils import timezone
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Picture, Submit
from .forms import SubmitForm
from .service import get_submit_streak


# Create your views here.
class IndexView(LoginRequiredMixin, FormView):
    template_name = 'index.html'
    form_class = SubmitForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        day, is_submitted = get_submit_streak(self.request.user)

        context['day'] = day
        context['is_submitted'] = is_submitted

        return context

    def form_valid(self, form):
        submit = Submit(user=self.request.user)
        submit.date = timezone.now()
        submit.save()

        pic1 = Picture(submit_id=submit.id, title=form.fields['main_pic'].label,
                       picture=form.cleaned_data['main_pic']).save()
        pic2 = Picture(submit_id=submit.id, title=form.fields['new_technique_pic'].label,
                       picture=form.cleaned_data['new_technique_pic']).save()
        pic3 = Picture(submit_id=submit.id, title=form.fields['sketch_pic'].label,
                       picture=form.cleaned_data['sketch_pic']).save()

        return redirect('index')
