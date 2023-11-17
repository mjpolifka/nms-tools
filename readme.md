# No Man's Sky Tools

## This is basically abandoned
I don't play the game anymore and don't intend to finish anything in here.

### Under Construction:
#### Solar power calculator
- Input daylight and night hours, including seconds of 50% power
- How many solar panels do you need for 2x output?
- How many batteries do you need to last the night?

### Feature brainstorming

- Targeting the mobile browser, since the game only runs well in Fullscreen
- Database of all components with their base sell value
- Database of all possible recipes
- Page to calculate how to get the best return for the ingredients you have on hand
    - Allow for missing components so you can decide if it's worth farming them
- List of upgrades you can buy and their location
    - Be able to build a shopping list to prioritize/plan and remember
~~- Solar power calculator~~ Implementing
    ~~- How many solar panels do you need for 2x output~~
    ~~- How many batteries do you need to last the night~~
    ~~- Input daylight and night hours, including seconds of 50% power~~

### Architecture

I'm planning for this to be a Python/Flask backend for wide deployment options (looking at you, Raspberry Pi).
But I want the frontend to be React, just so I can build my skills.
Flask can probably handle the frontend easily, as it did with my Satisfactory Tools.  

Basically write everything starting in React.
Only features requiring database access will have anything written in Python/Flask.
When you need to look up some data, write an API call and a Flask function.  

Now that I'm thinking about it, I don't think there's any user-generated data.
Therefore, we don't necessarily need a database.
But I do need something that can do the relationships for the recipes.
I know sqlite can do this, and tbh it's pretty light.
But it might be worth looking for other packages that are more targeted to my needs.
Or even writing something myself, it would certainly be a good exercise.  

I still need a backend though, and I still want it to be Python/Flask.
If it ends up being a 100%-React app, I'll still need something to serve it.  

But definitely I need to start this in React and see where it goes from there, while I build up my data in a file
