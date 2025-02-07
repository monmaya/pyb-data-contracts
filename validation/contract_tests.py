import pytest
from pydantic import BaseModel, validator
from typing import List, Dict, Optional
from datetime import datetime

class CustomerProfile(BaseModel):
    profile_id: str
    email: str
    email_status: str
    address: Dict[str, str]
    preferences: Dict[str, List[str]]
    
    @validator('email_status')
    def validate_email_status(cls, v):
        allowed_statuses = ['verified', 'pending', 'invalid']
        if v not in allowed_statuses:
            raise ValueError(f'Invalid email status: {v}')
        return v
    
    @validator('preferences')
    def validate_preferences(cls, v):
        allowed_channels = ['email', 'sms', 'postal']
        if 'communication' in v:
            for channel in v['communication']:
                if channel not in allowed_channels:
                    raise ValueError(f'Invalid communication channel: {channel}')
        return v

def test_customer_profile_contract():
    # Test valid profile
    valid_profile = {
        'profile_id': '123e4567-e89b-12d3-a456-426614174000',
        'email': 'user@example.com',
        'email_status': 'verified',
        'address': {
            'street': '123 Main St',
            'city': 'Springfield',
            'country': 'US'
        },
        'preferences': {
            'communication': ['email', 'sms']
        }
    }
    
    profile = CustomerProfile(**valid_profile)
    assert profile.email_status == 'verified'
    
    # Test invalid email status
    with pytest.raises(ValueError):
        invalid_profile = valid_profile.copy()
        invalid_profile['email_status'] = 'unknown'
        CustomerProfile(**invalid_profile)
    
    # Test invalid communication channel
    with pytest.raises(ValueError):
        invalid_profile = valid_profile.copy()
        invalid_profile['preferences']['communication'] = ['email', 'invalid']
        CustomerProfile(**invalid_profile)

def test_profile_transitions():
    """Test valid state transitions for email status"""
    valid_transitions = {
        'pending': ['verified', 'invalid'],
        'verified': ['invalid'],
        'invalid': ['pending']
    }
    
    def is_valid_transition(from_status: str, to_status: str) -> bool:
        return to_status in valid_transitions.get(from_status, [])
    
    assert is_valid_transition('pending', 'verified')
    assert is_valid_transition('pending', 'invalid')
    assert not is_valid_transition('verified', 'pending')
    assert is_valid_transition('invalid', 'pending') 