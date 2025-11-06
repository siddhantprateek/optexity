import asyncio
import logging

from playwright.async_api import Locator, Page

from optexity.inference.api.core.run_interaction import run_interaction_action
from optexity.inference.api.infra.browser import Browser
from optexity.schema.actions.interaction_action import InteractionAction
from optexity.schema.automation import Automation
from optexity.schema.memory import BrowserState, Memory

logger = logging.getLogger(__name__)


async def run_automation(automation: Automation, memory: Memory, browser: Browser):

    automation = expand_automation(automation)
    automation = fill_input_variables(automation, memory)

    for i, node in enumerate(automation.nodes):
        memory.automation_state.step_index = i
        memory.automation_state.try_index = 0
        memory.browser_states.append(BrowserState(url=browser.page.url))
        logger.debug(
            f"--------------------------------Running node {i}--------------------------------"
        )
        try:
            if node.interaction_action:
                await run_interaction_action(node.interaction_action, memory, browser)
            # elif node.assertion_action:
            #     await browser.run_assertion_action(node.assertion_action)
            # elif node.extraction_action:
            #     await browser.run_extraction_action(node.extraction_action)
            # elif node.python_script_action:
            #     await browser.run_python_script_action(node.python_script_action)
        except Exception as e:
            logger.error(f"Error running node {i}: {e}")
            raise e

        await asyncio.sleep(1)
        logger.debug(
            f"--------------------------------Finished node {i}--------------------------------"
        )


def expand_automation(automation: Automation) -> Automation:
    return automation


def fill_input_variables(automation: Automation, memory: Memory) -> Automation:
    return automation
