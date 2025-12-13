from optexity.schema.actions.interaction_action import (
    DownloadUrlAsPdfAction,
    GoToUrlAction,
    InteractionAction,
)
from optexity.schema.automation import ActionNode, Automation, Parameters

description = "Download PDF URL Example"
endpoint_name = "download_pdf_url"
automation = Automation(
    url="about:blank",
    parameters=Parameters(
        input_parameters={
            "pdf_url": ["https://s24.q4cdn.com/216390268/files/doc_downloads/test.pdf"],
        },
        generated_parameters={},
    ),
    nodes=[
        ActionNode(
            type="action_node",
            interaction_action=InteractionAction(
                go_to_url=GoToUrlAction(
                    url="{pdf_url[0]}",
                ),
            ),
        ),
        ActionNode(
            type="action_node",
            interaction_action=InteractionAction(
                download_url_as_pdf=DownloadUrlAsPdfAction(
                    download_filename="example.pdf",
                ),
            ),
        ),
    ],
)
