from mcstatus import JavaServer, BedrockServer


def Java(ip: str) -> JavaServer:
    server = JavaServer.lookup(f"{ip}").status()
    return server


def Bedrock(ip: str, port: int = 19132) -> BedrockServer:
    server = BedrockServer.lookup(f"{ip}:{port}").status()
    return server
