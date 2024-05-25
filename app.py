import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

st.title("Creative Text Generator with GPT-3")
st.write("Generate creative text formats based on your prompts and choices.")

# User prompt input
user_prompt = st.text_input("Enter your prompt:")

# Text format selection
format_options = ["Poem", "Story", "Article", "Song Lyrics"]
selected_format = st.selectbox("Choose the text format:", format_options)

# Level of creativity
creativity_level = st.slider("Select creativity level:", 0.0, 1.0, 0.5)

if st.button("Generate"):
    if user_prompt:
        # Call the GPT-3 API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate a {selected_format.lower()} based on the following prompt:\n\n{user_prompt}",
            max_tokens=500,
            temperature=creativity_level
        )
        
        generated_text = response.choices[0].text.strip()
        st.write("### Generated Text")
        st.write(generated_text)
    else:
        st.warning("Please enter a prompt to generate text.")

if st.button("Generate"):
    if user_prompt:
        # Step 1: Refine the prompt
        st.write("Refining your prompt...")
        refined_prompt_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Refine the following prompt for clarity and creativity:\n\n{user_prompt}",
            max_tokens=150
        )
        refined_prompt = refined_prompt_response.choices[0].text.strip()
        st.write("### Refined Prompt")
        st.write(refined_prompt)

        # Step 2: Generate the creative text
        st.write("Generating your creative text...")
        creative_text_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate a {selected_format.lower()} based on the following refined prompt:\n\n{refined_prompt}",
            max_tokens=500,
            temperature=creativity_level
        )
        generated_text = creative_text_response.choices[0].text.strip()
        st.write("### Generated Text")
        st.write(generated_text)
    else:
        st.warning("Please enter a prompt to generate text.")
