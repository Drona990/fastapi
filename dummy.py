from sqlalchemy import UUID, create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from faker import Faker
import uuid

# Define the database URL
DATABASE_URL = "postgresql+asyncpg2://postgres:12345678@localhost/wedlock"


# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a base class
Base = declarative_base()

# Define the Recommendation model
class RecommendationModel(Base):
    __tablename__ = 'Recommendations'

    userId = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, nullable=True)
    usertype = Column(String, nullable=True)
    qualification = Column(String, nullable=True)
    currentWorkingStatus = Column(String, nullable=True)
    occupation = Column(String, nullable=True)
    income = Column(String, nullable=True)
    firstName = Column(String, nullable=True)
    lastName = Column(String, nullable=True)
    displayName = Column(String, nullable=True)
    martialalStatus = Column(String, nullable=True)
    numberOfChildren = Column(String, nullable=True)
    aboutYourSelf = Column(String, nullable=True)
    caste = Column(String, nullable=True)
    community = Column(String, nullable=True)
    subCommunity = Column(String, nullable=True)
    religion = Column(String, nullable=True)
    motherTongue = Column(String, nullable=True)
    gotra = Column(String, nullable=True)
    height = Column(String, nullable=True)
    bodyType = Column(String, nullable=True)
    weight = Column(String, nullable=True)
    language = Column(String, nullable=True)
    smokingHabbit = Column(String, nullable=True)
    drinkingHabbit = Column(String, nullable=True)
    diet = Column(String, nullable=True)
    complexion = Column(String, nullable=True)
    fatherOccupation = Column(String, nullable=True)
    motherOccupation = Column(String, nullable=True)
    numberOfSiblings = Column(String, nullable=True)
    livingWithFamily = Column(String, nullable=True)
    citizenShip = Column(String, nullable=True)
    country = Column(String, nullable=True)
    state = Column(String, nullable=True)
    austrailanVisaStatus = Column(String, nullable=True)
    currentLocation = Column(String, nullable=True)
    cityOfResidence = Column(String, nullable=True)
    nationality = Column(String, nullable=True)
    residencyVisaStatus = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    lookingFor = Column(String, nullable=True)
    weddingGoals = Column(String, nullable=True)
    age = Column(String, nullable=True)
    lookingPartnerAge = Column(String, nullable=True)
    livingInAustralia = Column(String, nullable=True)
    horoscopeMatch = Column(String, nullable=True)
    castReligionMatterOrNot = Column(String, nullable=True)
    interest_and_hobbies = Column(String, nullable=True)

# Create all tables
Base.metadata.create_all(engine)

# Set up the session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Use Faker to generate random data
faker = Faker()

def create_dummy_data(session, num_records):
    for _ in range(num_records):
        record = RecommendationModel(
            email=faker.email(),
            usertype=faker.random_element(elements=('normal', 'exclusive')),
            qualification=faker.job(),
            currentWorkingStatus=faker.random_element(elements=('working', 'not working')),
            occupation=faker.job(),
            income=f"${faker.random_int(min=100, max=500)}-${faker.random_int(min=500, max=1000)}",
            firstName=faker.first_name(),
            lastName=faker.last_name(),
            displayName=f"{faker.first_name()} {faker.last_name()}",
            martialalStatus=faker.random_element(elements=('Married', 'Unmarried', 'Widowed', 'Null', 'Divorced')),
            numberOfChildren=faker.random_int(min=0, max=5),
            aboutYourSelf=faker.text(),
            caste=faker.random_element(elements=('General', 'OBC', 'SC', 'ST')),
            community=faker.random_element(elements=('Community1', 'Community2')),
            subCommunity=faker.random_element(elements=('SubCommunity1', 'SubCommunity2')),
            religion=faker.random_element(elements=('Hindu', 'Muslim', 'Christian', 'Sikh')),
            motherTongue=faker.language_name(),
            gotra=faker.word(),
            height=f"{faker.random_int(min=4, max=6)}\"{faker.random_int(min=0, max=11)}",
            bodyType=faker.random_element(elements=('Slim', 'Average', 'Athletic', 'Heavy')),
            weight=f"{faker.random_int(min=50, max=100)} kg",
            language=faker.language_name(),
            smokingHabbit=faker.random_element(elements=('Yes', 'No')),
            drinkingHabbit=faker.random_element(elements=('Yes', 'No')),
            diet=faker.random_element(elements=('Vegetarian', 'Non-Vegetarian', 'Vegan')),
            complexion=faker.random_element(elements=('Fair', 'Wheatish', 'Dark')),
            fatherOccupation=faker.job(),
            motherOccupation=faker.job(),
            numberOfSiblings=faker.random_int(min=0, max=5),
            livingWithFamily=faker.random_element(elements=('Yes', 'No')),
            citizenShip=faker.country(),
            country=faker.country(),
            state=faker.state(),
            austrailanVisaStatus=faker.random_element(elements=('Yes', 'No')),
            currentLocation=faker.city(),
            cityOfResidence=faker.city(),
            nationality=faker.country(),
            residencyVisaStatus=faker.random_element(elements=('Yes', 'No')),
            gender=faker.random_element(elements=('Male', 'Female')),
            lookingFor=faker.random_element(elements=('Male', 'Female')),
            weddingGoals=faker.random_element(elements=('Marriage', 'Companionship', 'Friendship')),
            age=f"{faker.random_int(min=18, max=65)}",
            lookingPartnerAge=f"{faker.random_int(min=18, max=35)}-{faker.random_int(min=36, max=65)}",
            livingInAustralia=faker.random_element(elements=('Yes', 'No')),
            horoscopeMatch=faker.random_element(elements=('Yes', 'No')),
            castReligionMatterOrNot=faker.random_element(elements=('Yes', 'No')),
            interest_and_hobbies=faker.words(nb=5, ext_word_list=None, unique=False)
        )
        session.add(record)
    session.commit()

# Create and insert 1000 dummy records
create_dummy_data(session, 1000)

# Close the session
session.close()
