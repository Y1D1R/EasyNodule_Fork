import os
import sys
from PySide2 import *
from ui_interface import *
from Custom_Widgets.Widgets import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.gridspec import GridSpec
import numpy as np
from PIL import Image


class MainWindow(QMainWindow):
    def clicker(self):
        print("You clicked the button to choose a file !")
        fname = QFileDialog.getOpenFileName(self, "Open File and Choose the 3D Nodule", "C:\\Users\\21379\\Desktop\\memoire\\DATA" , "All Files (*);; Python Files(*.npy)")
        Nodule3D = np.load(fname[0], allow_pickle=True)
        #print(Nodule3D.shape)   
        #plt.plot(Nodule3D[10,:,:,0])
        #plt.show()
        
        #Clear the canvas 
        self.figure.clear()
        #plot
        #im = Image.fromarray(Nodule3D[10,:,:,0])
        #im.show()
        #plt.imshow(Nodule3D[10,:,:,0],'gray')
        self.ax1 = self.figure.add_subplot(self.grid[0, 0])
        self.ax1.imshow(Nodule3D[0,0][32, :, :], cmap='gray')
        self.ax1.set_title('Vue X')
        self.ax2 = self.figure.add_subplot(self.grid[0, 1])
        self.ax2.imshow(Nodule3D[0,0][:, 32, :], cmap='gray')
        self.ax2.set_title('Vue Y')
        self.ax3 = self.figure.add_subplot(self.grid[0, 2])
        self.ax3.imshow(Nodule3D[0,0][:, :, 32], cmap='gray')
        self.ax3.set_title('Vue Z')
        #refresh
        self.canvas.draw()
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################

        ########################################################################
        
        
        self.show()
        
        #expand center menu size
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        
        self.ui.textIdC.setText("C02555")
        self.ui.textUsernameC.setText("user_124qsgqfgdgfdq")
        self.ui.textNameC.setText("KOULAL yidhir aghiles")
        self.ui.textHospital.setText("AlgerHdfg")
        self.ui.textWilayaC.setText("Tizi Ouzou")
        self.ui.textGrade.setText("Pr")
        
        #Open file btn
        self.ui.openfileBtn.clicked.connect(self.clicker)
        
        #matplolib
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout(self.ui.frame_matplotlib)
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        #canva
        self.figure = plt.figure()
        self.grid = GridSpec(1, 3)  # CrÃ©e une grille de 1 ligne et 3 colonnes pour les sous-graphiques
        

        self.canvas = FigureCanvas(self.figure)
        #end of canva
        
        #add canva
        self.horizontalLayout_44.addWidget(self.canvas)
        
    
        
        #close center menu 
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())
          
        #expand right menu size
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
     
        
        
        #close right menu 
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())
        
        #close Notification 
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())     