from backend.routes import auth, index

__all__ = ["routers"]

routers = [
    auth.router,
    index.router,
]
