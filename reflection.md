# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  The hints were opposite. Every time I guessed a number that was higer than the secret number it told me to go higher but in reality to should have told me to go lower. The score keeps glitching everytime I enter a new guess in and it doesn't stay consistent. The attempt starts with 1 instead of it starting at 0.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude and Copilot. One example that was correct when it figured out why the hints were opposite. AI suggested that it was looking at if the guessed b=number was even or odd and then depending on that incrementing the score. I checked and saw that since it was testing to see if the guessednum % 2 and then depending on that statement it was decrementing the score.

One example that was misleading was when I was trying to fix why the hints were opposite it started touching the scoring logic but that was not needed at the moment so I went to see why it was doing it and it was looking at my old FixMe comment for the scoring logic that I had put in. But then I myself looked at the hint logic one more time and realized that the print statements were switched both cases and changed those to match the needed logic.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I physically played the game to check if the bugs were fixed each time. For example I would an input that was not the secret number to check if the hints were saying what they were supposed to say. It showed me that the code was working properly and that the fixes I made had worked. After that i wrote a test cases to check the scoring logic with the help of claude to construct them for me. I think AI helped me understand the test case logic because it showed some flaws in the actual code and then I had to go fix it to make it match the test case.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

A secret number was generated each time because the a "rerun" re-executes the whole script from top to bottome after any user interaction. The fix was to wrapping the secret generation in if "secret" not in st.session_state so it only runs once.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I think one habit I would resue is how much I would check to see if the game was working properly or not each time after I made a change. This was both physical and with pytest. I think something I can do differently is be more clear on what I want to fix using AI. I feel like sometimes Claude got confused on what to fix and would start fixing a multitude of things all at once which was overwhelming. This project change the way I think about AI generated code because It showed me that 
