import streamlit as st

from langchain_sequential import overall_chain
from generate_image import text_to_image
from voicevox import text_to_voice


def main():
    st.title("Stable Diffusion with ChatGPT")
    st.subheader("テーマ")
    user_input = st.text_input("テーマを入力してください。Enterキーを押すたびに画像とシナリオが生成されます。", "")

    if user_input:
        st.subheader("イラストとシナリオ")
        results = overall_chain(user_input)
        st.image(text_to_image(results["sd_prompt"]))
        st.write(results["synopsis"])
        text_to_voice(results["synopsis"])


if __name__ == "__main__":
    main()
