# amoy-todo-wallpaper

Set To-Do list as windows wallpaper. 

This is a python program coded by claude-sonnet-3.5 with minor revision. 

![](amoy-todo.jpg)

## How to use

1. download `amoy-todo-wallpaper.zip`
2. unzip all file
3. run `amoy-todo.exe`

This program will open `todo.txt` file for edit, click [Save & Apply] to set it as windows wallpaper.

## Files

1. source code [amoy-todo.py](amoy-todo.py)
2. background image `background.png` (by flux-schnell)
3. todo list `todo.txt`
4. download zip [amoy-todo-wallpaper.zip](amoy-todo-wallpaper.zip)

To compile the source into single executable: `pyinstaller -F -w amoy-todo.py`


## Prompt

```
write a python program to set a text file as wallpaper, add UI to edit todo.txt, and allow setup font-color and content background color.

- text file is "todo.txt", left-align, grey text color
- round content area 12px
- allow set font size setting, default 16px
- background image is "background.png"
- nice look fonts, support chinese
- show in top-right with margin 120px, light grey background #eee
- do not filter empty line
- output python code in code-block
```

## Notes

- 2025/02/03, v1, tested on `sonnet-3.5`, `deepseek-R1` and `o3-mini`, finally choose sonnet version as the code is most simple.
- 2025/02/03, v2, add font size setting.

enjoy it.
