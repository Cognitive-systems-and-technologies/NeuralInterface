# Neural Network Labyrinth Solver

## Description

This project implements a neural network-based algorithm to find a way out of a labyrinth. The neural network learns to navigate through the labyrinth by training on a set of labeled labyrinth maps.

The goal is to provide a solution to the problem of finding the shortest path from the starting point to the exit of a given labyrinth.

## Installation

1. Clone the repository:

   git clone https://github.com/your-username/labyrinth-solver.git

2. Create and activate a virtual environment:

   For Unix/Linux:
   python3 -m venv env
   source env/bin/activate  

   For Windows:
   python -m venv env
   .\env\Scripts\activate


3. Install the required dependencies:

   pip install -r requirements.txt

## Usage

1. Prepare the training data:

   - Create labeled labyrinth maps in the desired format. Each map should have a corresponding solution indicating the optimal path from the starting point to the exit.
   - Save the labeled maps in a suitable format (e.g., CSV, JSON).

2. Train the neural network:

   - Run the training script, specifying the path to the labeled labyrinth maps.
   - The neural network will be trained to learn the optimal path-finding strategy.

3. Test the neural network on new labyrinths:

   - Use the trained neural network to find a path out of a new labyrinth by providing the labyrinth map as input.
   - The neural network will predict the optimal path to navigate the labyrinth.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
