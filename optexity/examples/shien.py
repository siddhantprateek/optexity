from optexity.schema.actions.interaction_action import (
    CloseOverlayPopupAction,
    InteractionAction,
)
from optexity.schema.automation import ActionNode, Automation, Parameters

shien_test = Automation(
    url="https://www.auquan.com/",
    parameters=Parameters(
        input_parameters={},
        generated_parameters={},
    ),
    nodes=[
        ActionNode(
            before_sleep_time=5,
            interaction_action=InteractionAction(
                close_overlay_popup=CloseOverlayPopupAction(),
            ),
        ),
    ],
)
