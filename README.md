# **Advanced Task Board**

🚀 **Advanced Task Board** is a Python-powered application that allows you to manage tasks efficiently using a sleek UI and a hotkey trigger (`Ctrl + Shift + Z`). With features like adding, removing, clearing tasks, and scrollable task lists, it’s a great productivity tool for everyday use.

![image](https://github.com/user-attachments/assets/d4a3ce04-fb52-442f-95a4-734718d249bb)
---

## **Features**

✨ **Hotkey Activation**  
- Open the task board instantly using the `Ctrl + Shift + Z` combination.

✨ **User-Friendly Interface**  
- A modern and responsive UI built with Tkinter, featuring scrollable task lists and clean layouts.

✨ **Task Management**  
- **Add Task**: Easily add new tasks with a simple dialog box.  
- **Remove Task**: Select and remove tasks with a single click.  
- **Clear All Tasks**: Quickly clear all tasks with a confirmation dialog.

✨ **Customizable**  
- Modify colors, fonts, or task behaviors with minimal effort.

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<YourRepo>/advanced-task-board.git
   cd advanced-task-board
   ```

2. **Install Dependencies**:
   Install required Python libraries using `pip`:
   ```bash
   pip install keyboard
   ```

3. **Run the Script**:
   Execute the script in your terminal:
   ```bash
   python task_board.py
   ```

---

## **Usage**

1. Run the script.
2. Press `Ctrl + Shift + Z` to open the task board.
3. Use the buttons to manage tasks:
   - **Add Task**: Click the "Add Task" button, type your task, and click OK.  
   - **Remove Task**: Select a task from the list and click "Remove Task."  
   - **Clear All Tasks**: Click "Clear All" to remove all tasks at once.  
   - **Close**: Click "Close" to exit the task board.

4. Press `Esc` to stop the program.

---

## **Screenshots**

### **Task Board Interface**  
![image](https://github.com/user-attachments/assets/9b16096d-77b5-42a9-9460-b365c78eb37f)
---

## **Customization**

You can tweak the script to fit your needs:

- **Change UI Colors and Fonts**:
  Modify the `bg`, `fg`, or font properties in the `TaskBoard` class.

- **Hotkey**:  
  Change the `keyboard.add_hotkey` function to a different key combination:
  ```python
  keyboard.add_hotkey("ctrl+shift+z", open_task_board)
  ```

---

## **Contributing**

Contributions are welcome! If you have ideas to improve the task board, feel free to:
- Fork the repository.
- Make your changes.
- Submit a pull request.

---

## **License**

This project is licensed under the **MIT License**. Feel free to use it for personal or commercial projects.

---

