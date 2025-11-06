import asyncio
import logging
from copy import deepcopy

from optexity.inference.api.core.run_interaction import run_interaction_action
from optexity.inference.api.infra.browser import Browser
from optexity.schema.automation import Automation, BasicNode, ForLoopNode
from optexity.schema.memory import BrowserState, Memory

logger = logging.getLogger(__name__)

# TODO: static check that index for all replacement of input variables are within the bounds of the input variables

# TODO: static check that all for loop expansion for generated variables have some place where generated variables are added to the memory

# TODO: Check that all for loop expansion for generated variables have some place where generated variables are added to the memory

# TODO: give a warning where any variable of type {variable_name[index]} is used but variable_name is not in the memory in generated variables or in input variables


async def run_automation(automation: Automation, memory: Memory, browser: Browser):

    # automation = expand_for_loop_based_on_input_variables(automation, memory)
    automation.replace_input_variables(memory.variables.input_variables)

    for i, node in enumerate(automation.nodes):
        # TODO: Fill generated variables
        # TODO: Expand for loop based on generated variables
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


def expand_for_loop_based_on_input_variables(
    automation: Automation, memory: Memory
) -> Automation:
    new_automation = Automation(
        name=automation.name,
        description=automation.description,
        nodes=[],
    )
    for node in automation.nodes:
        if isinstance(node, ForLoopNode):
            if node.variable_name in memory.variables.input_variables:
                for index, basic_node in enumerate(node.nodes):
                    new_node = deepcopy(basic_node)
                    new_node.replace("[index]", index)
                    new_automation.nodes.append(new_node)

            else:
                new_automation.nodes.append(node)
        else:
            new_automation.nodes.append(node)

    return new_automation
