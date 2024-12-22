import sys
from PyQt5 import QtWidgets

import design


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.hex_in.textChanged.connect(self.on_change_hex)

        self.rgb_in_R.textChanged.connect(self.on_change_rgb)
        self.rgb_in_G.textChanged.connect(self.on_change_rgb)
        self.rgb_in_B.textChanged.connect(self.on_change_rgb)

    def on_change_hex(self):
        val = self.hex_in.text()
        self.updateHexIn(val)

        if len(val) < 6:
            return

        for n in val:
            if n not in "0123456789ABCDEF":
                return

        r = int(val[:2], 16)
        g = int(val[2:4], 16)
        b = int(val[4:], 16)

        self.update_background(r, g, b)

        self.rgb_in_R.setValue(r)
        self.rgb_in_G.setValue(g)
        self.rgb_in_B.setValue(b)

    def on_change_rgb(self):
        r = int(self.rgb_in_R.text())
        g = int(self.rgb_in_G.text())
        b = int(self.rgb_in_B.text())

        self.update_background(r, g, b)

        hex_r = str(hex(r))[2:]
        hex_g = str(hex(g))[2:]
        hex_b = str(hex(b))[2:]

        if len(hex_r) == 1: hex_r = "0" + hex_r
        if len(hex_g) == 1: hex_g = "0" + hex_g
        if len(hex_b) == 1: hex_b = "0" + hex_b

        self.updateHexIn(hex_r + hex_g + hex_b)
    def update_background(self, r, g, b):
        self.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")

    def updateHexIn(self, val):
        cursor_pos = self.hex_in.cursorPosition()
        self.hex_in.setText(val.upper())
        self.hex_in.setCursorPosition(cursor_pos)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.setWindowTitle("Color")
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
