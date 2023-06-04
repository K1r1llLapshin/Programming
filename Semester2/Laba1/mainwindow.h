#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT
    enum {Right, Left, Under};
public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    void paintEvent(QPaintEvent *event);
    void mousePressEvent(QMouseEvent *event);
private:
     int classify (QLineF line, QPoint point3);
    Ui::MainWindow *ui;
    QPoint point1, point2, normal_vector_1, normal_vector_2;
    QPointF points[3];
    QLineF new_vector1, new_vector2;

    int i = 0;

};
#endif // MAINWINDOW_H
