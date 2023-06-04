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

    for (int count_x = 0; count_x<contentsRect().width(); count_x++){
        for (int count_y = 0; count_y<contentsRect().height(); count_y++){
            painter.drawRect(kletca.translated(size_k*count_x, size_k*count_y));
        }
    }

    painter.drawEllipse(tree.center, tree.rad, tree.rad);
    painter.setBrush(QColor(128, 128, 128, 150));
    painter.drawEllipse(ant, 5, 5);
    painter.drawEllipse(fly, 5, 5);

    for (int i = 0; i<move_point.size()-1; i++){
        QPen pen (Qt::red, 3);
        painter.setPen(pen);
        painter.drawLine(move_point[i], move_point[i+1]);

    }

}

void MainWindow::mousePressEvent(QMouseEvent *event)
{
    if (count == 0){
        tree = {event->pos(), 60};
        for (int count_x = 0; count_x<contentsRect().width(); count_x++){
            for (int count_y = 0; count_y<contentsRect().height(); count_y++){
                QRect translated_k = kletca.translated(size_k*count_x, size_k*count_y);
                point_k.append(translated_k.topLeft());
            }
        }
    }

    if (count == 1){
      ant = point_on_setka(event->pos());
     qDebug ("x = %d; y = %d\n", ant.x(), ant.y());
    }

    if (count >= 2){
        move_point.clear();
        fly = point_on_setka(event->pos());

        QPoint ant_new = ant;
        while (ant_new != fly){
            move_p[0] = ant_new + QPoint (0, -size_k);//up
            move_p[1] = ant_new + QPoint (0, size_k);//down
            move_p[2] = ant_new + QPoint (-size_k, 0);//left
            move_p[3] = ant_new + QPoint (size_k, 0);//right
            move_point.append(ant_new);
            int min = INT_MAX;
            QPoint real_move;

            for (int i = 0; i<4; i++){
                for (int j = 0; j< move_point.size(); j++){
                    if (point_in_circle(move_p[i], tree) && move_p[i] != move_point[j]){
                     int dlina = dlina_1(fly, move_p[i]);
                        if (dlina < min){
                            min = dlina;
                            real_move = move_p[i];
                        }
                     }

                }
            }
            ant_new = real_move;

       }
        move_point.append(fly);
    }
        for (int i = 0; i<move_point.size();i++)
            qDebug ("x = %d; y = %d", move_point[i].x(), move_point[i].y());
    count++;

    repaint();
}



QPoint MainWindow::point_on_setka(QPoint p)
{
    int min = INT_MAX;
    QPoint real_point;
    for (int count_p = 0; count_p<point_k.size(); count_p++){
        QPoint point_t = point_k[count_p] - p;
        int dlina = dlina_1(point_k[count_p], p);
        if (dlina < min){
            min = dlina;
            real_point = point_k[count_p];
        }
    }
    return real_point;
}

bool MainWindow::point_in_circle(QPoint p, Circle c)
{
    if (dlina_1(c.center, p) <= c.rad)
        return false;
    return true;
}

int MainWindow::dlina_1(QPoint p1, QPoint p2)
{
    QPoint point_dlina = p1 - p2;
    return sqrt(pow(point_dlina.x(),2)+pow(point_dlina.y(),2));
}
