Bee's Bounty

A 2D game developed with Python and Pygame, utilizing design patterns for a clean and modular architecture.
🚀 About the Project

Bee's Bounty is an academic/personal project focused on the practical application of Design Patterns, such as Factory and Mediator, to manage game entities and their interactions.
🛠️ Technologies Used

    Python: Main programming language.

    Pygame: Library for 2D game development.

    SQLite: Database for persistent score tracking (Top 10).

🏗️ Architecture and Design Patterns

The project is structured to be highly extensible:

    Factory Pattern (EntityFactory): Centralizes the creation of entities (players, backgrounds, points), making it easy to add new object types.

    Mediator Pattern (EntityMediator): Manages collision logic and interactions between entities, ensuring that objects remain decoupled.

    Clean Architecture: Clear separation between constants (Const.py), game logic (Level.py), entities (Entity.py), and persistence (DBProxy.py).

🎮 How to Play

    Prerequisites: Ensure you have Python and Pygame installed.

pip install pygame

2.  **Execution**: Run the `main.py` file (or your system's entry point).
3.  **Controls**:
    * **Player 1**: Arrow keys (Up, Down, Left, Right).
    * **Player 2**: WASD keys.
    * **Menu Navigation**: Arrow keys and Enter.

## 📋 Features
* 1-Player and 2-Player modes (Co-op/Competitive).
* Progressive level system.
* Score system with database persistence.
* Dynamic collision detection and entity health management.

## 📂 Folder Structure

```text
/code
  ├── Background.py    # Background management
  ├── Const.py         # Global configurations and constants
  ├── DBProxy.py       # SQLite database access
  ├── Entity.py        # Base class (Abstract)
  ├── EntityFactory.py # Entity factory
  ├── EntityMediator.py# Collision logic
  ├── Game.py          # Game loop management
  ├── Level.py         # Level loop
  ├── Menu.py          # Menu interface
  ├── Player.py        # Player logic
  ├── Point.py         # Point/Collectable logic
  └── Score.py         # Scoreboard interface
/asset                 # Images and audio files
