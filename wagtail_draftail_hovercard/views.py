from django.views.generic import View
from wagtail.admin.modal_workflow import render_modal_workflow

from wagtail_draftail_hovercard.forms import HovercardForm

class HovercardModalView(View):
    template_name = "wagtail_draftail_hovercard/modal.html"
    form_class = HovercardForm
    form_prefix = "hovercard"

    def get_initial_data(self):
        return {
            "heading": self.request.GET.get("heading", ""),
            "text": self.request.GET.get("text", ""),
        }

    def get_result_data(self):
        return {
            # Title is hardcoded (in Wagtail ModalWorkflowSource.js) to be used as placeholder when there is no selected text
            # We need it because otherwise the editor will just crash.
            "title": "Hovercard",
            "heading": self.form.cleaned_data["heading"].strip(),
            "text": self.form.cleaned_data["text"].strip(),
        }

    def get(self, request):
        self.form = self.form_class(
            initial=self.get_initial_data(), prefix=self.form_prefix
        )
        return self.render_form_response()

    def post(self, request):
        self.form = self.form_class(
            request.POST, initial=self.get_initial_data(), prefix=self.form_prefix
        )

        if self.form.is_valid():
            result = self.get_result_data()
            return self.render_chosen_response(result)
        else:
            return self.render_form_response()

    def render_form_response(self):
        return render_modal_workflow(
            self.request,
            self.template_name,
            None,
            {
                "form": self.form,
            },
            json_data={"step": "choose"},
        )

    def render_chosen_response(self, result):
        return render_modal_workflow(
            self.request,
            None,
            None,
            None,
            json_data={"step": "chosen", "result": result},
        )
