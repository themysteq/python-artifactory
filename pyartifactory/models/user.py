"""
Definition of all user related models.
"""

from datetime import datetime
from typing import List, Optional, Literal, Union
from pathlib import Path
from pydantic import BaseModel, EmailStr, SecretStr


class SimpleUser(BaseModel):
    """
    Models a simple user.
    https://jfrog.com/help/r/jfrog-rest-apis/get-user-list
    """

    name: str
    uri: Union[Path, str]
    status: Literal["invited", "enabled", "disabled", "locked"]
    realm: Optional[str] = None


class BaseUserModel(BaseModel):
    """
    Models a base user.
    https://www.jfrog.com/confluence/display/JFROG/Security+Configuration+JSON#SecurityConfigurationJSON-application/vnd.org.jfrog.artifactory.security.User+json
    """

    name: str
    admin: Optional[bool] = False
    profileUpdatable: Optional[bool] = True
    disableUIAccess: Optional[bool] = False
    internalPasswordDisabled: Optional[bool] = False
    groups: Optional[List[str]] = None


class NewUser(BaseUserModel):
    """Models a new user."""

    email: EmailStr
    password: SecretStr


class User(BaseUserModel):
    """Models a user."""

    email: Optional[EmailStr] = None


class UserResponse(BaseUserModel):
    """Models a user response."""

    email: EmailStr
    lastLoggedIn: Optional[datetime] = None
    realm: Optional[str] = None
    offlineMode: bool = False
