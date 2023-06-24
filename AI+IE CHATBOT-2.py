# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 22:07:22 2023

@author: 52795
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import openai
import gradio

openai.api_key = "*******************"

faq_questions_answers = [
    {"question": "What industries does AI+IE serve?",
     "answer": "AI+IE provides AI and industrial engineering solutions for a wide range of industries, including manufacturing, logistics, healthcare, finance, retail, and more. We focus on small and medium-sized businesses and organizations that are looking to optimize their operations and enhance their productivity."},
    {"question": "Can AI+IE develop custom applications for my business?",
    "answer": "Yes, AI+IE can develop custom applications using machine learning, deep learning, natural language processing (NLP), and computer vision technologies. These applications can help automate tasks, improve customer service, enhance decision-making, and more, depending on your business's specific needs."},
    # Add the other FAQs in the same format here
]

messages = [{"role": "system", "content": "You are an AI+IE company website assistant"}]

for faq in faq_questions_answers:
    messages.append({"role": "user", "content": faq["question"]})
    messages.append({"role": "assistant", "content": faq["answer"]})

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="AI+IE Assistant")

demo.launch(share=True)