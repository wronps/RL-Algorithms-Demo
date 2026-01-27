# RL-Algorithms-Demo

This repository contains implementations of various Reinforcement Learning (RL) algorithms for educational and demonstration purposes. The goal is to provide clear and concise examples of how different RL algorithms work, along with code that can be easily understood and modified.

## Tools and Librarys Used
- uv
- PiSide6
- NumPy
- pyyaml
- pyqtgraph


## init
First init the uv environment by running the following command:
```bash
uv init
```
Add the environment
```bash
uv add pyside6 numpy pyyaml pyqtgraph
```
There can be more.
To run the program
```bash
uv run main.py
```
## Project Structure (something like that)
```
RL-Algorithms-Demo/
  app/
    __init__.py
    main.py
    ui/
      __init__.py
      main_window.py
      widgets/
        __init__.py
        grid_canvas.py
        tool_panel.py
    workers/
      __init__.py
      dp_worker.py
  core/
    __init__.py
    mdp/
      __init__.py
      types.py
      gridworld.py
    dp/
      __init__.py
      value_iter.py
  tests/
    test_gridworld_transitions.py
```
This makes sure the code is seperated into core algorithms and app for the UI.
## potential roadmap:
Qt Widgets + unique canvas + pyqtgraph for showing the plots for training process.