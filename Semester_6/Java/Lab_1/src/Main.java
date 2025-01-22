import java.util.Scanner;

public class Main {
    static Scanner in = new Scanner(System.in);
    public static void main(String[] args) throws Exception {
        System.out.println("Выберете задание:\n1. Сиракузская последовательность\n2. Сумма ряда\n3. Ищем клад\n4. Логический максимин\n5. Дважды чётное число\n6 Завершить");
        int num = in.nextInt();
        switch (num) {
            case 1:
                System.out.print("Введите число: ");
                int n = in.nextInt();
                System.out.println("Количество шагов: " + Siracusa_sequence(n));
                break;
            
            case 2:
                Sum_series();
                break;

            case 3:
                Treasure_hunt();
                break;

            case 4:
                Logistic_max_and_min();
                break;

            case 5:
                Twice_even_number();
                break;
        }
        
        in.close();
    }

    // Задание №1. Сиракузская последовательность 
    static int Siracusa_sequence(int n) {
        int count = 0;
        while (n != 1){
            if (n % 2 != 0) 
                n = 3*n + 1;
            else
                n /= 2;

            count++;
        }
        return count;
    }

    // Задание №2. Сумма ряда
    static void Sum_series(){
        System.out.print("Введите число: ");
        int res = 0;
        int n = in.nextInt();
        for(int i = 1; i <= n; i++){
            int num = in.nextInt();
            if (i % 2 == 0)
                res -= num;
            else
                res += num;
        }
        System.out.println("Ответ: " + res);
    }

    // Задание №3. Ищем клад 
    static void Treasure_hunt(){
        System.out.println("Введи координаты клада.");
        int x_treasure = in.nextInt();
        int y_treasure = in.nextInt();

        System.out.println("Введи указания карты.");

        int x_now = 0;
        int y_now = 0;
        int count = 0;
        boolean flag = true;

        while (true){
            String direction = in.next();
            if (direction.equals("stop"))
                break;

            int step = in.nextInt();

            if (direction.equals("north"))
		        y_now += step;
	        else if (direction.equals("south")) 
		        y_now -= step;
	        else if (direction.equals("east")) 
		        x_now -= step;
	        else if (direction.equals("west")) 
		        x_now += step;

            if (x_now == x_treasure && y_now == y_treasure){
                count++;
                flag = false;
            }

            if (flag) 
                count++;
        }
        System.out.println("Ответ: " + count);
    }

    // Задание №4. Логический максимин
    static void Logistic_max_and_min() {
        int max_car = 0;
        int num_road = 0;

        System.out.print("Введите количество дорог: ");
        int count_road = in.nextInt();

        for (int i = 1; i <= count_road; i++) {
            int min_tunnel = Integer.MAX_VALUE;
            System.out.print("Введите количество туннелей на дороге " + i + ": ");
            int count_tunnel = in.nextInt();

            for (int j = 1; j <= count_tunnel; j++) {
                System.out.print("Введите размер (см) туннеля " + j + ": ");
                int height_tunnel = in.nextInt();

                if (min_tunnel > height_tunnel) {
                    min_tunnel = height_tunnel;
                }
            }

            if (max_car < min_tunnel) {
                max_car = min_tunnel; 
                num_road = i; 
            }
        }

        System.out.println("Номер дороги: " + num_road + "\nМаксимальная высота (минимальная среди всех туннелей): " + max_car);
    }

    // Задание №5. Дважды чётное число
    static void Twice_even_number(){
        System.out.print("Введите число: ");
        int num = in.nextInt();
        int multiply = (num / 100) * (num / 10 % 10) * (num % 10);
        int plus = (num / 100) + (num / 10 % 10) + (num % 10);

        if (multiply % 2 == 0 && plus % 2 == 0)
            System.out.println ("Дважды чётное число");
        else
        System.out.println ("Дважды чётным числом не является");
    }
}
