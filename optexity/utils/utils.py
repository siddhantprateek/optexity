import re


def replace_variable_name_with_value(
    text: str | None, input_variables: dict[str, list[str]]
) -> str | None:
    if text is None:
        return None
    for key, values in input_variables.items():
        pattern = rf"\{{{re.escape(key)}\[(\d+)\]\}}"
        matches = re.findall(pattern, text)

        if matches:
            matches = [int(match) for match in matches]
            for match in matches:
                if match >= len(values):
                    raise ValueError(
                        f"Input variable {key} has only {len(values)} values. {text} is out of bounds"
                    )

                text = text.replace(f"{{{key}[{match}]}}", values[match])
        return text
