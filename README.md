# Wagtail Draftail Hovercard

[![License: MIT](https://img.shields.io/pypi/l/wagtail-draftail-hovercard)](https://github.com/Stormbase/wagtail-draftail-hovercard/blob/main/LICENSE)
[![Version](https://img.shields.io/pypi/v/wagtail-draftail-hovercard.svg)](https://pypi.python.org/pypi/wagtail-draftail-hovercard/)

A Wagtail plugin that adds a hovercard to Wagtail's Draftail rich text editor. You are responsible for rendering the hovercard in your frontend.

## Requirements

- Wagtail 4.2+

## Installation

1. Install the package

```sh
pip install wagtail-draftail-hovercard
```

2. Add ``wagtail_draftail_hovercard`` to your ``INSTALLED_APPS``

```python
INSTALLED_APPS = [
    # ...
    "wagtail_draftail_hovercard",
    # ...
]
```

3. Add the `hovercard` feature to your `RichTextField` or `RichTextBlock`

```python
class MyModel(models.Model):
    content = RichTextField(features=["hovercard"])
```

That's it! You now have a hovercard feature in your Draftail editor toolbar.

## Rendering the hovercard on the frontend of your site

You are responsible for rendering the hovercard in your frontend. The rich text representation in limited to a `<span>` element with the extra fields added as data attributes. You need to write some JS to look for `span[data-type="hovercard"]` and replace it with your whatever you want to render.

Here's what the HTML rendered by Draftail looks like:

```html
<span data-type="hovercard" data-text="I'm the text inside the hovercard" data-heading="I'm the heading or I can be blank">
    I'm the text that the hovercard is attached to
</span>
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
