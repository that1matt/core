import aiohttp
import asyncio
import re

class NeurioData:
    async def get_local_current_sample(ip_address: str):
        """Gets current sample from *local* Neurio device IP address.

        This is a static method. It doesn't require a token to authenticate.

        Note, call get_user_information to determine local Neurio IP addresses.

        Args:
        ip_address (string): the IP address to your Generac PWRView

        Returns:
        dictionary object containing current sample information
        """
        
        valid_ip_pattern = re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")

        if ip_address is None:
            raise ValueError("An IP Address is required to connect to the local sensor.")

        if not valid_ip_pattern.match(ip_address):
            raise ValueError("ip address invalid")

        url = "http://%s/current-sample" % (ip_address)
        headers = { "Content-Type": "application/json" }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                return await resp.json()