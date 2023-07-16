# Интерфейс для обучения агентов

## Описание

Этот проект реализует алгоритм на основе нейронной сети для поиска выхода из лабиринта. Нейронная сеть учится перемещаться по лабиринту, обучаясь на наборе размеченных карт лабиринта.

Цель состоит в том, чтобы предоставить решение проблемы поиска кратчайшего пути от начальной точки до выхода из заданного лабиринта.

Данный проект создан для управления агентами и их данными, отображения актуальной информации об обучении агентов.

## Установка
1. Установите python с версией не менее 3.9. 

   Ссылка: https://www.python.org/downloads/
2. Установите Git.
   
   Ссылка: https://git-scm.com/downloads

3. Откройте командную строку и пропишите путь к папке, в которой будет запускаться проект, используя команду: 
   
   cd C:\Project

   Замените C:\Project на необходимую Вам дерикторию. 
4. Пропишите команду, используя командную строку:
   
   git clone https://github.com/Cognitive-systems-and-technologies/pythonProject

   Также, Вы можете сделать данное действие, без использования Git. Для этого нажмите на кнопку "Code", а затем в 
   выпадающем меню нажмите Download ZIP. После этого распакуйте содержимое архива в нужную папку.
5. Create and activate a virtual environment:

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
