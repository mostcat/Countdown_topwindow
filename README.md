# Countdown_topwindow

中文版本请查看 READM_CN.md

## Functionality

- Stays on top of all windows

- Window can be dragged across screens to desired position with mouse

- Hides window borders, title bar, and maximize/minimize buttons 

- Window size calculated to fit 00:00, using font size 40, system default font

- Flashes window when 1 minute remaining and when paused

- Continues flashing when time is up, shows overtime 

- Window transparency decreases as time elapses

- Different flash style when paused

- Runs on Python 3+ without admin rights 

- No additional libraries required

### When total time is set

- Pausing does not pause total time

- Resetting does not reset total time

### When mouse is over window

- Time add/subtract buttons appear, add/subtract 1 minute each click, seconds set to 0

- Time set in minutes, default 5 minutes 

- Pause button

- Reset button, resets to default time

- Exit button

### When mouse is not over window  

- Shows remaining time 

- Format: MM:SS

- Updates display every second

- Window is transparent

- Not transparent when paused 

- Transparency based on ratio of total/remaining times

- Not transparent for first 5 seconds after start

- More transparency as remaining time decreases, fully opaque at 1 minute left

### Usage

Command line example:

python CountdownTopWin.py 5 60

- Param 1: Single timer time, max 99 minutes 

- Param 2: Total time, max 99 minutes

- No params: Default single time 5 minutes, no total time

### Known Issues

- Buttons must be exited from button area to hide, exiting time area does not auto-hide
