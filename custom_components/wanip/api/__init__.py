"""
API package for wanip.

Architecture:
    Three-layer data flow: Entities → Coordinator → API Client.
    Only the coordinator should call the API client. Entities must never
    import or call the API client directly.

Exception hierarchy:
    WANIPApiClientError (base)
    ├── WANIPApiClientCommunicationError (network/timeout)
    └── WANIPApiClientAuthenticationError (401/403)

Coordinator exception mapping:
    ApiClientAuthenticationError → ConfigEntryAuthFailed (triggers reauth)
    ApiClientCommunicationError → UpdateFailed (auto-retry)
    ApiClientError             → UpdateFailed (auto-retry)
"""

from .client import (
    WANIPApiClient,
    WANIPApiClientAuthenticationError,
    WANIPApiClientCommunicationError,
    WANIPApiClientError,
)

__all__ = [
    "WANIPApiClient",
    "WANIPApiClientAuthenticationError",
    "WANIPApiClientCommunicationError",
    "WANIPApiClientError",
]
