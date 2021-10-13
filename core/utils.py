from fastapi.requests import Request


def get_db(request: Request):
    """Get db session"""
    return request.state.db
