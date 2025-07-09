# Python for Data Analytics

A link to my project: https://colab.research.google.com/drive/1OYDxpFhXo_Apu1uUsuKaYDNQNd6OrJqn?authuser=1

## A Chess Question

This is a Python program that will answer a simple question – given a board state that the user enters, with 1 white figure and up to 16 black figures, which black figures can the white figure take?

# Task Requirements

### 1. User Input for White Piece

- The program must prompt the user to input a white piece and its position on the board.
- The user must choose between two predefined piece types (e.g., pawn and rook). -> **I have decided to leave all positions available for choosing** 
- The input format must be: (e.g., knight a5).
- The program must confirm a successful addition or display an error message if the input is invalid.

### 2. User Input for Black Pieces
- After the white piece is set, the user must input the black pieces one by one.
- Each black piece must follow the same format (e.g., bishop d6).
- The user must add at least one and at most sixteen black pieces.
- The user can enter "done" to stop adding black pieces only after at least one black piece has been added.
- The program must confirm a successful addition or display an error message if the input is invalid.

### 3. Input Validation
- The program must ensure that input coordinates follow the correct format (where the letter is a-h and the digit is 1-8, e.g., a1, d4, h8).
- The program must handle edge cases, such as:
- Attempting to enter "done" before adding at least one black piece.
- Providing invalid chess piece names.
- Entering out-of-bounds coordinates.

### 4. Output and Gameplay Logic
- After all pieces are added, the program must display a list of black pieces that the white piece can capture based on valid chess moves.
- If no black pieces are captured, the program should indicate this clearly.


# Running the code

### User Input:
1. White piece and position
<div><img width="451" alt="image" src="https://github.com/user-attachments/assets/29fbfcfd-e315-433c-82c8-04c07a9853e1" /><div>
<br>

3. Black pieces and positions
   
<div><img width="498" alt="image" src="https://github.com/user-attachments/assets/116e3584-2477-4bef-a73c-8b8665487a99" /></div>
<div><img width="503" alt="image" src="https://github.com/user-attachments/assets/345ca2f7-3e94-422f-9258-96c379e900ab" /></div>

<br> 

3. Finishing inputs
</div><img width="492" alt="image" src="https://github.com/user-attachments/assets/0ecf530f-70a4-4071-b5fd-6459d55849b4" /></div>
