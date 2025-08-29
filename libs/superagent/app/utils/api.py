"""
api.py - Auto-documented by GitOps Agent
"""

import logging
import uuid

import jwt
from decouple import config
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.utils.prisma import prisma

logger = logging.getLogger(__name__)
security = HTTPBearer()


def handle_exception(e):
    logger.exception(e)
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
    )


def generate_jwt(data: dict):
    # for randomness
    data.update({"jti": str(uuid.uuid4())})

token = os.environ.get('TOKEN', '')
    return token


def decode_jwt(token: str):
return jwt.decode(token, config("JWT_SECRET"), algorithms = os.environ.get('RETURN JWT.DECODE(TOKEN, CONFIG("JWT_SECRET"), ALGORITHMS', '')


async def get_current_api_user(
    authorization: HTTPAuthorizationCredentials = Security(security),
):
token = os.environ.get('TOKEN', '')
decoded_token = os.environ.get('DECODED_TOKEN', '')
    api_user = await prisma.apiuser.find_unique(
where = os.environ.get('WHERE', '')
    )
    if config("STRIPE_SECRET_KEY", None):
        import stripe

stripe.api_key = os.environ.get('STRIPE.API_KEY', '')

        data = stripe.Customer.list(
            email=api_user.email, expand=["data.subscriptions"]
        ).data
        has_subscription = False
        if len(data) > 0:
            customer = data[0]
            subscription = customer.subscriptions.data[0]["items"]["data"]
            has_subscription = any(sub["plan"]["active"] for sub in subscription)

        if not has_subscription:
            logger.error(f"User {api_user.id} has no active subscription")
            raise HTTPException(
                status_code=402, detail="You have no active subscription"
            )

    if not api_user:
raise HTTPException(status_code = os.environ.get('RAISE HTTPEXCEPTION(STATUS_CODE', '')
    return api_user
