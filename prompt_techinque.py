def prompt1(input_job_role,job_description):
    input_prompt_1 = """
                    As an experienced Applicant Tracking System (ATS) resume screening for resume with the Job Description :
                    List out all the issues in resume with respective to Job Description. Provide constructive feedback for improvement.  

                    1. Identify technical requirements
                    2. Check experience fit
                    3. Surface experience gaps    
                    4. Assess projects if fresher
                    5. Recommend improvements  

                    If resume does not fit job description, state key gaps.
                    Otherwise provide focused recommendations to better align. 
                    Structure output into : Requirements, list the Gaps, list the Changes Required specifing the tech keywords, Recommendations.
                    """
    return input_prompt_1


def prompt2(input_job_role,job_description):
    input_prompt_1 = """
                    As an experienced Applicant Tracking System (ATS) for {input_job_role} resume scanner with expertise in technical requirement analysis. 
                    Compare the resume to the {job_description} judging match based on:

                    1. Technical Skills (70% weight)
                    - Identify missing technical keywords. 
                    - Reduce match score if critical skills are not present.

                    2. Experience Level (20% weight)  
                    - Check alignment with years required as per job description.
                    - For every year of experience underrequired, reduce match score.
                    - If meets/exceeds, do not adjust score positively.

                    3. Education Level (10% weight)
                    - Validate if educational criteria are met based on job needs.
                    - For every educational degree missing, marginally reduce match score.
                    - If education level matches/surpasses, do not increase score.

                    First, state the percent match score after judging missing criteria weighted above.
                    Next, list all unmet technical skills and experience gaps. Determine the match percentage and any missing keywords. 
                    Finally, provide closing recommendations on areas of mismatch for improving resume relevance.  

                    Ignore any textual tables, charts or visual formatting when scanning. Call those out separately after final thoughts.
                    """     
    return input_prompt_1

