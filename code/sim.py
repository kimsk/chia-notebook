from cdv.test import Network

network: Network = None

async def get_network_async():
    global network
    if network == None:
        network = await Network.create()
        await network.farm_block()
    return network

async def close_network_async():
    global network
    if network != None:
        await network.close()
    network = None
