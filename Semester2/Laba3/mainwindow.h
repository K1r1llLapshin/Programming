#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT
    struct Circle
    {
       QPoint center;
       int rad;
    };
public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    void paintEvent(QPaintEvent *event);
    void mousePressEvent(QMouseEvent *event);
    QPoint point_on_setka (QPoint p);
    bool point_in_circle (QPoint p, Circle c);
    int dlina_1 (QPoint p1, QPoint p2);
private:
    Ui::MainWindow *ui;
    int size_k = 30;
    int count = 0;
    QRect kletca = QRect (QPoint (0,0), QSize(size_k, size_k));
    QPoint ant, fly;
    Circle tree;
    QVector <QPoint> point_k, move_point;
    QPoint move_p[4];



};
#endif // MAINWINDOW_H
