# Arisu's Borderland Adventures (Text-Based RPG)

A text-based survival adventure game developed for a university assignment. 

I customized the standard homework requirements by theming the game around the survival series **Alice in Borderland**. Instead of a generic explorer, the player controls **Arisu** as he navigates through dangerous decisions to survive.

## Personal Touches
- **Themed Storytelling:** Adapted the scenario to fit the "Borderland" universe.
- **Custom Logs:** The game generates a `treasure_log.txt` that chronicles Arisu's specific journey and choices.

## Features
- **Branching Storylines:** Players choose between "Pack A" (The Golden River) and "Pack B" (The Dangerous Canyon).
- **Game Mechanics:**
  - Manages **Health (HP)** and **Gold** globally.
  - Turn-based events (traps, healing herbs, enemies like 'Bee Swarm').
  - Game Over states (running out of HP).
- **File I/O:** Reads intro text and logs gameplay history.

## Technologies Used
- Python
- File Operations (`open`, `write`, `read`)
- Global State Management