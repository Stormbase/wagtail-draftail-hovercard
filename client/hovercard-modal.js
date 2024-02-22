/*

This file is based on internal Wagtail code and is not part of the public API.

The purpose of this code is to register a custom Draftail source that opens a modal.

The modal HTML is loaded from the server (which is why we need to register an admin url and retrieve it here).

Wagtail's ModalWorkflowSource will handle requesting the modal HTML. We only need to give it the URL and some event handlers.

*/

function getConfig() {
  const element = document.getElementById(
    "wagtail-draftail-hovercard-settings"
  );

  try {
    return JSON.parse(element.textContent);
  } catch (e) {
    console.error("Failed to parse wagtail-draftail-hovercard settings", e);
    return {};
  }
}

// These are event handlers for a lower-level Chooser API that the ModalWorkflowSource uses.
const ONLOAD_HANDLER = {
  // "choose" refers to the step name returned from the server-side view.
  // Here we define what should happen when we get this response from the server.
  choose(modal, jsonData) {
    // This is called when the modal is opened, we need to bind event handlers for the form inside the modal HTML response.
    // We let the `ajaxifyForm` internal Wagtail API do that for us. It expects to get a jQuery selector (modal.body is a jQuery selector; `.find` gives us another jQuery selector).
    // It will make sure that the form inside the modal is submitted via AJAX, and that the response is handled correctly.
    modal.ajaxifyForm(modal.body.find("form"));
  },
  // "chosen" refers to the step name returned from the server-side view.
  // Here we define what should happen when we get this response from the server.
  chosen(modal, jsonData) {
    // A selection has been made through the chooser, now we need to tell the modal and the editor about it.
    // This instance of "chosen" refers to a response the modal will handle
    modal.respond("chosen", jsonData.result);
    modal.close();
  },
};

class HovercardModalWorkflowSource extends window.draftail.ModalWorkflowSource {
  getChooserConfig(entity, selectedText) {
    const config = getConfig();
    const url = config.hovercardModalUrl;
    const urlParams = {
      selectedText: selectedText,
      heading: entity && entity.data.heading || "",
      text: entity && entity.data.text || "",
    };

    return {
      url,
      urlParams,
      onload: ONLOAD_HANDLER,
      responses: {
        // Bind the chosen response to a function provided by ModalWorkflowSource
        // The implementation handles updating the Draftail editor.
        chosen: this.onChosen,
      },
    };
  }

  filterEntityData(data) {
    return {
      heading: data.heading,
      text: data.text,
    };
  }

  render() {
    return null;
  }
}

export default HovercardModalWorkflowSource;
