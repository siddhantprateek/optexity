import logging
from datetime import timedelta
from urllib.parse import urljoin

import httpx

from optexity.inference.infra.browser import Browser
from optexity.schema.actions.two_factor_auth_action import (
    EmailTwoFactorAuthAction,
    SlackTwoFactorAuthAction,
    TwoFactorAuthAction,
)
from optexity.schema.inference import (
    FetchOTPFromEmailRequest,
    FetchOTPFromEmailResponse,
)
from optexity.schema.memory import Memory
from optexity.utils.settings import settings

logger = logging.getLogger(__name__)


async def run_two_factor_auth_action(
    two_factor_auth_action: TwoFactorAuthAction, memory: Memory, browser: Browser
):
    logger.debug(
        f"---------Running 2fa action {two_factor_auth_action.model_dump_json()}---------"
    )

    if isinstance(two_factor_auth_action.action, EmailTwoFactorAuthAction):
        code = await handle_email_two_factor_auth(
            two_factor_auth_action.action, memory, browser
        )
    elif isinstance(two_factor_auth_action.action, SlackTwoFactorAuthAction):
        code = await handle_slack_two_factor_auth(
            two_factor_auth_action.action, memory, browser
        )

    memory.automation_state.start_2fa_time = None
    if code is None:
        raise ValueError("No 2FA code found")

    memory.variables.generated_variables[
        two_factor_auth_action.output_variable_name
    ] = code

    return code


async def handle_email_two_factor_auth(
    email_two_factor_auth_action: EmailTwoFactorAuthAction,
    memory: Memory,
    browser: Browser,
):
    async with httpx.AsyncClient() as client:
        url = urljoin(settings.SERVER_URL, settings.FETCH_OTP_FROM_EMAIL_ENDPOINT)

        body = FetchOTPFromEmailRequest(
            integration_id=email_two_factor_auth_action.integration_id,
            email_address=email_two_factor_auth_action.email_address,
            start_2fa_time=memory.automation_state.start_2fa_time,
            end_2fa_time=memory.automation_state.start_2fa_time
            + timedelta(seconds=email_two_factor_auth_action.max_wait_time),
            email_provider=email_two_factor_auth_action.email_provider,
        )
        response = await client.post(url, json=body.model_dump())
        response.raise_for_status()
        response_data = FetchOTPFromEmailResponse.model_validate_json(response.json())

        logger.debug(f"OTP: {response_data.otp}")
        logger.debug(f"Message ID: {response_data.message_id}")
        logger.debug(f"Message Text: {response_data.message_text}")

        return response_data.otp


async def handle_slack_two_factor_auth(
    slack_two_factor_auth_action: SlackTwoFactorAuthAction,
    memory: Memory,
    browser: Browser,
):
    raise NotImplementedError("Slack 2FA is not implemented")
