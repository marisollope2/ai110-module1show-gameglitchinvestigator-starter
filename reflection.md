# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

- Gives opposite hints. I guessed 71 when the answer was 61 and it said go higher instead of lower
- Clicked new game and it said game over and to click to start a new game.
- Takes in negative inputs when the range should only be 0-100

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|71     |Give a go lower hint |Gave a go higher hint |None |
|New Game| Reset and start a new game|Displayed a message to press New Game | Game over, click new game for a new game.|
|-1 |Return an error message, only inputs from 0-100 |Didn't return an error and accepted the input |None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Code in VS Code.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggested I redo the difficulty for Hard because It didn't make much sense for it to have a smaller range than normal despit having less attempts. I did my own work to compare the chance of a user getting it correct within the attempted tries for each and decided to change the logic for hard mode.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
To be honest, I didn't find a specific incorrect suggestion. The AI did bring up random edge cases for the input type that I didn't think were necessary because I had already tested them in the game.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I had the game open and tested it after the code was changed. I also had claude brainstorm edge cases.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  After the game status bug was fixed, I tried it in the game to verify after receiving different scores and with even and odd attempts. I was able to start a new game after clicking the button.
- Did AI help you design or understand any tests? How?
It helped me understand how to format tests in a simple and readable manner and account for edge cases.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
When you interact with a Streamlit app the entire Python script reruns from top to bottom, wiping all your variables. st.session_state is a special dictionary that survives these reruns, letting you hold onto data between interactions. Think of regular variables as a whiteboard that gets erased on every click, and st.session_state as more permanent.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
In the future, I'll definitely open a new chat for each bug because I feel like that helped me keep track of changes and prevented unneccesary additions of random files or functions.
- What is one thing you would do differently next time you work with AI on a coding task?
Give more precise prompting so the AI doesn't deviate or hallucinate.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I think AI generated code can be almost simpler to read than other code because it adds comments and has well-done syntax that maybe other devs lack. AI is useful but should always be checked.
