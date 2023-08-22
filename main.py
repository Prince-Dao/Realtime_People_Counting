### IMPORTS
import sys
import time

import cv2
import supervision as sv
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QGraphicsDropShadowEffect, QMessageBox, QComboBox
from ultralytics import YOLO

### UI
from countwindow import Ui_MainWindow

t0 = time.time()
global_state = 0
LINE_START = sv.Point(0, 240)
LINE_END = sv.Point(640, 240)


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("People Counter Monitoring System")

        self.stop_flag = False
        self.call_flag = False
        self.maximumPeople = 0
        self.current = 0
        self.cameraNumber = 0  # Initial camera number

        ## Buttons
        self.ui.btn_close.clicked.connect(self.save_and_exit)
        self.ui.B_Start.clicked.connect(self.counterWindow)
        self.ui.btn_setMaximum.clicked.connect(self.setMaxPeople)
        self.ui.btn_setCurrent.clicked.connect(self.setCurrentPeople)

        self.ui.title_bar.mouseMoveEvent = self.moveWindow
        self.ui.btn_Settings.clicked.connect(self.open_settings)

        ##Timer & Date
        self.timer = QTimer(app)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.center_on_screen()
        self.uiDefinitions()

        self.cameraNumber = 0

    def open_settings(self):
        # Create a QMessageBox with four input fields for the user to set the values
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Settings")
        msg_box.setText("Establish the designated entrance direction for incoming individuals:"

                        "                     0 for west, 1 for east, 2 for north, 3 for south")
        msg_box.setIcon(QMessageBox.Information)

        # Create a QComboBox for selecting the camera number
        combo_box = QComboBox()
        combo_box.addItems([str(i) for i in range(4)])
        combo_box.setCurrentText(str(self.cameraNumber))

        # Set the layout of the QMessageBox to include the QComboBox
        layout = msg_box.layout()
        layout.addWidget(combo_box, 1, 2)  # Add the QComboBox in the second row
        msg_box.setLayout(layout)

        # Add the Ok button
        msg_box.addButton(QMessageBox.Ok)

        # Show the QMessageBox and retrieve the camera number
        if msg_box.exec_() == QMessageBox.Ok:
            self.cameraNumber = int(combo_box.currentText())
    def maximize_restore(self):
        global global_state
        status = global_state

        if status == 0:
            self.showMaximized()
            global_state = 1

            self.ui.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
            self.ui.drop_shadow.setStyleSheet(
                "background-color: rgb(24,78,119); border-radius: 0px; color: rgb(255, 255, 255);")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            global_state = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.verticalLayout_7.setContentsMargins(10, 10, 10, 10)
            self.ui.drop_shadow.setStyleSheet(
                "background-color: rgb(24,78,119); border-radius: 10px; color: rgb(255, 255, 255);")
            self.ui.btn_maximize.setToolTip("Maximize")

    def uiDefinitions(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.btn_maximize.clicked.connect(lambda: self.maximize_restore())
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.ui.drop_shadow.setGraphicsEffect(self.shadow)

    def center_on_screen(self):
        # Get the primary screen geometry
        screen_geometry = QApplication.desktop().screenGeometry()

        # Get the center point of the screen
        center_point = screen_geometry.center()

        # Set the window geometry to be centered on the screen
        self.setGeometry(
            center_point.x() - self.width() // 2,
            center_point.y() - self.height() // 2,
            self.width(),
            self.height()
        )

    def save_and_exit(self):
        if self.stop_flag:
            sys.exit(app.exec_())
        else:
            self.stop_flag = True

    def moveWindow(self, event):
        if self.returnStatus() == 1:
            self.maximize_restore()

        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def returnStatus(self):
        return global_state

    def update_time(self):
        # get the current time
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()

        time_string = current_time.toString(Qt.DefaultLocaleLongDate)
        date_string = current_date.toString(Qt.DefaultLocaleLongDate)

        self.ui.Time_Label.setText(time_string)
        self.ui.Date_Label.setText(date_string)

    def setMaxPeople(self):
        self.value = 0
        self.value, ok = QInputDialog.getInt(None, "Set capacity", "Enter maximum people:")

        while self.value == 0 and ok:
            self.value, ok = QInputDialog.getInt(None, "Set capacity", "Enter maximum people:")

        self.maximumPeople = self.value
        print(self.maximumPeople)

    def counterWindow(self):
        self.setMaxPeople()
        if self.value > 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.Mainpage)
            self.tracker()

    def setCurrentPeople(self, current):
        current, ok = QInputDialog.getInt(None, "Set current people", "Enter current people inside:")
        self.current = current
        self.call_flag = True
        return self.call_flag

    def update_people_counter(self, count):
        capacity = self.maximumPeople

        if count >= capacity:
            color = "#ff6464"
            self.ui.peopleCounter.setStyleSheet("QLabel{border: 8px solid rgb(255, 100, 100);border-radius: 300px;}")
        else:
            color = "#b3ffae"
            self.ui.peopleCounter.setStyleSheet("QLabel{border: 8px solid rgb(179, 255, 174);border-radius: 300px;}")

        self.ui.peopleCounter.setText(
            f"<html><head/><body><p align=\"center\"><span style=\" font-size:120pt; color:{color};\">" + str(
                count) + " / " + str(capacity))

    def tracker(self):
        status = "Waiting"
        line_counter = sv.LineZone(start=LINE_START, end=LINE_END)
        line_annotator = sv.LineZoneAnnotator(thickness=2,
                                              text_thickness=1,
                                              text_scale=0.5,
                                              )
        box_annotator = sv.BoxAnnotator(
            thickness=1,
            text_thickness=1,
            text_scale=0.3,
            color=sv.Color.green()
        )
        model = YOLO("yolo/yolov8n.pt")
        for result in model.track(source=self.cameraNumber, stream=True, agnostic_nms=True):
            frame = result.orig_img
            detections = sv.Detections.from_yolov8(result)

            if result.boxes.id is not None:
                detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)
                status = "Tracking"
            else:
                status = "Waiting"

            detections = detections[(detections.class_id == 0)]

            labels = [
                f"#{tracker_id} {confidence:0.4f}"
                for _, confidence, class_id, tracker_id
                in detections
            ]

            frame = box_annotator.annotate(
                scene=frame,
                detections=detections,
                labels=labels
            )

            line_counter.trigger(detections=detections)
            line_annotator.annotate(frame=frame, line_counter=line_counter)

            enter_total = line_counter.out_count
            exit_total = line_counter.in_count

            print("people going in: ", enter_total)
            print("people going out: ", exit_total)

            if self.call_flag is True:
                enter_total = 0
                exit_total = 0
                self.call_flag = False
            else:
                total_inside = int(enter_total - exit_total)

            show_total = max(0, total_inside + self.current)

            self.update_people_counter(show_total)
            print(show_total)

            if show_total >= self.maximumPeople:
                self.ui.Status_Label.setStyleSheet("color: #ff6464;")
                self.ui.Status_Label.setText("MAXIMUM AMOUNT OF PEOPLE IS INSIDE THE FACILITY")
            else:
                self.ui.Status_Label.setStyleSheet("color: #ffffff;")
                self.ui.Status_Label.setText(status)

            cv2.imshow("Live feed Analysis Window", frame)

            if (cv2.waitKey(30) == 27 or self.stop_flag == True):
                cv2.destroyAllWindows()
                sys.exit(app.exec_())
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = Mainwindow()
    main_win.show()
    sys.exit(app.exec_())
