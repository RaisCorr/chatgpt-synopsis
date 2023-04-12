import os
import replicate

# Replicate APIkey
REPLICATE_API_TOKEN = os.environ["REPLICATE_API_TOKEN"]
replicate.Client(api_token=REPLICATE_API_TOKEN)


def text_to_image(prompt):
    """
    Generate an image using Replicate AI's image generation API.

    :param prompt: a string containing the prompt text for image generation
    :return: a string containing the URL of the generated image
    """
    # Generate an image using Replicate API with the given prompt
    output = replicate.run(
        "cjwbw/anything-v3-better-vae:09a5805203f4c12da649ec1923bb7729517ca25fcac790e640eaa9ed66573b65",
        input={
            "prompt": """(masterpiece), (best quality), [watercolor], a picturesque scenery, (1girl:1.3),"""
            + prompt
            + """(loli:1.2), field of depth, light particles, backlighting, pale color, gradient, petals,""",
            "negative_prompt": "sketch, lowres, outline, nsfw, worst quality, low quality, vivid, breasts, animal, fat, jewel, jpeg artifacts, signature, watermark, username, blurry, neon, horror, brack, dark,",
            "scheduler": "DDIM",
            "width": 768,
            "height": 512,
            "guidance_scale": 8,
        },
    )

    # Confirm the prompt and URL of the generated image
    print("prompt:", prompt)
    print("URL: ", output[0])

    res = output[0]

    return res
