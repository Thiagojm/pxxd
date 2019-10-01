import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
import queue

class QtPlotter:
    def __init__(self, buffer_size):
        self.ports = []
        self.timer = pg.QtCore.QTimer()
        self.win = pg.GraphicsWindow()
        self.ax = self.win.addPlot()
        self.timer.timeout.connect(self.update)
        self.timer.start(0)
        self.ax.setAspectLocked(True)
        self.ax.addLegend()
        self.buffer_size = buffer_size

    def getPort(self):
        q = queue.Queue()
        plt = self.ax
        self.ports.append((q, plt))
        return q

    def update(self):
        for q, plt in self.ports:
            try:
                data = q.get(block=False)

                plt.clear()
                self.ax.legend.scene().removeItem(self.ax.legend)

                self.ax.addLegend()
                for index, variable in enumerate(data):
                    plt.plot(
                        np.asarray(data[variable]['time'][-self.buffer_size:]).flatten(),
                        np.asarray(data[variable]['value'][-self.buffer_size:]).flatten(),
                        name=variable,
                        pen=(index, len(data)), symbol="o",
                        symbolPen=pg.mkPen({'color': "#00FFFF", 'width': 2}),
                        symbolSize=1
                    )
            except queue.Empty:
                pass

import sys
import time
import threading

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

def data_loop(curve, data):
    while True:
        data['x']['time'] = np.append(data['x']['time'], np.array([data['x']['time'][-1] + 1]))
        data['y']['time'] = np.append(data['y']['time'], np.array([data['y']['time'][-1] + 1]))
        data['x']['value'] = np.append(data['x']['value'], np.array([data['x']['value'][-1] * 0.8]))
        data['y']['value'] = np.append(data['y']['value'], np.array([data['y']['value'][-1] * 1.2]))
        curve.put(data)
        time.sleep(1)

def qt_loop():
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

def main():
    viewer = QtPlotter(buffer_size=100)
    curve = viewer.getPort()

    data = {
        'x': {
            'time': np.array([0]),
            'value': np.array([1]),
        },
        'y': {
            'time': np.array([0]),
            'value': np.array([1]),
        },
    }
    threading.Thread(target=data_loop, args=(curve, data)).start()

    qt_loop()

if __name__ == '__main__':
    main()
