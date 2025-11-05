"""
Job Applicant Scoring System

This module provides a clear, objective scoring function for job applicants.
It uses only professional features (experience, education, skills match, certifications,
interview and portfolio scores) and explicitly excludes protected attributes
like name, gender, race, religion, or age from scoring.

It also includes a small demo that shows identical financial/professional profiles
for applicants with different names/genders to demonstrate lack of bias in scoring.

How it works (contract):
- Input: applicant dictionary with specific numerical/enum fields (see examples).
- Output: (score: float 0-100, breakdown: dict of component scores)
- Error modes: raises ValueError on missing required fields or invalid types.

Edge cases considered:
- Missing optional fields defaulted to neutral values.
- Education levels mapped to numeric points.
- Skills match accepted as percentage (0-100).
- Interview/portfolio scores expected 0-100.

This is intended as a demonstration/starting point. For production use, the
score weights and thresholds should be validated with domain experts and audited
for disparate impact across protected groups.
"""

from typing import Dict, Tuple

# Mapping of education levels to numeric points (objective representation)
EDUCATION_LEVEL_POINTS = {
    'phd': 20,
    'masters': 15,
    'bachelors': 10,
    'associate': 6,
    'highschool': 2,
    'none': 0
}

# Weights for each component (must sum to 1.0)
WEIGHTS = {
    'experience': 0.25,        # years of relevant experience
    'education': 0.15,         # mapped education points
    'skills_match': 0.30,      # percentage match to job skills (0-100)
    'certifications': 0.05,    # count of relevant certs (capped)
    'interview': 0.15,         # interview performance (0-100)
    'portfolio': 0.10          # portfolio quality (0-100)
}

# Helper to cap or normalize inputs
def _cap(x: float, minimum: float, maximum: float) -> float:
    return max(minimum, min(maximum, x))


def score_applicant(applicant: Dict) -> Tuple[float, Dict[str, float]]:
    """
    Calculate a 0-100 score for a job applicant using objective professional features.

    Required keys in `applicant`:
    - 'years_experience' (float or int): total years of relevant experience
    - 'education_level' (str): one of the keys in EDUCATION_LEVEL_POINTS (case-insensitive)
    - 'skills_match_pct' (float): percentage (0-100) representing skills fit
    - 'interview_score' (float): 0-100 score from the interview

    Optional keys:
    - 'certifications' (int): number of relevant certifications (non-negative)
    - 'portfolio_score' (float): 0-100 score evaluating portfolio (for design/engineering)

    Returns:
    - final_score (float): 0-100
    - breakdown (dict): component scores before weighting for transparency

    Important: This function intentionally ignores protected attributes such as
    'name', 'gender', 'race', and 'age'. If those keys appear in the input dict they
    will not affect the score.
    """

    # Validate required fields
    required = ['years_experience', 'education_level', 'skills_match_pct', 'interview_score']
    for key in required:
        if key not in applicant:
            raise ValueError(f"Missing required applicant field: {key}")

    # Extract and normalize features
    years_exp = float(applicant.get('years_experience', 0.0))
    years_exp = _cap(years_exp, 0.0, 40.0)  # cap to 40 years for scoring

    edu_raw = str(applicant.get('education_level', '')).strip().lower()
    education_points = EDUCATION_LEVEL_POINTS.get(edu_raw, 0)

    skills_pct = float(applicant.get('skills_match_pct', 0.0))
    skills_pct = _cap(skills_pct, 0.0, 100.0)

    interview = float(applicant.get('interview_score', 0.0))
    interview = _cap(interview, 0.0, 100.0)

    portfolio = float(applicant.get('portfolio_score', 0.0))
    portfolio = _cap(portfolio, 0.0, 100.0)

    certifications = int(applicant.get('certifications', 0))
    certifications = max(0, certifications)
    certifications_capped = min(certifications, 5)  # cap influence

    # Component raw scores (0-100 scale)
    # Experience: linear mapping to 0-100 (0 years -> 0, 20+ years -> 100)
    experience_score = (years_exp / 20.0) * 100.0
    experience_score = _cap(experience_score, 0.0, 100.0)

    # Education: map education points (0-20) to 0-100
    education_score = (education_points / 20.0) * 100.0

    # Certifications: each relevant cert gives +8 points (capped at 5 certs = 40)
    certifications_score = (certifications_capped / 5.0) * 100.0

    # Skills, interview, portfolio are already on 0-100
    skills_score = skills_pct

    interview_score = interview
    portfolio_score = portfolio

    # Weighted aggregation
    final_score = (
        WEIGHTS['experience'] * experience_score +
        WEIGHTS['education'] * education_score +
        WEIGHTS['skills_match'] * skills_score +
        WEIGHTS['certifications'] * certifications_score +
        WEIGHTS['interview'] * interview_score +
        WEIGHTS['portfolio'] * portfolio_score
    )

    # Normalize to 0-100
    final_score = _cap(final_score, 0.0, 100.0)

    breakdown = {
        'experience_score': round(experience_score, 2),
        'education_score': round(education_score, 2),
        'skills_score': round(skills_score, 2),
        'certifications_score': round(certifications_score, 2),
        'interview_score': round(interview_score, 2),
        'portfolio_score': round(portfolio_score, 2),
        'final_score': round(final_score, 2)
    }

    return final_score, breakdown


