from pydantic import BaseModel, EmailStr
from typing import List, Optional
from uuid import UUID

class Recommendation(BaseModel):
    userId: UUID
    email: EmailStr
    usertype: Optional[str] = None
    qualification: Optional[str] = None
    currentWorkingStatus: Optional[str] = None
    occupation: Optional[str] = None
    income: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    displayName: Optional[str] = None
    maritalStatus: Optional[str] = None
    numberOfChildren: Optional[str] = None
    aboutYourSelf: Optional[str] = None
    caste: Optional[str] = None
    community: Optional[str] = None
    subCommunity: Optional[str] = None
    religion: Optional[str] = None
    motherTongue: Optional[str] = None
    gotra: Optional[str] = None
    height: Optional[str] = None
    bodyType: Optional[str] = None
    weight: Optional[str] = None
    language: Optional[str] = None
    smokingHabit: Optional[str] = None
    drinkingHabit: Optional[str] = None 
    diet: Optional[str] = None
    complexion: Optional[str] = None
    fatherOccupation: Optional[str] = None
    motherOccupation: Optional[str] = None
    numberOfSiblings: Optional[str] = None
    livingWithFamily: Optional[str] = None
    citizenship: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    australianVisaStatus: Optional[str] = None
    currentLocation: Optional[str] = None
    cityOfResidence: Optional[str] = None
    nationality: Optional[str] = None
    residencyVisaStatus: Optional[str] = None
    gender: Optional[str] = None
    lookingFor: Optional[str] = None
    weddingGoals: Optional[str] = None
    age: Optional[str] = None
    lookingPartnerAge: Optional[str] = None
    livingInAustralia: Optional[str] = None
    horoscopeMatch: Optional[str] = None
    casteReligionMatterOrNot: Optional[str] = None  # Corrected typo from "castReligionMatterOrNot"
    interest_and_hobbies: List[str]
    image :List[str]


class RecommendationCreate(Recommendation):
    # Define any additional fields or validation for creation if needed
    pass

class RecommendationOut(Recommendation):
    id: int  # Include the ID field for responses

    class Config:
        orm_mode = True  # This allows Pydantic to work with SQLAlchemy models
