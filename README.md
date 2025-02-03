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

1. source code [amoy-todo.py]()
2. background image [amoy-todo.py]()
3. download zip [amoy-todo-wallpaper.zip]()

## Prompt

```
write a python program to set a text file as wallpaper, add UI to edit todo.txt, and allow setup font-color and content background color.

- text file is "todo.txt", left-align, grey text color
- round content area 12px font size 16px
- background image is "background.png"
- nice look fonts, support chinese
- show in top-right with margin 120px, light grey background #eee
- do not filter empty line
- output python code in code-block
```

## Notes

2025/02/03, tested on `sonnet-3.5`, `deepseek-R1` and `o3-mini`, all doing well but we finally choose sonnet version as the code is most simple.

enjoy it.
