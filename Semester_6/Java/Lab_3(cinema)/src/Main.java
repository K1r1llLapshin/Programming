import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        TicketSystem ticketSystem = new TicketSystem();
        Scanner in = new Scanner(System.in);
        String log_and_pass_User = "User34";
        String log_and_pass_Admin = "Admin34";
        
        while (true) { 
            System.out.println("1. Зайти как пользователь. \n2. Зайти как админ. \nЛюбая другая кнопка. Выход из программы.");
            int num = in.nextInt();
            if (num == 1){
                System.err.print("Введите логин: ");
                String log = in.next();
                System.err.print("Введите пароль: ");
                String pass = in.next();

                if (log_and_pass_User.equals(log) && log_and_pass_User.equals(pass)){
                    User user = new User(ticketSystem);
                    user.Interface();
                }
                else
                    System.err.print("Неверен логин или пароль\n\n");
            }
            else if(num == 2){
                System.err.print("Введите логин: ");
                String log = in.next();
                System.err.print("Введите пароль: ");
                String pass = in.next();

                if (log_and_pass_Admin.equals(log) && log_and_pass_Admin.equals(pass)){
                    Administration admin = new Administration(ticketSystem);
                    admin.Interface();
                }
                else
                    System.err.print("Неверен логин или пароль\n\n");
            }
            else
                break;
        }
    }

}