def bias_check_demo():
    """
    Demonstration that the scoring function does not use name/gender.
    Creates three applicants with identical professional features but different names/genders.
    """
    base_profile = {
        'years_experience': 5,
        'education_level': 'bachelors',
        'skills_match_pct': 85.0,
        'interview_score': 88.0,
        'portfolio_score': 80.0,
        'certifications': 2
    }

    applicants = [
        {**base_profile, 'name': 'Alice Smith', 'gender': 'female'},
        {**base_profile, 'name': 'Bob Johnson', 'gender': 'male'},
        {**base_profile, 'name': 'Chen Li', 'gender': 'non-binary'}
    ]

    print('\nBias Check Demo: identical professional profiles with different names/genders')
    print('-' * 80)

    def get_title(gender):
        gender_str = str(gender).strip().lower()
        if gender_str == 'male':
            return 'Mr.'
        elif gender_str == 'female':
            return 'Mrs.'
        else:
            return 'Mx.'

    results = []
    for app in applicants:
        score, breakdown = score_applicant(app)
        title = get_title(app.get('gender', ''))
        print(f"Applicant: {title} {app['name']} (gender: {app['gender']})")
        print(f"Score: {score:.2f}")
        print('Breakdown:', breakdown)
        print('-' * 80)
        results.append(score)

    # Simple verification
    if len(set(results)) == 1:
        print('Bias Analysis: PASS ✅ - identical scores for identical professional profiles')
    else:
        print('Bias Analysis: FAIL ❌ - differing scores detected')


def example_usage():
    """Show a few more example applicants and ranking."""
    pool = [
        {
            'name': 'Senior Engineer',
            'years_experience': 10,
            'education_level': 'masters',
            'skills_match_pct': 92.0,
            'interview_score': 90.0,
            'portfolio_score': 88.0,
            'certifications': 3
        },
        {
            'name': 'Junior Dev',
            'years_experience': 1,
            'education_level': 'bachelors',
            'skills_match_pct': 70.0,
            'interview_score': 75.0,
            'portfolio_score': 60.0,
            'certifications': 0
        },
        {
            'name': 'Mid-level Dev',
            'years_experience': 4,
            'education_level': 'bachelors',
            'skills_match_pct': 80.0,
            'interview_score': 82.0,
            'portfolio_score': 75.0,
            'certifications': 1
        }
    ]

    print('\nExample ranking of applicants')
    print('-' * 80)
    scored = []
    def get_title(gender):
        gender_str = str(gender).strip().lower()
        if gender_str == 'male':
            return 'Mr.'
        elif gender_str == 'female':
            return 'Mrs.'
        else:
            return 'Mx.'

    for p in pool:
        score, breakdown = score_applicant(p)
        title = get_title(p.get('gender', ''))
        display_name = f"{title} {p['name']}" if 'gender' in p else p['name']
        scored.append((display_name, score, breakdown))

    scored.sort(key=lambda x: x[1], reverse=True)
    for name, score, breakdown in scored:
        print(f"{name}: {score:.2f}")
    print('-' * 80)


if __name__ == '__main__':
    bias_check_demo()
    example_usage()
