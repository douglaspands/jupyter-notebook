""" Interface do client do GraphQL
"""
from typing import Optional, List, Dict, Any
from typing_extensions import TypedDict


class IGraphQLResponse(TypedDict, total=False):
    """GraphQL Response
    """
    data: Optional[Dict[str, Any]]
    errors: Optional[List[Dict[str, Any]]]
