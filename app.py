import random
import streamlit as st
import time
from PIL import Image
import webbrowser

# Set page config to make app mobile-friendly and responsive
st.set_page_config(
    page_title="Disney Movie Night",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="auto",
)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
    background_color: #123cd0;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)




# Add CSS to apply custom styling based on screen size
st.markdown(
    """
    <style>
    @media only screen and (max-width: 600px) {
        /* Styles for screens smaller than 600px */
        body {
            font-size: 14px;
            padding: 10px;
            text-align: center;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add CSS to center all elements in the app
st.markdown(
    """
    <style>
    body {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add your Streamlit app code here

# A dictionary of some popular Disney movie titles and their trailer video IDs and recipe URLs
disney_movies = {
    "Snow White and the Seven Dwarfs": {
        "trailer_id": "5fzZFQBXSLM",
        "recipe_url": "https://i.pinimg.com/originals/64/30/1f/64301f3b204a6387db456968ce592783.jpg",
        "image_url": "https://media1.tenor.com/images/a5e8183f7fb0fd2453efcc60435e15e4/tenor.gif?itemid=3917339"
    },
    "Cinderella": {
        "trailer_id": "UcjYD91YW_M",
        "recipe_url": "https://mealplanningblueprints.com/blog/disney-movie-night-themed-dinner-recipe-ideas-cinderella/",
        "image_url": "https://media.giphy.com/media/13O1owG7Q1z4E8/giphy.gif"
    },
    "Sleeping Beauty": {
        "trailer_id": "CfsyUyi_FJM",
        "recipe_url": "https://happiestmemoriesonearth.blogspot.com/2018/09/disney-meal-34-sleeping-beauty.html",
        "image_url": "https://media.giphy.com/media/xDMb2lcyXeoFO/giphy.gif"
    },
    "The Little Mermaid": {
        "trailer_id": "nPE0f-MB_bQ",
        "recipe_url": "http://mommyandthings.blogspot.com/2013/09/disney-movie-night-little-mermaid.html",
        "image_url": "https://th.bing.com/th/id/OIP.LEi6I8Qgl6jfC8a5Jm3i-QHaEG?pid=ImgDet&rs=1"
    },
    "Beauty and the Beast": {
        "trailer_id": "iurbZwxKFUE",
        "recipe_url": "https://mealplanningblueprints.com/blog/disney-movie-night-themed-dinner-recipe-ideas-beauty-beast/",
        "image_url": "https://media.giphy.com/media/JuyipPBCvmTbW/giphy.gif"
    },
    "Aladdin": {
        "trailer_id": "eTjHiQKJUDY",
        "recipe_url": "https://mealplanningblueprints.com/blog/disney-movie-night-themed-dinner-recipe-ideas-aladdin/",
        "image_url": "https://data.whicdn.com/images/307549180/original.gif"
    },
    
    "Toy Sory": {
        "trailer_id": "v-PjgYDrg70",
        "recipe_url": "https://happiestmemoriesonearth.blogspot.com/2018/08/disney-meal-22-toy-story.html",
        "image_url": "https://media.giphy.com/media/kUiVangO4Yf8Q/giphy.gif"
    },
}





# Define the Streamlit app
def app():
    st.title("Disney Movie Night Generator")
    
    
    
    image = Image.open("disneylogo.jpg")
    st.image(image, width=200, use_column_width=True)

    

    
    st.write("Click the button below to get a random Disney movie title:")
    

    # Define a button that generates a random movie title and plays its trailer
    if st.button("Generate Movie"):
        with st.spinner("Choosing a movie..."):
            # Simulate a delay to give the spinner some time to spin
            time.sleep(2)
            random_movie = random.choice(list(disney_movies.keys()))
            trailer_id = disney_movies[random_movie]['trailer_id']
            recipe_url = disney_movies[random_movie]['recipe_url']
            image_url = disney_movies[random_movie]['image_url']
        
            st.success(f"Your random Disney movie is: {random_movie}")
            st.image(image_url, width=200)

            st.write("# Here's the trailer:")
            video_url = f"https://www.youtube.com/embed/{trailer_id}?autoplay=1&mute=1"
            st.markdown(f'<iframe width="365" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
                

            st.write(f"# Looking for dinner inspiration? Check out this recipe website for {random_movie}!")
            st.write(f"Click [here]({recipe_url}) to find recipes related to {random_movie}")

if __name__ == "__main__":
    app()















