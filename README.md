Quantum Maze Generator and Random Utilities
This project provides three main components:

1. Maze Generator and Player: 
A game that generates a randomized maze where users can navigate through dynamic pathways.

2. Quantum Random Utilities: 
Functions for creating high-entropy random values for secure applications, 
character generation, and color transitions.

3. Chocolate Defender System: 
System Composed of running button and Impossible Password that protects the chocolates 

Setup
Ensure Python and required libraries are installed for seamless functionality.

Install the necessary libraries.
Pygame for the game GUI 
for the QRNG :
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator


Running the Maze:
This game component generates a randomized maze, 
allowing users to navigate from a start point to an end goal. 
When the game is started, a procedurally generated maze appears, 
complete with randomized walls and paths.

Note: 
- by changing the tile (the cell size) you can change the maze size.
- by changing the clock.tick() (the last line) You can controll generation speed.


Game Controls:
Movement: Use arrow keys to navigate through the maze.
Objective: Start from the initial cell and reach the green cell.


Visual Features:
Dynamic Color Shifting: Colors in the maze dynamically shift for an immersive experience.
Randomized Pathways: Each maze path is unique, making each game session different from the last.


Quantum Random Utilities
The Quantum Random Utilities include versatile high-entropy random functions 
that are useful for secure applications, 
including generating characters, symbols, emojis, and more.


Functionality:
Random Integer Generator: Produces quantum-random integers within a specified range.
Random Character Generators: Creates single characters from letters, digits, punctuation, emojis, or currency symbols.
Password Generator: Constructs secure, random passwords using various character types.
Array Element Selector: Randomly selects an item from an array.
Color Transition Simulator: Smoothly transitions between colors for dynamic visual effects.


Contact:
For inquiries or support, please reach out at [yokimaxwel@gmail.com].

Made by, Fun and Quirky Team!
- Youssef Mostafa      - Mohammad walid 
- Morkos Shenoda       - Youssef Tarek 
