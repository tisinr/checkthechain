from .. import rpc_constructors
from .. import rpc_digestors
from .. import rpc_request


async def async_eth_call(
    to_address,
    from_address=None,
    gas=None,
    gas_price=None,
    value_sent=None,
    block_number=None,
    call_data=None,
    function_parameters=None,
    provider=None,
    decode_response=True,
    delist_single_outputs=True,
    package_named_outputs=False,
    **function_abi_query
):
    request = rpc_constructors.construct_eth_call(
        to_address=to_address,
        from_address=from_address,
        gas=gas,
        gas_price=gas_price,
        value_sent=value_sent,
        block_number=block_number,
        call_data=call_data,
        function_parameters=function_parameters,
        **function_abi_query
    )
    response = await rpc_request.async_send(request, provider=provider)
    return rpc_digestors.digest_eth_call(
        response,
        to_address=to_address,
        function_abi_query=function_abi_query,
        decode_response=decode_response,
        delist_single_outputs=delist_single_outputs,
        package_named_outputs=package_named_outputs,
    )


async def async_eth_estimate_gas(
    to_address,
    from_address=None,
    gas=None,
    gas_price=None,
    value_sent=None,
    call_data=None,
    function_parameters=None,
    provider=None,
    decode_response=True,
    **function_abi_query
):
    request = rpc_constructors.construct_eth_estimate_gas(
        to_address=to_address,
        from_address=from_address,
        gas=gas,
        gas_price=gas_price,
        value_sent=value_sent,
        call_data=call_data,
        function_parameters=function_parameters,
        **function_abi_query
    )
    response = await rpc_request.async_send(request, provider=provider)
    return rpc_digestors.digest_eth_estimate_gas(
        response,
        decode_response=decode_response,
    )


async def async_eth_get_balance(
    address,
    block_number='latest',
    provider=None,
    decode_response=True,
):
    request = rpc_constructors.construct_eth_get_balance(
        address=address,
        block_number=block_number,
    )
    response = await rpc_request.async_send(request, provider=provider)
    return rpc_digestors.digest_eth_get_balance(
        response,
        decode_response=decode_response,
    )


async def async_eth_get_storage_at(
    address,
    position,
    block_number='latest',
    provider=None,
):
    request = rpc_constructors.construct_eth_get_storage_at(
        address=address,
        position=position,
        block_number=block_number,
    )
    response = await rpc_request.async_send(request, provider=provider)
    return rpc_digestors.digest_eth_get_storage_at(response)


async def async_eth_get_code(address, block_number=None, provider=None):
    request = rpc_constructors.construct_eth_get_code(
        address=address,
        block_number=block_number,
    )
    response = await rpc_request.async_send(request, provider=provider)
    return rpc_digestors.digest_eth_get_code(response)
