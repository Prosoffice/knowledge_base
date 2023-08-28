from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import httpx

from app.core.utils import logger

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="token")


async def auth_service(token: str = Depends(reusable_oauth2)):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://127.0.0.1:8001/validate_token/{token}")
            user = response.json()
            logger.info(f"{user['first_name']} is requesting access to KMS...")
            return user
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
