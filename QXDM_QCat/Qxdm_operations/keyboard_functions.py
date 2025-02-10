import keyboard


class KeyboardAction:
    def __init__(self):
        pass


    def keyboard_events(self, alt=False, popup_alert=False):
        if alt:
            keyboard.press_and_release('alt')
        if popup_alert:
            keyboard.press_and_release('alt+f4')


    def press_tab_n_times(self, n):
        for _ in range(n):
            keyboard.press_and_release('tab')

    def press_enter_n_times(self, n):
        for _ in range(n):
            keyboard.press_and_release('enter')

    def press_down_n_times(self, n):
        for _ in range(n):
            keyboard.press_and_release('down')
