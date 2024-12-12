# CMPSC 350: Final Reflection

## Final title

Clementine the Cat's Flipbook Adventures

## Summary

My work involves the portrayal of an orange cat running and leaping through a field of flowers. An original picture of a standing orange cat is generated, then edited 29 times to add slight movements with each additional image, so the images can then be compiled into a flipbook that brings the orange cat to life.

## Reference works

1. project2-childrensbook
This project assisted me in providing functions to link an LLM to my prototype, generate the images, save the images as a pdf, then create a final pdf for the flipbook that incorporates all the images. Instead of simply generating the images as I did in the children's book, this project incorporates a generate image edit function that feeds in the original image to ensure style consistency throughout the generated images.

2. prompt7-visual-narrative
This project entails generating images that are cohesive with one another and can be combined to tell a full and complete narrative. The images for my flipbook must be consistent with one another for the flipbook to work as intended and tell the story of the orange cat that I aim to tell.

3. https://thegradient.pub/an-introduction-to-ai-story-generation/ 
This reading goes into detail on how AI can assist in story generation. I will utilize key concepts of this reading, including definitions of narrative, story, and plot, as well as story planners and neutral story generation to better understand the goals I'm aiming to accomplish through my project, and how I can most efficiently implement my code to match those goals.

## Describe your single largest success.

My largest success was finding a way to incorporate the generate image edit function. I was able to find a function that utilizes dall-e-2 to take in an original image as input, a transparent image that highlights the part I wish to edit, then produce an edited version of the original image based on my prompting.

## Describe your single largest challenge or failure.

The largest challenge, and perhaps failure, was creating images that incorporate the small movements of the cat so they can be effectively flipped through to portray the actions I intend. Even with specific prompting, the images aren't as accurate as I had hoped, so there are some inconsistencies when I flip through them. This is mostly due to the fact that only dall-e-2 is compatible with the generate image edit function, so utilizing this earlier version of dall-e comes with inconsistencies and inaccuracies that wouldn't occur with dall-e-3.

## The role of feedback

The feedback from my peers allowed me to further research and inspect how to use different prompting techniques to accomplish my project's goals. It also motivated me to think more about the final product I aim to create, whether that's a pdf generated through code, or a slideshow, or both.

## Contextualizing

My work fits my understanding of the course, as I had to use trial and error, as well as many different prompting techniques, to ensure the images I generated were as accurate as possible. Through altering my prompt and seeing how it impacted the results, I was able to find a prompt structure that worked best for me. I was also able to generate images that together tell a narrative story. The images portray the story of an orange cat named Clementine that runs and jumps in a field of flowers. My final take-away from participating in this project was that even the smallest edits to a prompt can create an entirely new generation, and even running the same prompt twice creates different images. It's important to understand exactly what keywords trigger my intended results, and how to incorporate those keywords into many different types of prompts, all intending to create something different that contributes to the overall narrative.