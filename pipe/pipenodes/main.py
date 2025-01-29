import os, sys
from qtpy.QtWidgets import QApplication
from qtpy.QtGui import QIcon
sys.path.insert(0, os.path.join( os.path.dirname(__file__), "..", ".." ))

from pipe.pipenodes.pipe_window import CalculatorWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # print(QStyleFactory.keys())
    app.setStyle('Fusion')
    # app.setWindowIcon(QIcon(''))

    wnd = CalculatorWindow()
    wnd.show()

    sys.exit(app.exec_())
