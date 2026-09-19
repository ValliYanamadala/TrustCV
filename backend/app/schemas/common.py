from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(default="ok", description="Operational status of TrustCV backend")
    service: str = Field(default="TrustCV", description="Service name")
    version: str = Field(default="0.1.0", description="API version")
    message: str = Field(
        default="TrustCV backend is operational",
        description="Human-readable status message",
    )
