from infraestructure.security.jwt_provider import JwtProvider

jwt_provider = JwtProvider()

def login(username: str, password: str) -> str:
    if username == "admin" and password == "1234":
        return jwt_provider.create_access_token({"sub": username})
    raise ValueError("Credenciales inválidas")
