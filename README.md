## Project: Random Intrusive Windows

This project creates a simple Python application using the `Tkinter` library to generate multiple graphical windows with random titles and messages. The program is designed to simulate popup windows that display alert messages, which could be used for fun or as a demo for handling graphical user interfaces (GUIs) in Python.

### Features
- Generates multiple pop-up windows (3 in this case) with random titles and messages.
- Uses the `Tkinter` library for the GUI.
- Randomized content on each window, ensuring different user experiences.

### Requirements

To run this script, you'll need the following:
- Python 3.x
- Tkinter (Included by default with most Python installations)

### How It Works

1. The script defines two lists:
   - **`window_titles`**: A list of random window titles that simulate system alerts or warnings.
   - **`random_texts`**: A list of random messages that appear within the windows.

2. The `create_window()` function:
   - Creates a new `Tkinter` window.
   - Randomly selects a title from the `window_titles` list and a message from the `random_texts` list.
   - Displays the title and message in the window.
   - Sets the window's size to 700x500 pixels.

3. A loop generates 3 pop-up windows, each with a randomly chosen title and message.

### Usage

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   ```
   
2. **Navigate to the project directory**:
   ```bash
   cd <project-directory>
   ```

3. **Run the script**:
   ```bash
   python script.py
   ```

### Customization

You can easily modify the behavior of this script:
- **Number of windows**: Change the `for i in range(3)` to generate more or fewer windows.
- **Titles and messages**: Add more entries to the `window_titles` and `random_texts` lists to customize the content.

### Example Output
Three windows will appear with random combinations of:
- **Window Titles**: "Attention !", "Alerte Système !", "Fenêtre Intrusive !", etc.
- **Messages**: "Votre attention est requise !", "Ne fermez pas cette fenêtre.", "Vous avez gagné un prix !", etc.
