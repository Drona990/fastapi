from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class RecommendationModel(Base):
    __tablename__ = 'Recommendations'

    userId = Column(UUID(as_uuid = True), primary_key = True)
    email = Column(String,nullable = True)
    usertype = Column(String,nullable = True) # user type will be normal, exclusive
    qualification = Column(String,nullable = True)
    currentWorkingStatus = Column(String,nullable = True) # working / not working
    occupation = Column(String,nullable = True) 
    income = Column(String,nullable = True)           #should be in ranges like $100-$200    
    firstName = Column(String,nullable = True)
    lastName = Column(String,nullable = True)
    displayName = Column(String,nullable = True)
    martialalStatus =  Column(String,nullable = True) # Married , unmarried , widdows , nulled , diverce etc
    numberOfChildren =  Column(String,nullable = True)
    aboutYourSelf =  Column(String,nullable = True)
    caste =  Column(String,nullable = True)
    community =  Column(String,nullable = True)
    subCommunity = Column(String,nullable = True)
    religion = Column(String,nullable = True)
    motherTongue = Column(String,nullable = True)
    gotra = Column(String,nullable = True)
    height = Column(String,nullable = True)  # height will be in feet and inches like 5"7
    bodyType = Column(String,nullable = True) # weight in kg
    weight = Column(String,nullable = True)
    language = Column(String,nullable = True)
    smokingHabbit = Column(String,nullable = True)
    drinkingHabbit = Column(String,nullable = True)
    diet = Column(String,nullable = True)
    complexion = Column(String,nullable = True)
    fatherOccupation = Column(String,nullable = True)
    motherOccupation = Column(String,nullable = True)
    numberOfSiblings = Column(String,nullable = True)
    livingWithFamily = Column(String,nullable = True)
    citizenShip = Column(String,nullable = True)
    country = Column(String,nullable = True)
    state = Column(String,nullable = True)
    austrailanVisaStatus = Column(String,nullable = True)
    currentLocation = Column(String,nullable = True)
    cityOfResidence = Column(String,nullable = True)
    nationality = Column(String,nullable = True)
    residencyVisaStatus = Column(String,nullable = True)
    gender = Column(String,nullable = True) # this is own gender
    lookingFor = Column(String,nullable = True) # this also gener of parttner
    weddingGoals = Column(String,nullable = True)
    age = Column(String,nullable = True) # this is own age
    lookingPartnerAge = Column(String,nullable = True) # this is partner age in ranges like 23-30
    livingInAustralia = Column(String,nullable = True)
    horoscopeMatch = Column(String,nullable = True)
    castReligionMatterOrNot = Column(String,nullable = True)
    interest_and_hobbies = Column(String,nullable = True) # this is a list of hobbies and interest
    image = Column(String,nullable = True) # this is a list of images

















    








   