
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sklearn.metrics.pairwise import cosine_similarity
from app.models import RecommendationModel
from app.database import get_session
from app.schemas import RecommendationCreate, RecommendationOut
from typing import List
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class UserIdRequest(BaseModel):
    userId: str

def parse_age_range(age_range: str):
    try:
        start_age, end_age = map(int, age_range.split('-'))
        return start_age, end_age
    except ValueError:
        return 0, 0

def is_age_in_range(age: str, age_range: str):
    start_age, end_age = map(int, age_range.split('-'))
    age = int(age)
    return start_age <= age <= end_age

def compute_similarity(user1, user2):
    features = list(set(user1['interest_and_hobbies'] + user2['interest_and_hobbies']))

    def get_feature_vector(user):
        return [
            user['age'],
            user['gender'] == user1['gender'],
            user['lookingFor'] == user1['gender'],
            user['lookingFor'] == user1['lookingFor'],
            is_age_in_range(user1['age'], user['lookingPartnerAge']),
            user['caste'] == user1['caste'],
            user['community'] == user1['community'],
            user['religion'] == user1['religion']
        ] + [1 if feature in user['interest_and_hobbies'] else 0 for feature in features]

    vector1 = get_feature_vector(user1)
    vector2 = get_feature_vector(user2)

    sim = cosine_similarity([vector1], [vector2])[0][0]

    return round(sim * 100, 2)

@app.post("/get_matches/", response_model=List[dict])
async def get_matches(request: UserIdRequest, session: AsyncSession = Depends(get_session)):
    userId = request.userId

    # Fetch the current user by userId
    result = await session.execute(select(RecommendationModel).filter(RecommendationModel.userId == userId))
    current_user = result.scalars().first()

    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Fetch all recommendations
    result = await session.execute(select(RecommendationModel))
    recommendations = result.scalars().all()

    matches = []

    # Prepare current_user dictionary
    current_user_data = {
        "userId": current_user.userId,
        "age": int(current_user.age) if current_user.age else 0,
        "gender": current_user.gender,
        "lookingFor": current_user.lookingFor,
        "lookingPartnerAge": current_user.lookingPartnerAge,
        "caste": current_user.caste,
        "community": current_user.community,
        "religion": current_user.religion,
        "interest_and_hobbies": current_user.interest_and_hobbies or []
    }

    for user in recommendations:
        if user.userId != current_user.userId:
            user_data = {
                "userId": user.userId,
                "age": int(user.age) if user.age else 0,
                "gender": user.gender,
                "lookingFor": user.lookingFor,
                "lookingPartnerAge": user.lookingPartnerAge,
                "caste": user.caste,
                "community": user.community,
                "religion": user.religion,
                "firstName":user.firstName,
                "lastName":user.lastName,
                "displayName":user.displayName,
                "occupation":user.occupation,
                "state":user.state,
                "country":user.country,
                "userType":user.usertype,
                "about":user.aboutYourSelf,
                "fatherOccupation":user.fatherOccupation,
                "motherOccupation":user.motherOccupation,
                "nosOfSiblings":user.numberOfSiblings,
                "livingWithFamily":user.livingWithFamily,
                "subCommunity":user.smokingHabbit,
                "gothra":user.gotra,
                "motherTongue":user.motherTongue,
                "currentLocation":user.currentLocation,
                "cityOfResidence":user.cityOfResidence,
                "nationality":user.nationality,
                "citizenship":user.citizenShip,
                "residencyVizaStatus":user.residencyVisaStatus,
                "height":user.height,
                "weight":user.weight,
                "boyType":user.bodyType,
                "language": user.language,
                "smokingHabbits":user.smokingHabbit,
                "drinkingHabbits":user.drinkingHabbit,
                "diet":user.diet,
                "complexion":user.complexion,
                "education": user.qualification,
                "incom": user.income,
                "interest_and_hobbies": user.interest_and_hobbies,
                "profileImages": user.image,
            }

            similarity = compute_similarity(current_user_data, user_data)

            if user.gender == current_user.lookingFor and is_age_in_range(user.age, current_user.lookingPartnerAge):
                matches.append({
                    "userId": user.userId,
                    "match_percentage": similarity,
                    "user_details": user_data
                })

    matches = sorted(matches, key=lambda x: x['match_percentage'], reverse=True)

    return matches

if __name__ == "__main__":
    # Start FastAPI on port 9000
    uvicorn.run(app, host="0.0.0.0", port=9000)