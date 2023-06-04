#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QPainter>
#include <QMouseEvent>
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::paintEvent(QPaintEvent *event)
{
    QPainter painter (this);
    if (!point1.isNull() && !point2.isNull()){
    painter.drawLine(point1,point2);
    painter.drawLine(new_vector1);
    painter.drawLine(new_vector2);
    painter.setBrush(QColor(237, 225, 33, 140));
    painter.drawPolygon(points, 3);
    }

}

void MainWindow::mousePressEvent(QMouseEvent *event)
{
    i++;
    if (i == 1)
        point1 = event->pos();
    if (i == 2){
        point2 = event->pos();
        new_vector1.setLine(point2.x(),point2.y(),point1.x(),point1.y());
        new_vector1.setAngle(30);
        new_vector2.setLine(point2.x(),point2.y(),point1.x(),point1.y());
        new_vector2.setAngle(-30);
        QPoint q = point2 - point1;
        normal_vector_1 = QPoint (-q.y(),q.x());
        normal_vector_2 = QPoint (q.y(),-q.x());
        points[0] = point2;
        points[1] = new_vector1.p2();
        points[2] = new_vector2.p2();
    }
    if ( i>=3){
        int vector = classify(QLineF(point1,point2),event->pos());
        int vector1 = classify(new_vector1,event->pos());
        int vector2 = classify(new_vector2,event->pos());
        int normal_vector_back = classify(QLineF (normal_vector_2+point1, normal_vector_1+point1),event->pos());
        QString string;
        if (normal_vector_back == Right)
            string = string + " С зади";
        if (vector1 == Right && vector2 == Left)
            string = string + " Вижу";
        if (normal_vector_back == Left && vector1 == Left && vector == Left)
           string = string + "Лево, середина";
        if (normal_vector_back == Left && vector2 == Right && vector == Right)
           string = string + "Право, середина";
        QMessageBox::information(this, "Фонарик", string);
    }

    repaint();
}

int MainWindow::classify(QLineF line, QPoint point3)
{
    QPointF vector = line.p2() - line.p1();
    QPointF points = point3 - line.p1();
    int position = points.x()*vector.y() - points.y()*vector.x();
    if (position > 0 )
        return Left;
    if (position < 0)
        return Right;
    return Under;
}

