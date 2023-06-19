**Author**: Guillaume Pernelle

**Date**: 19/06/2023

## Objective 
Our aim is to design and implement a proof-of-concept recommender engine using Django. The engine is designed
to suggest adventure recommendations to users as they navigate through the application, with these suggestions tailored
according to their behavior and preferences.

## Our Approach 
Our strategy emphasizes the construction of a user profile that can efficiently generate highly
personalized recommendations. For some key data points, we gather the information directly during the user's initial
connection to the application. The rest is estimated via Gaussian Processes, a statistical technique (see [GP.md](GP.md)) that allows us to build a user model with a limited number of input questions (less than 5) and refine this model
as the user interacts with the app. Our initial focus lies on user preferences, and as our user base expands, we plan to
incorporate collaborative filtering for further enhancement of recommendations.

Ideally, we would conduct preliminary research to identify the primary predictors of adventure choices among our target
audience. These could include factors such as age, sex, profession, and others. If relevant datasets are available, we
could use principal component analysis to identify the most crucial components. However, given the context of this
exercise, we make certain assumptions about the most relevant indicators to ensure the recommendations are as accurate
as possible.

Our recommendation system revolves around two main components: adventures and users, with the aim of pairing adventures
with appropriate users. As a future expansion, we could also consider matching users with other users who have similar
profiles.

## The current Adventure model includes the following fields

- Category
- Adrenalin (e.g., a rating of 0 for a peaceful park meditation, and 10 for a high-adrenaline wingsuit flight in Chamonix)
- Kid-friendly
- Location

We are also considering the addition of the following fields:

- Fitness level requirement (ranging from low-demand activities like going to the movie theater, to high-demand activities
like climbing Everest)
- Wheelchair access (boolean)
- Season (e.g., winter, all year, etc.)
- Time of the day (suitable for early birds, night owls, or available all day)
- Weather dependency
- Single participant allowance
- Maximum group size
- Requirement of a permit (for activities like sailing, diving, fishing, etc.)
- Public transport access
- Price range

## The User model comprises the following fields:

- Category preferences: A value between 0 and 10 for each category, with a default of 5
- Wheelchair accessibility requirement
- Fitness level
- Single activity preference
- Held permits
- Requirement of public transport
- Maximum price per activity 


## Description of the User Experience:

### On First Connection
We gather key data that aids in filtering out unsuitable suggestions.

- Location: The user's location is either requested upon initial connection or derived from their GPS data. Activities
falling outside of the location range are filtered out.
- Kids: This is a boolean field. If the user has kids (Kids=True), we exclude all activities unsuitable for children.
- Wheelchair Access: If the user requires wheelchair access (True), we filter out all inaccessible activities.
- Permits, Public Transport Requirement, Max Price per Activity: These are either obtained directly or assumed based on
the user's profile.

We propose asking five questions to construct a user profile, with each question designed based on the answers to
previous ones. The Gaussian Process is used to target data that refines the model most effectively.

## On Following Connections

As the user continues to engage with our app, we use a 'like/bookmark' feature to further refine our model. We also plan
to introduce a 'dislike' button to help filter out less desirable suggestions and possibly incorporate a specific model