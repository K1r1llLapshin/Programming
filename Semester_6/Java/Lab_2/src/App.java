import java.util.Arrays;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        Scanner in = new Scanner(System.in);

        while (true) {
            System.out.println("Выбирите пункт:"+
                                "\n1. Найти наибольшую подстроку без повторяющихся символов."+
                                "\n2. Объединить два отсортированных массива."+
                                "\n3. Найти максимальную сумму подмассива."+
                                "\n4. Повернуть двумерный массив на 90 градусов по часовой стрелке."+
                                "\n5. Найти пару элементов в массиве, сумма которых равна заданному числу."+
                                "\n6. Найти сумму всех элементов в двумерном массиве."+
                                "\n7. Найти максимальный элемент в каждой строке двумерного массива."+
                                "\n8. Повернуть двумерный массив на 90 градусов против часовой стрелке.\n"
                                );

            int num = in.nextInt();
            String string = "Hello World and Hello Java";
            int target = 17;
            int[] arr_1 = {1, 3, 7, 9, 10, 15};
            int[] arr_2 = {0, 2, 4, 11, 17};
            int[][] matrix ={ {1, 2, 4, 3},
                              {5, 6, 7, 8},
                              {9, 10, 11, 12},
                              {13, 14, 16, 15}
                            };

            switch (num) {
                case 1:
                    LargestSubstring(string);
                    break;
                case 2:
                    MergingArrays(arr_1, arr_2);
                    break;
                case 3:
                    MaxSum(arr_1);
                    break;
                case 4:
                    RotateMatrix90_r(matrix);
                    break;
                case 5:
                    FindNum(arr_2, target);
                    break;
                case 6:
                    SumMatrix(matrix);
                    break;
                case 7:
                    MaxElementInRows(matrix);
                    break;
                case 8:
                    RotateMatrix90_l(matrix);
                    break;
            }

            System.out.println("\nВыбирите пункт:\n1. Рестарт.\n2. Завершить программу.\n");
            int restart = in.nextInt();
            if (restart == 2)
                break;
        }
        
    }


    // Задание 1. Найти наибольшую подстроку без повторяющихся символов. 
    static void LargestSubstring(String string) {

        int lengthString = string.length();
        boolean[] letters = new boolean[128];
        int start = 0;
        int maxLength = 0; 
        int startIndex = 0;
    
        for (int end = 0; end < lengthString; end++) {
            char currentChar = string.charAt(end);
    
            while (letters[currentChar]) {
                letters[string.charAt(start)] = false;
                start++;
            }

            letters[currentChar] = true;
            if (end - start + 1 > maxLength) {
                maxLength = end - start + 1;
                startIndex = start;
            }
        }
        System.out.println(string.substring(startIndex, startIndex + maxLength));
    }

    // Задание 2. Объединить два отсортированных массива. 
    static void MergingArrays(int[] arr1, int[] arr2){
        
        int lengthArr1 = arr1.length;
        int lengthArr2 = arr2.length;
        int[] res = new int[lengthArr1 + lengthArr2];

        int i = 0;
        int j = 0; 
        int k = 0; 

        
        while (i < lengthArr1 && j < lengthArr2) {
            if (arr1[i] <= arr2[j]) {
                res[k++] = arr1[i++];
            } else {
                res[k++] = arr2[j++];
            }
        }

        while (i < lengthArr1) {
            res[k++] = arr1[i++];
        }

        while (j < lengthArr2) {
            res[k++] = arr2[j++];
        }
        System.out.println(Arrays.toString(res));
       
    }

    // Задание 3. Найти максимальную сумму подмассива.
    static void MaxSum(int[] arr){
        
        int max_sum = Integer.MIN_VALUE;
        int lenght_arr = arr.length;

        for(int i = 1; i <= lenght_arr; i++){
            for(int j = 0; j <= lenght_arr - i; j++){
                int sum = 0;
                for(int k = j; k < i+j; k++){
                    sum += arr[k];
                }
                if (sum > max_sum)
                    max_sum = sum;
            }
        }
        System.out.println(max_sum);
    }

    // Задание 4. Повернуть массив на 90 градусов по часовой стрелке.
    static void RotateMatrix90_r(int[][] matrix){
        int columns = matrix[0].length;
        int rows = matrix.length;
        int[][] res = new int[columns][rows];
        
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < columns; j++)
                res[j][i] = matrix[i][j];
        
        for (int i = 0; i < columns; i++){
            for(int j = 0; j < rows/2; j++){
                int time_el = res[i][j];
                res[i][j] = res[i][rows-1-j];
                res[i][rows-1-j] = time_el;
            }
        }

        for(int[] row : res)
           System.out.println(Arrays.toString(row)); 
    }

    // Задание 5. Найти пару элементов в массиве, сумма которых равна заданному числу.
    static void FindNum(int[] arr, int target){

        boolean in_arr = false;
        int[] res = new int[2];

        for (int i = 0; i < arr.length-1; i++)
            for (int j = i+1; j < arr.length; j++){
                if (arr[i] + arr[j] == target){
                    in_arr = true;
                    res[0] = arr[i];
                    res[1] = arr[j];
                    break;
                }
            }
        if (in_arr)
            System.out.println(Arrays.toString(res));
        else
            System.out.println("null");
    }

    // Задание 6. Найти сумму всех элементов в двумерном массиве.
    static void SumMatrix(int[][] arr){

        int sum = 0;

        for(int i = 0; i < arr.length; i++)
            for(int j = 0; j< arr[0].length; j++)
                sum += arr[i][j];
        
        System.out.println(sum);
    }

    // Задание 7. Найти максимальный элемент в каждой строке двумерного массива.
    static void MaxElementInRows(int[][] arr){

        int[] max_el = new int[arr.length];

        for(int i = 0; i < arr.length; i++)
            for(int j = 0; j < arr[i].length; j++){
                if (arr[i][j] > max_el[i])
                max_el[i] = arr[i][j];
            }
        
        System.out.println(Arrays.toString(max_el));
    }

    // Задание 8. Повернуть двумерный массив на 90 градусов против часовой стрелке.
    static void RotateMatrix90_l(int[][] matrix){

        int columns = matrix[0].length;
        int rows = matrix.length;
        int[][] res = new int[columns][rows];
            
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < columns; j++)
                res[j][i] = matrix[i][j];
            
        for (int i = 0; i < rows; i++){
            for(int j = 0; j < columns/2; j++){
                int time_el = res[j][i];
                res[j][i] = res[columns-1-j][i];
                res[columns-1-j][i] = time_el;
            }
        }

        for(int[] row : res)
        System.out.println(Arrays.toString(row)); 
    }
}
