#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QPainter>
#include <QMouseEvent>
#include <math.h>

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
    painter.setBrush(grass_image);
    painter.drawRect(contentsRect());
    painter.drawImage(pool, water_image);

    for (int count_square = 0; count_square <bush_square.size(); count_square++)
        painter.drawImage(bush_square[count_square], bush_square_image);

    for (int count_circle = 0; count_circle<bush_circle.size(); count_circle++){
        painter.setBrush(bush_circle_image);
        painter.drawEllipse(bush_circle[count_circle].cent, bush_circle[count_circle].rad,bush_circle[count_circle].rad);
    }


}

void MainWindow::mousePressEvent(QMouseEvent *event)
{
    if (event->button() & Qt::LeftButton){
        QRect bush_square_1 = QRect(QPoint(0,0),pool.size() * 0.1);
        bush_square_1.moveCenter(event->pos());
        if (intersection_square(bush_square_1))
            bush_square.append(bush_square_1);

    }


    if (event->button() & Qt::RightButton){
        bush = {event->pos(), rad_1};
        if (intersection_circle(bush)){
            bush_circle.append(bush);
            rad_1 += rad_1* 0.05;
        }

    }
    repaint();
}

bool MainWindow::intersection_square(QRect bush_intersection) //пересечение прямоугольных клумб
{
    if (pool.contains(bush_intersection.center()))
        return false;

    for (int count = 0; count<bush_square.size(); count++){
        if (bush_square[count].intersects(bush_intersection)){
           QRect intersected_square = bush_square[count].intersected(bush_intersection); // прямоугольник, постороенный пересечением 2-ч других
           float s_bush_intersection = bush_intersection.width() * bush_intersection.height(); //площадь поставленного прямоугольника
           float s_bush_intersected = intersected_square.width() * intersected_square.height(); //площадь intersected_square
           if (s_bush_intersected  <= s_bush_intersection * 0.6)
               return false;
        }
    }
    for (int count = 0; count<bush_circle.size();count++){
        if (!intersected_circle_and_square(bush_circle[count],bush_intersection)){
                return false;
        }
    }
    return true;
}

bool MainWindow::intersection_circle(Circle bush_intersection) // пересечение круглых кустов
{
    if (pool.contains(bush_intersection.cent))
        return false;

    for (int count = 0; count<bush_circle.size(); count++){
        if (intersected_circle(bush_intersection, bush_circle[count]))// проверка пересекаются ли круги
            return false;
    }
    for (int count = 0; count<bush_square.size(); count++){
        if (!intersected_circle_and_square(bush_intersection,bush_square[count]))
            return false;
    }


    return true;
}

bool MainWindow::intersected_circle(Circle circle_1, Circle circle_2) // пересечение кругов (возврошает true, когда пересекаются)
{
    QPoint cent_circle_1(circle_1.cent);
    QPoint cent_circle_2(circle_2.cent);
    QPoint vector (cent_circle_2 - cent_circle_1);
    int d = pow(vector.x(),2) + pow(vector.y(),2);
    if (d > pow(circle_1.rad + circle_2.rad,2))
        return false;

    return true;
}

bool MainWindow::point_in_circle(Circle circle, QPoint point) // попадает ли точка в круг (возврощает true, когда точка не поподает в круг)
{
    QPoint vector(point-circle.cent);
    int d_vector = pow(vector.x(),2) + pow(vector.y(),2);
    if (d_vector > pow(circle.rad,2))
        return false;
    return true;
}

bool MainWindow::intersected_circle_and_square(Circle circle, QRect square) // пересекае ли круг и прямоугольник (возврощает true, когда не пересекаются)
{
    for (int i_x =0; i_x<square.width();i_x++){
        for (int i_y =0; i_y<square.height();i_y++){
            QPoint inter (square.topLeft() + QPoint(i_x,i_y));
            if (point_in_circle(circle, inter))
                return false;
    }
   }
    return true;
}









