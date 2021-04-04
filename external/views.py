"""External views."""
from django.views.generic import TemplateView, FormView

from . import forms
from imagetext.GAN import GAN

class ImagetextLandingView(TemplateView):
    """Basic backend view to call frontend from."""

    template_name = "base.html"


class PredictView(FormView):
	"""Get the prediction from the submitted image and return result."""
	template_name = "base.html"
	form_class = forms.Form

	def form_valid(self, form):
		"""Handle valid form POST."""
		image = self.request.data['image']
		prediction = GAN.compute_prediction(image)
		response = super(PredictView, self).form_valid(form)
		return redirect('output', text=prediction)


class OutputView(TemplateView):
	"""Basic view to display results of model."""

	template_name = ""

    def get_context_data(self, **kwargs):
        context = super(OutputView, self).get_context_data(**kwargs)
        context['text'] = self.kwargs.get('text')
        return context
