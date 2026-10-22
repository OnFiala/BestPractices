"""Original local teaching fixture; not production authentication or a server."""

from .service import TOKEN_ALPHA, TOKEN_BETA, FixtureServer

__all__ = ["FixtureServer", "TOKEN_ALPHA", "TOKEN_BETA"]
