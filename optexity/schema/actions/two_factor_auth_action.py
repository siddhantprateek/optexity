from typing import Literal

from pydantic import BaseModel


class Base2FaAction(BaseModel):
    max_wait_time: float = 300.0
    integration_id: str


class EmailTwoFactorAuthAction(Base2FaAction):
    type: Literal["email_two_factor_auth"] = "email_two_factor_auth"
    email_address: str
    email_provider: Literal["gmail", "outlook"]


class SlackTwoFactorAuthAction(Base2FaAction):
    type: Literal["slack_two_factor_auth"] = "slack_two_factor_auth"
    channel_id: str


class TwoFactorAuthAction(BaseModel):
    action: [EmailTwoFactorAuthAction, SlackTwoFactorAuthAction]
    output_variable_name: str
