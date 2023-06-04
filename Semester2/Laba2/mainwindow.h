#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

struct Circle{
      QPoint cent;
      int rad;
};

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    void paintEvent(QPaintEvent *event);
    void mousePressEvent(QMouseEvent *event);


private:
    QImage grass_image = QImage(":/new/prefix1/resources/grass.png");
    QImage water_image = QImage(":/new/prefix1/resources/water.png");
    QImage bush_circle_image = QImage(":/new/prefix1/resources/bush_circle.png");
    QImage bush_square_image = QImage(":/new/prefix1/resources/bush_square.jpg");

    QRect pool = QRect(QPoint(150,100), QSize(400,200));
    QVector <QRect> bush_square;
    QVector <Circle> bush_circle;
    QPoint bush_circle_1;
    int s_circle = 20;
    int c = 10;
    int rad_1 = 20;
    Circle bush;

    bool intersection_square (QRect bush_intersection);
    bool intersection_circle (Circle bush_intersection);
    bool intersected_circle (Circle circle_1, Circle circle_2);
    bool point_in_circle (Circle circle, QPoint point);
    bool intersected_circle_and_square (Circle circle, QRect square);
    Ui::MainWindow *ui;

};
#endif // MAINWINDOW_H

