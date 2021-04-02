from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    string: str,
) -> Dict[str, Any]:
    url = "{}/metadata/uuid".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "string": string,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[None, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = None

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[None, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    string: str,
) -> Response[Union[None, HTTPValidationError]]:
    kwargs = _get_kwargs(
        client=client,
        string=string,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    string: str,
) -> Optional[Union[None, HTTPValidationError]]:
    """  """

    return sync_detailed(
        client=client,
        string=string,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    string: str,
) -> Response[Union[None, HTTPValidationError]]:
    kwargs = _get_kwargs(
        client=client,
        string=string,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    string: str,
) -> Optional[Union[None, HTTPValidationError]]:
    """  """

    return (
        await asyncio_detailed(
            client=client,
            string=string,
        )
    ).parsed
