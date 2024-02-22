from django.urls import reverse, path
from django.utils.html import json_script
from django.utils.safestring import mark_safe

from wagtail import hooks
from wagtail.admin.rich_text.editors.draftail import features as draftail_features
from django.utils.translation import gettext_lazy as _

from wagtail_draftail_hovercard.handlers import (
    hovercard_entity_decorator,
    HovercardEntityElementHandler,
)
from wagtail_draftail_hovercard.views import HovercardModalView


@hooks.register("register_rich_text_features")
def register_hovercard_feature(features):
    """
    Registering the `shortcode` feature, which uses the `SHORTCODE` Draft.js entity type,
    and is stored as a unique anchor `<a linktype="shortcode" shortcode="shortcode-value">` tag (see shortcode_entity_decorator),
    and rendered via a LinkHandler with a matching identifier (the identifier being linktype="shortcode").
    """
    feature_name = "hovercard"
    type_ = "HOVERCARD"

    control = {
        "type": type_,
        "icon": "tag",
        "description": _("Hovercard - let the user hover over text to see more information."),
    }

    features.register_editor_plugin(
        "draftail",
        feature_name,
        draftail_features.EntityFeature(
            control, js=["wagtail_draftail_hovercard/wagtail-draftail-hovercard.js"]
        ),
    )

    features.register_converter_rule(
        "contentstate",
        feature_name,
        {
            "from_database_format": {
                'span[data-type="hovercard"]': HovercardEntityElementHandler(type_)
            },
            "to_database_format": {
                "entity_decorators": {type_: hovercard_entity_decorator}
            },
        },
    )

@hooks.register("insert_global_admin_js")
def register_hovercard_settings_script():
    return mark_safe(
        json_script(
            {
                "hovercardModalUrl": reverse("wagtail_draftail_hovercard_modal"),
            },
            "wagtail-draftail-hovercard-settings",
        )
    )


@hooks.register('register_admin_urls')
def register_hovercard_modal_view():
    return [
        path('wagtail_draftail_hovercard/modal/', HovercardModalView.as_view(), name='wagtail_draftail_hovercard_modal'),
    ]
