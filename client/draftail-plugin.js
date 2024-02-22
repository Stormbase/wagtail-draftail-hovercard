const { TooltipEntity } = window.draftail;
const { Icon } = window.wagtail.components;

import HovercardWorkflowSource from './hovercard-modal';

// This component is rendered inline and represents the entity in the editor
const HovercardDecorator = (props) => {
  const { entityKey, contentState } = props;
  const data = contentState.getEntity(entityKey).getData();
  const label = data.heading || "Hovercard";

  const icon = window.React.createElement(Icon, { name: "tag" });

  return window.React.createElement(TooltipEntity, {
    icon: icon,
    label: label,
    ...props,
  });
};

window.draftail.registerPlugin(
  {
    type: "HOVERCARD",
    source: HovercardWorkflowSource,
    decorator: HovercardDecorator,
  },
  "entityTypes"
);
