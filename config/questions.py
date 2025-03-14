# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "all resumes/default/resume.pdf"  # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience?
years_of_experience = "2.7"  # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"  # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = "https://preetham-p-m.vercel.app"  # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/preetham-p-m"  # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Non-citizen seeking work authorization"


## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = (
    2600000  # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
)
"""
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs),
then it will add '.' before last 5 digits and answer. Examples:
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
"""

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = (
    2200000  # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
)
"""
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs),
then it will add '.' before last 5 digits and answer. Examples:
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
"""

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg:
# currency = "INR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 30  # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
"""
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months),
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
"""

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "Full Stack Developer at Coupa and 2.7+ years of experience"  # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
I am a Full Stack Engineer with expertise in both back-end and front-end development, working with technologies like Java, Spring Boot, React, C#, and ASP.Net Core,. I enjoy solving complex challenges and have built scalable solutions for various projects. My experience includes integrating powerful search capabilities with Elasticsearch, implementing CI/CD pipelines, and leveraging Docker, Kubernetes, and AWS for containerization and orchestration. Additionally, I have worked with Kafka and RabbitMQ to build robust and efficient messaging systems.

With a strong problem-solving mindset, I continuously strive to improve my skills and deliver efficient, high-quality solutions. I'm passionate about contributing to impactful projects and collaborating in innovative teams.
"""

"""
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
"""

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Dear Hiring Manager,

I am excited to apply for the Backend Engineer position at your company. With expertise in Spring Boot and React.js, I specialize in building scalable backend systems, optimizing APIs, and ensuring seamless front-end integration. I have experience in developing microservices, implementing CI/CD pipelines, and working with cloud technologies to enhance system performance.

I am passionate about solving complex challenges and improving development processes to deliver efficient and high-quality solutions. I would welcome the opportunity to contribute to your team and discuss how my skills align with your needs. Looking forward to your response.
"""

"""
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
"""

# Name of your most recent employer
recent_employer = (
    "Not Applicable"  # "", "Lala Company", "Google", "Snowflake", "Databricks"
)

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = (
    "9"  # Any number between "1" to "10" including 1 and 10, put it in quotes ""
)
##


# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = True  # True or False, Note: True or False are case-sensitive
"""
Note: Will be treated as False if `run_in_background = True`
"""

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True  # True or False, Note: True or False are case-sensitive
"""
Note: Will be treated as False if `run_in_background = True`
"""
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = (
    False  # True or False, Note: True or False are case-sensitive
)
