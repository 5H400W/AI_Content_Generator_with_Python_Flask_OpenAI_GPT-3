import os
import openai
import config
openai.api_key = config.OPENAI_API_KEY


#function for Product description
def productDescription(query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generate a detailed product description for :{}".format(query),
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = "OOPS! You beat the AI this time"
    else:
        answer = "OOPS! You beat the AI this time"


    return answer

# function for jobdescription

def jobDescription(query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generate a detailed job description for :{}".format(query),
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = "OOPS! You beat the AI this time"
    else:
        answer = "OOPS! You beat the AI this time"


    return answer


#tweet contents
def tweetIdeas(query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="find tweet contents about :{}".format(query),
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = "OOPS! You beat the AI this time"
    else:
        answer = "OOPS! You beat the AI this time"

    return answer

#cold emails
def coldEmails(query):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="generate perfect professional cold email content for :{}".format(query),
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = "OOPS! You beat the AI this time"
    else:
        answer = "OOPS! You beat the AI this time"

    return answer




#socialMedia
def socialMedia(query):
    response = openai.Completion.create(
        model="text-curie-001",
        prompt="create unique social media advert ideas for:{}".format(query),
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = "OOPS! You beat the AI this time"
    else:
        answer = "OOPS! You beat the AI this time"

    return answer


#businessPitch ideas

def businessPitch(query):
    response = openai.Completion.create(
        model="text--curie-001",
        prompt="Create some ideas for a paragraph business pitch idea for:{}".format(query),
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = "OOPS! You beat the AI this time"
    else:
        answer = "OOPS! You beat the AI this time"

    return answer


#videoIdeas
def videoIdeas(query):
    response = openai.Completion.create(
        model="davinci",
        prompt="Create some YouTube Video Ideas for:{}".format(query),
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = "OOPS! You beat the AI this time"
    else:
        answer = "OOPS! You beat the AI this time"

    return answer


#videoDescription

def videoDescription(query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Create some cool video descriptions based on:{}".format(query),
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = "OOPS! You beat the AI this time"
    else:
        answer = "OOPS! You beat the AI this time"

    return answer


