from pydantic import BaseModel, Field, model_validator

from optexity.schema.automation import SecureParameter


class InferenceRequest(BaseModel):
    endpoint_name: str
    input_parameters: dict[str, list[str | int | float | bool]]
    unique_parameter_names: list[str] = Field(default_factory=list)
    secure_parameters: dict[str, list[SecureParameter]] = Field(default_factory=dict)
    use_proxy: bool = False

    @model_validator(mode="after")
    def validate_unique_parameter_names(self):
        for unique_parameter_name in self.unique_parameter_names:
            if unique_parameter_name not in self.input_parameters and (
                self.secure_parameters is None
                or unique_parameter_name not in self.secure_parameters
            ):
                raise ValueError(
                    f"unique_parameter_name {unique_parameter_name} not found in input_parameters or secure_parameters"
                )
        return self
