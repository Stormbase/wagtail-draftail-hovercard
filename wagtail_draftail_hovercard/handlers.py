from draftjs_exporter.dom import DOM
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineEntityElementHandler,
)



HOVERCARD_TYPE_IDENTIFIER = "hovercard"


def hovercard_entity_decorator(props):
    """
    Draft.js ContentState to database HTML.
    Converts HOVERCARD entities into a span tag, which will then
    be further altered by a custom EntityHandler.
    """
    return DOM.create_element(
        "span",
        {
            "data-heading": props.get("heading"),
            "data-text": props.get("text"),
            "data-type": HOVERCARD_TYPE_IDENTIFIER,
        },
        props["children"],
    )



class HovercardEntityElementHandler(InlineEntityElementHandler):
    """
    Database HTML to Draft.js ContentState.
    Converts the span tag into a hovercard entity, with the right data.
    """

    mutability = "IMMUTABLE"

    def get_attribute_data(self, attrs):
        return {
            "heading": attrs.get("data-heading"),
            "text": attrs.get("data-text"),
        }
